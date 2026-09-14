# Severity & Priority Framework

Severity and priority are intentionally separated in this lab.

## Severity

### Critical
Use when the issue creates severe business, security, financial, or data impact with no acceptable workaround.

Examples:
- Unauthorized access to sensitive account data
- Duplicate customer charges at scale
- Data loss or corruption
- Complete production outage

### High
Use when a core workflow is blocked for affected users and there is no practical workaround, or when the impact is serious but not Critical.

Examples:
- Users cannot access their accounts after password reset
- Core checkout flow fails for a supported browser
- Workspace admin actions are blocked

### Medium
Use when functionality is degraded but a workaround exists or the scope is limited.

Examples:
- Important mobile UI action is inaccessible in one viewport range
- Export produces malformed formatting but data is intact

### Low
Use for cosmetic, minor usability, or low-impact issues with little operational risk.

Examples:
- Misaligned icon
- Non-blocking copy issue
- Minor visual inconsistency

## Priority

### P0 — Immediate
Respond/escalate immediately. Usually Critical incidents, security, financial harm, or widespread production outage.

### P1 — Urgent
High-impact issue requiring rapid engineering attention, but not necessarily a full incident response.

### P2 — Normal
Important defect that should enter the normal engineering queue.

### P3 — Low
Low-impact improvement, cosmetic defect, or non-urgent request.

## Decision rule

Severity answers: **How bad is the impact?**  
Priority answers: **How soon should the team act?**

A High-severity defect may be P2 if it affects an unsupported edge case. A Medium-severity issue may be P1 if it affects a strategic launch or a large percentage of customers. The assignment must be justified by evidence.
