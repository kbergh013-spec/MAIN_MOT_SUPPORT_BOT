import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

sql = """
-- =====================
-- NEW TABLES
-- =====================

CREATE TABLE IF NOT EXISTS prop_firms (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS account_types (
    id SERIAL PRIMARY KEY,
    prop_firm_id INTEGER NOT NULL REFERENCES prop_firms(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (prop_firm_id, name)
);

CREATE TABLE IF NOT EXISTS account_sizes (
    id SERIAL PRIMARY KEY,
    label TEXT NOT NULL UNIQUE,
    numeric_size INTEGER,
    active BOOLEAN NOT NULL DEFAULT true,
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS prize_catalog (
    id SERIAL PRIMARY KEY,
    prop_firm_id INTEGER NOT NULL REFERENCES prop_firms(id) ON DELETE CASCADE,
    account_type_id INTEGER NOT NULL REFERENCES account_types(id) ON DELETE CASCADE,
    account_size_id INTEGER NOT NULL REFERENCES account_sizes(id) ON DELETE CASCADE,
    display_name TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (prop_firm_id, account_type_id, account_size_id)
);

ALTER TABLE winners
    ADD COLUMN IF NOT EXISTS prize_catalog_id INTEGER,
    ADD COLUMN IF NOT EXISTS prop_firm_id INTEGER,
    ADD COLUMN IF NOT EXISTS account_type_id INTEGER,
    ADD COLUMN IF NOT EXISTS account_size_id INTEGER,
    ADD COLUMN IF NOT EXISTS custom_prize_text TEXT;
"""

with psycopg2.connect(DATABASE_URL, sslmode="require") as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()

print("✅ Tables created successfully")
