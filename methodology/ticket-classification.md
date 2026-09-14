# Ticket Classification Guide

## Product defect
The current product does not behave according to expected or documented behavior.

Evidence should include reproducible steps whenever possible.

## User / configuration issue
The product behaves as designed, but account settings, permissions, browser state, or user actions cause the reported result.

A useful support response explains the cause and provides a safe resolution path.

## Feature request
The customer is asking for behavior the product does not currently provide.

Do not disguise missing functionality as a bug. Record the requested outcome and business use case.

## Unable to reproduce
Use only after reasonable investigation. Record what was tested, environment, result, and what evidence would be needed to continue.

This is not the same as proving that the customer did not experience the issue.

## Service incident
Use when symptoms indicate a shared service problem, outage, degraded dependency, or multi-user production impact.

Incident tickets should be linked to the operational incident rather than investigated as isolated customer bugs.

## Escalation tags used in this lab

- `ENG-BUG` — confirmed defect requiring engineering
- `SECURITY` — authorization/privacy/security concern
- `BILLING` — financial or payment impact
- `INCIDENT` — shared service degradation/outage
- `PRODUCT` — feature request/product decision
- `SUPPORT` — can be resolved without engineering
