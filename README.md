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

## v0.2 — Blocking Rule Layer

Version 0.2 introduces a machine-readable Blocking Rule Layer.

The Allocation Readiness Record defined in v0.1 records the current readiness state of a case.

The Blocking Rule Layer defines how specific readiness conditions affect downstream progression.

```text
Readiness State
       ↓
Rule Matching
       ↓
Blocking Decision
       ↓
Issue Record
       ↓
Remediation Action
       ↓
Reassessment
```

Each blocking rule can define:

* rule identity
* priority
* matching conditions
* resulting decision status
* blocking issue code
* severity
* human review requirement
* terminal or non-terminal behavior
* remediation action
* required evidence

### Example rule flow

```text
Open Dispute
      ↓
Rule Match
      ↓
Decision: disputed
      ↓
Allocation progression suspended
      ↓
Human review
      ↓
Dispute resolution evidence
      ↓
Readiness reassessment
```

### Rule Resolution

v0.2 supports explicit rule conflict resolution.

The default decision precedence is:

```text
rejected
   ↓
disputed
   ↓
blocked
   ↓
pending_review
   ↓
ready
```

A rule set may use either:

* `most_restrictive_decision`
* `highest_priority_first`

The rule layer does not itself execute royalty allocation or settle disputes.

Its purpose is to provide a deterministic, reviewable explanation of why a case may or may not proceed.

### Core Principle

> A blocking decision should not be a dead end.

Whenever remediation is possible, the protocol records the next required action and the evidence needed for reassessment.

This creates a reusable cycle:

```text
Detect
  ↓
Block
  ↓
Explain
  ↓
Repair
  ↓
Reassess
```

The Blocking Rule Layer therefore transforms allocation readiness from a static checklist into a controlled transition system.

## v0.3 — Contribution Claim Bundle

Version 0.3 introduces the Contribution Claim Bundle.

The Allocation Readiness Protocol can determine whether a case is ready to proceed and which conditions may block that progression.

Before readiness can be meaningfully evaluated, however, contribution claims must be collected in a structured and reviewable form.

The Contribution Claim Bundle records:

* who claims contribution
* what type of contribution is claimed
* which part of the subject the claim concerns
* what evidence supports the claim
* how the claim relates to other claims
* whether the claim has been assessed
* whether conflicts have been detected

### Core Flow

```text
Actor
  ↓
Contribution Claim
  ↓
Evidence
  ↓
Relationship
  ↓
Assessment
  ↓
Conflict Detection
  ↓
Allocation Readiness
```

### Contribution Types

The initial vocabulary includes:

* human question
* human direction
* concept origin
* structural design
* AI transformation
* AI analysis
* AI verification
* source contribution
* tool contribution
* memory contribution
* derivative transformation
* review contribution

The protocol intentionally separates different contribution roles.

An originating question, an AI transformation, a source contribution, and a verification action are not assumed to be economically equivalent.

v0.3 records these roles without assigning final royalty percentages.

### Claim and Assessment Separation

A claimant may assert a contribution.

That assertion is not automatically treated as verified.

```text
Claimant Assertion
        ↓
Evidence
        ↓
Assessment
        ↓
Supported / Partial / Unsupported / Disputed
```

This separation preserves the difference between:

* what is claimed
* what is evidenced
* what has been reviewed

### Contribution Relationships

Contribution claims may reference dependencies and influence relationships.

```text
Human Question
      ↓
AI Transformation
      ↓
Verification
      ↓
Reviewed Contribution Bundle
```

This allows the bundle to represent a minimal contribution graph rather than a flat participant list.

### Conflict Detection

The protocol can flag possible conflicts including:

* duplicate claims
* overlapping scope
* origin conflicts
* evidence conflicts
* identity conflicts
* license conflicts
* allocation conflicts

Conflict flags do not automatically resolve disputes.

They identify cases that may require review or escalation.

### Bundle Assessment

A Contribution Claim Bundle may be classified as:

* unassessed
* pending
* assessed
* disputed
* blocked

Its allocation eligibility may be:

* eligible for readiness check
* requires review
* blocked
* disputed

### Core Principle

> Participation is not the same as contribution, and contribution is not the same as allocation.

v0.3 separates these stages.

```text
Participation
      ↓
Contribution Claim
      ↓
Evidence
      ↓
Assessment
      ↓
Readiness
      ↓
Allocation
```

The Contribution Claim Bundle creates the reviewable bridge between activity records and downstream economic allocation.

## v0.4 — Review / Dispute Gate

Version 0.4 introduces a procedural Review and Dispute Gate.

The Contribution Claim Bundle introduced in v0.3 can identify overlapping scopes, conflicting origin claims, evidence conflicts, identity conflicts, license conflicts, and other contribution-related issues.

v0.4 defines how these cases move through a structured review and resolution process.

### Core Flow

```text
Conflict Detection
        ↓
Review Routing
        ↓
Participant Notification
        ↓
Dispute Window
        ↓
Evidence Submission
        ↓
Response / Counterclaim
        ↓
Review Findings
        ↓
Resolution
        ↓
Readiness Handoff
```

The Review / Dispute Gate does not determine royalty percentages.

Its purpose is to provide procedural structure before unresolved contribution claims are allowed to proceed toward economic allocation.

### Review Routing

Cases may use different review routes:

* single review
* multi-stage review
* Multi-Wing review followed by human decision
* human-only review
* mediation followed by review

The protocol can explicitly preserve human final authority.

```yaml
review_route:
  route_type: multi_wing_then_human
  human_final_authority: true
```

This allows AI systems to organize evidence, detect inconsistencies, compare claims, and generate review recommendations while preserving final human authority where required.

### Dispute Window

v0.4 introduces explicit dispute windows.

A case can record:

* opening time
* closing time
* current window status
* late submission policy
* extension reasons

Late submission policies include:

* rejection
* manual exception review
* acceptance with a procedural flag

The dispute window prevents unresolved claims from remaining procedurally open indefinitely.

### Submissions and Counterclaims

Participants may submit:

* initial statements
* responses
* evidence
* counter-evidence
* clarifications
* responses to reviewer requests

The protocol also supports structured counterclaims.

Counterclaims may challenge a contribution claim on grounds including:

* prior origin
* scope overlap
* insufficient evidence
* incorrect attribution
* license restriction
* identity mismatch

This converts disagreement into a reviewable procedural record.

### Review Findings

Review findings are separate from final resolution decisions.

A finding may concern:

* origin
* scope
* evidence
* identity
* licensing
* contribution
* procedure

Each finding may be classified as:

* supported
* partially supported
* unsupported
* inconclusive

This separation preserves the difference between factual assessment and final case disposition.

### Resolution

Resolution decisions may include:

* claims confirmed
* claims modified
* claim removed
* bundle returned for reassessment
* case rejected
* no resolution

A resolution may also specify required updates to upstream records, including:

* claim scope changes
* assessment status changes
* new evidence attachment
* unsupported claim removal
* conflict flag resolution
* identity updates
* license status updates

### Readiness Handoff

A resolved case does not automatically enter royalty allocation.

The Review / Dispute Gate may return the case to:

* allocation readiness reassessment
* contribution assessment
* audit
* continued blocking
* terminal rejection

```text
Resolution
    ↓
    ├─ Readiness Reassessment
    ├─ Contribution Reassessment
    ├─ Audit
    ├─ Remain Blocked
    └─ Rejected
```

### Core Principle

> Conflict should suspend automatic allocation, but conflict resolution should create a structured path back into the protocol lifecycle.

v0.4 therefore establishes the cycle:

```text
Detect
  ↓
Review
  ↓
Challenge
  ↓
Submit Evidence
  ↓
Decide
  ↓
Repair Records
  ↓
Reassess
```

The Review / Dispute Gate adds procedural fairness to the transition from contribution evidence toward value allocation.



