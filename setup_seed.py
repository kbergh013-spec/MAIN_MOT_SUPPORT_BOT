import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

sql = """
-- =====================
-- PROP FIRMS
-- =====================

INSERT INTO prop_firms (name, sort_order) VALUES
    ('Alpha Futures', 1),
    ('FFF', 2),
    ('Lucid', 3),
    ('Tradeify', 4),
    ('MFF', 5),
    ('TPT', 6),
    ('Funded Next', 7),
    ('Apex', 8),
    ('MOT Indicator', 9)
ON CONFLICT (name) DO NOTHING;

-- =====================
-- ACCOUNT TYPES
-- =====================

-- Alpha Futures
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Zero', 1 FROM prop_firms WHERE name = 'Alpha Futures'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Standard', 2 FROM prop_firms WHERE name = 'Alpha Futures'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Advanced', 3 FROM prop_firms WHERE name = 'Alpha Futures'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- FFF
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Premier', 1 FROM prop_firms WHERE name = 'FFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Prime', 2 FROM prop_firms WHERE name = 'FFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'S2F', 3 FROM prop_firms WHERE name = 'FFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Velocity', 4 FROM prop_firms WHERE name = 'FFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- Lucid
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Flex', 1 FROM prop_firms WHERE name = 'Lucid'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Pro', 2 FROM prop_firms WHERE name = 'Lucid'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Direct', 3 FROM prop_firms WHERE name = 'Lucid'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- Tradeify
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Growth', 1 FROM prop_firms WHERE name = 'Tradeify'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Select', 2 FROM prop_firms WHERE name = 'Tradeify'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Lightning Funded', 3 FROM prop_firms WHERE name = 'Tradeify'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- MFF
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Rapid', 1 FROM prop_firms WHERE name = 'MFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Flex', 2 FROM prop_firms WHERE name = 'MFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Pro', 3 FROM prop_firms WHERE name = 'MFF'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- TPT
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Main', 1 FROM prop_firms WHERE name = 'TPT'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- Funded Next
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Bolt', 1 FROM prop_firms WHERE name = 'Funded Next'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Rapid', 2 FROM prop_firms WHERE name = 'Funded Next'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Legacy', 3 FROM prop_firms WHERE name = 'Funded Next'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- Apex
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Main', 1 FROM prop_firms WHERE name = 'Apex'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- MOT Indicator
INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Weekly', 1 FROM prop_firms WHERE name = 'MOT Indicator'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

INSERT INTO account_types (prop_firm_id, name, sort_order)
SELECT id, 'Monthly', 2 FROM prop_firms WHERE name = 'MOT Indicator'
ON CONFLICT (prop_firm_id, name) DO NOTHING;

-- =====================
-- ACCOUNT SIZES
-- =====================

INSERT INTO account_sizes (label, numeric_size, sort_order) VALUES
    ('25k', 25000, 1),
    ('50k', 50000, 2),
    ('75k', 75000, 3),
    ('100k', 100000, 4),
    ('150k', 150000, 5),
    ('N/A', NULL, 6)
ON CONFLICT (label) DO NOTHING;
"""

with psycopg2.connect(DATABASE_URL, sslmode="require") as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()

print("✅ Seed data inserted")
