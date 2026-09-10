#!/usr/bin/env python3
"""Align the preserved heuristic demo and documentation with draft 1.3."""
from pathlib import Path
from apply_revision_1_3 import replace_once, replace_span
ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'index.html'
s = p.read_text()
s = replace_span(s, '      Each cell re-runs the current scenario', '    </p>\n    <div class="canvas-shell', '''      Each cell evaluates chosen heuristic coefficients at dimensionless protocol-quality and
      task-dependence settings. These sliders are not measured bits or an estimate of R*.
      No information-theoretic diagonal is imposed: the winner follows this scenario's total
      objective, and lossy boundaries can win. The split scenario uses three groups; it does
      not optimize unit count. Use the <a href="analytical-workbench.html">analytical workbench</a>
      for the Gaussian economic threshold and an explicit integer granularity sweep.
      The crosshair marks your current levers.''')
s = replace_span(s, '  // capacity threshold R* = kappa:', '  const cx = padL',
                 '  // Sliders are dimensionless; do not draw a fabricated R*=kappa boundary.')
s = replace_once(s,
    'The hero example as a control panel. This is the granularity sweet spot m* = √(A/B): raise interface quality (lower B) and the efficient number of services rises; raise domain coupling (raise A) and it falls back toward a monolith.',
    'A heuristic scenario, not a fit of m* = √(A/B). Internal coordination burden A and cross-boundary decision dependence are distinct: raising A alone favors splitting in the balanced-unit model, whereas increasing loss at a cut can favor coalescence. Agents may change both A and B. Use the analytical workbench for unit-count optimization.')
s = replace_once(s, '  let totalLoss = 0;\n  let totalSurprise = 0;',
                 '  let totalLoss = 0;\n  let totalBaselineLoss = 0;\n  let totalSurprise = 0;')
s = replace_once(s, '    totalLoss += loss;', '    totalLoss += loss;\n    totalBaselineLoss += x * x; // fixed zero-action baseline, same cases')
s = replace_once(s, '  const loss = totalLoss / cfg.trials;',
                 '  const loss = totalLoss / cfg.trials;\n  const baselineLoss = totalBaselineLoss / cfg.trials;\n  const decisionValue = baselineLoss - loss;')
s = replace_once(s, 'const objective = surprise * 16 + loss * 18',
                 'const objective = loss * 18')
s = replace_span(s, '  const agility = clamp((information * (quality / 100) * 18)',
                 '  return { ...option, surprise, loss,', '''  // Q / [tau * (1 + C/C0)]; signs are preserved. Scores are not percentages.
  // Setup delay is included once in this toy per-decision latency convention.
  const effectiveLatency = latency + planningDelay;
  const agility = decisionValue / (effectiveLatency * (1 + cost / 55));''')
s = replace_once(s, 'return { ...option, surprise, loss, latency, cost,',
                 'return { ...option, surprise, loss, baselineLoss, decisionValue, effectiveLatency, latency, cost,')
s = replace_once(s, '.map((option, idx) => simulateBoundary(option, cfg, idx * 10007))',
                 '.map(option => simulateBoundary(option, cfg, 0)) // paired latent cases and noise draws')
s = replace_once(s, 'const fmt2 = n => (Math.round(n * 100) / 100).toFixed(2);',
                 'const fmt2 = n => (Math.round(n * 100) / 100).toFixed(2);\nconst fmtAgility = n => Number(n).toFixed(4);')
s = s.replace('fmt(best.agility)', 'fmtAgility(best.agility)').replace('fmt(row.agility)', 'fmtAgility(row.agility)')
s = replace_once(s, "      ${makeBar('Agility', row.agility, 100, 'teal')}",
                 '      <p>Baseline-relative value: ${fmt2(row.decisionValue)}; cost-adjusted agility: ${fmtAgility(row.agility)} loss units per minute (signed, not a percentage).</p>')
s = s.replace('<th>Quality</th>', '<th>Sign accuracy</th>').replace('<th>Agility</th>', '<th>Agility (loss/min)</th>')
s = replace_once(s, 'Monte Carlo companion for the Coase–Information Theory paper (rev 1.2, 2026-06-09): boundary capacity threshold (R* = κ) and the granularity law m* = √(A/B). Stylized simulation, not a causal estimate.',
                 'Draft revision 1.3 (2026-09-09). Heuristic scenario model, not a causal estimate or an implementation of optimal coding. Agility uses signed baseline-relative squared-loss reduction. See the separate analytical workbench for economic thresholds and granularity.')
s = replace_once(s, '<body>', '<body>\n<div class="container"><p><strong>Draft 1.3:</strong> <a href="analytical-workbench.html">Open the analytical workbench</a> for explicit model assumptions, a lossy economic switching threshold, and integer unit-count optimization. The animation and scenario sliders below are conceptual illustrations, not measured information rates.</p></div>')
p.write_text(s)

p = ROOT / 'README.md'
s = p.read_text()
s = replace_once(s, '# Coase–Information Theory Demo Repo', '# Coase–Information Theory\n\n**Draft revision 1.3 — September 9, 2026.** The canonical TeX and rebuilt PDF contain the technical revision. Draft-branch changes are not live on the public companion until merged and deployed.\n\n[Revision notes](docs/revision-1.3-notes.md) · [Analytical workbench](analytical-workbench.html)\n\nThe central economic comparison is `excess decision loss <= coordination savings`: a lossy boundary can be optimal. The Gaussian coding example and balanced-unit square-root model are conditional analytical benchmarks, not universal organizational laws.')
s = s.replace('A boundary **phase map** shows which architecture wins across protocol quality and task interdependence, with the `R* = κ` capacity threshold drawn in.',
              'A heuristic **phase map** shows which architecture wins under chosen scenario coefficients. Its dimensionless sliders are not estimates of `R*` or bit capacity. The separate analytical workbench evaluates the Gaussian switching threshold and sweeps integer unit counts explicitly.')
s = s.replace('Choose one empirical spine — preferably incident response or support routing — and replace the current stylized coefficients with real trace calibration.',
              'Run a controlled incident-response or support-routing replay: freeze cases and decision policy, vary only the interface representation or budget, and report decision loss, latency, and resource costs separately. Observational deployment studies need explicit identification assumptions.')
s += '\n## Validation\n\n`node tests/model.test.cjs` checks the analytical formulas, integer optimization, and signed scenario agility. `latexmk -pdf -halt-on-error -interaction=nonstopmode -outdir=build paper/coase-information-theory.tex` builds the paper. The revision migration is guarded against an unexpected 1.2 source and is not part of normal application startup.\n\nHistorical notes and `paper/coase-information-theory-draft.md` are retained as archives; they are not the current mathematical specification.\n'
p.write_text(s)

for rel in ('docs/formal-note.md', 'docs/formal-paper-analysis.md', 'docs/app-model-assumptions.md',
            'docs/arxiv-submission-plan.md', 'paper/coase-information-theory-draft.md'):
    p = ROOT / rel
    s = p.read_text()
    p.write_text('> Historical document. The canonical paper and `docs/revision-1.3-notes.md` supersede mathematical, measurement, and demo claims in this file.\n\n' + s)

p = ROOT / 'docs/measurement-playbook.md'
p.write_text('''# Measurement playbook — draft 1.3

The first test is whether a boundary or protocol improves a declared decision objective, not whether ticket proxies look like bits. This is a proposed protocol, not an externally preregistered or completed study.

## Controlled paired replay

Freeze cases, evidence available at decision time, downstream model/policy version, tools, permissions, and a loss rubric. Compare local-only evidence, a fixed structured handoff, an agent-mediated handoff under a declared budget, and a full-evidence reference. Vary interface representation or budget independently of case difficulty. Preserve the same cases across arms, repeat stochastic policies, and blind scoring where feasible. Postmortems may label outcomes but must not leak future evidence into earlier decisions.

The full-evidence reference is not automatically Bayes-optimal. Report negative empirical reference gaps rather than clipping them. Pre-specify effects of interest and use pilot variance and clustering to plan sample size; a quarter of tickets is not a power calculation.

## Minimal event schema

Retain case_id, timestamp, actor_type, owner, event_type, and outcome quality. Add arm, policy_version, decision_id, evidence_cutoff, representation_type, declared_message_budget, action_loss, baseline_loss, compute_cost, interpretation_minutes, and review_minutes when available. Treat repeated observations within an incident as clustered, not independent samples.

## Separate measurements before aggregating

Decision value Q is baseline_loss minus action_loss under the same rubric. Latency is signal-to-action elapsed time; report triage, decision, and resolution intervals separately. Resource cost includes compute, communication, human interpretation, and review using disjoint accounting. Use cost-adjusted agility Q/[tau(1+C/C0)] only with declared positive time and cost scales. Preserve negative Q and negative agility. This ratio is not generally equivalent to minimizing the full objective.

For a stabilized descriptive trace proxy use Q/[(t0+T_resolution)(1+alpha*handoff_count)], with a fixed reference time t0 and declared alpha. Handoff counts here are not the economic coordination savings H. Do not charge the same handoff twice through both an explicit cost and a proxy penalty. For sequential non-overlapping episodes, aggregate value as sum(Q)/sum(tau), not the unweighted mean of episode ratios; concurrent workflows need separate throughput accounting.

## Prediction scores

Evaluate predictive surprise on a fixed set of tasks, targets, times, weights, and reference measures across architectures. Do not sum surprise over a changing number of agents. Reopens, escalations, and reversals are useful diagnostics but are not literal Shannon surprise without a probability model.

## What operational proxies cannot establish

Clarification requests partly result from an inadequate interface; they are not an exogenous estimate of R*. Schema completeness fractions are not bit capacities. Do not subtract these proxies to claim an R*-kappa deficit. Actual operational bits require a specified alphabet, code, and rate convention; token budgets are engineering constraints, not semantic information rates by definition.

An operational preservation threshold does not imply a kink or elbow. The fourfold-per-bit deficit reduction is specific to the memoryless scalar Gaussian/quadratic, asymptotically optimally coded benchmark. Reopen probability and resolution time do not inherit that law. Test flexible alternatives, and do not log nonpositive estimated excess losses.

## Economic comparison and uncertainty

Compare excess decision loss with coordination savings in the same units per decision. Include amortized transition costs and coding delay. Report paired effects, appropriate uncertainty intervals, clustering choices, and sensitivity to objective weights. Treat observational before/after matching as adjustment for measured case mix, not proof of causality; staggered adoption still needs identification assumptions and spillover checks.

## Granularity

Compare feasible partitions and measure changes in both internal coordination burden A and interface cost B. Distinguish A from cross-boundary decision dependence. The square-root comparative static applies only to its balanced-size, sparse-interface, constant-cost interior regime; clipping, indivisible components, and interacting deficits can change the result.

The old workflow-trace-mapper URL redirects to the scenario companion; it does not currently implement a CSV analysis pipeline. The sample CSV files are illustrative inputs, not empirical validation.
''')
print('Aligned scenario implementation, README, and measurement documentation.')
