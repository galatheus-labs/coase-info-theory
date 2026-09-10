/* Draft 1.3 analytical benchmarks. No estimated empirical parameters. */
(function (root) {
  'use strict';
  function finite(value, name, minimum = -Infinity) {
    if (!Number.isFinite(value) || value < minimum) throw new RangeError(`${name} must be finite and >= ${minimum}`);
    return value;
  }
  function deficit(delta0, kappa) {
    finite(delta0, 'delta0', 0); finite(kappa, 'kappa', 0);
    return delta0 * 2 ** (-2 * kappa);
  }
  function economicThreshold(delta0, savings) {
    finite(delta0, 'delta0', 0); finite(savings, 'savings');
    if (savings < 0) return Infinity;
    if (delta0 === 0) return 0;
    if (savings === 0) return Infinity;
    return Math.max(0, (Math.log2(delta0) - Math.log2(savings)) / 2);
  }
  function granularity(A, B, N) {
    finite(A, 'A', Number.MIN_VALUE); finite(B, 'B', Number.MIN_VALUE);
    if (!Number.isInteger(N) || N < 1 || N > 10000) throw new RangeError('N must be an integer in [1,10000]');
    const continuous = Math.min(N, Math.max(1, Math.sqrt(A / B)));
    const rows = Array.from({length: N}, (_, i) => {
      const m = i + 1;
      const q = Math.floor(N / m), r = N % m;
      const internal = A / m;
      const interfaces = B * (m - 1);
      const integerInternal = A * ((m - r) * q * q + r * (q + 1) ** 2) / (N * N);
      return {m, internal, interfaces, cost: internal + interfaces, integerCost: integerInternal + interfaces};
    });
    const best = rows.reduce((a, b) => b.cost < a.cost ? b : a);
    const integerBest = rows.reduce((a, b) => b.integerCost < a.integerCost ? b : a);
    return {continuous, best, integerBest, rows};
  }
  function agility(baselineLoss, actionLoss, latency, cost, costScale) {
    finite(baselineLoss, 'baselineLoss'); finite(actionLoss, 'actionLoss');
    finite(latency, 'latency', Number.MIN_VALUE); finite(cost, 'cost', 0); finite(costScale, 'costScale', Number.MIN_VALUE);
    return (baselineLoss - actionLoss) / (latency * (1 + cost / costScale));
  }
  const api = {deficit, economicThreshold, granularity, agility};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.CoaseAnalytical = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
