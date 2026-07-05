# Allocation Readiness Protocol

A machine-readable protocol for determining whether audited traces, origin claims, derivative relationships, contribution records, and disputes are ready to proceed toward royalty allocation.

---

## Overview

AI agents can record actions.

Trace systems can preserve evidence.

Origin systems can register claims.

Derivative systems can describe transformation relationships.

Audit systems can evaluate provenance and structural consistency.

Royalty systems can calculate and distribute value.

However, an important procedural gap exists between audit and allocation:

> Is this case actually ready to enter economic allocation?

The **Allocation Readiness Protocol** defines a machine-readable gate between audited contribution evidence and downstream royalty systems.

It provides structured records and rules for:

* readiness assessment
* blocking conditions
* remediation paths
* contribution claims
* contribution evidence
* contribution relationships
* conflict detection
* review procedures
* dispute handling
* resolution
* readiness reassessment
* Royalty OS handoff

The protocol does not calculate royalty percentages.

It does not execute payments.

It does not determine legal ownership.

Its role is to determine whether a contribution case is structurally and procedurally ready to proceed toward downstream economic evaluation.

---

## Why This Protocol Exists

A completed audit does not automatically imply allocation readiness.

For example:

```text
Trace exists                  ✓
Origin verified               ✓
Derivative relationship known ✓
Audit passed                  ✓

But...

Identity unresolved           ×
License unclear               ×
Contribution claim disputed   ×
Human review pending          ×
```

Such a case should not be transferred directly into royalty calculation.

The Allocation Readiness Protocol introduces an independent procedural layer:

```text
Evidence
   ↓
Contribution Assessment
   ↓
Conflict Review
   ↓
Dispute Resolution
   ↓
Readiness Decision
   ↓
Royalty OS Handoff
```

The protocol therefore separates:

```text
Evidence
≠
Contribution

Contribution
≠
Allocation Eligibility

Allocation Eligibility
≠
Percentage Assignment

Percentage Assignment
≠
Payment Execution
```

---

## Core Principle

> Value should not enter economic circulation before its evidence, contribution relationships, conflicts, and procedural conditions have been reviewed.

The protocol is built around five questions:

```text
v0.1
Is this case ready?

v0.2
Why is it blocked,
and how can it return?

v0.3
Who contributed what,
and what evidence supports the claim?

v0.4
What happens when claims conflict?

v0.5
How is an approved case safely handed
to a downstream Royalty OS?
```

---

# Protocol Architecture

The first protocol arc consists of five layers.

```text
Trace / Origin / Derivative
          ↓
┌──────────────────────────────┐
│ v0.1 Allocation Readiness    │
│ Record                       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ v0.2 Blocking Rule Layer     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ v0.3 Contribution Claim      │
│ Bundle                       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ v0.4 Review / Dispute Gate   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ v0.5 Royalty OS Bridge       │
└──────────────┬───────────────┘
               ↓
        Royalty Allocation
               ↓
           Settlement
```

---

# v0.1 — Allocation Readiness Record

v0.1 introduces the minimal record for determining whether a subject is ready to proceed toward allocation.

The record evaluates eight readiness dimensions:

* origin status
* derivative status
* contribution status
* audit status
* identity status
* license status
* human review status
* dispute status

The readiness decision uses one of the following states:

```text
ready
pending_review
blocked
disputed
rejected
```

A `ready` decision requires all applicable conditions to be satisfied.

Examples of invalid transitions include:

```text
audit_status: failed
decision.status: ready
```

and:

```text
dispute_status: open
decision.status: ready
```

The Allocation Readiness Record therefore acts as the first formal gate between review and economic progression.

---

## Readiness Flow

```text
Upstream Evidence
      ↓
Readiness Checks
      │
      ├─ Origin verified?
      ├─ Derivative resolved?
      ├─ Contributions assessed?
      ├─ Audit passed?
      ├─ Identity ready?
      ├─ License permitted?
      ├─ Human review complete?
      └─ Dispute resolved?
      │
      ▼
Decision
```

---

# v0.2 — Blocking Rule Layer

v0.2 transforms readiness assessment from a static checklist into a controlled transition system.

The Blocking Rule Layer defines:

* what condition triggers a block
* which decision state follows
* which issue code is recorded
* how severe the issue is
* whether human review is required
* whether the rule is terminal
* what remediation action is required
* what evidence is needed for reassessment

The core lifecycle is:

```text
Readiness State
      ↓
Rule Matching
      ↓
Decision
      ↓
Blocking Issue
      ↓
Remediation
      ↓
Evidence Update
      ↓
Reassessment
```

---

## Initial Blocking Conditions

The initial rule layer can handle conditions including:

* open disputes
* failed audits
* restricted licenses
* unknown licenses
* unverified origins
* unresolved derivative relationships
* unassessed contributions
* unbound identities
* incomplete human review

---

## Rule Matching

Rules support:

```text
all
any
```

A rule may activate only when all conditions match, or when any listed condition matches.

---

## Decision Resolution

Multiple rules may match the same readiness case.

Supported strategies include:

```text
most_restrictive_decision
highest_priority_first
```

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

---

## Remediation

A block should not always be a dead end.

Where recovery is possible, a rule may define a next action such as:

* verify origin
* resolve derivative relationship
* assess contribution
* rerun audit
* bind identity
* clarify license
* complete human review
* resolve dispute
* provide evidence
* perform manual review

The resulting cycle is:

```text
Detect
  ↓
Block
  ↓
Explain
  ↓
Repair
  ↓
Provide Evidence
  ↓
Reassess
```

---

# v0.3 — Contribution Claim Bundle

v0.3 introduces a structured, evidence-linked contribution layer.

Before a case can be evaluated fairly for allocation readiness, the protocol must be able to answer:

> Who contributed what?

> What kind of contribution was it?

> Which part of the subject does it concern?

> What evidence supports the claim?

> How does it relate to other contributions?

The Contribution Claim Bundle records:

* claimant identity
* actor type
* contribution type
* claim scope
* artifact references
* contribution time window
* evidence
* causal relationships
* claimant assertion
* assessment status
* formal assessment
* conflict flags
* bundle-level assessment

---

## Contribution Types

The initial vocabulary includes:

* `human_question`
* `human_direction`
* `concept_origin`
* `structural_design`
* `ai_transformation`
* `ai_analysis`
* `ai_verification`
* `source_contribution`
* `tool_contribution`
* `memory_contribution`
* `derivative_transformation`
* `review_contribution`
* `other`

The protocol intentionally separates different contribution roles.

For example:

```text
Human
  Originating Question
          ↓
AI Agent
  Structural Transformation
          ↓
Verification Wing
  Verification Contribution
```

These are related contributions, but they are not assumed to be identical or economically equivalent.

---

## Participation Is Not Contribution

The core principle of v0.3 is:

> Participation is not the same as contribution, and contribution is not the same as allocation.

The lifecycle is therefore separated:

```text
Participation
      ↓
Contribution Claim
      ↓
Evidence
      ↓
Assessment
      ↓
Conflict Review
      ↓
Allocation Readiness
      ↓
Royalty Allocation
```

---

## Evidence Model

Every contribution claim requires evidence.

Initial evidence types include:

* trace receipt
* source interaction
* timestamp record
* diff record
* audit record
* human attestation
* tool log
* memory trace
* derivative record
* other evidence

A contribution claim is not automatically a verified contribution.

The protocol separates:

```text
Claim
  ↓
Evidence
  ↓
Assessment
```

---

## Claimant Assertion and Independent Assessment

A claimant may assert:

```text
This contribution was critical.
```

The assessment process may still determine:

```text
supported

partially_supported

unsupported

disputed
```

This preserves the distinction between:

* what is claimed
* what is evidenced
* what is independently assessed

---

## Contribution Relationships

Claims may describe causal relationships.

Supported relationship roles include:

* originating
* derivative
* transformative
* supporting
* verification-only
* unknown

Claims may also reference:

* claims they depend on
* claims they influence

This enables a minimal contribution causality graph:

```text
Human Question
      ↓
AI Transformation
      ↓
Verification
      ↓
Reviewed Contribution Bundle
```

The Contribution Claim Bundle is therefore not a participant list.

It is a machine-readable representation of contribution causality.

---

## Conflict Detection

v0.3 can flag:

* duplicate claims
* scope overlap
* origin conflict
* evidence conflict
* identity conflict
* license conflict
* allocation conflict
* other conflicts

Conflict detection does not resolve the dispute.

It routes the case toward the Review / Dispute Gate.

---

# v0.4 — Review / Dispute Gate

v0.4 introduces a procedural layer for contested contribution cases.

A conflict can originate from:

* contribution claim conflict
* manual review
* blocking rule
* audit exception
* license issue
* identity issue
* open dispute
* another procedural trigger

The core lifecycle is:

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
Record Repair
        ↓
Readiness Reassessment
```

---

## Review Routes

Supported routes include:

* single review
* multi-stage review
* Multi-Wing review followed by human decision
* human-only review
* mediation followed by review

The protocol can preserve human final authority.

Example:

```yaml
review_route:
  route_type: multi_wing_then_human
  reviewer_type: hybrid_review_panel
  human_final_authority: true
```

This allows AI systems to assist with:

* evidence organization
* claim comparison
* inconsistency detection
* review recommendations

while preserving final human authority where required.

---

## Participant Roles

Supported procedural roles include:

* claimant
* respondent
* reviewer
* mediator
* human gate
* observer

The protocol can also record notification status:

```text
pending
notified
acknowledged
not_required
```

---

## Dispute Window

v0.4 introduces procedural time boundaries.

A dispute window may be:

* scheduled
* open
* closed
* extended
* waived

Late submissions may be:

* rejected
* routed to manual exception review
* accepted with a procedural flag

This prevents allocation cases from remaining indefinitely open without procedural boundaries.

---

## Submissions and Counterclaims

Participants may submit:

* initial statements
* responses
* evidence
* counter-evidence
* clarifications
* reviewer-request responses

Counterclaims may challenge a claim because of:

* prior origin
* scope overlap
* insufficient evidence
* incorrect attribution
* license restriction
* identity mismatch
* another specified basis

The protocol converts informal disagreement into a structured review record.

---

## Review Findings

Review findings are separate from final case resolution.

A finding may concern:

* origin
* scope
* evidence
* identity
* license
* contribution
* procedure

Finding states include:

* supported
* partially supported
* unsupported
* inconclusive

For example:

```text
Finding 1
Human origin claim supported

Finding 2
AI transformation claim supported

Finding 3
Scope overlap can be resolved
        ↓
Final Resolution
Claims modified
```

This allows multiple facts to be evaluated before a final procedural decision.

---

## Escalation

Cases may be escalated because of:

* material evidence conflict
* reviewer deadlock
* identity failure
* license uncertainty
* procedural violation
* human request
* another specified condition

Possible escalation routes include:

* senior human review
* independent review panel
* mediation
* external legal review
* return to audit
* manual case management

---

## Resolution

Resolution outcomes include:

* claims confirmed
* claims modified
* claim removed
* bundle returned for reassessment
* case rejected
* no resolution

A resolution may require upstream record repair, including:

* claim scope updates
* assessment status updates
* additional evidence
* unsupported claim removal
* conflict flag resolution
* identity binding updates
* license status updates

The principle is:

> Resolution should repair the protocol state, not merely close the case.

---

## Readiness Handoff

A resolved case does not automatically enter royalty calculation.

It may return to:

* readiness reassessment
* contribution reassessment
* audit
* continued blocking
* terminal rejection

```text
Resolution
    ↓
    ├─ Readiness Reassessment
    ├─ Contribution Reassessment
    ├─ Return to Audit
    ├─ Remain Blocked
    └─ Rejected
```

---

# v0.5 — Royalty OS Bridge

v0.5 completes the first protocol arc.

It defines a machine-readable handoff from Allocation Readiness into downstream Royalty OS processing.

The bridge transfers:

* approved readiness state
* assessed contribution claims
* audit references
* origin references
* derivative references
* review references
* dispute resolution references
* eligible claim references
* excluded claim references
* policy references
* integrity information
* destination information
* transfer status
* acknowledgement

The core flow is:

```text
Audited Evidence
      ↓
Reviewed Contribution
      ↓
Resolved Conflict
      ↓
Allocation Ready
      ↓
Royalty OS Handoff
      ↓
Royalty Calculation
      ↓
Settlement
```

---

## Eligibility Gate

A Royalty OS Handoff requires an explicit eligibility gate.

The package confirms that applicable conditions have been satisfied:

```text
Readiness        = ready
Origin           = verified
Derivative       = resolved
Contribution     = assessed
Audit            = passed
Identity         = bound
License          = permitted
Human Review     = completed
Conflict         = none / resolved
Dispute          = none / resolved
```

Incomplete cases should not enter downstream allocation systems as if they were finalized.

---

## Allocation Input Package

The Royalty OS Bridge packages the minimum structured input required for downstream economic evaluation.

It identifies:

* candidate contributions
* eligible claims
* excluded claims
* evidence and decision basis
* calculation policy references
* settlement policy references
* calculation authority
* policy flags

A candidate contribution may include:

* claim reference
* claimant reference
* contribution type
* assessment status
* inclusion status
* inclusion or exclusion reason

---

## Protocol Boundary

The bridge explicitly preserves the boundary between readiness and economic calculation.

```text
Eligible Contribution
        ≠
Percentage Assigned
        ≠
Payment Executed
```

The handoff therefore records:

```text
percentage_assignment_status:
  not_assigned_by_this_protocol

payment_execution_status:
  not_executed_by_this_protocol
```

The downstream Royalty OS remains responsible for:

* valuation
* weighting
* percentage calculation
* allocation policy
* settlement policy
* payment execution

---

## Integrity Layer

The handoff package may include:

* hash algorithm
* package hash
* immutable reference state
* generation authority
* generation timestamp
* signature reference
* previous handoff reference

The integrity layer protects the boundary between reviewed protocol state and downstream allocation processing.

```text
Reviewed Records
      ↓
Integrity Package
      ↓
Royalty OS Handoff
      ↓
Acknowledgement
```

---

## Destination Model

Supported destination types include:

* Royalty OS
* allocation engine
* settlement preprocessor
* manual review queue

Supported transport modes include:

* protocol record
* API
* queue
* file exchange
* manual import

The bridge remains implementation-neutral.

---

## Transfer Lifecycle

The handoff lifecycle includes:

```text
prepared
   ↓
submitted
   ↓
accepted
   ↓
acknowledged
```

or:

```text
submitted
   ↓
rejected
```

A downstream acknowledgement can record:

* acknowledgement identity
* receiving timestamp
* receiving system
* acceptance state
* optional message

This preserves receipt continuity across the protocol boundary.

---

# First Arc

Versions v0.1 through v0.5 form the first complete arc of the Allocation Readiness Protocol.

```text
v0.1
Allocation Readiness Record
        ↓
v0.2
Blocking Rule Layer
        ↓
v0.3
Contribution Claim Bundle
        ↓
v0.4
Review / Dispute Gate
        ↓
v0.5
Royalty OS Bridge
```

Together, they create a controlled path from evidence to downstream value circulation.

```text
Trace
  ↓
Origin
  ↓
Derivative
  ↓
Contribution Claim
  ↓
Evidence
  ↓
Assessment
  ↓
Conflict Detection
  ↓
Review / Dispute
  ↓
Resolution
  ↓
Readiness
  ↓
Integrity Check
  ↓
Royalty OS Handoff
```

---

# Repository Structure

```text
allocation-readiness-protocol/
├─ README.md
├─ CHANGELOG.md
├─ requirements.txt
│
├─ schemas/
│  ├─ allocation-readiness-record.schema.json
│  ├─ allocation-blocking-rule-set.schema.json
│  ├─ contribution-claim-bundle.schema.json
│  ├─ review-dispute-gate.schema.json
│  └─ royalty-os-handoff.schema.json
│
├─ examples/
│  ├─ allocation-readiness-record.example.yaml
│  ├─ allocation-blocking-rule-set.example.yaml
│  ├─ contribution-claim-bundle.example.yaml
│  ├─ review-dispute-gate.example.yaml
│  └─ royalty-os-handoff.example.yaml
│
├─ scripts/
│  └─ validate_examples.py
│
└─ .github/
   └─ workflows/
      └─ validate.yml
```

---

# Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected validation flow:

```text
[validate] Allocation Readiness Record
[ok] allocation-readiness-record.example.yaml is valid

[validate] Allocation Blocking Rule Set
[ok] allocation-blocking-rule-set.example.yaml is valid

[validate] Contribution Claim Bundle
[ok] contribution-claim-bundle.example.yaml is valid

[validate] Review and Dispute Gate
[ok] review-dispute-gate.example.yaml is valid

[validate] Royalty OS Handoff
[ok] royalty-os-handoff.example.yaml is valid

[success] All examples are valid.
```

GitHub Actions automatically validates protocol examples against their JSON Schemas.

---

# Design Boundaries

The Allocation Readiness Protocol does not:

* calculate royalty percentages
* assign monetary values
* execute payments
* determine legal ownership
* replace courts or legal processes
* automatically resolve every dispute
* treat all participation as contribution
* treat all claims as valid
* bypass human review requirements
* grant AI systems automatic final authority
* guarantee economic value
* guarantee settlement

Its purpose is:

> To determine whether contribution evidence is procedurally ready to enter downstream economic evaluation.

---

# Protocol Position

```text
Question / Action
       ↓
Trace Receipt
       ↓
Origin Verification
       ↓
Derivative Analysis
       ↓
Contribution Claim Bundle
       ↓
Blocking Rule Evaluation
       ↓
Review / Dispute Gate
       ↓
Resolution
       ↓
Allocation Readiness
       ↓
Royalty OS Bridge
       ↓
Royalty Allocation
       ↓
Settlement
```

The Allocation Readiness Protocol occupies the procedural boundary between:

```text
What happened?
```

and:

```text
How should value be distributed?
```

---

# Civilizational Position

The protocol is based on a simple observation:

AI systems are becoming increasingly capable of:

* generating artifacts
* transforming prior work
* calling tools
* using external sources
* collaborating with humans
* collaborating with other agents
* operating across long chains of actions

As this activity grows, activity logs alone are insufficient.

Economic systems require a more structured transition:

```text
Action
  ↓
Trace
  ↓
Contribution
  ↓
Evidence
  ↓
Review
  ↓
Resolution
  ↓
Readiness
  ↓
Allocation
```

The Allocation Readiness Protocol defines the procedural gate in that transition.

Its role is not to decide all value.

Its role is to prevent unresolved evidence, claims, conflicts, and permissions from silently becoming economic facts.

---

# Status

The first protocol arc is defined through:

```text
v0.1.0-candidate
v0.2.0-candidate
v0.3.0-candidate
v0.4.0-candidate
v0.5.0-candidate
```

The current first-arc endpoint is:

> **v0.5 — Royalty OS Bridge**

The protocol now provides a machine-readable path from audited contribution evidence to downstream value allocation systems.




