# Changelog

All notable changes to the Allocation Readiness Protocol are documented in this file.

The protocol follows a staged first arc:

```text
Readiness
    ↓
Blocking
    ↓
Contribution
    ↓
Review / Dispute
    ↓
Royalty OS Handoff
```

---

## v0.5.0-candidate — Royalty OS Bridge

### Overview

v0.5 introduces the Royalty OS Bridge and completes the first protocol arc.

This release defines a machine-readable handoff package for transferring reviewed, resolved, and allocation-ready contribution records into downstream royalty allocation systems.

The bridge does not assign final percentages or execute payments.

Its responsibility is safe and reviewable protocol handoff.

### Added

* Royalty OS Handoff schema
* source protocol declaration
* subject records
* allocation eligibility gate
* upstream protocol references
* contribution candidate records
* eligible claim references
* excluded claim references
* evidence and decision basis references
* calculation policy references
* settlement policy references
* calculation authority declaration
* percentage assignment boundary
* payment execution boundary
* policy flags
* integrity hash metadata
* immutable reference declaration
* generation authority
* generation timestamp
* signature references
* previous handoff references
* destination records
* destination types
* transport modes
* acknowledgement requirements
* transfer lifecycle states
* downstream acknowledgement records
* rejection reason handling
* Royalty OS Handoff example
* validation target for the v0.5 schema and example

### Eligibility Gate

The handoff package can confirm:

* readiness status
* origin status
* derivative status
* contribution bundle status
* audit status
* identity status
* license status
* human review status
* conflict status
* dispute status
* allocation eligibility

The bridge is intended for reviewed and allocation-ready cases.

### Allocation Input Package

The handoff package can identify:

* candidate contributions
* claimant references
* contribution types
* assessment results
* inclusion states
* eligibility reasons
* eligible claims
* excluded claims
* decision basis records
* calculation policy
* settlement policy

### Protocol Boundary

v0.5 explicitly preserves the separation between readiness and downstream allocation.

```text
percentage_assignment_status:
  not_assigned_by_this_protocol

payment_execution_status:
  not_executed_by_this_protocol
```

The Allocation Readiness Protocol does not determine final royalty percentages or execute payment.

### Integrity Layer

The handoff package may include:

* hash algorithm
* package hash
* immutable reference status
* generation authority
* generation timestamp
* signature reference
* previous handoff reference

This protects the transition between reviewed protocol state and downstream economic processing.

### Destination Model

Supported destination types include:

* `royalty_os`
* `allocation_engine`
* `settlement_preprocessor`
* `manual_review_queue`

Supported transport modes include:

* `protocol_record`
* `api`
* `queue`
* `file_exchange`
* `manual_import`

### Transfer Lifecycle

v0.5 introduces:

* `prepared`
* `submitted`
* `accepted`
* `rejected`
* `acknowledged`

Accepted and acknowledged transfers may include downstream receipt records.

Rejected transfers require a reason.

### First Arc Completion

v0.5 completes:

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

The first arc now supports:

```text
Evidence
   ↓
Contribution Claim
   ↓
Assessment
   ↓
Conflict Review
   ↓
Resolution
   ↓
Readiness
   ↓
Royalty OS Handoff
```

### Core Principle

> Allocation readiness is permission to enter economic evaluation, not a final economic judgment.

---

## v0.4.0-candidate — Review / Dispute Gate

### Overview

v0.4 introduces the procedural layer required when contribution claims, origin assertions, evidence records, identity conditions, license conditions, or allocation eligibility are contested.

The release creates a structured path from conflict detection to resolution and readiness reassessment.

### Added

* Review / Dispute Gate schema
* procedural case records
* subject references
* review trigger records
* participant roles
* notification status
* review routing
* reviewer types
* human final authority flag
* review scope control
* case lifecycle states
* dispute windows
* dispute window status
* late submission policies
* extension reasons
* participant submissions
* evidence submission records
* response records
* clarification records
* counterclaims
* counterclaim grounds
* review findings
* escalation policies
* escalation triggers
* escalation routes
* resolution records
* resolution decisions
* resolution finality states
* required upstream record updates
* readiness handoff records
* example resolved review case
* validation target for the v0.4 schema and example

### Review Triggers

Supported triggers include:

* `claim_conflict`
* `manual_review`
* `blocking_rule`
* `audit_exception`
* `license_issue`
* `identity_issue`
* `open_dispute`
* `other`

### Participant Roles

Supported roles include:

* `claimant`
* `respondent`
* `reviewer`
* `mediator`
* `human_gate`
* `observer`

### Review Routes

Supported review routes include:

* `single_review`
* `multi_stage_review`
* `multi_wing_then_human`
* `human_only`
* `mediation_then_review`

The protocol can explicitly preserve human final authority.

### Case Lifecycle

v0.4 introduces:

* `queued`
* `under_review`
* `awaiting_response`
* `disputed`
* `escalated`
* `resolved`
* `closed_without_resolution`

### Dispute Window

The protocol can record:

* opening time
* closing time
* current status
* late submission policy
* extension reason

Supported late submission handling includes:

* `reject`
* `manual_exception_review`
* `accept_with_flag`

### Counterclaims

Counterclaims can challenge claims because of:

* prior origin
* scope overlap
* insufficient evidence
* incorrect attribution
* license restriction
* identity mismatch
* other grounds

### Review Findings

Finding types include:

* origin finding
* scope finding
* evidence finding
* identity finding
* license finding
* contribution finding
* procedural finding

Finding status may be:

* supported
* partially supported
* unsupported
* inconclusive

### Escalation

Supported triggers include:

* material evidence conflict
* reviewer deadlock
* identity failure
* license uncertainty
* procedural violation
* human request
* other defined conditions

Supported routes include:

* senior human review
* independent review panel
* mediation
* external legal review
* return to audit
* manual case management

### Resolution

Initial resolution decisions include:

* `claims_confirmed`
* `claims_modified`
* `claim_removed`
* `bundle_returned_for_reassessment`
* `case_rejected`
* `no_resolution`

Resolution records may require:

* claim scope updates
* assessment status updates
* new evidence attachment
* unsupported claim removal
* conflict flag resolution
* identity binding updates
* license status updates

### Readiness Handoff

Resolved cases may be routed to:

* allocation readiness reassessment
* contribution reassessment
* audit
* continued blocking
* terminal rejection

### Core Principle

> Conflict should suspend automatic allocation, but conflict resolution should create a structured path back into the protocol lifecycle.

The protocol now supports:

```text
Conflict
   ↓
Review
   ↓
Evidence
   ↓
Counterclaim
   ↓
Finding
   ↓
Resolution
   ↓
Record Repair
   ↓
Reassessment
```

---

## v0.3.0-candidate — Contribution Claim Bundle

### Overview

v0.3 introduces a structured contribution layer between trace evidence and allocation readiness.

The release provides a machine-readable format for recording:

* who claims contribution
* what type of contribution is claimed
* which part of the subject is affected
* what evidence supports the claim
* how the claim relates to other contributions
* whether the claim has been assessed
* whether conflicts have been detected

### Added

* Contribution Claim Bundle schema
* subject records
* upstream trace references
* origin references
* derivative references
* claimant actor records
* actor types
* identity status
* contribution type vocabulary
* claim scope records
* artifact references
* contribution time windows
* evidence records
* evidence types
* contribution relationship records
* dependency references
* influence references
* claimant assertions
* claimed importance levels
* contribution assessment states
* formal assessment records
* assessor types
* evidence sufficiency status
* conflict flags
* bundle-level assessment
* claim count fields
* allocation eligibility status
* review references
* dispute references
* Contribution Claim Bundle example
* validation target for the v0.3 schema and example

### Contribution Types

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

### Actor Types

Contribution claims may be associated with:

* human
* AI model
* AI agent
* organization
* source
* tool
* memory system
* mixed actor structure

### Evidence Types

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

### Assessment States

Contribution claims may be:

* `unassessed`
* `pending`
* `supported`
* `partially_supported`
* `unsupported`
* `disputed`

Claims with completed assessment outcomes require an assessment record.

### Relationship Model

Supported contribution relationships include:

* originating
* derivative
* transformative
* supporting
* verification-only
* unknown

Claims may also reference dependencies and influence relationships.

This allows contribution records to form a minimal causal graph.

### Conflict Flags

Initial conflict types include:

* `duplicate_claim`
* `scope_overlap`
* `origin_conflict`
* `evidence_conflict`
* `identity_conflict`
* `license_conflict`
* `allocation_conflict`
* `other`

### Bundle Assessment

Contribution bundles may record:

* bundle status
* claim count
* supported claim count
* pending claim count
* disputed claim count
* conflict status
* allocation eligibility
* assessment summary

### Core Principle

> Participation is not the same as contribution, and contribution is not the same as allocation.

The lifecycle becomes:

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
```

---

## v0.2.0-candidate — Blocking Rule Layer

### Overview

v0.2 introduces a machine-readable rule layer for determining why a case is blocked, deferred, disputed, or rejected.

The release transforms allocation readiness from a static state record into a controlled transition system.

### Added

* Allocation Blocking Rule Set schema
* machine-readable rule conditions
* rule identity
* rule priority
* rule enable / disable state
* `all` matching
* `any` matching
* decision transition actions
* blocking issue generation
* severity classification
* human review requirements
* terminal rule behavior
* remediation actions
* required evidence declarations
* conflict resolution strategy
* decision precedence
* default behavior
* example blocking rule set
* validation target for the v0.2 schema and example

### Initial Blocking Rules

The example rule set introduces handling for:

* open disputes
* failed audits
* restricted licenses
* unknown licenses
* unverified origins
* unresolved derivative relationships
* unassessed contributions
* unbound identities
* incomplete human review

### Resolution Policy

Supported rule resolution strategies include:

* `most_restrictive_decision`
* `highest_priority_first`

The default precedence is:

```text
rejected
disputed
blocked
pending_review
ready
```

### Remediation Actions

Initial remediation actions include:

* `verify_origin`
* `resolve_derivative`
* `assess_contribution`
* `rerun_audit`
* `bind_identity`
* `clarify_license`
* `complete_human_review`
* `resolve_dispute`
* `provide_evidence`
* `manual_review`

### Core Principle

> A blocking decision should not be an unexplained dead end.

Where remediation is possible, the protocol records:

* why the case was stopped
* what action must occur next
* what evidence is needed
* how the case may return to reassessment

The control cycle is:

```text
Detect
  ↓
Block
  ↓
Explain
  ↓
Repair
  ↓
Evidence Update
  ↓
Reassess
```

---

## v0.1.0-candidate — Allocation Readiness Record

### Overview

v0.1 introduces the minimal Allocation Readiness Record.

The release defines a machine-readable structure for determining whether an audited value trace is ready to proceed toward downstream royalty allocation.

### Added

* Allocation Readiness Record schema
* protocol version metadata
* record identity
* creation timestamp
* subject records
* subject types
* upstream trace references
* origin references
* derivative references
* contribution references
* audit references
* readiness checks
* readiness decision states
* blocking issue records
* decision reason
* decision authority
* decision timestamp
* human-review-aware validation
* dispute-aware validation
* ready-state constraints
* YAML example
* Python validation script
* GitHub Actions validation workflow
* initial README
* initial changelog

### Readiness Dimensions

The first release evaluates:

* origin status
* derivative status
* contribution status
* audit status
* identity status
* license status
* human review status
* dispute status

### Decision States

The protocol introduces:

* `ready`
* `pending_review`
* `blocked`
* `disputed`
* `rejected`

### Ready-State Constraints

A `ready` decision requires applicable readiness conditions to be satisfied.

For example:

* failed audit cannot be marked ready
* open dispute cannot be marked ready
* pending required human review cannot be marked ready
* unresolved critical readiness conditions cannot be silently treated as ready

### Blocking Issues

Initial issue codes include:

* `unverified_origin`
* `unresolved_derivative`
* `contribution_unassessed`
* `audit_failed`
* `identity_unbound`
* `license_unknown`
* `license_restricted`
* `human_review_required`
* `open_dispute`
* `missing_evidence`
* `other`

### Core Principle

> Audit completion does not automatically imply allocation readiness.

A case may remain blocked because of:

* unresolved origin
* unresolved derivative relationships
* incomplete contribution assessment
* identity conditions
* license uncertainty
* pending human review
* open dispute

v0.1 establishes the minimal procedural gate between audited provenance and downstream economic allocation.

---

# First Arc Summary

The first protocol arc evolves as follows:

```text
v0.1
Record whether a case is ready.
        ↓
v0.2
Explain why it is blocked and how it can return.
        ↓
v0.3
Structure who contributed what and why.
        ↓
v0.4
Review and resolve contribution conflicts.
        ↓
v0.5
Transfer approved cases into downstream Royalty OS processing.
```

The complete lifecycle is:

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
Blocking / Review
  ↓
Dispute Resolution
  ↓
Record Repair
  ↓
Readiness
  ↓
Integrity
  ↓
Royalty OS Handoff
```

The first arc establishes a procedural bridge between:

> **audited contribution causality**

and:

> **downstream value circulation**

