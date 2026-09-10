> Historical document. The canonical paper and `docs/revision-1.3-notes.md` supersede mathematical, measurement, and demo claims in this file.

# Coase–Information Theory: formal note and demo plan

## Core thesis

Coase–Information Theory is a theory of agent boundaries. An agent may be an individual, team, firm, vendor network, software agent, or temporary coalition. Agents coalesce when shared representation and control reduce surprise, delay, error, and misalignment more than they increase coordination cost. Agents split when modularity and local autonomy reduce cost more than they increase interface surprise.

The boundary of the firm is therefore one case of a broader question:

> Where should an information-processing system draw boundaries between shared internal state and protocol-mediated coordination?

## Core mathematical framing

Let the environment generate a latent world state \(X_t\). Organizational nodes \(i \in V\) receive local observations \(Y_t^i\), exchange messages \(M_t^{ij}\) over a communication graph \(G\), and choose actions \(a_t^i\).

Nodes are recursive agents. A node can be a person, team, firm, vendor, software service, or composite group. Let \(\mathcal{B}\) be a partition of primitive actors into bounded agents. Boundary design chooses \(\mathcal{B}\) together with communication protocols and local policies.

A general organization is a distributed policy:

\[
a_t^i \sim \pi_i\big(Y_{\le t}^i, M_{\le t}^{*i}\big).
\]

Let organizational utility be \(U(X_t, a_t)\), where \(a_t\) is the joint action profile.
A Coase–Information Theory objective is:

\[
\max_{\mathcal{B}, \Pi, G} \; \mathbb{E}\Big[\sum_t U(X_t, a_t)\Big]
- C_{\text{comm}}
- C_{\text{compute}}
- C_{\text{interp}}
- C_{\text{delay}}
- C_{\text{misalign}}.
\]

This reframes transaction-cost economics as a distributed inference-and-control problem.

An idealized boundary objective is:

\[
\min_{\mathcal{B},\Pi,G} \; \mathbb{E}\left[S_t(\mathcal{B}) + L(X_t,a_t)\right] + C(\mathcal{B},G,\Pi),
\]

where \(S_t\) is surprise or prediction error under the agent's internal representation, \(L\) is action loss, and \(C\) includes communication, delay, monitoring, and governance costs.

## Agility

Define decision value as loss reduction relative to a baseline action:

\[
Q_t := \mathbb{E}[L(X_t,a_t^0)-L(X_t,a_t)].
\]

Define organizational agility as the rate at which the organization turns relevant information into coordinated action:

\[
\mathcal{G}_t := \frac{Q_t}{\tau_t},
\]

or a cost-adjusted version,

\[
\mathcal{G}_t^{(c)} := \frac{Q_t}{\tau_t(1+\widetilde C_t)}.
\]

Here \(\tau_t\) is end-to-end sensing-to-action latency and \(\widetilde C_t\) is a normalized resource-cost index. Mutual information remains useful as an idealized fidelity proxy, but decision value is the primary quality quantity.

## Compression view of organization

Roles, APIs, runbooks, dashboards, schemas, tickets, and operating cadences are compressed internal representations \(Z_t\):

\[
X_t \to Z_t \to a_t.
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
2. **Agent proposition.** For structured tasks, software agents reduce sensing-to-action latency and can increase decision value by improving routing and execution fidelity.
3. **Boundary proposition.** Agents coalesce or split according to whether shared representation reduces surprise and action loss more than it raises coordination cost.
4. **Agility proposition.** In volatile environments, organizations with higher \(\mathcal{A}_t\) dominate even when static coordination costs are not minimal.

## Why the example site matters

The theory risks sounding abstract unless the reader can see the quantities move under realistic assumptions. The canonical example site is `index.html`; the older prototype pages redirect there.

### 1. Incident response
Use-case: SRE, support, product, infrastructure, vendor, and agent traces during an outage.
Paper connection: running example.
What it shows: an incident room can become a temporary bounded agent when shared representation beats interface delay.

### 2. Support routing and workflow traces
Use-case: software-agent routing in support or internal service operations.
Paper connection: agentic-routing proposition and empirical agenda.
What it shows: structured intake, policy coverage, and governed autonomy can reduce handoffs and improve decision value per unit time.

### 3. Vendor/API boundary
Use-case: decide whether a capability should remain external, move in-house, or use an agent-mediated hybrid boundary.
Paper connection: theory-of-the-firm section.
What it shows: machine-readable coordination can reduce cross-boundary interpretation costs and create a region between classic hierarchy and classic market contracting.

### 4. Internal service modularization
Use-case: teams or services split into bounded modules.
Paper connection: interdependence and modularity proposition.
What it shows: high protocol quality and moderate interdependence can make internal mini-monoliths cheaper than one large boundary.

### 5. Blueprint-heavy versus reactive planning
Use-case: datacenter or infrastructure planning.
Paper connection: executable illustration.
What it shows: plans are information investments: they reduce runtime surprise in stable environments but add up-front delay and rigidity under volatility.

## Best next paper structure

1. **Introduction.** Coase revisited under modern information-processing constraints.
2. **Formal model.** World state, partial observations, communication graph, actions, utility, and cost terms.
3. **Agility.** Define \(Q_t\), \(\tau_t\), and a cost-adjusted agility functional.
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
