# Performance

Performance budgets, optimization rules, and profiling conventions.

---

## 1. Principles

- **Measure before optimizing** — never optimize without a profiling baseline
- **Budget-driven** — every project has explicit performance budgets (bundle size, render time, API latency)
- **Progressive enhancement** — core experience works without JS/large assets; enhancements layer on
- **Lazy by default** — defer everything that isn't needed for the initial render/interaction

---

## 2. Performance Budgets

| Metric | Budget | Measurement |
|--------|--------|-------------|
| Initial bundle (JS/CSS) | `< 200 KB` gzipped | Webpack/Rollup bundle analyzer |
| Time to Interactive | `< 2.5s` on 3G | Lighthouse |
| First Contentful Paint | `< 1.5s` | Lighthouse |
| API p95 latency | `< 500ms` | APM / custom metrics |
| DB query p95 | `< 100ms` | DB monitoring |
| Image load | `< 1s` visible | Network tab / Lighthouse |
| Animation frame | `60 fps` | DevTools performance tab |

---

## 3. Rules

### Bundle / Asset Size

- Tree-shake unused imports — regular audit with bundle analyzer
- Code-split by route — each route loads only its own code
- Lazy-load below-fold images and heavy components
- No large inline SVGs — reference as external files or sprites
- Prefer native formats (WebP, AVIF) over PNG/JPEG

### Rendering (UI)

- Virtualize long lists — only render visible rows
- Debounce search inputs (300ms minimum)
- Memoize expensive computations; avoid premature memoization of cheap ones
- No layout thrashing — batch DOM reads and writes
- Reduce re-render scope — push state down to the component that needs it

### Data / API

- Paginate all list endpoints (cursor preferred, offset for admin)
- Batch related requests into a single call
- Cache server responses with stale-while-revalidate
- Compress API responses (gzip / brotli)
- Index all query columns in the database

### Images & Media

- Responsive images — serve multiple resolutions, let the browser pick
- Lazy-load offscreen images (`loading="lazy"`)
- Preload critical (above-fold) images (`<link rel="preload">`)
- Video: use compressed codecs (H.265, AV1), stream not download

---

## 4. Profiling Checklist

When diagnosing a performance issue:

- [ ] Check bundle size — is the page loading more code than it needs?
- [ ] Check network — are there unnecessary or large requests?
- [ ] Check render count — is a component re-rendering too often?
- [ ] Check query count — is there an N+1 in the API/DB layer?
- [ ] Check images — are they larger or higher-res than needed?
- [ ] Check animation — are there frame drops in the DevTools performance tab?
- [ ] Check cache — is the response cacheable but not cached?

---

## 5. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Bundle | Bundle size within budget | bundlesize / webpack-bundle-analyzer | `npm run check:size` | Exceeds budget |
| Lighthouse | Performance, accessibility, SEO scores | Lighthouse CI | `npm run lighthouse` | Score drops below threshold |
| Profile | Render count, re-render causes | React Profiler / DevTools | Manual | Unexpected re-renders |
| API | Latency p95, response size | k6 / autocannon | `npm run test:perf` | Latency or size exceeds budget |
| DB | Query performance, N+1 detection | pg_stat_statements / EXPLAIN ANALYZE | `npm run test:db-perf` | Slow query detected |

### Self-Validation

```bash
npm run check:size && npm run lighthouse -- --budget=budget.json
```
