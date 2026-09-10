#!/usr/bin/env python3
"""Final accounting, numerical, and rendering checks for the one-time draft build."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
p=ROOT/'paper/coase-information-theory.tex'
s=p.read_text().replace('\x08eta',r'\beta')
start=r'\begin{remark}[Agentic routing: accounting condition]'
end=r'\paragraph{Governance limit: a conditional hypothesis.}'
if start in s:
    a=s.index(start);b=s.index(end,a)
    s=s[:a]+r'''\begin{remark}[Agentic routing: net-objective accounting]
Let $\Delta L$ and $\Delta C_j$ denote agent-assisted minus baseline expected
loss and each disjoint cost component, respectively, in the same evaluation
horizon. With fixed objective weights and $\beta_S=0$, the exact net-objective
condition is
\[
\Delta J=\Delta L+\sum_j\lambda_j\Delta C_j<0.
\]
Any independently priced predictive burden adds $\beta_S\Delta S$.
Execution effort belongs in computation cost; measurable reviews and approvals
belong in monitoring cost. Broader governance burdens must not be counted again
under overlapping labels. Routing or execution savings alone are insufficient
if direct decision loss or other costs increase by more.

An improvement in this objective does not automatically improve the agility
ratio. That comparison separately requires
$Q'/[\tau'(1+\widetilde C')]>Q/[\tau(1+\widetilde C)]$, with a common
baseline, time unit, and cost scale. Neither information fidelity nor faster
execution alone is sufficient.
\end{remark}

'''+s[b:]
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s),'Control character in TeX'
p.write_text(s)
p=ROOT/'scripts/apply_revision_1_3.py'
if p.exists():
    s=p.read_text().replace('By default $'+chr(92)+'beta_S=0','By default $'+chr(92)*2+'beta_S=0')
    p.write_text(s)
p=ROOT/'tests/model.test.cjs'
if p.exists(): p.write_text(p.read_text().replace('Q0=2,eps=1e-5','Q0=2,eps=1e-6'))
p=ROOT/'analytical-workbench.html'
if p.exists():
    s=p.read_text().replace("const show=n=>Number.isFinite(n)?Number(n).toFixed(4):'no finite threshold';",
                           "const show=n=>Number.isFinite(n)?(n!==0&&Math.abs(n)<0.0001?n.toExponential(3):Number(n).toFixed(4)):'no finite threshold';")
    s=s.replace('const tie=Math.abs(gap)<=1e-12*Math.max(1,Math.abs(loss),Math.abs(h));',
                'const tie=gap===0||(Number.isFinite(threshold)&&threshold>0&&Math.abs(k-threshold)<1e-12);')
    s=s.replace('step="1" value="100"','step="any" value="100"').replace('step="0.25" value="4"></label>\n<label>Primitive','step="any" value="4"></label>\n<label>Primitive')
    s=s.replace('<title>Coordination cost by unit count</title><desc>Numeric values', '<title id="curve-title">Coordination cost by unit count</title><desc id="curve-desc">Numeric values')
    p.write_text(s)
print('Finalized TeX accounting and encoding, numerical finite difference, and small-deficit display.')
