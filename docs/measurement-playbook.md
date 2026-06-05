# Measurement Playbook

## Purpose

This playbook turns Coase–Information Theory from a conceptual framework into an instrumentation lens for real organizational workflows.

The objective is not to directly estimate Shannon mutual information in every setting. The objective is to estimate operational proxies for the theory's core quantities:

\[
\widehat{\mathcal{G}}_t \approx \frac{Q_t}{\tau_t(1+\widetilde C_t)}
\]

In practice:

- \(Q_t\), decision value, is proxied by decision/action quality or loss reduction,
- surprise is proxied by unexpected escalations, reopens, SLA misses, anomaly severity, or decision reversals,
- \(\tau_t\) is proxied by sensing-to-action latency,
- \(\widetilde C_t\) is proxied by handoffs, labor, events, messages, approvals, tool calls, or queue time.

## Minimal event schema

A useful trace can be as simple as:

```csv
case_id,timestamp,actor_type,owner,event_type,quality
INC-1,2026-06-04T09:00:00Z,system,observability,created,
INC-1,2026-06-04T09:03:00Z,agent,triage-bot,triage,
INC-1,2026-06-04T09:08:00Z,human,oncall,decision,
INC-1,2026-06-04T09:24:00Z,human,oncall,resolved,88
```

Recommended columns:

| Column | Meaning |
|---|---|
| `case_id` | Workflow case, incident, ticket, lead, request, etc. |
| `timestamp` | ISO timestamp for the event. |
| `actor_type` | `human`, `agent`, `system`, `vendor`, or `customer`. |
| `owner` | Responsible person, team, agent, vendor, or queue. |
| `event_type` | `created`, `triage`, `handoff`, `decision`, `action`, `resolved`, `reopened`, `rework`. |
| `quality` | Optional terminal quality score or outcome score. |

## Core metrics

### 1. Time to first triage

\[
T_{triage} = t_{first\;triage} - t_{created}
\]

Interpretation: sensing and routing latency.

### 2. Time to decision

\[
T_{decision} = t_{first\;decision} - t_{created}
\]

Interpretation: how long it takes the organization to select a coherent action.

### 3. Time to resolution

\[
T_{resolution} = t_{resolved} - t_{created}
\]

Interpretation: end-to-end organizational response time.

### 4. Handoff count

Count changes in `owner` within a case:

\[
H = \sum_k \mathbf{1}[owner_k \neq owner_{k-1}]
\]

Interpretation: coordination overhead and possible information-loss opportunities.

### 5. Agent-assisted share

\[
S_{agent} = \frac{\#\;agent\;events}{\#\;all\;events}
\]

Interpretation: degree of software-mediated coordination.

### 6. Rework/reopen count

Count events whose type includes `rework`, `reopen`, or `rollback`.

Interpretation: action error, distortion, or premature/incorrect decision-making.

### 7. Surprise proxy

Count or score events that show the agent's internal representation failed to anticipate the state:

- unexpected escalation,
- SLA miss,
- incident severity increase,
- decision reversal,
- customer-impacting anomaly,
- reopened or rerouted case.

Interpretation: boundary stress. If surprise concentrates at an interface between teams, vendors, queues, or software agents, the boundary may need better protocols, richer shared state, or a different partition of responsibility.

### 8. Action quality proxy

Use an observed outcome if available:

- incident severity reduction,
- customer satisfaction,
- SLA success,
- accepted lead routing,
- no rollback,
- no reopen,
- expert evaluation score.

If unavailable, use a coarse rubric:

| Score | Meaning |
|---|---|
| 100 | Correct first action, no rework, good outcome. |
| 80 | Correct path with minor delay. |
| 60 | Resolved but with significant handoffs or rework. |
| 40 | Wrong first action or customer-impacting delay. |
| 20 | Escalated failure. |

### 9. Practical agility proxy

A simple proxy:

\[
\widehat{\mathcal{A}} = \frac{Q}{1 + T_{resolution}} \cdot \frac{1}{1 + \alpha H}
\]

where:

- \(Q\) is quality on a 0–100 scale,
- \(T_{resolution}\) is time in hours,
- \(H\) is handoff count,
- \(\alpha\) is a handoff penalty such as 0.1.

This is not a direct mutual-information estimate. It is a practical operational proxy.

### 10. Boundary movement proxy

To study coalescing and splitting, compare whether a workflow performs better when work is:

- handled inside one bounded agent, such as one team or one software-mediated queue,
- split across separate agents with an explicit protocol,
- coordinated through a hybrid boundary, such as an agent-managed vendor or escalation path.

The empirical question is whether the boundary change lowers surprise and action loss enough to justify any added coordination or monitoring cost.

## Suggested first empirical case study

### Incident response

Why it is strong:

- has clear timestamps,
- has observable start and end points,
- involves routing, triage, escalation, and action,
- makes latency and misalignment visible,
- is legible to engineering and management readers.

Data sources:

- PagerDuty incidents,
- Slack incident channels,
- deployment logs,
- GitHub PR/revert events,
- Jira/Linear tickets,
- postmortems.

Paper mapping:

| Theory quantity | Incident trace proxy |
|---|---|
| \(X_t\) | true incident state / severity / root cause |
| \(Y_t^i\) | alerts, logs, customer reports, dashboards |
| \(M_t^{ij}\) | Slack messages, tickets, escalations, handoffs |
| \(a_t\) | mitigation, rollback, failover, customer communication |
| \(Q_t\) | action correctness / severity reduction / no rework |
| \(\tau_t\) | time to decision or resolution |
| \(C_t\) | handoffs, people involved, message volume, queue time |

## How to use the trace mapper app

Open `workflow-trace-mapper.html` and paste CSV data with the minimal schema above. The app will compute per-case metrics and aggregate proxies.

This gives the paper a companion method:

1. define the organizational trace,
2. estimate latency and handoffs,
3. score action quality,
4. compute an agility proxy,
5. compare human-heavy, agent-assisted, and protocolized workflows.

## What not to overclaim

Do not claim the proxy is literal mutual information unless the data supports such estimation. Instead, say:

> We use operational proxies for decision value per unit time. These proxies are designed to be observable in workflow traces and can later be refined into more direct information-theoretic estimates when ground-truth state labels are available.
