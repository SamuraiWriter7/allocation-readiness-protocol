# Allocation Readiness Protocol

A machine-readable protocol for determining whether audited traces, origin claims, derivative relationships, contribution records, and disputes are ready for royalty allocation.

## Purpose

AI agents can record actions.

Trace systems can preserve evidence.

Origin systems can register claims.

Audit systems can evaluate provenance and structural relationships.

Royalty systems can calculate and distribute value.

But an important question remains between audit and allocation:

> Is this case actually ready to proceed toward allocation?

The Allocation Readiness Protocol defines a machine-readable gate between audited provenance records and downstream royalty allocation systems.

It does not calculate royalty percentages.

It does not execute payments.

It does not determine legal ownership.

It records whether the required evidence, audit, identity, licensing, review, and dispute conditions are sufficiently resolved for a case to proceed.

---

## Core Flow

```text
Trace
  ↓
Origin Claim
  ↓
Derivative Record
  ↓
Contribution Assessment
  ↓
Audit
  ↓
Human Review
  ↓
Allocation Readiness
  ↓
Royalty Allocation
```

The protocol occupies the transition point between evidence review and economic allocation.

---

## v0.1 — Allocation Readiness Record

Version 0.1 introduces the minimal Allocation Readiness Record.

The record evaluates eight readiness dimensions:

* origin verification
* derivative resolution
* contribution assessment
* audit completion
* identity binding
* license status
* human review
* dispute status

The resulting decision uses one of the following states:

```text
ready
pending_review
blocked
disputed
rejected
```

---

## Core Principle

> Audit does not automatically imply allocation readiness.

A trace may exist while its origin remains uncertain.

An origin may be verified while a derivative relationship remains unresolved.

An audit may pass while a dispute is still open.

A contribution may be recorded while identity binding remains incomplete.

For this reason, allocation readiness is treated as an independent protocol stage.

---

## Decision Model

```text
Evidence
  │
  ▼
Readiness Checks
  │
  ├─ Origin verified?
  ├─ Derivative relation resolved?
  ├─ Contribution assessed?
  ├─ Audit passed?
  ├─ Identity bound?
  ├─ License permitted?
  ├─ Human review complete?
  └─ Dispute resolved?
  │
  ▼
Readiness Decision
```

A `ready` decision requires all applicable readiness checks to be satisfied.

Open disputes, pending human review, failed audits, and unresolved critical conditions prevent direct progression to allocation.

---

## Example

```yaml
decision:
  status: ready

  reason: >-
    Required provenance, contribution, audit, identity,
    license, and human-review checks are satisfied.

  decided_by: human_reviewer
```

The protocol also records blocking issues when a case cannot proceed.

```yaml
blocking_issues:
  - code: open_dispute
    severity: blocking
    message: Allocation cannot proceed while the dispute remains open.
```

---

## Design Boundaries

The Allocation Readiness Protocol does not:

* execute payments
* determine legal ownership
* calculate final royalty percentages
* automatically settle disputes
* replace human review
* create legal royalty claims
* guarantee economic value

Its purpose is readiness assessment and structured handoff.

---

## Repository Structure

```text
allocation-readiness-protocol/
├─ README.md
├─ CHANGELOG.md
├─ requirements.txt
├─ schemas/
│  └─ allocation-readiness-record.schema.json
├─ examples/
│  └─ allocation-readiness-record.example.yaml
├─ scripts/
│  └─ validate_examples.py
└─ .github/
   └─ workflows/
      └─ validate.yml
```

---

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

GitHub Actions automatically validates protocol examples against the JSON Schema.

---

## Roadmap

### v0.1 — Allocation Readiness Record

Define the minimal readiness record and decision states.

### v0.2 — Blocking Rule Layer

Formalize machine-readable reasons that prevent allocation progression.

### v0.3 — Contribution Claim Bundle

Bundle human, AI, source, tool, memory, and derivative contribution claims.

### v0.4 — Review and Dispute Gate

Formalize review routing, dispute windows, escalation, and final readiness decisions.

### v0.5 — Royalty OS Bridge

Define the structured handoff from allocation readiness into downstream royalty allocation systems.

---

## Protocol Position

```text
Trace Receipt
      ↓
Origin Verification
      ↓
Derivative Analysis
      ↓
Contribution Assessment
      ↓
Synchronization Audit
      ↓
Human Review
      ↓
Allocation Readiness Protocol
      ↓
Royalty OS
```

The Allocation Readiness Protocol is the final gate before value allocation begins.

Its responsibility is simple:

> Record when a value trace is ready to move from audited provenance into economic circulation.
