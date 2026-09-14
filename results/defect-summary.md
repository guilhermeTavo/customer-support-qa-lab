# Defect Summary

## Overview

The 20-ticket pilot produced **9 confirmed product defects**. Four of those defects were High or Critical severity and required urgent engineering attention.

| Severity | Count |
| --- | ---: |
| Critical | 2 |
| High | 2 |
| Medium | 4 |
| Low | 1 |
| **Total defects** | **9** |

## Highest-risk defects

### BUG-002 — Duplicate subscription charge
**Critical / P0** — A payment timeout followed by retry can create two successful charges for one subscription purchase. This creates direct financial impact and requires immediate containment and engineering investigation.

### BUG-004 — Billing authorization bypass
**Critical / P0** — A non-billing workspace member can open a restricted billing page through a direct URL. The product hides the navigation entry but does not consistently enforce access server-side.

### BUG-001 — Password reset loop
**High / P1** — Successful password reset can leave the user trapped in the recovery flow and unable to regain normal account access.

### SUP-012 — Invoice download HTTP 500
**High / P1** — A generated invoice cannot be downloaded because one invoice path returns an HTTP 500 response.

## Other confirmed defects

- **SUP-003 / Medium** — Save action inaccessible at 360 px viewport.
- **SUP-005 / Medium** — CSV export ignores pt-BR workspace date format.
- **SUP-009 / Medium** — Activity log displays UTC rather than workspace timezone.
- **SUP-015 / Medium** — PDF upload stalls near completion for files within the documented limit.
- **SUP-020 / Low** — Avatar thumbnail appears soft on high-DPI displays.

## Triage quality notes

The lab intentionally separates technical impact from customer emotion. A frustrated customer does not automatically mean a High-severity bug, while a calm report can still reveal a Critical authorization or billing issue.

The highest-value triage work in this pilot was identifying the small number of reports that required immediate escalation while resolving configuration issues and feature requests without unnecessarily involving engineering.
