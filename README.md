# Coase–Information Theory Demo Repo

This repo packages a small set of static web apps plus formal paper material for the **Coase–Information Theory** project.

The central claim is:

> Firms are a special case of agent-boundary formation. Agents coalesce when shared representation reduces surprise and action loss more than it raises coordination cost, and split when modularity lowers cost more than it raises interface surprise.

The practical implication:

> Organizations are information architectures. Their economic performance depends on how efficiently they convert distributed, noisy signals into coordinated action under latency, cost, and distortion constraints.

The browser demo translates that claim into tangible software.

The current example site follows the paper's main use cases:

- incident response as a temporary bounded agent,
- support routing and workflow traces,
- vendor/API boundaries,
- internal service modularization,
- blueprint-heavy versus reactive planning,
- classical in-house versus market coordination.

## Contents

### App

- `index.html` — the canonical browser simulation. It runs the scenario-driven Monte Carlo model where paper use cases map into the same abstract boundary levers: protocol quality, interdependence, observability, agent coverage, governance, market friction, volatility, and planning depth.

The earlier prototype pages now redirect to `index.html` so old links do not open stale concepts.

### Paper and analysis

- `paper/coase-information-theory.tex` — canonical working-paper source
- `paper/coase-information-theory.pdf` — rendered working-paper PDF
- `paper/coase-information-theory-draft.md` — earlier prose draft, retained for reference
- `docs/formal-paper-analysis.md` — original mathematical framing, propositions, agent extension, and completion plan
- `docs/formal-note.md` — compact note tying the apps back to the theory
- `docs/paper-completion-plan.md` — concrete path from note to finished paper
- `docs/review-and-improvement-plan.md` — review of the current work and prioritized improvements
- `docs/measurement-playbook.md` — how to estimate theory quantities from workflow traces
- `docs/app-model-assumptions.md` — assumptions and calibration plan for the demo apps

### Sample data

- `sample-data/incident-trace.csv`
- `sample-data/support-ticket-trace.csv`

These samples are retained for future calibration work.

## How to use

The simulation is a static HTML file. You can either open `index.html` directly in a browser or serve the repo locally:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Why these apps matter

The paper is strongest when it does five things together:

1. **Formalizes agents** as bounded information-processing units: individuals, teams, firms, vendors, and software agents.
2. **Explains boundaries** as coalescing/splitting choices around surprise reduction and coordination cost.
3. **Defines agility** as the rate at which information becomes coordinated action.
4. **Shows executable examples** where software agents shift latency, distortion, monitoring, and the effective boundary of the firm.
5. **Runs a simulation** where the formal objective produces boundary phase behavior across protocol quality and task interdependence.

The simulation is deliberately simple. It is not a calibrated causal estimate. It is an executable illustration and measurement scaffold.

## Most important next step

Choose one empirical spine — preferably incident response or support routing — and replace the current stylized coefficients with real trace calibration.

## Public positioning

This repo should support a public paper/essay package:

- arXiv-style working paper,
- companion demo repo,
- short founder essay,
- video walkthrough,
- one trace-based case study.

The thought-leadership sentence:

> AI-native companies are not just companies with AI tools. They are organizations whose sensing, routing, decision, and execution loops are increasingly software-mediated.
