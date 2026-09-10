# Measurement playbook — draft 1.3

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
