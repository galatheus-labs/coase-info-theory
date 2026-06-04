# App Model Assumptions

## Status of the current apps

The current web apps are illustrative toy models. They are designed to make comparative statics visible, not to provide calibrated causal estimates.

They are useful because they let a reader change variables that correspond to the paper's formal terms:

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

They should be presented as executable diagrams.

## Why the toy formulas are acceptable at this stage

The formulas are useful if the paper clearly states:

1. they are stylized,
2. coefficients are chosen for qualitative behavior,
3. the goal is to illustrate mechanisms,
4. real calibration is a future empirical step.

## How to calibrate later

For each app, replace arbitrary coefficients with estimates from traces.

### Topology Lab

Potential calibration data:

- number of teams involved,
- approval layers,
- observed response latency,
- message/meeting volume,
- action quality or rework rate.

### Incident Room

Potential calibration data:

- time to detect,
- time to triage,
- time to decision,
- time to resolution,
- number of people involved,
- reopens/rollbacks,
- severity reduction.

### Boundary Explorer

Potential calibration data:

- vendor onboarding time,
- contract cycle time,
- SLA misses,
- cross-boundary escalation latency,
- audit/review cost,
- rework/error rates.

### Support Router

Potential calibration data:

- first-touch resolution,
- handoffs per ticket,
- time to resolution,
- CSAT,
- reopen rate,
- policy coverage,
- agent escalation rate.

### Workflow Trace Mapper

This app is the bridge to real calibration. It accepts event traces and computes observable proxies that can later replace toy assumptions.

## Recommended language in the paper

Use language like:

> The apps are executable illustrations of the model. They are not calibrated causal estimates. Their purpose is to show how the formal quantities map onto observable workflow variables and to provide a path toward empirical calibration.

Avoid language like:

> The app proves that agentic organizations are better.

A better claim is:

> The app illustrates regions in which agentic coordination can dominate under the model's assumptions, especially when protocol quality and governance are high.
