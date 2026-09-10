> Historical document. The canonical paper and `docs/revision-1.3-notes.md` supersede mathematical, measurement, and demo claims in this file.

# App Model Assumptions

## Status of the current example site

The canonical example site is `index.html`. The older prototype pages redirect there so public readers do not land on stale concepts.

The current simulation is an illustrative model. It is designed to make comparative statics visible, not to provide calibrated causal estimates.

It is useful because it lets a reader choose paper-aligned use cases and change variables that correspond to the formal terms:

- protocol quality,
- agent coverage,
- observability,
- approval depth,
- task complexity,
- vendor trust,
- compliance pressure,
- monitoring load,
- modularity,
- asset specificity.

The current scenarios are:

- incident response as a temporary bounded agent,
- support routing and workflow traces,
- vendor/API boundary coordination,
- internal service modularization,
- blueprint-heavy versus reactive planning,
- classical in-house capability formation.

They should be presented as executable diagrams.

## Why the toy formulas are acceptable at this stage

The formulas are useful if the paper clearly states:

1. they are stylized,
2. coefficients are chosen for qualitative behavior,
3. the goal is to illustrate mechanisms,
4. real calibration is a future empirical step.

## How to calibrate later

For the canonical simulation, replace arbitrary coefficients with estimates from traces.

### Incident response

Potential calibration data:

- time to detect,
- time to triage,
- time to decision,
- time to resolution,
- number of people involved,
- reopens/rollbacks,
- severity reduction.

### Vendor/API boundary

Potential calibration data:

- vendor onboarding time,
- contract cycle time,
- SLA misses,
- cross-boundary escalation latency,
- audit/review cost,
- rework/error rates.

### Agent boundary simulation

Potential calibration data:

- ground-truth incident or ticket state labels,
- team or vendor ownership partitions,
- cross-boundary handoff latency,
- reopen/escalation/surprise events,
- action correctness or expert outcome scores,
- protocol maturity and schema completeness,
- monitoring and governance effort.

The boundary simulation is a computational illustration of the formal objective. It should be read as: under these modeled coefficients, protocol quality and task interdependence change which boundary partition minimizes surprise, action loss, and coordination cost.

### Support routing

Potential calibration data:

- first-touch resolution,
- handoffs per ticket,
- time to resolution,
- CSAT,
- reopen rate,
- policy coverage,
- agent escalation rate.

### Workflow traces

Workflow traces are the bridge to real calibration. Incident and support CSV samples are included as starting points for observable proxies that can later replace toy assumptions.

## Recommended language in the paper

Use language like:

> The apps are executable illustrations of the model. They are not calibrated causal estimates. Their purpose is to show how the formal quantities map onto observable workflow variables and to provide a path toward empirical calibration.

Avoid language like:

> The app proves that agentic organizations are better.

A better claim is:

> The app illustrates regions in which agentic coordination can dominate under the model's assumptions, especially when protocol quality and governance are high.
