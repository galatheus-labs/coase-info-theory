> Historical document. The canonical paper and `docs/revision-1.3-notes.md` supersede mathematical, measurement, and demo claims in this file.

# Coase–Information Theory: Agent Boundaries, Organizational Agility, and Software Agents

## Abstract

This paper proposes a Coase–Information Theory of agent boundaries. Classical transaction-cost economics explains the firm as an alternative to market coordination when internal organization is cheaper than contracting. We generalize this account by treating an agent as any bounded information-processing unit: an individual, team, organization, firm, vendor, software agent, or coalition of these. Boundaries form when agents coalesce into shared representations and control loops; boundaries dissolve or split when the cost of shared coordination exceeds its reduction in uncertainty, delay, error, or surprise. We decompose transaction and coordination costs into information-processing terms: sensing, communication, interpretation, monitoring, delay, error, and misalignment. We define organizational agility as the rate at which decision-relevant information about the world becomes effective action, formalized as an information-to-action rate. Software agents matter because they alter the cost surface of coordination: they can reduce communication, interpretation, and execution latency for structured tasks while introducing new governance and misalignment costs. This creates an agent-mediated design region between hierarchy and market, and a broader theory of when agents should merge, remain separate, or coordinate through protocols. We present a formal model, propositions, and executable toy applications that illustrate the theory and provide a path toward empirical calibration using workflow traces.

## 1. Introduction

Coase framed the firm as a response to the costs of using the price mechanism. Firms exist because contracting, searching, negotiating, monitoring, and enforcing every transaction through the market can be more costly than directing work internally. But modern organizations increasingly coordinate through software systems, APIs, observability pipelines, ticket queues, chat systems, workflow engines, and now software agents. These tools do not merely lower generic transaction costs. They change how information moves, how decisions are formed, and how quickly actions can be coordinated.

This suggests a sharper question:

> Given a changing environment, what organizational architecture best converts distributed, noisy information into coordinated action under latency, cost, and governance constraints?

The answer determines not only the boundary of the firm but also its agility. More generally, it determines which agents should coalesce into a larger agent, which agents should split apart, and which should remain separate but coupled through protocols.

This paper argues that the firm should be modeled as an information-processing and control system, but the same logic applies below and above the legal firm. A person, team, department, firm, vendor network, and software agent can each be treated as an agent if it has observations, internal state, policies, actions, and a boundary. Organizational structure is a communication graph. Roles, dashboards, runbooks, APIs, metrics, and managers are compression mechanisms. Software agents are organizational nodes with observation channels, message protocols, policies, and tool interfaces. The economic performance of the organization depends on the fidelity, speed, and cost with which latent world states are converted into action.

The key contribution is not the broad claim that firms process information. The stronger contribution is a formal decomposition of boundary formation, organizational cost, and agility that can be operationalized in software and workflow traces.

## 2. Formal model

Let the external or internal environment generate a latent state

\[
X_t \in \mathcal{X}
\]

at time \(t\). This state may include customer demand, a production incident, a supply shock, a workflow backlog, a vendor outage, or any other decision-relevant facts.

An organization is a directed graph

\[
G = (V,E),
\]

where nodes \(i \in V\) are humans, teams, services, vendors, or software agents. Edges \((i,j) \in E\) are communication or coordination channels.

The word agent is used recursively. A node may be a primitive actor, such as a person or software service, or a composite actor, such as a team, firm, platform, vendor network, or incident-response group. Let \(V_0\) be the set of primitive actors and let

\[
\mathcal{B} = \{B_1,\ldots,B_m\}
\]

be a partition of \(V_0\) into bounded agents. Each block \(B_\ell\) is an agent when its members share enough representation, policy, governance, and action interfaces to be treated as one decision-making unit at the relevant level of analysis.

Each node receives a local observation

\[
Y_t^i \sim P_i(Y \mid X_t),
\]

and may send messages

\[
M_t^{ij} \in \mathcal{M}_{ij}
\]

to neighboring nodes. Messages may be unstructured human communication, structured tickets, API calls, database writes, workflow events, or agent-generated summaries.

Each node maintains a compressed local representation

\[
Z_t^i = f_i(Y_{\leq t}^i, M_{\leq t}^{*i}),
\]

where \(M_{\leq t}^{*i}\) denotes messages received by node \(i\). Node \(i\) chooses an action according to a local policy

\[
A_t^i \sim \pi_i(Z_t^i).
\]

The organization produces a joint action

\[
A_t = g(A_t^1, \ldots, A_t^n),
\]

and receives utility

\[
U(X_t,A_t).
\]

The general organizational design problem is:

\[
\max_{\mathcal{B},G,\Pi,F} \; \mathbb{E}\left[\sum_t U(X_t,A_t)\right]
- C_{comm}
- C_{comp}
- C_{delay}
- C_{error}
- C_{misalign}
- C_{monitor}.
\]

Here \(\Pi = \{\pi_i\}\) is the set of local policies and \(F=\{f_i\}\) is the set of compression or representation maps.

The cost terms are:

| Term | Interpretation |
|---|---|
| \(C_{comm}\) | Meetings, messages, handoffs, routing, API calls, protocol overhead. |
| \(C_{comp}\) | Human or machine effort to analyze, summarize, decide, or execute. |
| \(C_{delay}\) | Loss from acting after the state has changed or the opportunity has decayed. |
| \(C_{error}\) | Loss from stale, incomplete, distorted, or misrouted information. |
| \(C_{misalign}\) | Loss from local actions that do not compose into good global action. |
| \(C_{monitor}\) | Governance, audit, review, compliance, and oversight burden. |

This decomposition is the Coase–Information move. Transaction cost is not a primitive. It is partly an information-processing quantity.

### Endogenous agent boundaries

The boundary of an agent determines which observations, representations, and actions are internal to a shared control loop and which must cross an interface. Internal coordination can preserve richer context and reduce surprise, but it also creates communication, governance, and computation costs. External coordination can reduce internal burden and preserve modularity, but it can increase interpretation, monitoring, contracting, and delay costs.

Let \(Z_t^B\) denote the internal representation held by a bounded agent \(B\). One idealized measure of surprise is:

\[
S_t^B = -\log P_B(X_t \mid Z_t^B),
\]

the degree to which the true state is unexpected under the agent's representation. In decision settings, the same role can be played by prediction error or action loss \(L(X_t,A_t^B)\). The boundary-design problem can then be stated as choosing a partition \(\mathcal{B}\) that trades off expected surprise and action loss against coordination cost:

\[
\min_{\mathcal{B},G,F,\Pi} \; \mathbb{E}\left[\sum_t S_t(\mathcal{B}) + L(X_t,A_t)\right] + C(\mathcal{B},G,F,\Pi).
\]

Two agents should coalesce when the merged boundary lowers expected surprise or action loss more than it raises internal coordination and governance cost:

\[
\mathbb{E}[S_{\mathrm{merged}} + L_{\mathrm{merged}}] + C_{\mathrm{merged}}
<
\mathbb{E}[S_{\mathrm{separate}} + L_{\mathrm{separate}}] + C_{\mathrm{separate}}.
\]

They should split when the inequality reverses. This makes the boundary of the firm a special case of a more general agent-boundary problem: where should the system draw the line between shared representation and protocol-mediated coordination?

## 3. Organizational agility

Speed alone is not agility. An organization can act quickly and incorrectly. Accuracy alone is not agility either. An organization can make a correct decision too late.

Let \(\tau_t\) be the end-to-end latency from signal availability to coordinated action. Let decision quality be proxied by the mutual information between the latent world state and organizational action:

\[
Q_t = I(X_t;A_t).
\]

Define organizational agility as:

\[
\mathcal{A}_t = \frac{I(X_t;A_t)}{\tau_t}.
\]

A cost-adjusted version is:

\[
\mathcal{A}^{(c)}_t = \frac{I(X_t;A_t)}{\tau_t C_t},
\]

where \(C_t\) is the resource cost of producing the action.

This definition captures the core intuition:

- higher information fidelity improves agility,
- lower latency improves agility,
- lower cost improves cost-adjusted agility,
- delay and distortion can both destroy organizational performance.

### Practical proxies

In most organizational traces, \(I(X_t;A_t)\) will not be directly observable. The empirical version should use proxies:

| Formal quantity | Operational proxy |
|---|---|
| \(I(X_t;A_t)\) | action correctness, SLA success, no rework, severity reduction, expert quality score |
| \(S_t\) or prediction surprise | unexpected escalation, reopen, SLA miss, anomaly, decision reversal, incident severity surprise |
| \(\tau_t\) | time to triage, time to decision, time to resolution |
| \(C_t\) | handoffs, people involved, messages, meetings, queue time, tool calls |
| \(C_{error}\) | reopen rate, rollback rate, bad routing, decision reversal |
| \(C_{monitor}\) | approvals, audits, review steps, escalation requirements |

The theory should be honest: mutual information is the idealized concept; workflow telemetry provides measurable proxies.

## 4. Compression and organizational structure

Organizations rarely transmit the full state \(X_t\). Instead, they construct internal representations:

\[
X_t \rightarrow Z_t \rightarrow A_t.
\]

Examples include:

- roles,
- dashboards,
- metrics,
- status reports,
- tickets,
- runbooks,
- APIs,
- schemas,
- plans,
- OKRs,
- approvals,
- incident summaries.

These are compression mechanisms. They reduce communication burden but can also destroy decision-relevant information.

The organizational design problem is a rate-distortion problem:

\[
\min_{f} \; C_{repr}(f) + \lambda \; \mathbb{E}[L(X_t,A_t(f(X_t)))],
\]

where \(C_{repr}(f)\) is the cost of maintaining and communicating representation \(f\), and \(L\) is decision loss.

A dashboard that compresses a complex operational state into one green/yellow/red indicator is valuable if it preserves the information needed for action. It is dangerous if it hides the structure needed for diagnosis.

## 5. Software agents as organizational nodes

A software agent can be modeled as a node:

\[
\mathrm{Agent}_i = (\mathcal{O}_i, \mathcal{M}_i, \pi_i, \mathcal{T}_i, \Gamma_i),
\]

where:

- \(\mathcal{O}_i\) is the set of observation channels,
- \(\mathcal{M}_i\) is the message schema or protocol,
- \(\pi_i\) is the local decision policy,
- \(\mathcal{T}_i\) is the set of tools or actuators,
- \(\Gamma_i\) is the governance envelope: permissions, constraints, auditability, and escalation rules.

Agents change the feasible set of organizational designs. They can:

- observe continuously,
- summarize and route information,
- enforce schemas,
- call tools,
- monitor queues,
- escalate uncertainty,
- execute routine actions.

But agentic coordination is not automatically superior. It may increase:

- local-global misalignment,
- proxy optimization,
- monitoring burden,
- structured propagation of bad assumptions,
- compression loss from over-summary.

The relevant comparison is conditional:

> Agents improve organizational agility when tasks are sufficiently structured, protocols are sufficiently expressive, and governance is strong enough to control misalignment.

## 6. Boundary of the firm

The boundary of the firm is one level of the broader boundary-selection problem. At any level, the question is whether coordination should happen through a shared internal representation or through an interface between separate agents.

Let \(k\) index a coordination form:

\[
k \in \{internal, market, hybrid\}.
\]

Each form has cost:

\[
C_k = C_{search,k} + C_{contract,k} + C_{comm,k} + C_{interp,k} + C_{monitor,k} + C_{delay,k} + C_{error,k} + C_{misalign,k}.
\]

The efficient boundary is selected by:

\[
k^* = \arg\min_k C_k - \mathbb{E}[U_k].
\]

Classical hierarchy reduces some contracting and search costs but can increase internal communication delay and bureaucratic compression. Market coordination can reduce internal burden but increase search, contracting, monitoring, and interpretation costs. Agent-mediated hybrid coordination can reduce cross-boundary interpretation and delay if protocols and governance are strong enough.

The claim is not that agents make firms smaller or markets always better. The claim is:

> Software agents and machine-readable protocols alter enough cost terms to create a new efficient region between classic hierarchy and classic market contracting.

The deeper claim is that firms, teams, vendors, and software agents are all boundary choices over information-processing units. Coalescence is valuable when shared state reduces surprise, delay, and misalignment more than it raises internal coordination cost. Splitting is valuable when modularity and local autonomy reduce cost more than they increase interface surprise.

## 7. Propositions

### Proposition 1 — Protocol informativeness

For a fixed organizational graph and decision policy class, improving protocol quality weakly increases achievable expected utility when it makes received representations more informative about the latent state without increasing delay or cost.

**Intuition.** A machine-readable schema, API, or structured ticket that preserves relevant state is a less garbled signal. Better downstream decisions become feasible.

### Proposition 2 — Latency under volatility

Suppose the relevance of information decays with environmental hazard rate \(\lambda\). If a decision is taken after latency \(\tau\), the value of otherwise correct information is approximately discounted by \(e^{-\lambda \tau}\). Therefore, the marginal value of latency reduction rises with volatility.

**Sketch.** If the probability that the relevant state remains stable after delay \(\tau\) is \(e^{-\lambda \tau}\), then effective information available for action is proportional to \(I_0 e^{-\lambda \tau}\). Higher \(\lambda\) makes delay more costly.

### Proposition 3 — Agentic routing

For structured or semi-structured workflows, agent nodes can increase organizational agility when their reduction in routing, interpretation, and execution latency exceeds their added monitoring and misalignment costs.

**Condition.** Agentic coordination improves cost-adjusted agility when

\[
\Delta C_{delay} + \Delta C_{comm} + \Delta C_{interp}
>
\Delta C_{monitor} + \Delta C_{misalign} + \Delta C_{error}.
\]

### Proposition 4 — Boundary coalescence and splitting

When cross-boundary communication, interpretation, and monitoring become programmable, the efficient boundary shifts toward the partition of agents that minimizes expected surprise, action loss, and coordination cost.

**Intuition.** APIs, schemas, shared observability, and agents reduce the information costs that traditionally made external coordination expensive. This can make splitting more attractive for modular work, while high interdependence can still make coalescence into a larger agent more efficient.

### Proposition 5 — Governance limit

Agentic decentralization has diminishing or negative returns when governance quality is low because autonomy can increase misalignment and monitoring costs faster than it reduces delay.

**Intuition.** A fast local optimizer is valuable only when its actions compose into the global objective.

## 8. Executable illustrations

The companion repo includes six static web apps.

### Topology Lab

Compares hierarchy, market coordination, and agentic mesh under shared environmental assumptions. It illustrates how volatility, interdependence, protocols, observability, approval layers, and agent coverage change estimated agility.

### Incident Room

Simulates deployment incidents, customer escalations, lead routing failures, and vendor outages. It makes delay and distortion visible through detection, triage, decision, and recovery stages.

### Boundary Explorer

Compares in-house, outsourced, and hybrid agentic boundary choices using decomposed cost terms.

### Agent Boundary Simulation

Runs a Monte Carlo model in which primitive agents observe a latent world state under alternative boundary partitions. It shows how protocol quality and task interdependence can create phase behavior across coalesced, split, market, and agent-mediated hybrid forms.

### Support Router

Shows a concrete software-agent workflow where structured intake, policy coverage, agent autonomy, and knowledge quality affect first-touch accuracy, handoffs, and resolution time.

### Workflow Trace Mapper

Accepts a simple CSV event trace and computes observable proxies: triage latency, resolution time, handoffs, agent-assisted share, rework, and an agility proxy. This is the bridge from toy models to empirical measurement.

## 9. Empirical agenda

A first empirical study should use incident response or support routing traces.

Minimal research design:

1. collect workflow traces,
2. map events to cases,
3. compute latency, handoffs, and action-quality proxies,
4. compare human-heavy, protocolized, and agent-assisted workflows,
5. estimate whether agentic coordination improves agility after controlling for case complexity.

A practical agility proxy can be:

\[
\widehat{\mathcal{A}} = \frac{Q}{1 + T_{resolution}} \cdot \frac{1}{1 + \alpha H},
\]

where \(Q\) is quality, \(T_{resolution}\) is resolution time, \(H\) is handoff count, and \(\alpha\) is a handoff penalty.

## 10. Limitations

This framework has several limitations.

First, mutual information is not directly observable in most organizations. The paper must distinguish the idealized formal quantity from operational proxies.

Second, agents do not universally improve coordination. They help most when workflows are structured, observability is high, and governance is clear.

Third, some organizational knowledge is tacit and difficult to encode into protocols. Over-protocolization can compress away context.

Fourth, the current apps are toy models. They illustrate mechanisms but do not yet estimate causal effects.

Fifth, organizational utility is multi-objective. Speed, accuracy, compliance, safety, morale, and strategic learning may trade off.

## 11. Conclusion

Coase–Information Theory reframes the firm as an information architecture. The key economic question is not only whether work should be coordinated by markets or hierarchy, but which agents should coalesce, which should split, and which should coordinate through protocols so that distributed observations become coordinated action.

Organizational agility is the rate of this transformation. Software agents matter because they can change the latency, fidelity, and cost of coordination. Their importance is not simply that they automate tasks. It is that they alter where boundaries should be drawn: inside firms, across teams, between vendors, and between human and machine actors.

The next generation of AI-native companies will be designed not merely around people using AI tools, but around software-mediated sensing, routing, decision, and execution loops. The purpose of Coase–Information Theory is to provide a language for designing and measuring those loops.
