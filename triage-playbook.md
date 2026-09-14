# Support Triage Playbook

## 1. Intake

Start with the customer's actual impact, not the assumed cause.

Capture:
- What the user was trying to do
- What happened instead
- When it started
- Account/workspace context
- Device, browser, app version, or API client when relevant
- Exact error text
- Whether the issue is reproducible
- Screenshots, logs, request IDs, or timestamps when available

Do not ask for information that is not needed to investigate the case.

## 2. Clarify

Convert vague reports into testable statements. Example:

> "Login is broken" → "After completing password reset, the user is redirected to `/reset-password` again instead of `/dashboard` on Chrome 152 and Firefox 143."

## 3. Reproduce

Use the smallest reliable reproduction path.

1. Match the reported environment when possible.
2. Start from a known account state.
3. Record exact steps.
4. Compare expected vs. actual behavior.
5. Retest at least once to rule out a transient failure.
6. Check nearby scenarios to estimate scope.

## 4. Classify

Every ticket receives one primary classification:

- **Product defect** — expected product behavior is broken.
- **User/configuration issue** — product works as designed; setup, permissions, or usage caused the issue.
- **Feature request** — requested behavior is not part of the current product.
- **Unable to reproduce** — evidence is insufficient or the behavior cannot be reproduced after reasonable investigation.
- **Service incident** — degradation/outage affects multiple users or a shared dependency.

## 5. Assess severity and priority

Severity describes **impact**. Priority describes **response order**.

Never use customer frustration alone as severity. Base severity on business impact, data/security risk, scope, and workaround availability.

## 6. Document

A useful engineering handoff includes:

- Concise title
- Environment
- Preconditions
- Reproduction steps
- Expected behavior
- Actual behavior
- Frequency
- Scope
- Evidence
- Severity / priority
- Workaround
- Customer impact

## 7. Escalate

Escalate when any of the following applies:

- Critical or High confirmed defect
- Security/authorization concern
- Billing or financial impact
- Multi-user service incident
- Data loss or corruption risk
- Support cannot safely mitigate the issue
- Engineering logs or code-level diagnosis are required

## 8. Customer communication

Customer updates should explain what is known, what happens next, and any safe workaround. Do not expose internal speculation as fact or promise an ETA that engineering has not committed to.

## 9. Retest

For a fix:

1. Re-run the original reproduction steps.
2. Confirm expected behavior.
3. Test at least one adjacent path for regression risk.
4. Verify the workaround is no longer required.
5. Record build/version and result.

## 10. Closure

Close only when the issue is fixed, correctly explained as expected behavior/configuration, intentionally declined as a feature request, or documented as unable to reproduce after sufficient investigation.
