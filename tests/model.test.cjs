'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const M = require('../assets/analytical-model.js');
let checks = 0;
function close(a,b){assert.ok(Math.abs(a-b)<1e-10*Math.max(1,Math.abs(a),Math.abs(b)),`${a} != ${b}`);checks++;}
close(M.deficit(4,0),4); close(M.deficit(4,1),1); close(M.deficit(4,2),0.25);
close(M.economicThreshold(4,1),1); close(M.economicThreshold(4,4),0); close(M.economicThreshold(4,5),0);
assert.equal(M.economicThreshold(4,0),Infinity); assert.equal(M.economicThreshold(0,-1),Infinity); close(M.economicThreshold(0,0),0);
for(const A of [0.2,1,10,100,1e4])for(const B of [.1,1,7,100])for(const N of [1,2,7,20]){
  const g=M.granularity(A,B,N);
  close(g.best.cost,Math.min(...g.rows.map(r=>r.cost)));
  assert.ok([Math.floor(g.continuous),Math.ceil(g.continuous)].includes(g.best.m));
  for(const r of g.rows)assert.ok(r.integerCost+1e-10>=r.cost);
  for(let i=0;i<N-1;i++)close(g.rows[i+1].cost-g.rows[i].cost,B-A/((i+1)*(i+2)));
}
close(M.granularity(100,4,20).continuous,5); close(M.granularity(100,2,20).continuous/5,Math.sqrt(2));
close(M.granularity(50,2,20).continuous,5);
close(M.granularity(25,2,20).continuous/5,Math.sqrt(.5));
close(M.agility(1,2,10,55,55),-.05); close(M.agility(1,.5,10,0,55),.05);
assert.throws(()=>M.deficit(-1,1)); assert.throws(()=>M.granularity(1,0,4)); assert.throws(()=>M.granularity(1,1,2.5));
assert.throws(()=>M.agility(1,.5,0,1,55));
const lambda=.5,tau=3,Q0=2,eps=1e-6;
const marginal=x=>Q0*x*Math.exp(-x*tau);
assert.ok((marginal(lambda+eps)-marginal(lambda-eps))/(2*eps)<0);
close(Q0*Math.exp(-lambda*tau)*(1-lambda*tau),(marginal(lambda+eps)-marginal(lambda-eps))/(2*eps));
for(const f of ['index.html','analytical-workbench.html']){
  const html=fs.readFileSync(path.join(__dirname,'..',f),'utf8');
  for(const match of html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g))new vm.Script(match[1],{filename:f});
}
const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');
const inline=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(s=>s.includes('function simulateBoundary('));
assert.ok(inline,'scenario script found');
const cutoff=inline.indexOf("\ndocument.getElementById('runBtn')");
assert.ok(cutoff>0,'cut before UI startup');
const context=vm.createContext({console,Math,assert});
vm.runInContext(inline.slice(0,cutoff),context);
vm.runInContext(`
const cfg={protocol:60,interdependence:50,observability:60,agentCoverage:50,governance:60,marketFriction:40,volatility:40,planning:50,agentCount:12,trials:2000,seed:101};
const result=runSimulation(cfg);
assert.equal(result.length,4);
for(const row of result){
  assert.ok(Number.isFinite(row.objective)&&Number.isFinite(row.agility));
  assert.ok(Math.abs(row.agility-(row.baselineLoss-row.loss)/(row.effectiveLatency*(1+row.cost/55)))<1e-12);
  assert.ok(Math.abs(row.baselineLoss-result[0].baselineLoss)<1e-12);
}
const original=boundaryStructure;
boundaryStructure=(id,c)=>({...original(id,c),extraNoise:10});
const bad=simulateBoundary(BOUNDARIES[0],cfg);
assert.ok(bad.decisionValue<0&&bad.agility<0,'negative decision value must remain negative');
boundaryStructure=original;
`,context);
const tex=fs.readFileSync(path.join(__dirname,'../paper/coase-information-theory.tex'),'utf8');
assert.ok(tex.includes('draft revision 1.3, 2026-09-09'));
assert.ok(tex.includes('cor:economic')&&tex.includes('1-\\lambda\\tau'));
assert.ok(!tex.includes('no causal identification beyond'));
assert.ok(!tex.includes('any strictly convex internal cost yields'));
assert.ok(!html.includes('// capacity threshold R* = kappa:'));
console.log(`Passed ${checks} numerical checks, edge cases, inline JavaScript syntax, paired scenario comparisons, negative agility, and revision assertions.`);
