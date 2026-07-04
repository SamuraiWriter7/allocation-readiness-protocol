# Changelog

All notable changes to the Allocation Readiness Protocol will be documented in this file.

---

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
