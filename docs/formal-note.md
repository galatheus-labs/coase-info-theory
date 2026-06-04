# Coase–Information Theory: formal note and demo plan

## Core thesis

Coase–Information Theory is a theory of agent boundaries. An agent may be an individual, team, firm, vendor network, software agent, or temporary coalition. Agents coalesce when shared representation and control reduce surprise, delay, error, and misalignment more than they increase coordination cost. Agents split when modularity and local autonomy reduce cost more than they increase interface surprise.

The boundary of the firm is therefore one case of a broader question:

> Where should an information-processing system draw boundaries between shared internal state and protocol-mediated coordination?

## Core mathematical framing

Let the environment generate a latent world state \(X_t\). Organizational nodes \(i \in V\) receive local observations \(Y_t^i\), exchange messages \(M_t^{ij}\) over a communication graph \(G\), and choose actions \(A_t^i\).

Nodes are recursive agents. A node can be a person, team, firm, vendor, software service, or composite group. Let \(\mathcal{B}\) be a partition of primitive actors into bounded agents. Boundary design chooses \(\mathcal{B}\) together with communication protocols and local policies.

A general organization is a distributed policy:

\[
A_t^i \sim \pi_i\big(Y_{\le t}^i, M_{\le t}^{*i}\big).
\]

Let organizational utility be \(U(X_t, A_t)\), where \(A_t\) is the joint action profile.
A Coase–Information Theory objective is:

\[
\max_{\mathcal{B}, \Pi, G} \; \mathbb{E}\Big[\sum_t U(X_t, A_t)\Big]
- C_{\text{comm}}
- C_{\text{compute}}
- C_{\text{delay}}
- C_{\text{misalign}}.
\]

This reframes transaction-cost economics as a distributed inference-and-control problem.

An idealized boundary objective is:

\[
\min_{\mathcal{B},\Pi,G} \; \mathbb{E}\left[S_t(\mathcal{B}) + L(X_t,A_t)\right] + C(\mathcal{B},G,\Pi),
\]

where \(S_t\) is surprise or prediction error under the agent's internal representation, \(L\) is action loss, and \(C\) includes communication, delay, monitoring, and governance costs.

## Agility

Define a decision-quality proxy by the mutual information between world state and action:

\[
Q_t := I(X_t ; A_t).
\]

Define organizational agility as the rate at which the organization turns relevant information into coordinated action:

\[
\mathcal{A}_t := \frac{I(X_t ; A_t)}{\tau_t},
\]

or a cost-adjusted version,

\[
\mathcal{A}_t^{(c)} := \frac{I(X_t ; A_t)}{\tau_t \cdot C_t}.
\]

Here \(\tau_t\) is end-to-end sensing-to-action latency.

## Compression view of organization

Roles, APIs, runbooks, dashboards, schemas, tickets, and operating cadences are compressed internal representations \(Z_t\):

\[
X_t \to Z_t \to A_t.
\]

The design problem is a rate-distortion problem: compress enough to coordinate efficiently, but not so much that critical decision information is lost.

## Software agents

Model a software agent as a node with observation channels, message space, policy, and tool interfaces:

\[
\text{Agent}_i = (\mathcal{O}_i, \mathcal{M}_i, \pi_i, \mathcal{T}_i).
\]

Agents change the cost surface by reducing structured communication cost, interpretation cost, and delay for routine or semi-structured tasks. They may also change monitoring and misalignment costs.

## Proposed propositions

1. **Protocol proposition.** Increasing machine-readable protocol quality increases effective decision-relevant throughput and reduces distortion.
2. **Agent proposition.** For structured tasks, software agents reduce sensing-to-action latency and can increase \(I(X_t;A_t)\) by improving routing and execution fidelity.
3. **Boundary proposition.** Agents coalesce or split according to whether shared representation reduces surprise and action loss more than it raises coordination cost.
4. **Agility proposition.** In volatile environments, organizations with higher \(\mathcal{A}_t\) dominate even when static coordination costs are not minimal.

## Why the web apps matter

The theory risks sounding abstract unless the reader can see the quantities move under realistic assumptions.

### 1. Topology lab
Use-case: compare hierarchy, market, and agentic mesh.
Paper connection: core theory section.
What it shows: as volatility and interdependence rise, organizations need more usable information-processing capacity. Protocols and agents can shift the best-fit topology.

### 2. Incident room
Use-case: deployment incident, customer escalation, vendor outage, lead routing failure.
Paper connection: agility section.
What it shows: delay and distortion become visible in stage-by-stage response time. Agentic systems reduce detection and triage latency when observability and protocols are strong.

### 3. Boundary explorer
Use-case: decide whether to keep work internal, outsource it, or use an agent-mediated hybrid boundary.
Paper connection: theory-of-the-firm section.
What it shows: machine-readable coordination reduces cross-boundary costs and creates a new region between classic hierarchy and classic market contracting.

### 4. Support router
Use-case: software-agent routing in support or internal service operations.
Paper connection: agents section.
What it shows: structured intake + policy coverage + agent autonomy increase first-touch accuracy and reduce handoffs, directly illustrating agents as organizational nodes.

## Best next paper structure

1. **Introduction.** Coase revisited under modern information-processing constraints.
2. **Formal model.** World state, partial observations, communication graph, actions, utility, and cost terms.
3. **Agility.** Define \(I(X_t;A_t)\), \(\tau_t\), and a cost-adjusted agility functional.
4. **Compression and internal representations.** Roles, APIs, metrics, and policies as information bottlenecks or accelerants.
5. **Software agents.** Agent nodes, structured protocols, tool use, governance, and failure modes.
6. **Boundary of the firm.** How agent-mediated coordination changes the efficient frontier.
7. **Illustrations / demos / empirical agenda.** Connect to incidents, support, routing, and vendor orchestration.

## Best empirical follow-up

Later, replace the toy models with real telemetry from:
- PagerDuty or incident logs
- Jira / Linear workflow traces
- Zendesk / Intercom support tickets
- Salesforce / HubSpot lead routing
- ERP or procurement approval traces

The most convincing paper will show that these quantities can be estimated, not merely discussed.
