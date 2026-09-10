# Draft revision 1.3 — September 9, 2026

This is a focused technical revision of revision 1.2 (June 9, 2026), preserving the author's recursive agent-boundary thesis, organizational example, and bibliography. It is a draft for review, not a claim of empirical validation.

## Main changes

The economic switching threshold is now central. For a fixed cut with positive coordination savings H and scalar Gaussian/quadratic excess decision loss Δ(κ)=Δ(0)2^(−2κ), splitting is weakly preferable at κ >= max(0, 0.5 log2[Δ(0)/H]). The text covers ties, zero and negative savings, zero deficits, and capacity-dependent costs. Lossless information preservation and economic efficiency are explicitly different notions.

Predictive surprise is evaluated over fixed targets, scoring times, weights, and reference measures across architectures. It is no longer summed over a changing number of agents, and its independent objective weight defaults to zero unless an additional economic burden justifies pricing it.

The capacity dichotomy is identified as an operational definition and monotonicity result, not a new coding theorem or a prediction of an empirical elbow. The Gaussian benchmark states scalar state, memoryless samples, quadratic loss, decoder side information, unrestricted policies, asymptotic coding, and the omitted cost of block delay.

The volatility result now distinguishes proportional delay sensitivity from the absolute marginal benefit of reducing latency, which increases with hazard only while λτ < 1.

The granularity model separates balanced sizes, quadratic internal burden, sparse interfaces, constant interface costs, and loss assumptions. It clips the continuous optimum to [1,N], gives the integer-step condition, distinguishes indivisible primitives, and states the comparative static for changes in both A and B. Joint deficits across multiple cuts need not be additive.

The empirical section now proposes a controlled paired replay with a fixed downstream policy, independent interface variation, leakage prevention, declared loss and cost units, and uncertainty analysis. Clarification counts and schema completeness are diagnostics, not commensurate information rates. Matching on measured case mix is not treated as sufficient causal identification.

## Companion alignment

The existing scenario demo is preserved and labeled as heuristic. Its false R*=κ phase-map diagonal and the reversed interpretation of A are removed. Agility uses signed baseline-relative squared-loss reduction rather than mutual-information-times-accuracy, and comparisons share latent cases and random draws. Its fixed three-group split is stated explicitly rather than presented as unit-count optimization.

The new analytical workbench directly evaluates the Gaussian economic threshold and sweeps integer unit counts. It reports both the balanced-size relaxation and costs for indivisible primitives. It is an executable benchmark, not an estimated organizational model.

Historical Markdown drafts and mathematical planning notes remain archived with supersession notices. The measurement playbook is revised to match the paper.

## Validation and limitations

`node tests/model.test.cjs` checks threshold edge cases, exhaustive integer-surrogate minima over a parameter grid, the discrete marginal condition, both-cost comparative statics, the volatility derivative, inline JavaScript syntax, common-case scenario comparisons, and preservation of negative agility.

The branch-scoped build compiles the canonical TeX, checks for unresolved citations/references, and rebuilds the PDF on the draft branch only. The build also produces page previews as an artifact. It does not deploy GitHub Pages or merge into main. Passing tests is a consistency check, not an independent mathematical peer review or empirical validation. Browser interaction and visual layout should be distinguished from source/numerical tests in any validation report.
