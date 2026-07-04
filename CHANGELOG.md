# Changelog

All notable changes to the Allocation Readiness Protocol will be documented in this file.

---

## v0.2.0-candidate — Blocking Rule Layer

### Added

* Allocation Blocking Rule Set schema
* machine-readable rule conditions
* rule priority
* rule enable / disable control
* `all` and `any` condition matching
* decision transition actions
* blocking issue generation
* severity classification
* human review requirements
* terminal rule behavior
* remediation actions
* required evidence declarations
* deterministic conflict resolution policy
* decision precedence
* default no-match behavior
* example blocking rule set
* validation target for the new v0.2 schema and example

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

v0.2 introduces explicit rule resolution behavior.

Supported strategies:

* `most_restrictive_decision`
* `highest_priority_first`

The default decision precedence is:

```text
rejected
disputed
blocked
pending_review
ready
```

### Remediation Model

Blocking rules can now define how a case may return to readiness assessment.

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

v0.2 formalizes the principle that a blocking decision should be explainable and, where appropriate, recoverable.

The protocol now supports the cycle:

```text
Readiness Check
      ↓
Rule Match
      ↓
Block or Review
      ↓
Remediation
      ↓
Evidence Update
      ↓
Reassessment
```

This release transforms allocation readiness from a static status record into a controlled transition layer between audit and royalty allocation.


## v0.1.0-candidate — Allocation Readiness Record

### Added

* Initial Allocation Readiness Record schema
* Machine-readable readiness checks
* Subject and upstream record references
* Readiness decision states
* Blocking issue records
* Human-review-aware decision logic
* Open-dispute blocking rules
* Ready-state validation constraints
* YAML example record
* Python validation script
* GitHub Actions validation workflow

### Readiness dimensions

The initial protocol evaluates:

* origin status
* derivative status
* contribution status
* audit status
* identity status
* license status
* human review status
* dispute status

### Decision states

The protocol defines:

* `ready`
* `pending_review`
* `blocked`
* `disputed`
* `rejected`

### Core principle

Audit completion does not automatically imply allocation readiness.

A case may remain blocked because of unresolved origin claims, derivative relationships, contribution assessment, identity binding, licensing conditions, human review requirements, or open disputes.

### Purpose

v0.1 establishes the minimal gate between audited provenance records and downstream royalty allocation systems.

### Important note

This protocol does not execute payments, determine legal ownership, calculate final royalty shares, or create legal royalty claims.

It records allocation readiness and preserves reasons for progression, review, blocking, dispute, or rejection.
