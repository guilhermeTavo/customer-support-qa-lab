# Customer Support QA & Bug Triage Lab

A hands-on portfolio project that simulates a SaaS support operation and demonstrates how customer-reported problems move from first contact to investigation, bug triage, engineering handoff, retest, and customer communication.

**Project page:** https://guilhermetavo.github.io/customer-support-qa-lab/

## Project goal

The goal of this lab is to show a practical QA + Technical Support workflow rather than a collection of isolated test cases. The project focuses on turning incomplete customer reports into reproducible technical evidence and clear next actions.

## What this project demonstrates

- Support ticket triage
- Troubleshooting and reproduction
- Bug vs. user error vs. feature request classification
- Severity and priority assessment
- Clear bug reports for engineering
- Customer-facing communication
- Escalation decisions
- Retesting and closure criteria
- Basic operational metrics

## Pilot dataset

This repository uses a fictional SaaS product and a controlled set of 20 support tickets created specifically for this portfolio exercise. The tickets are not production data and do not represent a benchmark of any real company.

### Pilot outcome

| Metric | Result |
| --- | ---: |
| Tickets reviewed | 20 |
| Confirmed product defects | 9 |
| User/configuration issues | 4 |
| Feature requests | 3 |
| Unable to reproduce | 2 |
| Service incidents | 2 |
| Engineering escalations | 11 |
| High/Critical defects | 4 |

## Workflow

`Ticket intake → clarify → reproduce → classify → prioritize → document → escalate → retest → close`

## Repository structure

```text
customer-support-qa-lab/
├── README.md
├── triage-playbook.md
├── methodology/
│   ├── severity-priority.md
│   └── ticket-classification.md
├── tickets/
│   └── support-tickets.csv
├── results/
│   ├── triage-results.csv
│   ├── defect-summary.md
│   └── operations-report.md
├── bug-reports/
│   ├── BUG-001.md
│   ├── BUG-002.md
│   ├── BUG-003.md
│   └── BUG-004.md
├── scripts/
│   └── analyze_tickets.py
└── docs/
    ├── index.html
    ├── project-summary.md
    └── interview-guide.md
```

## Featured cases

### BUG-001 — Password reset loop
Users can successfully reset their password but are redirected back to the reset flow instead of the application. Classified as **High severity / P1 priority** because it blocks account access for affected users.

### BUG-002 — Duplicate subscription charge
A retry after a payment timeout can create two successful charges while the UI reports a single purchase. Classified as **Critical severity / P0 priority** because it creates direct financial impact.

### BUG-003 — Mobile settings page unusable
At 360 px width, the Save button is rendered outside the viewport and cannot be reached without changing orientation. Classified as **Medium severity / P2 priority**.

### BUG-004 — Team member can view restricted billing data
A user with a non-billing role can open a billing details endpoint from a previously copied URL. Classified as **Critical severity / P0 priority** because it is an authorization defect involving sensitive account data.

## Quick links

- [Project page](https://guilhermetavo.github.io/customer-support-qa-lab/)
- [Triage playbook](triage-playbook.md)
- [Support tickets](tickets/support-tickets.csv)
- [Triage results](results/triage-results.csv)
- [Defect summary](results/defect-summary.md)
- [Operations report](results/operations-report.md)
- [Interview guide](docs/interview-guide.md)

## Skills demonstrated

`Technical Support` · `Manual QA` · `Bug Triage` · `Troubleshooting` · `Defect Reporting` · `Severity/Priority` · `Customer Communication` · `Engineering Escalation` · `Retesting` · `SaaS Support`

## Author

**Guilherme Tavares**  
QA Analyst · AI Quality · Technical Support · Web Development
