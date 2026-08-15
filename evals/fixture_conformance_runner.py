#!/usr/bin/env python3
"""
fixture-conformance-runner v2

Structural conformance runner for the waa-agent-delegation regression fixtures.

WHAT IT DOES
  Reads evals/trigger-cases.json plus evals/cases.md and checks that every
  fixture RECORD is well formed, internally consistent, and correctly
  cross-referenced. Reports PASS or FAIL per fixture, plus file-level checks
  and a summary.

WHAT IT DOES NOT DO
  It sends no fixture prompt to any executor and judges no executor behavior.
  Fixture expected_conditions and forbidden_conditions are natural-language
  statements about how an executor must behave; deciding whether a response
  satisfies them needs a model-backed run plus a semantic judgment, and neither
  is deterministic. This runner therefore leaves every behavioral status exactly
  as recorded and never turns "missing evidence" into a behavioral result.

FALSIFIABILITY
  MAINTAINING.md requires an absence-oriented check to be shown able to fail
  before a zero result counts as evidence. Phase 1 runs every check against a
  positive control carrying the defect the check exists to find, and against a
  negative control that does not carry it and still exercises the check. A check
  failing either control is reported UNVERIFIED and the run exits 2, because a
  zero result from it would be meaningless. A conditional check whose antecedent
  never fires on the real file is reported vacuous, never as passed.

v2 CHANGE
  Adds bounded_evidence_declares_no_run. The evidence field carries two
  different things: a behavioral result, and context recorded while the
  behavioral result is still missing. Only the second is legal under
  status "missing evidence", and it must say so in its own text, so that a
  reader cannot mistake context for a verdict. v1 checked the first direction
  only and was blind to this one.

v3 CHANGE
  Adds case_refs. Every fixture names, in a case_refs list, the narrative case
  it instantiates; chk_case_refs_valid verifies each ref resolves to a real
  Case heading, and the summary reports narrative coverage with unreferenced
  cases listed. Coverage is reported, not gated: a case with no fixture is a
  documented residual, not a structural failure.

USAGE
  python3 fixture_conformance_runner.py <trigger-cases.json> <cases.md>

EXIT CODES
  0  every check verified falsifiable, and every fixture structurally passed
  1  at least one structural failure was found
  2  at least one check failed its own control: the run is not evidence
  3  the inputs could not be read or parsed
"""

import hashlib, json, re, sys

VERSION = "fixture-conformance-runner v3"
# Status value meaning "no behavioral result recorded yet". Taken from the
# vocabulary the fixture file itself uses; update if that vocabulary changes.
UNRECORDED_STATUS = "missing evidence"
# Exact phrase an evidence string must carry when it accompanies the unrecorded
# status, so that context can never be read as a behavioral verdict.
NO_RUN_MARKER = "no forward run of this fixture"
CANONICAL_KEYS = ("id","category","prompt","expected_conditions","forbidden_conditions","status","evidence","case_refs")
# Protocol tokens that cannot occur as ordinary English prose because they carry
# an underscore. Single-word labels (BLOCKED, ACCEPTED, DONE, PARTIAL, FAILED)
# are deliberately excluded: they appear as ordinary words in fixture text, so a
# case-insensitive match on them yields false positives.
UNDERSCORE_TOKENS = ("MISSING_CAPABILITY","CAPABILITY_OUT_OF_SCOPE","PLATFORM_PERMISSION_BLOCKED","EXECUTION_SUBAGENT","TASK_SPECIALIST_SUBAGENT","NAMED_AGENT","LIST_ONLY","LIST_IS_START_DISCLOSE_BEYOND","PLATFORM_UNKNOWN","RECORD_CONTRACT_ANOMALY")
TOKEN_PATTERNS = [(t, re.compile(r"\b" + re.escape(t) + r"\b", re.IGNORECASE)) for t in UNDERSCORE_TOKENS]
CROSSREF_RE = re.compile(r"cases\.md Case ([0-9]+[A-Z]?)")
HEADING_RE = re.compile(r"^## Case ([0-9]+[A-Z]?)\b", re.MULTILINE)

def _snip(t, n=90):
    s = " ".join(str(t).split())
    return s if len(s) <= n else s[:n] + "..."

def _d(v):
    return type(v).__name__ + " " + _snip(repr(v), 40)

def _ne(v):
    return isinstance(v, str) and v.strip() != ""

def chk_schema_keys(c, x):
    if not isinstance(c, dict):
        return (["record is not a JSON object"], True)
    have, want = set(c.keys()), set(CANONICAL_KEYS)
    return ([("missing key: " + k) for k in sorted(want - have)] + [("unexpected key: " + k) for k in sorted(have - want)], True)

def chk_field_types(c, x):
    out = []
    for k in ("id","category","prompt","status"):
        if k in c and not _ne(c[k]):
            out.append(k + ": expected non-empty string, got " + _d(c[k]))
    for k in ("expected_conditions","forbidden_conditions"):
        if k in c:
            v = c[k]
            if not isinstance(v, list):
                out.append(k + ": expected list, got " + _d(v))
            else:
                for i, item in enumerate(v):
                    if not _ne(item):
                        out.append(k + "[" + str(i) + "]: expected non-empty string, got " + _d(item))
    if "case_refs" in c:
        v = c["case_refs"]
        if not isinstance(v, list):
            out.append("case_refs: expected list, got " + _d(v))
        else:
            for i, item in enumerate(v):
                if not _ne(item):
                    out.append("case_refs[" + str(i) + "]: expected non-empty string, got " + _d(item))
    if "evidence" in c and c["evidence"] is not None and not _ne(c["evidence"]):
        out.append("evidence: expected null or non-empty string, got " + _d(c["evidence"]))
    return (out, True)

def chk_id_unique(c, x):
    i = c.get("id")
    if not isinstance(i, str):
        return ([], True)
    n = x["id_counts"].get(i, 0)
    return ([] if n == 1 else ["id occurs " + str(n) + " times in cases[]"], True)

def chk_conditions_present(c, x):
    out = []
    for k in ("expected_conditions","forbidden_conditions"):
        v = c.get(k)
        if isinstance(v, list) and len(v) == 0:
            out.append(k + ": empty; a fixture that asserts nothing can never fail")
    return (out, True)

def chk_conditions_consistent(c, x):
    out = []
    e = [i for i in c.get("expected_conditions", []) if isinstance(i, str)]
    f = [i for i in c.get("forbidden_conditions", []) if isinstance(i, str)]
    for k, v in (("expected_conditions", e), ("forbidden_conditions", f)):
        seen = set()
        for i in v:
            if i in seen:
                out.append(k + ": duplicate condition: " + _snip(i))
            seen.add(i)
    for i in sorted(set(e) & set(f)):
        out.append("condition is both expected and forbidden: " + _snip(i))
    return (out, True)

def _texts(c):
    p = []
    if isinstance(c.get("prompt"), str):
        p.append(c["prompt"])
    for k in ("expected_conditions","forbidden_conditions"):
        v = c.get(k)
        if isinstance(v, list):
            p.extend([i for i in v if isinstance(i, str)])
    if isinstance(c.get("evidence"), str):
        p.append(c["evidence"])
    return p

def chk_label_token_case(c, x):
    out, fired = [], False
    for t in _texts(c):
        for tok, pat in TOKEN_PATTERNS:
            for m in pat.finditer(t):
                fired = True
                if m.group(0) != tok:
                    out.append("non-canonical token " + m.group(0) + " (expected " + tok + ") in: " + _snip(t))
    return (out, fired)

def chk_evidence_status_coherence(c, x):
    s = c.get("status")
    if not isinstance(s, str) or s == UNRECORDED_STATUS:
        return ([], False)
    if not _ne(c.get("evidence")):
        return (["status is " + _d(s) + " but evidence is empty; a recorded result needs its evidence"], True)
    return ([], True)

def chk_bounded_evidence_declares_no_run(c, x):
    # The inverse of the check above. Under the unrecorded status an evidence
    # string is context, not a verdict, and must say so in its own words, or a
    # later reader cannot tell the two apart from the record alone.
    s = c.get("status")
    ev = c.get("evidence")
    if not isinstance(s, str) or s != UNRECORDED_STATUS or not _ne(ev):
        return ([], False)
    if NO_RUN_MARKER.lower() in ev.lower():
        return ([], True)
    return (["status is " + repr(UNRECORDED_STATUS) + " and evidence is present, but the evidence does not state " + repr(NO_RUN_MARKER) + "; context is indistinguishable from a behavioral result: " + _snip(ev)], True)

def chk_case_refs_valid(c, x):
    # A fixture's case_refs bind it to the narrative case it instantiates. Every
    # ref must resolve to a real Case heading and the list may not be empty: an
    # unbound fixture is invisible to any coverage question asked of the corpus.
    v = c.get("case_refs")
    if v is None:
        return (["case_refs: missing; every fixture names the case it instantiates"], True)
    if not isinstance(v, list) or not v:
        return (["case_refs: expected a non-empty list, got " + _d(v)], True)
    return ([("case_refs: " + repr(r) + " has no matching Case heading") for r in v if isinstance(r, str) and r not in x["case_headings"]], True)

def chk_evidence_crossref(c, x):
    ev = c.get("evidence")
    if not isinstance(ev, str):
        return ([], False)
    refs = CROSSREF_RE.findall(ev)
    if not refs:
        return ([], False)
    return ([("evidence references cases.md Case " + r + ", which has no matching heading") for r in refs if r not in x["case_headings"]], True)

CASE_CHECKS = (("schema_keys", chk_schema_keys),("field_types", chk_field_types),("id_unique", chk_id_unique),("conditions_present", chk_conditions_present),("conditions_consistent", chk_conditions_consistent),("label_token_case", chk_label_token_case),("evidence_status_coherence", chk_evidence_status_coherence),("bounded_evidence_declares_no_run", chk_bounded_evidence_declares_no_run),("evidence_crossref", chk_evidence_crossref),("case_refs_valid", chk_case_refs_valid))

def fchk_regression_watch(cases, x):
    # MAINTAINING.md: keep Cases 7A and 7B and their regression-watch entries.
    out = []
    w = [c for c in cases if isinstance(c, dict) and c.get("category") == "regression_watch"]
    if len(w) < 2:
        out.append("expected at least 2 regression_watch fixtures, found " + str(len(w)))
    anchors = set()
    for c in w:
        if isinstance(c.get("evidence"), str):
            anchors.update(CROSSREF_RE.findall(c["evidence"]))
    for need in ("7A","7B"):
        if need not in anchors:
            out.append("no regression_watch fixture anchors cases.md Case " + need)
        if need not in x["case_headings"]:
            out.append("cases.md has no heading for Case " + need)
    return out

def fchk_top_level(doc, x):
    out = [("missing top-level key: " + k) for k in ("schema_version","purpose","scoring","automatic_gate","cases") if k not in doc]
    if "cases" in doc and not isinstance(doc["cases"], list):
        out.append("cases: expected a list")
    return out

def _base():
    return {"id":"control-clean","category":"control","prompt":"A control prompt without protocol tokens.","expected_conditions":["Control condition A"],"forbidden_conditions":["Control condition B"],"status":UNRECORDED_STATUS,"evidence":None,"case_refs":["7A"]}

CTRL_CTX = {"id_counts":{"control-clean":1,"control-duplicate":2},"case_headings":set(["7A","7B"])}

def _controls():
    o = {}
    p = _base(); p["notes"] = "extra"; o["schema_keys"] = (p, _base())
    p = _base(); p["expected_conditions"] = "not a list"; o["field_types"] = (p, _base())
    p = _base(); p["id"] = "control-duplicate"; o["id_unique"] = (p, _base())
    p = _base(); p["forbidden_conditions"] = []; o["conditions_present"] = (p, _base())
    p = _base(); p["expected_conditions"] = ["Shared","Shared"]; p["forbidden_conditions"] = ["Shared"]; o["conditions_consistent"] = (p, _base())
    p = _base(); p["prompt"] = "Return missing_capability when absent."
    n = _base(); n["prompt"] = "Return MISSING_CAPABILITY when absent."
    o["label_token_case"] = (p, n)
    p = _base(); p["status"] = "recorded"; p["evidence"] = None
    n = _base(); n["status"] = "recorded"; n["evidence"] = "Recorded by a dated forward run."
    o["evidence_status_coherence"] = (p, n)
    p = _base(); p["evidence"] = "Environment facts were reproduced on a dated observation."
    n = _base(); n["evidence"] = "Environment facts were reproduced on a dated observation; no forward run of this fixture has been performed."
    o["bounded_evidence_declares_no_run"] = (p, n)
    p = _base(); p["case_refs"] = ["99"]
    o["case_refs_valid"] = (p, _base())
    p = _base(); p["evidence"] = "See evals/cases.md Case 99."
    n = _base(); n["evidence"] = "See evals/cases.md Case 7A."
    o["evidence_crossref"] = (p, n)
    return o

def _wcase(i, ref):
    return {"id":i,"category":"regression_watch","prompt":"p","expected_conditions":["a"],"forbidden_conditions":["b"],"status":UNRECORDED_STATUS,"evidence":"See evals/cases.md Case " + ref + "."}

GOOD_WATCH = [_wcase("w1","7A"), _wcase("w2","7B")]
GOOD_DOC = {"schema_version":"1.0","purpose":"p","scoring":"none","automatic_gate":False,"cases":[]}
BAD_DOC = {"schema_version":"1.0","purpose":"p","scoring":"none","cases":[]}

def _read(path):
    with open(path, "rb") as fh:
        return fh.read()

def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: fixture_conformance_runner.py <trigger-cases.json> <cases.md>\n")
        return 3
    fx, cm = argv
    try:
        raw = _read(fx)
        h_fx = hashlib.sha256(raw).hexdigest()
        doc = json.loads(raw.decode("utf-8"))
    except Exception as e:
        sys.stderr.write("cannot read or parse fixtures: " + str(e) + "\n")
        return 3
    try:
        raw_md = _read(cm)
        h_cm = hashlib.sha256(raw_md).hexdigest()
        md = raw_md.decode("utf-8")
    except Exception as e:
        sys.stderr.write("cannot read cases file: " + str(e) + "\n")
        return 3
    if not isinstance(doc, dict) or not isinstance(doc.get("cases"), list):
        sys.stderr.write("fixture file has no cases[] list\n")
        return 3
    cases = doc["cases"]
    headings = set(HEADING_RE.findall(md))
    ids = {}
    for c in cases:
        if isinstance(c, dict) and isinstance(c.get("id"), str):
            ids[c["id"]] = ids.get(c["id"], 0) + 1
    ctx = {"id_counts": ids, "case_headings": headings}

    print(VERSION)
    print("=" * 74)
    print("fixtures   : " + fx)
    print("  sha256   : " + h_fx)
    print("cases file : " + cm)
    print("  sha256   : " + h_cm)
    print("declared   : schema_version=" + str(doc.get("schema_version")) + "  scoring=" + str(doc.get("scoring")) + "  automatic_gate=" + str(doc.get("automatic_gate")))
    print("corpus     : " + str(len(cases)) + " fixtures, " + str(len(headings)) + " Case headings extracted from the cases file")
    print("")
    print("SCOPE. This runner checks the structural conformance of fixture RECORDS.")
    print("It sends no prompt to any executor and judges no executor behavior, so it")
    print("changes no behavioral verdict. Every fixture keeps its recorded status.")
    print("")
    print("-- PHASE 1: check falsifiability self-test --------------------------------")
    ctrl = _controls()
    verified, reasons = {}, {}
    for name, fn in CASE_CHECKS:
        p, n = ctrl[name]
        pf, _ = fn(p, CTRL_CTX)
        nf, nfired = fn(n, CTRL_CTX)
        verified[name] = len(pf) > 0 and len(nf) == 0 and nfired
        reasons[name] = "positive control flagged: " + ("yes" if pf else "NO") + "; negative control clean: " + ("yes" if not nf else "NO") + "; negative control exercised: " + ("yes" if nfired else "NO")
    live = len(headings) > 0
    if not live:
        verified["evidence_crossref"] = False
        reasons["evidence_crossref"] += "; LIVE-TARGET FAIL: no Case headings extracted"
        verified["case_refs_valid"] = False
        reasons["case_refs_valid"] += "; LIVE-TARGET FAIL: no Case headings extracted"
    fv = {}
    fpf = fchk_regression_watch([GOOD_WATCH[0]], CTRL_CTX)
    fnf = fchk_regression_watch(GOOD_WATCH, CTRL_CTX)
    fv["regression_watch_anchors"] = (len(fpf) > 0 and len(fnf) == 0 and live)
    reasons["regression_watch_anchors"] = "positive control flagged: " + ("yes" if fpf else "NO") + "; negative control clean: " + ("yes" if not fnf else "NO") + "; live target: " + ("yes" if live else "NO")
    fpf2 = fchk_top_level(BAD_DOC, CTRL_CTX)
    fnf2 = fchk_top_level(GOOD_DOC, CTRL_CTX)
    fv["top_level_shape"] = (len(fpf2) > 0 and len(fnf2) == 0)
    reasons["top_level_shape"] = "positive control flagged: " + ("yes" if fpf2 else "NO") + "; negative control clean: " + ("yes" if not fnf2 else "NO")
    allv = dict(verified); allv.update(fv)
    for name, _fn in CASE_CHECKS:
        print(("[VERIFIED  ] " if verified[name] else "[UNVERIFIED] ") + name.ljust(34) + reasons[name])
    for name in ("regression_watch_anchors","top_level_shape"):
        print(("[VERIFIED  ] " if fv[name] else "[UNVERIFIED] ") + name.ljust(34) + reasons[name])
    unverified = sorted([k for k, v in allv.items() if not v])
    print("")
    print("-- PHASE 2: structural conformance, per fixture ---------------------------")
    fired_count = dict((n, 0) for n, _fn in CASE_CHECKS)
    failed_fixtures, total_findings = [], 0
    for idx, c in enumerate(cases):
        cid = c.get("id") if isinstance(c, dict) else None
        label = cid if isinstance(cid, str) else "cases[" + str(idx) + "] (no id)"
        findings = []
        for name, fn in CASE_CHECKS:
            f, fired = fn(c if isinstance(c, dict) else {}, ctx)
            if fired:
                fired_count[name] += 1
            for item in f:
                findings.append(name + ": " + item)
        if findings:
            failed_fixtures.append(label)
            total_findings += len(findings)
            print("FAIL  " + label)
            for item in findings:
                print("        " + item)
        else:
            print("PASS  " + label)
    print("")
    print("-- PHASE 3: file-level checks ---------------------------------------------")
    file_findings = []
    for name, res in (("regression_watch_anchors", fchk_regression_watch(cases, ctx)), ("top_level_shape", fchk_top_level(doc, ctx))):
        if res:
            print("FAIL  " + name)
            for item in res:
                print("        " + item)
            file_findings.extend(res)
        else:
            print("PASS  " + name)
    print("")
    print("-- SUMMARY ----------------------------------------------------------------")
    print("checks verified falsifiable : " + str(len(allv) - len(unverified)) + "/" + str(len(allv)))
    print("fixtures structurally PASS  : " + str(len(cases) - len(failed_fixtures)) + "/" + str(len(cases)))
    print("fixture-level findings      : " + str(total_findings))
    print("file-level findings         : " + str(len(file_findings)))
    vac = [n for n, _fn in CASE_CHECKS if fired_count[n] == 0]
    if vac:
        print("vacuous on this file (antecedent never fired -> unverified, not passed):")
        for n in vac:
            print("  - " + n)
    else:
        print("vacuous on this file        : none")
    print("check firings               : " + ", ".join([n + "=" + str(fired_count[n]) for n, _fn in CASE_CHECKS]))
    st = {}
    for c in cases:
        if isinstance(c, dict):
            s = c.get("status")
            st[s] = st.get(s, 0) + 1
    print("behavioral status untouched : " + ", ".join([str(v) + " x " + repr(k) for k, v in sorted(st.items(), key=lambda kv: str(kv[0]))]))
    refs = set()
    for c in cases:
        if isinstance(c, dict) and isinstance(c.get("case_refs"), list):
            refs.update([x2 for x2 in c["case_refs"] if isinstance(x2, str)])
    unref = sorted(headings - refs, key=lambda u: (int(re.match(r"[0-9]+", u).group()), u))
    print("narrative coverage          : " + str(len(refs & headings)) + "/" + str(len(headings)) + " case headings referenced by at least one fixture")
    if unref:
        print("cases with no fixture       : " + ", ".join(unref) + "  (reported, not gated)")
    print("")
    if unverified:
        print("RESULT: NOT EVIDENCE. These checks failed their own control: " + ", ".join(unverified))
        print("A zero result from an unverified check cannot be read as a pass.")
        return 2
    if failed_fixtures or file_findings:
        print("RESULT: STRUCTURAL FAILURES FOUND. See the FAIL lines above.")
        return 1
    print("RESULT: all fixture records are structurally conformant.")
    print("This says nothing about whether an executor satisfies any fixture. Behavioral")
    print("verdicts need a model-backed forward run recording method, date, result,")
    print("evidence path, and the verbatim return; this runner performs no such run.")
    if doc.get("automatic_gate") is False:
        print("NOT A GATE: the fixture file declares automatic_gate=false and scoring=none.")
    return 0

sys.exit(main(sys.argv[1:]))
