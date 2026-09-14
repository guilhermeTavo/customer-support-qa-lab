# Interview Guide — Customer Support QA & Bug Triage Lab

## 30-second explanation

I built a simulated SaaS support queue with 20 customer tickets to practice the overlap between Technical Support and QA. I triaged each report, reproduced issues where possible, separated bugs from configuration problems and feature requests, assigned severity and priority, and documented engineering escalations. The pilot produced 9 confirmed defects, including billing and authorization issues that required P0/P1 attention.

## 2-minute explanation

The project starts from customer language rather than prewritten test cases. Each ticket is intentionally incomplete, like a real support report. My process was to identify the user's actual impact, clarify the environment, reproduce the behavior, compare expected and actual results, then classify the ticket.

I separated severity from priority because impact and response order are not always the same thing. Confirmed bugs received structured reports with steps, environment, frequency, workaround, customer impact, investigation notes, and retest criteria. I also included cases where engineering should not be involved, such as device clock drift causing invalid 2FA codes or a browser extension blocking a modal.

The strongest examples were a duplicate-charge retry bug and an authorization issue where a normal member could open restricted billing details through a direct URL. Those cases show why support triage needs to recognize financial and security risk quickly rather than treating every ticket as equal.

## Strong STAR example

**Situation:** A customer reports that they were charged twice after purchasing one subscription.  
**Task:** Determine whether this is user error, payment-provider behavior, or a reproducible product defect, and reduce further financial impact.  
**Action:** Reproduced the checkout under a timeout condition, identified that retrying could create two successful transactions, classified it Critical/P0, documented the exact sequence and frequency, recommended immediate billing review, and escalated the likely missing idempotency protection to engineering.  
**Result:** The case became an actionable engineering report with clear containment and retest criteria instead of a vague billing complaint.

## Questions I should be ready to answer

### How do you decide whether something is a bug?
I compare the observed behavior against expected/documented behavior and verify the account/environment state. If the product works as designed but configuration or permissions explain the outcome, I treat it as a support issue rather than a defect.

### What is the difference between severity and priority?
Severity represents impact; priority represents response order. Security, financial impact, data loss, scope, core-workflow blockage, and workaround availability drive severity. Business timing and operational urgency also influence priority.

### What do you do when you cannot reproduce an issue?
I document exactly what I tested and ask for the next evidence that would materially improve the investigation, such as a timestamp, request ID, console error, account state, or recording. I do not treat unable-to-reproduce as proof that the customer did not experience the issue.

### What makes a good engineering escalation?
A concise problem statement, environment, preconditions, exact reproduction steps, expected vs. actual behavior, frequency, scope, evidence, impact, severity/priority, and any workaround or investigation already completed.

### How do you communicate with the customer during investigation?
I explain what is confirmed, what is still being investigated, what the next action is, and any safe workaround. I avoid presenting hypotheses as facts or promising an engineering ETA that has not been committed.

## CV bullet

Built a SaaS Support QA & Bug Triage portfolio lab covering 20 customer tickets, defect reproduction, severity/priority assessment, engineering escalation, customer communication, and retest criteria; identified 9 simulated product defects including Critical billing and authorization failures.

## LinkedIn summary

Built a hands-on Customer Support QA & Bug Triage Lab to practice the workflow between customer support and engineering: turning vague user reports into reproducible defects, support resolutions, product requests, incidents, and clear technical handoffs.
