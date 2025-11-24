## Competitive Intelligence Engine (v1)

**Classification:** MAOS → Intelligence Plane → Web Analysis Agents → Client Portal  
**Status:** Required per Charter  
**Purpose:** Provide always-on external surveillance so the Client Intelligence Portal, Reflex DAG, Teamwork, and Codex governance have a synchronized view of competitor and industry motion.

---

### 1. Module Mandate
- Restore Charter integrity by pairing the internal Action Matrix with external context.
- Maintain a live map of every client’s competitive set, industry shifts, algorithm changes, and sentiment indicators.
- Output actionable deltas (tasks, alerts, briefs) instead of passive summaries.
- Preserve Custodian-grade governance: every signal carries summary, market impact, implication, recommended action, governance notes, confidence score, and custodian hash.

---

### 2. System Composition
| Layer | Description | Key Artifacts |
| --- | --- | --- |
| **Competitor Definition Map** | Canonical roster of competitors, industries, and monitored assets per client. | `clients/*.yaml` (source), Notion “Client Matrix”, Codex tables |
| **Web Analysis Agents** | Specialized crawlers/scrapers tuned for pricing pages, ads, product notes, etc. | `agents/agents.md` (assignment + triggers) |
| **Signal Processing** | Normalizes raw scrapes, extracts deltas, ranks risk/opportunity, and writes Governance Briefs. | Reflex DAG node `cie_signal_normalizer` |
| **Execution Bridge** | Routes approved deltas into Teamwork, Heartbeats, Strategy Sprints, and KPI sheets. | `servers/teamwork/server.yaml` + Reflex automation |
| **Client Portal Surfaces** | Competitor Intelligence tab, Industry Radar, Trend Watch, Revenue Impact view, Red/Yellow alerts. | Client Portal schema (`portal/`) |

---

### 3. Competitor Definition Map
1. **Sources**  
   - Client Matrix & Onboarding packets  
   - CRM opportunity notes  
   - Existing briefs / win-loss reports  
   - External indexes (Crunchbase, SimilarWeb, ad libraries)  
2. **Schema (minimum fields)**  
   - `client_id`, `competitor_id`, `competitor_name`, `segment`, `persona`, `geo_focus`  
   - `products_monitored[]`, `pricing_urls[]`, `campaign_assets[]`, `keywords[]`  
   - `threat_level` (enum), `last_seen`, `custodian_hash`  
3. **Automation**  
   - Nightly sync from Notion → Codex table → YAML export for Reflex pipeline.  
   - Change log hashed and stored for governance review.

---

### 4. Web Analysis Agent Wiring
Agents run inside the Intelligence Plane with hardened egress rules. Each agent exposes MCP tools defined in `agents/agents.md`.

| Agent | Scope | Trigger | Output Contract |
| --- | --- | --- | --- |
| `surveillance_agent` | Whole-site change detection, sitemap drift | Scheduled 6h sweep or URL watchlist delta | DOM diff package + risk tag |
| `research_agent` | Long-form assets (blogs, PR, whitepapers) | RSS ping, manual enqueue | Extracted claims, vectors, credibility score |
| `competitor_watch_agent` | Pricing + SKU catalogs | Pricing URL change, manual price check | Normalized pricing table + delta |
| `web_crawler_agent` | Deep crawl for new feature docs | Launch rumor, new subdomain | Feature summary, impacted personas |
| `signal_harvester_agent` | Social + ad libraries | Daily schedule | Campaign meta, spend hints, CTA classification |
| `content_diff_agent` | Before/after diff of key sections | Triggered by `surveillance_agent` output | Markdown diff, potential motive, urgency |

All agents emit:
```
{
  "signal_id": "...",
  "client_id": "...",
  "competitor_id": "...",
  "evidence_uri": "...",
  "confidence": 0-1,
  "raw_payload": {...}
}
```

---

### 5. Signal Processing & Governance
1. **Normalization**  
   - Convert raw payloads into typed deltas (pricing, SKU, campaign, positioning, sentiment).  
   - Enrich with historical baselines and KPI tie-ins (ARR impact, funnel impact).  
2. **Governance Brief Builder**  
   - Template: Summary, Market Impact, Strategic Implication, Recommended Actions, Governance Notes, Confidence Score, Custodian Hash.  
   - Stored alongside Reflex DAG provenance for audits.  
3. **Confidence Policies**  
   - `<0.4` → park as Watchlist.  
   - `0.4–0.7` → manual validation queue.  
   - `>0.7` → eligible for automatic Reflex → Teamwork tasking.

---

### 6. Reflex → Teamwork Pipeline
1. `cie_signal_normalizer` publishes structured deltas to Reflex bus.  
2. `cie_delta_ranker` scores urgency (`critical`, `high`, `routine`).  
3. `cie_task_router` evaluates action matrices per client:  
   - Pricing hikes → Revenue pod  
   - SKU launches → Product/Enablement pod  
   - Keyword incursions → SEO/PPC pod  
4. `teamwork_task_writer` (leverages `servers/teamwork`) opens/updates tasks with:  
   - Charter brief snippet  
   - Required action, owner, SLA  
   - Cross-links to Client Portal + Codex record  
5. Heartbeat + KPI systems subscribe to updates for downstream dashboards.

Sample Reflex contract:
```
{
  "delta_type": "pricing_change",
  "client_id": "acme",
  "impact_estimate": "+6% CAC",
  "recommended_action": "Adjust tiered bundle messaging",
  "assignment": {
    "team": "Revenue Ops",
    "system": "Teamwork",
    "task_type": "reflex_auto"
  }
}
```

---

### 7. Client Portal Integration
- **Competitor Intelligence Tab**  
  - Timeline of deltas, current threat level, open reflex tasks, revenue impact heatmap.  
- **Industry Radar**  
  - Macro + micro signals aggregated by segment, surfaced as trend cards with watchlist toggles.  
- **Trend Watch**  
  - Rolling 30/60/90-day signal velocity, drillable to evidence.  
- **Risk Levels & Alerts**  
  - Red/Yellow statuses derived from Reflex ranker; mirrored into Heartbeats.  
- **Action Recommendations & KPI Impact**  
  - Auto-linked to Strategy Sprint backlog and Revenue mapping workbook.

Portal widgets pull from the same Custodian-backed datastore so governance verifiers can trace any claim back to evidence + hash.

---

### 8. Implementation Checklist
1. Stand up Competitor Definition Map sync (Notion → Codex → YAML).  
2. Deploy/verify each agent container + register tools in Agent Hub.  
3. Wire signal topics into Reflex DAG (`cie_signal_normalizer`, `cie_delta_ranker`, `cie_task_router`).  
4. Extend Teamwork automation to accept Reflex payloads (create/update tasks with Charter brief).  
5. Add Client Portal widgets + API endpoints for Competitor Intelligence, Industry Radar, and Risk Alerts.  
6. Document governance review cadence; ensure Custodian hashes stored with SHA-256 + timestamp.  
7. Run smoke test: inject mock competitor price hike, confirm end-to-end propagation (agent → Reflex → Teamwork → Portal).

---

### 9. Future Enhancements
- Add LLM ecosystem lenses (model release trackers, API pricing monitors).  
- Blend public sentiment (GDELT, Google Trends, Reddit) with campaign signals for richer risk scoring.  
- Introduce opportunity auto-drafting (Reflex suggests campaigns with templated creative).  
- Expand KPI mapping so every delta shows projected ARR + margin impact in <60 seconds.

Charter compliance now demands this module stay continuously active; this document is the canonical install reference for v1.
