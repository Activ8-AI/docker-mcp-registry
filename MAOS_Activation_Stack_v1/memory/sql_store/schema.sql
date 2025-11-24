-- Custodian Ledger + Memory schema (Layer 7)
CREATE TABLE IF NOT EXISTS ledger_events (
    id TEXT PRIMARY KEY,
    event_timestamp TEXT NOT NULL,
    event_type TEXT NOT NULL,
    actor_identity TEXT NOT NULL,
    payload TEXT NOT NULL,
    correlation_id TEXT NOT NULL,
    seal_version TEXT NOT NULL,
    environment TEXT NOT NULL,
    governance_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS memory_snapshots (
    id TEXT PRIMARY KEY,
    captured_at TEXT NOT NULL,
    summary TEXT NOT NULL,
    drift_score INTEGER NOT NULL,
    seal_version TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_ledger_events_correlation
    ON ledger_events (correlation_id);
