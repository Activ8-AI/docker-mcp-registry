## Agent Hub – Competitive Intelligence Plane

The Agent Hub orchestrates the six web-analysis agents that power the Competitive Intelligence Engine (v1). Each agent is defined as an MCP capability with a hardened runtime (Docker container or remote endpoint), shared logging, and a governance shim that reports status back to Codex.

---

### 1. Assignment Rules
| Agent | Primary Owner | Backup | Escalation Path | Notes |
| --- | --- | --- | --- | --- |
| `surveillance_agent` | Web Intelligence | Automation SRE | Reflex `cie_signal_normalizer` | DOM diffs + sitemap drift |
| `research_agent` | Strategy Research | Editorial Ops | Governance Council | Long-form analysis, sentiment |
| `competitor_watch_agent` | Revenue Ops | Pricing Desk | Finance Custodian | Pricing/SKU deltas |
| `web_crawler_agent` | Product Intelligence | Web Intelligence | Launch Commander | Deep crawl on rumor triggers |
| `signal_harvester_agent` | Growth Ops | Media Ops | Marketing Custodian | Social/ad library pulls |
| `content_diff_agent` | Editorial Ops | Web Intelligence | Governance Council | Before/after diffs, writes brief stubs |

Assignments are stored in Codex with SLA targets. Reflex references these tables to auto-route deltas.

---

### 2. Trigger Logic
| Trigger | Source | Agents Invoked | Notes |
| --- | --- | --- | --- |
| Scheduled Sweep | Cron (6h) | `surveillance_agent`, `signal_harvester_agent` | Maintains baselines |
| Watchlist URL Change | Tuned webhooks | `surveillance_agent`, `content_diff_agent` | Fires immediate diff |
| Pricing Alert | RSS / manual ping | `competitor_watch_agent` | Adds Task: “Validate SKU delta” |
| Launch Rumor | Slack / CRM note | `web_crawler_agent`, `research_agent` | Deep crawl + long-form brief |
| Keyword Collision | SEO telemetry | `signal_harvester_agent`, `competitor_watch_agent` | Auto create Teamwork reflex |

All triggers are reflected in the Reflex DAG so automation health is observable.

---

### 3. Output Contracts
Each agent publishes a normalized payload:
```
signal_id: uuid
agent: string
client_id: string
competitor_id: string
signal_type: enum
severity: {watchlist|monitor|action}
confidence: 0..1
evidence: [ {uri, hash, captured_at} ]
payload: object
custodian_hash: sha256
```

- `severity` is first-pass; Reflex can upgrade/downgrade.  
- `custodian_hash` combines agent id + evidence hash + timestamp.  
- Payloads exceeding the action threshold must include a draft governance brief for Codex.

---

### 4. Confidence Scoring & Governance Hooks
- `surveillance_agent` & `content_diff_agent`: deterministic DOM diff quality metrics → base confidence 0.75, penalty for low DOM overlap.  
- `research_agent`: citation completeness + sentiment consensus. <0.6 auto-routes to manual review.  
- `signal_harvester_agent`: uses channel-specific trust weighting; anomalies cross-check with third-party APIs.  
- Every emission recorded in Custodian ledger with `agent_run_id`, docker image digest, and dependency manifest.

Governance hooks:
1. **Validation Queue:** signals 0.4–0.7 enter Codex “Validation” view.  
2. **Audit Trail:** nightly job exports last 24h of runs + hashes to secure storage.  
3. **Fail-Safes:** if agent misses two consecutive sweeps, Reflex raises red alert to Operations Heartbeat.

---

### 5. Teamwork & Portal Contracts
- When Reflex promotes a signal, `teamwork_task_writer` builds the task body from the agent payload + Charter brief.  
- Fields pushed into Teamwork:
  - Title: `CIE | <client> | <delta>`  
  - Description: summary, evidence, recommended action, SLA, custodian hash  
  - Custom fields: `signal_id`, `confidence`, `urgency`, `portal_link`
- Client Portal consumes the same payload (read-only) to populate Competitor Intelligence widgets.

---

### 6. Operational Runbook
1. **Deploy** each agent container with secrets stored in Docker secrets manager.  
2. **Register** MCP metadata (tools, parameters) so clients discover capabilities via catalog.  
3. **Heartbeat**: 5-min cadence metric push (`agent_name`, `status`, `last_success`).  
4. **Incident Handling**:  
   - Severity 1 (agent offline): fail over to backup owner, notify Governance Council.  
   - Severity 2 (data quality): pause automation, rerun last sweep after fix.  
5. **Review Cadence:** weekly Governance sync reviews Custodian hashes vs. sample evidence.

Agent Hub documentation lives here so any future Charter audit can reconstruct who runs what, when it fires, and how outputs propagate.
