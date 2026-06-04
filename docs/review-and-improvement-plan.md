# Review and Improvement Plan

## Overall assessment

The project has a real and differentiated center: it connects Coase, information theory, organizational agility, and software agents in a way that can support both a paper and founder thought leadership.

The current repo already does three useful things:

1. gives the paper a clear conceptual spine,
2. makes the theory visual through simple web apps,
3. positions software agents as organizational nodes rather than merely productivity tools.

The main weakness is that the current artifacts still feel like a well-structured concept packet. To become publication-grade and founder-grade, the project needs a stronger empirical bridge, sharper mathematical claims, clearer limits, and a more explicit failure-mode story.

## Highest-leverage improvements

### P0 — Add one empirical spine

The most important improvement is to select one real workflow and carry it through the paper and apps.

Best candidates:

- incident response,
- support routing,
- vendor outage coordination,
- datacenter change management.

The repo now includes `workflow-trace-mapper.html` as the first bridge from toy slider models to real trace data. The point is not to prove the whole theory immediately. The point is to show that the quantities in the theory can be estimated from real organizational traces.

Minimum empirical schema:

- case id,
- timestamp,
- actor type,
- owner,
- event type,
- optional quality/outcome score.

From this, we can compute:

- time to first triage,
- time to resolution,
- handoff count,
- event count,
- agent-assisted share,
- rework/reopen count,
- resolution-quality proxy,
- agility proxy.

### P0 — Tighten the math

The current math is directionally good but still broad. The paper should sharpen around a few formal moves:

1. Treat the organization as a graph of partially informed decision nodes.
2. Treat agility as information-to-action rate.
3. Treat organizational artifacts as compression maps.
4. Treat agents as nodes with different cost, latency, and governance profiles.
5. Treat boundary choice as a minimization over internal, external, and hybrid cost functions.

The improved paper draft in `paper/coase-information-theory-draft.md` adds these pieces.

### P1 — Reframe the apps as instruments

The apps should be described as instruments for reasoning, not calibrated models.

Current problem:

- the sliders are useful but can look arbitrary,
- the coefficients are not explained,
- the apps risk seeming like persuasive dashboards rather than measurement tools.

Improvement:

- explicitly label them as toy/comparative models,
- document assumptions,
- add trace import,
- create a path from toy coefficients to real telemetry.

The new `docs/app-model-assumptions.md` and `workflow-trace-mapper.html` support this.

### P1 — Add failure modes

The software-agent story should not sound like “agents always improve organizations.” That would weaken credibility.

The paper should include at least four failure modes:

1. local agent optimization can damage global coordination,
2. low-quality protocols can propagate structured error faster,
3. excessive autonomy can increase monitoring and governance burden,
4. agentic systems can compress away context that humans would have preserved.

The best claim is contingent:

> Agents improve organizational agility when tasks are sufficiently structured, protocols are sufficiently expressive, and governance is strong enough to control local-global misalignment.

### P1 — Make the Coase contribution explicit

The novelty is not merely “firms process information.” That idea has a long history.

The stronger contribution is:

> Coasean transaction costs can be decomposed into communication, interpretation, monitoring, delay, error, and misalignment costs; software agents alter these terms enough to create a new efficient region between hierarchy and market.

This should appear in the abstract, introduction, and conclusion.

### P2 — Improve repo structure

The repo should evolve from static demo files into a public research artifact.

Suggested future structure:

```text
paper/
  coase-information-theory.tex or .md
  figures/
apps/
  topology-lab/
  incident-room/
  boundary-explorer/
  support-router/
  workflow-trace-mapper/
docs/
  measurement-playbook.md
  app-model-assumptions.md
  review-and-improvement-plan.md
sample-data/
  incident-trace.csv
  support-ticket-trace.csv
```

For now, the updated repo keeps static HTML at the root for easy local use.

## What to cut or avoid

Avoid these traps:

- too many equations without propositions,
- too many management buzzwords,
- claims that agents replace firms or make hierarchy obsolete,
- pretending mutual information is easy to measure directly in most orgs,
- presenting toy coefficients as calibrated facts.

## Recommended founder/thought-leadership package

The best public bundle is:

1. arXiv working paper,
2. demo repo,
3. short founder essay,
4. one 5-minute walkthrough video,
5. one real or semi-real workflow trace showing the measurement lens.

The thought-leadership positioning should be:

> AI-native companies are not just companies with AI tools. They are organizations whose sensing, routing, decision, and execution loops are increasingly software-mediated. Coase–Information Theory gives a language for designing those loops.

## Immediate next work

1. Choose the empirical spine.
2. Replace one toy scenario with a real or synthetic-but-realistic trace.
3. Write the paper draft to 8–12 pages.
4. Add a diagram of the organization as a graph.
5. Add one boundary-choice example with numbers.
6. Add a limitations section.
7. Publish the repo as companion material.
