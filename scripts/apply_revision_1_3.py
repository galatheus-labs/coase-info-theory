#!/usr/bin/env python3
"""Materialize the reviewed 1.3 draft from the exact 1.2 source.

This one-time migration refuses an unexpected source or partial reapplication.
It preserves the original author, bibliography, and unaffected discussion.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'paper/coase-information-theory.tex'


def replace_once(text, old, new):
    count = text.count(old)
    if count != 1:
        raise ValueError(f'Expected one occurrence, got {count}: {old[:100]!r}')
    return text.replace(old, new, 1)


def replace_span(text, start, end, replacement):
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[:a] + replacement.rstrip() + '\n\n' + text[b:]


def revise_paper(s):
    s = replace_once(s, r'\date{June 2026\\[2pt]' + '\n' + r'{\normalsize Working paper --- revision 1.2, 2026-06-09}}',
                     r'\date{September 2026\\[2pt]' + '\n' + r'{\normalsize Working paper --- draft revision 1.3, 2026-09-09}}')
    s = replace_span(s, r'\begin{abstract}', r'\noindent\textbf{Keywords:}', r'''
\begin{abstract}
Coase explained the firm as an alternative to market coordination when using
the price mechanism is costly. This paper extends that design problem from
the boundary of the firm to the boundary of the agent: a bounded
sensing--representation--decision--action loop that may comprise humans,
teams, services, vendors, or software agents. It develops a normative framework
for choosing such boundaries under a specified objective, decomposes
coordination costs into operational terms, and defines organizational agility
as decision value per unit time. Established information-theoretic tools yield
an analytical benchmark: for a memoryless scalar Gaussian estimation task
with quadratic loss and asymptotic one-way coding, the excess loss of splitting
is the zero-communication decision deficit multiplied by $2^{-2\kappa}$.
Combining that benchmark with coordination savings gives a finite economic
switching threshold, even when preserving all decision value requires
unbounded communication. Under balanced units, quadratic internal cost, and
sparse constant-cost interfaces, a separate continuous relaxation gives the
familiar square-root granularity rule. Agents can favor either finer
decomposition or greater integration, depending on their relative effects on
internal costs, interface costs, and decision loss. The contribution is the
integration of these results into a recursive boundary-design framework, not
a new general coding theorem or universal scaling law. A stylized companion
and a controlled-replay research design distinguish analytical benchmarks from
operational proxies and empirical evidence. Software agents are
boundary-shifting infrastructure because programmable observation,
communication, and action change where shared context is worth its cost.
\end{abstract}
''')
    s = replace_span(s, 'The contribution is not the broad claim that firms process information.',
                     'This paper does not claim that firms disappear', r'''
The contribution is not the broad claim that firms process information. That
intuition has deep roots in Hayek, Simon, Galbraith, and distributed decision
theory \cite{hayek1945,simon1947,galbraith1973,marschakradner1972}.
Formal organizational economics has derived structures from communication,
processing, and incentive costs
\cite{radner1993,boltondewatripont1994,garicano2000,alonso2008}.
This paper integrates those perspectives into a recursive design language for
human--software organizations. Programmable interfaces can change both the
cost of pooling information and the cost of communicating across a boundary;
neither direction is assumed to dominate.

Three analytical steps organize the argument. An operational capacity
threshold defines preservation of a specified decision value
(Proposition~\ref{prop:capacity}). A Gaussian--quadratic example applies
classical source coding with decoder side information to price excess decision
loss (Theorem~\ref{thm:deficit}). Combining that loss with coordination
savings gives the economic switching threshold
(Corollary~\ref{cor:economic}): information loss can be worth accepting.
A separate balanced-unit cost model gives a square-root granularity rule
(Theorem~\ref{thm:granularity}), with explicitly conditional comparative
statics. The contribution is their integration and organizational
interpretation, not novelty of the underlying coding or optimization machinery.

The framework is normative: it compares architectures under a specified
objective, feasible policy set, and governance constraints. It does not derive
bargaining equilibria, endogenous property rights, or the distribution of
surplus. Misalignment and monitoring are costs to be specified, not a
substitute for an incentive-compatibility model. Observed organizational
boundaries need not coincide with the optima described here.
''')
    s = replace_once(s, 'These models largely take the\ncommunication technology as given; the present paper is about what happens\nwhen that technology becomes programmable.',
                     'These models provide the foundation for treating communication and\nprocessing technologies as organizational design parameters. The present\npaper emphasizes programmable interfaces and recursively composed\nhuman--software decision units, without claiming that technological\ncomparative statics are absent from the earlier literature.')
    s = replace_once(s, 'The novelty of Coase--Information Theory is to combine these threads into a\nsingle recursive boundary problem.',
                     'The proposed synthesis combines these threads into a\nsingle recursive boundary-design problem.')
    s = replace_once(s, 'The general organizational design problem is',
                     'All cumulative quantities below refer to a common finite evaluation\nhorizon and case distribution; infinite-horizon applications require an\nexplicit discount or average-cost convention. The general organizational\ndesign problem is')
    s = replace_span(s, r'Here \(\E\sum_t S_t\) is cumulative expected surprise,',
                     'The scalar objective used by a particular organization', r'''
Here $\E\sum_t S_t$ is a predictive score evaluated on a fixed set of targets,
with the same scoring opportunities and weights for every architecture
(Section~\ref{sec:coalescence}). It is not a sum over a changing number of
agents. The term $\E\sum_t L(X_t,a_t)$ is cumulative action loss.
''')
    s = replace_once(s, 'Then an objective-efficient architecture satisfies',
                     'Weights are nonnegative and costs use a common declared accounting\nconvention. By default $\beta_S=0$: predictive surprise is a diagnostic unless\nan independent economic burden, not already in loss or other costs, justifies\npricing it. Then an objective-efficient architecture satisfies')
    s = replace_once(s, 'boundary is \\emph{Pareto-efficient} when no feasible boundary movement weakly',
                     'boundary is \\emph{Pareto-efficient} when no feasible architecture weakly')
    s = replace_once(s, 'feasible boundary movement lowers the organization\'s total expected objective',
                     'feasible architecture lowers the organization\'s total expected objective')
    s = replace_once(s, 'Objective efficiency selects a point on that frontier.',
                     'With strictly positive weights on all components, global objective\nminimizers are Pareto-efficient on the same feasible set. With zero weights,\na minimizer can be dominated on ignored components; use Pareto-efficient\ntie-breaking when that distinction matters. Efficiency against only local\nmerge/split moves is local optimality, not global Pareto efficiency.')
    s = replace_span(s, 'One idealized measure of surprise is',
                     'Surprise and action loss play different roles.', r'''
A local diagnostic of surprise is
\[
S_t^B=-\log P_B(X_t\mid Z_t^B).
\]
For continuous targets this denotes a density-based log score relative to a
fixed reference measure. Local scores help diagnose prediction failures, but
summing them over $B\in\calB$ is not an architecture-neutral objective:
merging two identical predictors would remove a term without improving any
prediction. Changing a continuous state's units would also add a constant per
agent, making the comparison depend on the number of blocks.

Instead fix a set $\mathcal D$ of decision or prediction targets, fixed
weights $w_j\geq0$, and fixed evaluation times, independently of the
architecture. Let $X_t^{(j)}$ be target $j$, and let
$\widehat P_{j,t}^{\calB}$ be the predictive distribution delivered at that
fixed evaluation interface by architecture $\calB$. Define
\[
S_t(\calB)=\sum_{j\in\mathcal D}w_j
\left[-\log\frac{d\widehat P_{j,t}^{\calB}}{d\nu_j}
                  (X_t^{(j)})\right],
\]
using common reference measures $\nu_j$, a common log base, and finite
expected scores. For discrete targets $\nu_j$ is counting measure. A common
change of units now shifts scores equally across architectures rather than
per block. Duplicate attention or prediction-maintenance work, when genuinely
costly, belongs in measured computation or monitoring costs. A boundary-design
problem can therefore be written
\[
\min_{\calB,G,F,\Pi}\;
\E\sum_t L(X_t,a_t)+\beta_S\E\sum_t S_t(\calB)
+C(\calB,G,F,\Pi),
\]
with $\beta_S=0$ unless separately justified.
''')
    s = replace_once(s, r'\E[S_{\mathrm{merged}}+L_{\mathrm{merged}}]+C_{\mathrm{merged}}',
                     r'\E[L_{\mathrm{merged}}]+\beta_S\E[S_{\mathrm{merged}}]+C_{\mathrm{merged}}')
    s = replace_once(s, r'\E[S_{\mathrm{separate}}+L_{\mathrm{separate}}]+C_{\mathrm{separate}}.',
                     r'\E[L_{\mathrm{separate}}]+\beta_S\E[S_{\mathrm{separate}}]+C_{\mathrm{separate}}.')
    s = replace_once(s, r'+C_{\mathrm{contract},k}' + '\n' + r'+C_{\mathrm{comm},k}',
                     r'+C_{\mathrm{contract},k}' + '\n' + r'+C_{\mathrm{comp},k}' + '\n' + r'+C_{\mathrm{comm},k}')
    s = replace_span(s, r'\section{The Granularity Sweet Spot}', r'\section{Organizational Agility}', ANALYTICAL_SECTION)
    s = replace_once(s, 'Let \\(\\tau_t\\) be the end-to-end latency from signal availability to coordinated\naction.',
                     'Let \\(\\tau_t>0\\) be the end-to-end latency from signal availability to\ncoordinated action, measured in a fixed time unit.')
    s = replace_once(s, 'where \\(\\widetilde C_t\\geq 0\\) is a normalized resource-cost index for\nproducing the action.',
                     'where \\(\\widetilde C_t=C_t/C_0\\geq 0\\) uses a declared, fixed resource-cost\nscale \\(C_0>0\\). Comparisons use the same baseline policy, loss, time unit,\nand cost scale. This ratio is a diagnostic, not generally an objective\nequivalent to minimizing \\(J\\). For non-overlapping sequential episodes, a\nvalue-rate aggregate is \\(\\sum_t Q_t/\\sum_t\\tau_t\\), not an unweighted\naverage of episode ratios. Concurrent workflows require an explicit\nthroughput and resource-accounting convention.')
    s = replace_once(s, r'\section{Propositions}', r'\section{Design Implications and Conditional Hypotheses}')
    s = replace_span(s, r'\begin{proposition}[Protocol-mediated coordination]',
                     r'\begin{proposition}[Latency under volatility]', r'''
\begin{proposition}[Protocol emulation]
At fixed architecture, suppose every policy feasible under protocol $P$ can
be emulated under $P'$ with the same conditional action distribution and no
greater total non-decision cost. Then the minimum net objective under $P'$
is no worse than under $P$.
\end{proposition}
\noindent\textit{Proof.} Emulate an optimal old policy (or an arbitrarily
close approximation); optimization over the new feasible set cannot do worse.
\hfill$\square$

A Blackwell improvement in information can supply the decision component of
this condition when the policy class is closed under the required garbling
\cite{blackwell1953}. It does not establish the cost component: a richer
schema can add interpretation, computation, review, or delay. Informativeness
alone is therefore insufficient for a net-objective claim.
''')
    s = replace_span(s, r'\begin{proposition}[Latency under volatility]',
                     r'\begin{proposition}[Interdependence and modularity]', r'''
\begin{proposition}[Latency under volatility]
\label{prop:latency}
Suppose a relevant state survives a delay $\tau$ with probability
$e^{-\lambda\tau}$, useful decision value is zero after a state change, and
$Q_0>0$ is held fixed. Then $Q(\tau)=Q_0e^{-\lambda\tau}$.
Greater hazard $\lambda$ increases the proportional sensitivity to delay:
$-\partial\log Q/\partial\tau=\lambda$. The absolute marginal benefit of
reducing delay is $Q_0\lambda e^{-\lambda\tau}$ and increases with $\lambda$
only while $\lambda\tau<1$.
\end{proposition}
\noindent\textit{Proof.} Condition on state survival and differentiate:
\[
\frac{\partial}{\partial\lambda}
\left(-\frac{\partial Q}{\partial\tau}\right)
=Q_0e^{-\lambda\tau}(1-\lambda\tau).
\]
Once information is already very stale, a small latency improvement has little
absolute value. The exponential form assumes a constant survival hazard; it
is not a general theorem about all dynamic decision problems.\hfill$\square$
''')
    s = replace_span(s, r'\begin{proposition}[Interdependence and modularity]',
                     r'\begin{proposition}[Agentic routing]', r'''
\paragraph{Interdependence and modularity: a conditional hypothesis.}
Greater cross-boundary decision dependence can raise excess loss and favor
coalescence, whereas lower interface costs can favor separation. This is not a
universal monotone relation with an undifferentiated ``coupling'' variable.
Internal coordination burden $A$ and cross-boundary decision deficit $D$ play
different roles: increasing $A$ alone favors splitting in the balanced-unit
model, while increasing the marginal deficit of additional cuts opposes it.
The economic comparison is Corollary~\ref{cor:economic}, not information
cleanliness alone.
''')
    s = replace_once(s, r'\begin{proposition}[Agentic routing]', r'\begin{remark}[Agentic routing: accounting condition]')
    a = s.index(r'\begin{remark}[Agentic routing: accounting condition]')
    b = s.index(r'\end{proposition}', a)
    s = s[:b] + r'\end{remark}' + s[b+len(r'\end{proposition}'):]
    s = replace_once(s, 'Here \\(I_{\\mathrm{monitor}}\\) denotes measurable oversight work, while',
                     'All changes must use the same objective weights and include any change\nin direct task loss. These labels are disjoint accounting buckets, not\nadditional terms to count again. Here \\(I_{\\mathrm{monitor}}\\) denotes measurable oversight work, while')
    s = replace_once(s, 'auditability, and escalation overhead. The execution and governance terms',
                     'auditability, and escalation overhead not already counted as monitoring.\nThe execution and governance terms')
    s = replace_span(s, r'\begin{proposition}[Governance limit]', r'\section{Executable Illustration}', r'''
\paragraph{Governance limit: a conditional hypothesis.}
Agentic decentralization can have diminishing or negative returns when
monitoring, unsafe actions, or local--global misalignment grow faster than
coordination savings. A fast local optimizer is useful only insofar as its
actions improve the declared global objective. The framework identifies terms
to measure; their signs and magnitudes require evidence.
''')
    s = replace_span(s, r'\section{Executable Illustration}', r'\section{Measurement and Empirical Agenda}', ILLUSTRATION_SECTION)
    s = replace_span(s, r'\section{Measurement and Empirical Agenda}', r'\section{Limitations}', MEASUREMENT_SECTION)
    s = replace_once(s, 'Sixth, organizational utility is multi-objective. Speed, accuracy, compliance,\nsafety, morale, trust, and strategic learning may trade off.',
                     'Sixth, organizational utility is multi-objective. Speed, accuracy, compliance,\nsafety, morale, trust, and strategic learning may trade off.\n\nSeventh, the Gaussian benchmark requires scalar quadratic estimation,\nmemoryless samples, optimal coding, and asymptotically long blocks. A real-time\nagent handoff need not approach that bound; block delay must be costed.\n\nEighth, balanced units, sparse interfaces, and constant interface costs are\nseparate assumptions. Heterogeneous tasks and interacting communication cuts\ncan invalidate the square-root model and additive deficit approximations.\n\nFinally, this is a normative design framework, not a theory of equilibrium\nownership or bargaining. Strategic behavior, transition costs, organizational\nlearning, and distributional consequences require explicit extensions.')
    s = replace_once(s, 'The next generation of AI-native companies will be designed not merely around',
                     'The central economic distinction is between preserving all decision value\nand preserving enough to justify a boundary\'s cost. A lossy interface can be\noptimal. Agents can move the optimum in either direction by changing internal\ncoordination, interface costs, and the value of shared context.\n\nThe next generation of AI-native companies may be designed not merely around')
    return s


ANALYTICAL_SECTION = r'''
\section{Information Preservation and Economic Boundaries}
\label{sec:granularity}

Information preservation and economic efficiency are different questions.
An interface can be lossy yet worth using, or lossless yet prohibitively
expensive. This section first defines preservation, then prices a deficit in
an analytically tractable case, and finally compares that deficit with the
coordination savings from drawing a boundary.

\subsection{An operational preservation threshold}

Fix a joint distribution of a scalar or vector state $X$ and pooled local
observations $(Y^A,Y^B)$, a loss $L$, and an admissible policy class. All
architectures are evaluated on that same problem. In the coalesced benchmark,
the deciding side holds both observations. In the split architecture it holds
$Y^A$ and a one-way message from an encoder that observes $Y^B$. Define
\[
\mathcal L_{\mathrm{coal}}
=\inf_\pi\E[L(X,\pi(Y^A,Y^B))],\qquad
\mathcal L_{\mathrm{split}}(r)
=\inf_{M\in\mathcal P(r),\,\pi}\E[L(X,\pi(Y^A,M))].
\]
Here $\mathcal P(r)$ is a nested family of protocols of rate at most $r$.
For a one-shot model this can mean a fixed-length message budget. For a
memoryless block model it means an asymptotic description rate per sample,
with average loss per sample. These are distinct operational problems: fix
one convention before comparing $r$ with interface capacity $\kappa$.
The deciding side's observation is decoder side information. General remote
decision problems need their own distortion/rate formulation; they are not
all ordinary source-reconstruction problems \cite{wynerziv1976}.

The coalesced policy class is assumed to include emulation of every split
protocol, including its randomization. Thus
$\mathcal L_{\mathrm{split}}(r)\geq\mathcal L_{\mathrm{coal}}$.

\begin{definition}[Decision-relevant interface rate]
\label{def:rstar}
The preservation threshold and its tolerance version are
\[
R^\star=\inf\{r\geq0:\mathcal L_{\mathrm{split}}(r)
=\mathcal L_{\mathrm{coal}}\},\qquad
R^\star_\varepsilon=\inf\{r\geq0:\mathcal L_{\mathrm{split}}(r)
\leq\mathcal L_{\mathrm{coal}}+\varepsilon\},
\]
with the infimum of an empty set equal to $+\infty$.
\end{definition}

\begin{proposition}[Capacity dichotomy]
\label{prop:capacity}
Assume nested protocol classes and attainment of both the required loss
infima and the lower endpoint defining $R^\star$ when finite. If
$\kappa\geq R^\star$, some feasible protocol attains coalesced risk.
If $\kappa<R^\star$, the optimal excess loss
\[
\Delta(\kappa)=\mathcal L_{\mathrm{split}}(\kappa)
-\mathcal L_{\mathrm{coal}}
\]
is positive and non-increasing with $\kappa$.
\end{proposition}
\noindent\textit{Proof.} Nested feasible sets make optimal split risk
non-increasing. Endpoint attainment gives the first claim. A zero gap below
$R^\star$ would put that rate in the defining set, a contradiction.
\hfill$\square$

Without attainment, use explicit rate/loss slack and distinguish an infimum
from an achieved protocol. The proposition follows from the operational
definition; it fixes terminology, not a novel coding theorem. It does not
imply a kink, a discontinuity, or a measurable elbow in the loss curve.
An $\varepsilon$-threshold may simply be a smooth tolerance crossing.

A cut is \emph{information-clean} relative to a specified decision problem
when it preserves coalesced risk. Conditional mutual information can help
characterize dependence, but is not a universal achievable communication rate
for an arbitrary decision loss. Neither low mutual information nor low
$R^\star$ alone identifies an economically optimal partition.

\subsection{A Gaussian--quadratic benchmark}

\begin{theorem}[Exponential interface-deficit benchmark]
\label{thm:deficit}
Let independent decision samples be drawn from a fixed jointly Gaussian
$(X,Y^A,Y^B)$, with scalar $X$, finite covariance, and quadratic loss
$L(x,a)=(x-a)^2$. The encoder observes $(Y^B)^n$ and sends at most
$n\kappa+o(n)$ bits; the decoder observes $(Y^A)^n$. With unrestricted
measurable encoding/decoding and asymptotic average loss as $n\to\infty$,
\[
\Delta(\kappa)=
\underbrace{\big[\operatorname{Var}(X\mid Y^A)
-\operatorname{Var}(X\mid Y^A,Y^B)\big]}_{\Delta(0)}
2^{-2\kappa}.
\]
If $\Delta(0)>0$, then $R^\star=\infty$ and, for
$0<\varepsilon\leq\Delta(0)$,
\[
R^\star_\varepsilon=\tfrac12\log_2\frac{\Delta(0)}{\varepsilon}.
\]
If $\Delta(0)=0$, no communication is needed.
\end{theorem}
\noindent\textit{Proof.} Center variables without loss of generality.
The coalesced conditional mean is
$T'=\E[X\mid Y^A,Y^B]=a^\top Y^A+b^\top Y^B$.
Let $V=b^\top Y^B$, computable by the encoder. Orthogonality of the
conditional-mean residual gives, per sample and hence averaged over a block,
\[
\E(X-\hat a)^2=\mathcal L_{\mathrm{coal}}
+\E(T'-\hat a)^2.
\]
Because the decoder knows $a^\top Y^A$, the excess term is the distortion
in estimating scalar $V$ with decoder side information $Y^A$.
Gaussian Wyner--Ziv coding has no rate loss relative to conditional
rate--distortion under quadratic loss \cite{wynerziv1976,wyner1978}, giving
$D(\kappa)=\operatorname{Var}(V\mid Y^A)2^{-2\kappa}$.
For the converse, giving $Y^A$ to the encoder cannot increase the minimum
distortion; conditional Gaussian rate--distortion already gives this same
lower bound, including encoders that retain all of $Y^B$.
Finally, the orthogonal decomposition
\[
X-\E[X\mid Y^A]=(X-T')+(V-\E[V\mid Y^A])
\]
shows $\operatorname{Var}(V\mid Y^A)=\Delta(0)$. Substitution and inversion
give the claims.\hfill$\square$

\begin{corollary}[Exact information bridge in the benchmark]
\label{cor:mibridge}
For positive coalesced residual variance in Theorem~\ref{thm:deficit},
\[
I(X;Y^B\mid Y^A)=\tfrac12\log_2
\frac{\operatorname{Var}(X\mid Y^A)}
     {\operatorname{Var}(X\mid Y^A,Y^B)},\qquad
\Delta(0)=\operatorname{Var}(X\mid Y^A)
\big(1-2^{-2I(X;Y^B\mid Y^A)}\big).
\]
\end{corollary}

This is an application of classical Gaussian source coding, not a new
source-coding theorem. The fourfold reduction per bit is exact only in this
benchmark. One-shot handoffs, discrete actions, non-Gaussian tasks, finite
blocks, restricted policies, and suboptimal codecs can have different curves.
Block-coding latency is also an economic cost, even though it is absent from
the rate--distortion expression. Capacity requirements grow logarithmically
with tolerance in this model, but acquiring capacity need not be cheap.

\subsection{The economic switching threshold}

For one fixed cut, let all non-decision costs use the same objective units as
expected loss. Let $C_{\mathrm{coal}}$ and $C_{\mathrm{split}}$ include
communication, computation, interpretation, delay, governance, and any
amortized transition costs. Set
\[
H=C_{\mathrm{coal}}-C_{\mathrm{split}}.
\]
For this comparison surprise is diagnostic ($\beta_S=0$), or any separately
justified predictive burden is already included in the stated costs. Then
\[
J_{\mathrm{split}}-J_{\mathrm{coal}}=\Delta(\kappa)-H.
\]

\begin{corollary}[Economic switching threshold]
\label{cor:economic}
Under Theorem~\ref{thm:deficit}, suppose $\Delta(0)>0$ and coordination
savings $H>0$ are held fixed as $\kappa$ varies. Splitting is weakly
preferable exactly when
\[
\kappa\geq\kappa_{\mathrm{economic}}
:=\max\left\{0,\tfrac12\log_2\frac{\Delta(0)}{H}\right\}.
\]
At a positive threshold the architectures tie; above it splitting is strictly
preferable. If $H>\Delta(0)$, splitting is strictly preferable even at zero
capacity; if $H=\Delta(0)$, zero capacity is a tie.
\end{corollary}
\noindent\textit{Proof.} Substitute the deficit benchmark into
$J_{\mathrm{split}}-J_{\mathrm{coal}}\leq0$ and solve
$\Delta(0)2^{-2\kappa}\leq H$ for $\kappa\geq0$.\hfill$\square$

If $H<0$, splitting cannot win under this fixed-cut comparison. If $H=0$
and $\Delta(0)>0$, no finite rate attains a tie in the Gaussian benchmark.
When $\Delta(0)=0$, compare the costs alone. More generally, capacity costs
or coding delay make $H=H(\kappa)$; then optimize or solve
$\Delta(\kappa)\leq H(\kappa)$ rather than apply the closed form blindly.

For example, with $\Delta(0)=4$ loss units and $H=1$ cost unit per decision,
the threshold is one bit. At that rate the remaining decision deficit is one
unit: the interface is lossy, but its savings exactly compensate. At two bits,
the deficit is $1/4$ and splitting improves the objective by $3/4$ unit.

\begin{quote}
An information-clean boundary loses no decision value. An economically
efficient boundary loses no more decision value than its coordination
savings justify.
\end{quote}

\subsection{Granularity in a balanced-unit cost model}

A separate model makes the number of units explicit. Let $N$ primitive
components be divided into $m$ equal-sized units. Assume within-unit
coordination cost $a n^2$ for size $n$, $a>0$, and a sparse, tree-like
quotient graph with $m-1$ interfaces costing $B>0$ each. The continuous
balanced-size relaxation is
\[
\Theta(m)=\frac{A}{m}+B(m-1),\qquad
A=aN^2,\quad 1\leq m\leq N.
\]
Quadratic internal cost is a modeling assumption motivated by possible
all-pairs interactions, not a claim that all coordination is all-pairs
\cite{brooks1975,simon1962}. Balanced sizes, sparse interfaces, and constant
per-interface costs are separate assumptions. Information-clean cuts do not
by themselves imply any of them. Decision loss must be constant or separately
modeled for minimizing $\Theta$ to minimize the full objective.

\begin{theorem}[Optimal decomposition in the continuous relaxation]
\label{thm:granularity}
For the stated cost model,
\[
m^\star_{\mathrm{cont}}=
\min\{N,\max\{1,\sqrt{A/B}\}\}.
\]
At an interior optimum, $\Theta(m^\star)=2\sqrt{AB}-B$.
For integer $m$ in the same surrogate cost, evaluate the feasible floor and
ceiling of the clipped continuous optimum and choose the lower-cost one.
\end{theorem}
\noindent\textit{Proof.}
$\Theta'(m)=-A/m^2+B$ and $\Theta''(m)=2A/m^3>0$.
Clipping the stationary point gives the constrained solution; convexity leaves
only its adjacent feasible integers to compare.\hfill$\square$

For integer steps in this surrogate, introducing one more unit reduces cost
exactly when
\[
\Theta(m+1)-\Theta(m)=B-\frac{A}{m(m+1)}<0.
\]
When indivisible primitives prevent equal sizes, the exact internal cost for
balanced integer groups is $a\sum_j n_j^2$, with group sizes differing by at
most one. Optimize that discrete expression rather than claiming the
continuous surrogate is exact. The square-root form is the familiar
opposing-cost structure, not a universal organizational scaling law.

\begin{corollary}[Relative cost changes shift granularity]
\label{cor:agents}
Within the interior regime of the same cost model,
\[
\frac{m^{\star\prime}}{m^\star}
=\sqrt{\frac{A'/A}{B'/B}},\qquad
\Delta\log m^\star=\tfrac12(\Delta\log A-\Delta\log B).
\]
Holding $A$ fixed, halving $B$ increases the continuous optimal count by
$\sqrt2$, approximately $41\%$. If both costs change, finer decomposition is
favored when interface costs fall proportionally more than internal costs;
the reverse can favor integration. Clipping and integer constraints can leave
the implemented count unchanged.
\end{corollary}

Internal coordination burden $A$ is distinct from cross-boundary decision
dependence. Raising $A$ alone favors splitting in this model; raising the
loss caused by a cut can favor coalescence. A single ``coupling'' slider
cannot be interpreted as both without an explicit mapping.

\begin{remark}[Lossy interfaces and interacting deficits]
\label{cor:floor}
With lossy cuts use a total excess decision-loss term
$D(\calB,\boldsymbol\kappa)$:
\[
J(\calB,\boldsymbol\kappa)=\mathcal L_{\mathrm{coal}}
+C(\calB,\boldsymbol\kappa)+D(\calB,\boldsymbol\kappa).
\]
Single-cut deficits generally cannot be added without assumptions excluding
shared, redundant, or interacting information. In a specified nested family
with surrogate $D_m$, adding a unit is worthwhile only if
$\Theta(m+1)-\Theta(m)+D_{m+1}-D_m<0$. Increasing these marginal deficits
opposes further splitting; a positive deficit by itself does not prohibit it.
A tolerance constraint $D_m\leq\varepsilon$ is a separate governance choice,
not an economic necessity.
\end{remark}

For a general within-unit cost $f$, use
$m f(N/m)+B(m-1)$. Strict convexity of $f$ does not guarantee an interior
optimum or a power-law solution. For the particular family $f(n)=a n^p$,
$p>1$, the interior solution is
$m^\star=[a(p-1)N^p/B]^{1/p}$. A dense-interface approximation
$A/m+Bm^2$ instead yields $(A/(2B))^{1/3}$. These examples make the
assumptions and topology dependence explicit
\cite{parnas1972,baldwinclark2000}. Sequential organization design additionally
requires transition, learning, and delay costs; the static results alone do
not solve that problem.
'''

ILLUSTRATION_SECTION = r'''
\section{Executable Illustration}

The companion is an executable illustration, not an empirical validation or a
calibrated causal estimate. Its original Monte Carlo scenario model uses
chosen noise and cost coefficients to compare coalesced, split, market, and
hybrid architectures. Those scenarios do not implement optimal Wyner--Ziv
codes, infer operational bit rates from schema sliders, or optimize arbitrary
partitions. Their phase map is a sensitivity visualization for that heuristic
model, not an estimated information-theoretic boundary.

A separate analytical workbench evaluates
$\Delta(\kappa)=\Delta(0)2^{-2\kappa}$, the economic switching condition,
and the balanced-unit cost curve over integer unit counts. It makes the
assumptions visible and separates a numerical evaluation of a formula from
experimental evidence. Decision-value agility in the scenario model uses the
zero-action baseline under squared loss and retains negative values; mutual
information and sign accuracy are diagnostics, not the quality numerator.
The original scenario architecture still has a fixed three-group split; the
integer granularity sweep belongs to the separate workbench.
\footnote{Companion:
\href{https://galatheus-labs.github.io/coase-info-theory/}{galatheus-labs.github.io/coase-info-theory}.
Analytical workbench: \texttt{analytical-workbench.html} in the
\href{https://github.com/galatheus-labs/coase-info-theory}{public repository}.
Draft-branch changes are not live until merged and deployed.}

Figure~\ref{fig:regimes} depicts the economic comparison directly, in common
objective units. It is an analytical decision diagram, not a simulation result.

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
  \fill[gray!10] (0,0) -- (7,0) -- (7,5) -- cycle;
  \draw[->,thick] (0,0) -- (7.4,0)
    node[below,align=center,pos=0.5,yshift=-0.35cm]
    {coordination savings $H=C_{\mathrm{coal}}-C_{\mathrm{split}}$};
  \draw[->,thick] (0,0) -- (0,5.4)
    node[above,align=center] {excess decision loss $\Delta$};
  \draw[thick,dashed] (0,0) -- (7,5);
  \node[fill=white,inner sep=3pt,rotate=35.5] at (3.6,2.57)
    {$\Delta=H$: equal total objective};
  \node[align=center] at (2.0,4.2)
    {\textbf{Coalesce}\\decision deficit exceeds savings};
  \node[align=center] at (5.0,1.1)
    {\textbf{Split}\\savings exceed decision deficit};
\end{tikzpicture}
\caption{Economic, not lossless, switching. Both axes use the same objective
units per decision; the drawing uses different display scales on the two
axes. For $H>0$, splitting is weakly preferable below $\Delta=H$, even with
positive excess loss. In the Gaussian benchmark at fixed $H$, increasing
capacity lowers $\Delta$ and can cross this line at the finite threshold in
Corollary~\ref{cor:economic}.}
\label{fig:regimes}
\end{figure}

The heuristic simulation also exposes a planning tradeoff: up-front
representation investment can lower runtime error while adding delay or
rigidity. The chosen coefficients illustrate that possibility; they do not
establish its empirical magnitude or direction in a particular organization.
'''

MEASUREMENT_SECTION = r'''
\section{Measurement and Empirical Agenda}
\label{sec:measurement}

The empirical goal is to determine whether a boundary or protocol change
improves a specified decision objective, and whether the measured improvement
comes from better information, lower resource cost, lower delay, or a
combination. No empirical validation is claimed in this draft.

\subsection{A controlled replay as the first test}

A tractable first study uses incident or support cases with a defensible
reference outcome and the evidence available at the original decision time.
Freeze the underlying cases, loss rubric, downstream policy or model version,
permissions, tool access, and evaluation horizon. Compare four information
conditions on the same cases: local evidence only; a fixed structured handoff;
an agent-mediated handoff under a declared communication budget; and a
full-evidence reference. The full-evidence reference is a practical comparator,
not automatically the Bayes-optimal coalesced risk.

Vary the permitted handoff representation or budget independently of case
complexity. Pre-specify randomization, paired evaluation, stochastic repeats,
and blinded outcome scoring where feasible. Agent mediation should not gain
extra tools or action authority unless those are separate experimental factors.
Prevent hindsight leakage: later postmortems can label an outcome but should
not become evidence available to a policy at the earlier decision point.

Report direct decision loss, end-to-end latency, compute and token expenditure,
human interpretation effort, review effort, and safety outcomes separately
before combining them with declared objective weights. Include reference-policy
loss on every case, uncertainty intervals on paired differences, and
sensitivity to the loss rubric and cost weights. An observed reference gap can
be negative if the full-evidence policy is not optimal; do not clip such gaps or
silently take their logarithms. Choose sample size from a pilot variance,
clustering structure, and a pre-specified effect of interest, not a calendar
quarter alone. Cluster resampling by incident or another defensible independent
unit when multiple observations share a case.

This tests a comparative boundary-design hypothesis, not the Gaussian coding
law by default. A separate synthetic Gaussian experiment can verify the
analytic expressions or compare finite-budget codecs with the asymptotic
benchmark. It must not label a suboptimal codec's finite-sample curve an exact
realization of that bound.

\subsection{Operational proxies and their limits}

\begin{table}[htbp]
\centering
\caption{Measurements, proxies, and interpretation limits}
\label{tab:proxies}
\begin{tabularx}{\textwidth}{@{}l>{\raggedright\arraybackslash}X@{}}
\toprule
Quantity & Operational treatment \\
\midrule
Decision value $Q$ & Paired loss reduction against a fixed baseline; expert
scores, avoided rework, or SLA outcomes need a declared loss mapping. \\
Predictive surprise $S$ & Proper log scores on fixed targets where predictive
distributions and labels exist; escalation and reopen events are diagnostics,
not themselves Shannon surprise. \\
Latency $\tau$ & Signal-to-triage, signal-to-decision, and signal-to-action
intervals reported separately in a fixed unit. \\
Interpretation cost & Clarification requests and active translation time;
request count is affected by task difficulty and protocol inadequacy. \\
Interface richness & Field availability, missingness, representation type,
and actual message budget; completeness fractions are not bit capacities. \\
Monitoring cost & Review minutes, approvals, audits, and escalations, with
non-overlapping accounting. \\
\bottomrule
\end{tabularx}
\end{table}

Clarification round-trips and schema completeness can diagnose interface
insufficiency, but they do not estimate $R^\star$ and $\kappa$ in common
units without a separate validated measurement model. Do not subtract them to
construct $R^\star-\kappa$. Clarification is partly an outcome of the
interface; treating it as an exogenous communication requirement can make the
proposed test circular.

Operational bits require a declared alphabet, code, and per-decision or
per-block rate convention. A token count is an engineering budget, not a
semantic information rate by definition. Field counts and completeness
fractions cannot test a fourfold-per-bit slope. Even a defensible bit measure
does not make reopen probability or resolution time a Gaussian quadratic
loss. Theorem~\ref{thm:deficit} supplies a benchmark; transfer of its functional
form to workflow outcomes is an additional hypothesis.

Likewise, Proposition~\ref{prop:capacity} does not predict an empirical elbow.
$R^\star_\varepsilon$ is an operational tolerance crossing that can occur on
a smooth curve. Compare flexible alternatives before claiming a threshold or
log-linear relationship, and estimate an excess-loss curve only against a
well-defined reference. The economic comparison is whether the loss increase
is outweighed by measured coordination savings in common units.

For continuity with the trace playbook, a descriptive proxy can be written
\[
\widehat{\calG}=
\frac{Q}{t_0(1+T_{\mathrm{resolution}}/t_0)(1+\alpha H_{\mathrm{handoff}})},
\qquad t_0>0,\quad\alpha\geq0.
\]
Here $Q$ is baseline-relative value, $t_0$ is a fixed reference time, and
$H_{\mathrm{handoff}}$ is a handoff count, distinct from the economic savings
$H$. Declare $t_0$ and $\alpha$, retain negative values, and report the
components separately. This stabilized proxy is neither a literal
information-rate estimate nor generally equivalent to minimizing $J$.
Avoid counting handoff penalties again when their full costs already enter
the objective.

\subsection{Observational deployment studies}

A matched before/after analysis can characterize associations after adjusting
for measured case mix. It does not eliminate unobserved selection, changing
staffing, incident severity, temporal trends, or simultaneous tooling changes.
Staggered adoption can support a stronger design only with stated identification
assumptions, an appropriate estimator, checks on pre-treatment behavior, and
attention to spillovers between teams. Randomized rollout or crossover, where
safe, can more directly isolate the interface intervention. Safety and
permission constraints remain part of the feasible experimental design.

To examine the granularity model, compare costs across alternative feasible
partitions, not merely the number of teams an organization happens to have.
Estimate changes in both $A$ and $B$, record cross-boundary deficits and
transition costs, and check the balanced-unit and sparse-interface assumptions.
The conditional prediction is
$\Delta\log m^\star=\tfrac12(\Delta\log A-\Delta\log B)$ within the
interior surrogate regime. Adoption alone does not predict a $41\%$ increase
or finer decomposition. Register the planned analysis before examining test
outcomes; this proposed protocol has not itself been externally preregistered.
'''


def main():
    source = PAPER.read_text()
    if 'draft revision 1.3, 2026-09-09' in source:
        print('Revision 1.3 is already materialized; refusing to reapply.')
        return
    blob = hashlib.sha1(b'blob ' + str(len(source.encode())).encode() + b'\0' + source.encode()).hexdigest()
    if blob != 'bddbeb5f531d57fa0ef262b5fb1a492f5e45af25':
        raise RuntimeError(f'Unexpected source blob: {blob}; review before migration.')
    revised = revise_paper(source)
    PAPER.write_text(revised)
    print(f'Revised {PAPER}: {len(source)} -> {len(revised)} characters')


if __name__ == '__main__':
    main()
