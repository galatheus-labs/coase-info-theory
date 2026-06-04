# Coase–Information Theory Demo Repo

This repo packages a small set of static web apps plus formal paper material for the **Coase–Information Theory** project.

The central claim is:

> Firms are a special case of agent-boundary formation. Agents coalesce when shared representation reduces surprise and action loss more than it raises coordination cost, and split when modularity lowers cost more than it raises interface surprise.

The practical implication:

> Organizations are information architectures. Their economic performance depends on how efficiently they convert distributed, noisy signals into coordinated action under latency, cost, and distortion constraints.

The demos translate that claim into tangible software.

## Contents

### Apps

- `index.html` — suite homepage
- `topology-lab.html` — compare hierarchy, market, and agentic coordination under the same environment
- `incident-room.html` — simulate incidents, escalations, vendor outages, and routing failures
- `boundary-explorer.html` — explore when work should stay in-house, move to the market, or sit in an agent-mediated hybrid boundary
- `support-router.html` — show when software agents can improve routing, handoffs, and resolution in service workflows
- `workflow-trace-mapper.html` — paste workflow CSV traces and compute empirical agility proxies

### Paper and analysis

- `paper/coase-information-theory-draft.md` — improved working-paper draft
- `docs/formal-paper-analysis.md` — original mathematical framing, propositions, agent extension, and completion plan
- `docs/formal-note.md` — compact note tying the apps back to the theory
- `docs/paper-completion-plan.md` — concrete path from note to finished paper
- `docs/review-and-improvement-plan.md` — review of the current work and prioritized improvements
- `docs/measurement-playbook.md` — how to estimate theory quantities from workflow traces
- `docs/app-model-assumptions.md` — assumptions and calibration plan for the demo apps

### Sample data

- `sample-data/incident-trace.csv`
- `sample-data/support-ticket-trace.csv`

These samples can be pasted into `workflow-trace-mapper.html`.

## How to use

These prototypes are static HTML files. You can either open `index.html` directly in a browser or serve the repo locally:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Why these apps matter

The paper is strongest when it does four things together:

1. **Formalizes agents** as bounded information-processing units: individuals, teams, firms, vendors, and software agents.
2. **Explains boundaries** as coalescing/splitting choices around surprise reduction and coordination cost.
3. **Defines agility** as the rate at which information becomes coordinated action.
4. **Shows executable examples** where software agents shift latency, distortion, monitoring, and the effective boundary of the firm.

The apps are deliberately simple. They are not calibrated causal estimates. They are executable illustrations and measurement scaffolds.

## Most important next step

Choose one empirical spine — preferably incident response, support routing, or datacenter/vendor coordination — and replace one toy scenario with real telemetry. The new `workflow-trace-mapper.html` is the first step toward that.

## Public positioning

This repo should support a public paper/essay package:

- arXiv-style working paper,
- companion demo repo,
- short founder essay,
- video walkthrough,
- one trace-based case study.

The thought-leadership sentence:

> AI-native companies are not just companies with AI tools. They are organizations whose sensing, routing, decision, and execution loops are increasingly software-mediated.
