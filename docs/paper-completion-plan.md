# Paper completion plan

## Immediate goal
Turn the current concept into a paper package that feels both formal and real:

1. a crisp paper draft,
2. a demo suite,
3. one reality-backed worked example.

## Step 1 — lock the core claim
Use two linked sentences throughout the paper:

> Coase–Information Theory is a theory of agent boundaries: agents coalesce when shared representation reduces surprise and action loss more than it raises coordination cost, and split when modularity lowers cost more than it raises interface surprise.
>
> Organizational agility is the rate at which an agent converts distributed, noisy information into coordinated action under latency and cost constraints.

That is the center of gravity. The firm is a special case, not the outer limit of the theory.

## Step 2 — stabilize notation
Use one notation set only:

- `X_t`: world state
- `Y_t^i`: local observation at node `i`
- `M_t^{ij}`: message from `i` to `j`
- `A_t^i`: local action
- `A_t`: aggregate organizational action
- `G=(V,E)`: organizational graph
- `𝓑`: partition of primitive actors into bounded agents
- `S_t`: surprise or prediction error under an agent's representation
- `τ_t`: sensing-to-action latency
- `I(X_t;A_t)`: decision-quality proxy
- `𝒜_t`: agility

## Step 3 — keep four propositions
Do not sprawl. Keep the paper organized around four propositions:

1. better protocols reduce distortion,
2. lower latency matters more in volatile environments,
3. software agents can raise agility for structured tasks,
4. programmable cross-boundary coordination changes when agents should coalesce, split, or remain separate.

## Step 4 — make one workflow the empirical spine
Best candidates:

- incident response,
- support routing,
- vendor coordination,
- datacenter change management.

Choose one and map the workflow into:

- nodes,
- messages,
- delays,
- escalations,
- error modes,
- outcome quality.

## Step 5 — use the apps as exhibits
The apps should appear in the paper as executable illustrations of the propositions:

- `topology-lab.html` for comparative organizational form,
- `incident-room.html` for agility under stress,
- `boundary-explorer.html` for firm-boundary analysis,
- `support-router.html` for software-agent coordination.

## Step 6 — finish a submission-grade bundle
A strong submission bundle would contain:

- 6–10 page paper draft,
- appendix with toy equations and simulation assumptions,
- repo of demos,
- one worked example from a real workflow.

## Most important risk
The main risk is conceptual drift into vague AI-organization commentary.

Avoid that by always returning to:

- agent boundaries,
- surprise reduction,
- information quality,
- latency,
- cost,
- coordination architecture,
- and agility.
