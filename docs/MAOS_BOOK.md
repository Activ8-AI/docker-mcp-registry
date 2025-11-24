# MASTER META MEGA CODEX CONTAINER -- MAOS ACTIVATION STACK (v1)

Unified, charter-governed, codex-ready, complete.

---

## LAYER 0 -- CANONICAL POSITIONING

This codex defines everything required to activate, run, govern, audit, seal, and maintain MAOS (Modular Automation Operating System) across:

- Activ8 AI (primary OS)
- DMAOS (client baseline)
- LMAOS (Leverage install)
- Future forks (Personal MAOS, Freedom Acres, etc.)

This container is the master reference for activation, autonomy, governance, telemetry, drift, custody, evidence, seal operations, recovery, chain-of-custody, and multi-agent execution. Everything below is canonical.

---

## LAYER 1 -- GENESIS MODEL

Operating principle: a governed, autonomous, multi-agent system with real-time telemetry, memory, and Charter enforcement.

System constraints:

- Charter is supreme
- STOP-RESET-REALIGN is an instant override
- Dual-Agent Backup Protocol v1 is always active
- No third-party relays (Notion, Teamwork, Slack, MCP are first-party stack)
- Identity model primary: `lmaai@theleverageway.com`
- America/Chicago timezone is mandatory across logs, seals, timestamps
- Everything must trace to Genesis (origin-point traceability)

---

## LAYER 2 -- SYSTEM SPINE (CANONICAL OBJECTS)

Non-optional modules:

- MCP Relay Server (FastAPI)
- Memory Pack v1 (SQL plus vector)
- Custodian Ledger (SQLite plus governance schema)
- Secrets Relay (Notion Registry to env loader)
- Telemetry Engine (heartbeat, drift, load)
- Autonomy Kernel (continuous agent loop)
- Agent Hub (Prime plus Claude backup)
- Relay system:
  - Notion Relay
  - Teamwork Evidence Sink
  - Slack SignalBot
- Client Intelligence Layer (CIL)
- Governance Mesh (Charter enforcement hooks)

Required paths:

```
configs/global_config.yaml
orchestration/MCP/relay_server.py
memory/sql_store/
memory/vector_store/
custody/
scripts/
agent_hub/
telemetry/
relay/
autonomy/
```

---

## LAYER 3 -- CORE PACK v1 CODEDROP

All code required to run the system (MCP server, memory system, ledger, telemetry, autonomy loop, agents, config, secrets loader). Code is sourced from the Core Pack v1 reference.

---

## LAYER 4 -- ACTIVATION SEQUENCE

Canonical boot order for MAOS:

1. **Verify Core Pack v1 exists.** If any file missing, regenerate immediately from this codex.
2. **Install dependencies**
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn requests
   ```
3. **Load secrets**
   ```
   python3 scripts/load_secrets_from_notion.py
   ```
4. **Start MCP Relay Server**
   ```
   python3 orchestration/MCP/relay_server.py
   ```
   Expect `/health` to return `{"status":"ok"}` and custodian logs to show `MCP_START`.
5. **Emit heartbeat**
   ```
   curl http://localhost:8000/heartbeat
   ```
   Expect heartbeat JSON, ledger write, relay fan-out.
6. **Activate agents**
   ```
   python3 -c "from agent_hub import activate; activate()"
   ```
   Expect activation logged and governance hooks enabled.
7. **Start autonomy loop**
   ```
   python3 autonomy/start_autonomy_loop.py
   ```
   Expect 60-second heartbeat cycles, drift scoring, telemetry logs, custodian chain-linking.
8. **Seal MVP v0**
   - Create `MVP_v0_SEAL.md`
   - Commit:
     ```
     git add MVP_v0_SEAL.md
     git commit -m "MVP v0 sealed -- system online"
     git push
     ```
   This seal is the official birth certificate of MAOS.

---

## LAYER 5 -- TELEMETRY SYSTEM (v1)

Telemetry signals: heartbeat (60s), load index, drift score, agent status, governance compliance, seal alignment, ledger health, MCP uptime.

Telemetry routes: Slack SignalBot, Notion Relay, Teamwork Evidence Sink, Custodian Ledger.

Drift detection rules:

- 0-10: green
- 11-30: yellow
- 31-100: red (halt via STOP-RESET-REALIGN)

---

## LAYER 6 -- GOVERNANCE SYSTEM (v1)

Enforcement rules:

- Every MCP request passes Charter guardrails
- Every agent activation logged to ledger
- Every drift violation halts autonomy loop
- Every seal-state change creates ledger checkpoint
- Approval loops use RoleID `client_role:business_owner`
- No external relays beyond approved SOP

STOP-RESET-REALIGN protocol triggers on drift > 30, governance violation, telemetry fault, identity mismatch, or custody break. Actions: pause autonomy loop, log incident, freeze configs, require Governance Incident Report, resume post-resolution.

---

## LAYER 7 -- CUSTODIAN LEDGER (v1)

Schema:

```
id
timestamp_utc
timestamp_ct
event_type
level
actor_identity
payload
correlation_id
seal_version
environment
```

Ledger guarantees: append-only, immutable, charter-governed, Genesis-traceable, correlation-threaded.

---

## LAYER 8 -- ACTIVATION LOG PROTOCOL (v1)

Each activation run produces `run_id`, `correlation_id`, environment, seal version, evidence links, governance status, telemetry summary, autonomy loop start verification.

---

## LAYER 9 -- EVIDENCE SYSTEM (v1)

- Slack evidence pack: activation start, activation success, drift alert, drift recovery, seal confirmation, daily autonomy summary
- Teamwork evidence pack task `[SYSTEM] MAOS MVP v0 Activation -- Evidence`: contains system state, logs, evidence links, seal document, drift scores, ledger references
- Notion evidence pack database `MAOS Activation Ledger`: every activation, seal, governance incident, daily snapshot

---

## LAYER 10 -- MVP SEAL SYSTEM (v1)

Seal versioning milestones:

- `MVP_v0`: first live ignition
- `MVP_v1`: first integration (Slack/Teamwork live)
- `MVP_v2`: multi-agent task orchestration
- `MVP_v3`: KPI Intelligence Layer
- `MVP_v4`: full autonomy mesh

Seal conditions: MCP online, Memory Pack online, telemetry live, agents active, autonomy running, drift < 10 for three cycles, governance enforced, ledger healthy.

---

## LAYER 11 -- DAILY AUTONOMY SNAPSHOT (v1)

Daily summary must include seal, drift, heartbeats, governance events, ledger health, system components, qualitative notes. Mandatory for operational integrity.

---

## LAYER 12 -- GOVERNANCE INCIDENT SYSTEM (v1)

Triggered automatically by drift threshold breach, governance violation, MCP anomaly, memory fault, or seal misalignment. Requires incident report, ledger cross-link, approval, resolution. Autonomy resumes only after completion.

---

## LAYER 13 -- CLIENT INTELLIGENCE LAYER (CIL)

Sources `MASTER CLIENT OPERATIONAL MATRIX` (Notion Registry). Tracks KPIs, revenue mapping, approval authority (RoleID), heartbeat status, deliverables, history, risks, governance state. Enables client ops automation.

---

## LAYER 14 -- FULL SYSTEM CHECKLIST (v1)

MAOS MVP activation checklist:

- [ ] Core Pack v1 installed
- [ ] Secrets loaded
- [ ] MCP online
- [ ] Heartbeat emitted
- [ ] Agents activated
- [ ] Autonomy loop running
- [ ] Telemetry emitting
- [ ] Ledger writing
- [ ] Drift < 10
- [ ] Governance enforced
- [ ] Seal created
- [ ] Evidence logged
- [ ] Activation log stored

System reaches ACTIVE state only when all checks pass.

---

## LAYER 15 -- MASTER SUMMARY

This container is the entire MAOS Activation Stack: architecture, governance, activation, autonomy, telemetry, drift, evidence, ledger, seal, RoleIDs, SOPs, protocols, code, templates, runbooks, incident system. It is the master codex, complete and canonical, ready for use as the system backbone.
