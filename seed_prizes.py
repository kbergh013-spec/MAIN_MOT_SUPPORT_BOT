import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

sql = """

-- =====================
-- PRIZE CATALOG
-- =====================

-- Alpha Futures - Zero
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Alpha Futures ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name = 'Zero'
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k')
WHERE pf.name = 'Alpha Futures'
ON CONFLICT DO NOTHING;

-- Alpha Futures - Standard
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Alpha Futures ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name = 'Standard'
JOIN account_sizes sz ON sz.label IN ('50k','100k','150k')
WHERE pf.name = 'Alpha Futures'
ON CONFLICT DO NOTHING;

-- Alpha Futures - Advanced
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Alpha Futures ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name = 'Advanced'
JOIN account_sizes sz ON sz.label IN ('50k','100k','150k')
WHERE pf.name = 'Alpha Futures'
ON CONFLICT DO NOTHING;

-- FFF
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'FFF ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k','150k')
WHERE pf.name = 'FFF'
ON CONFLICT DO NOTHING;

-- Lucid
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Lucid ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k','150k')
WHERE pf.name = 'Lucid'
ON CONFLICT DO NOTHING;

-- Tradeify
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Tradeify ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k','150k')
WHERE pf.name = 'Tradeify'
ON CONFLICT DO NOTHING;

-- MFF (Rapid/Flex small, Pro larger)
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'MFF ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name IN ('Rapid','Flex')
JOIN account_sizes sz ON sz.label IN ('25k','50k')
WHERE pf.name = 'MFF'
ON CONFLICT DO NOTHING;

INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'MFF ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name = 'Pro'
JOIN account_sizes sz ON sz.label IN ('50k','100k','150k')
WHERE pf.name = 'MFF'
ON CONFLICT DO NOTHING;

-- TPT
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'TPT ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','75k','100k','150k')
WHERE pf.name = 'TPT'
ON CONFLICT DO NOTHING;

-- Funded Next
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Funded Next ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k')
WHERE pf.name = 'Funded Next'
ON CONFLICT DO NOTHING;

-- Apex
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Apex ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k','150k')
WHERE pf.name = 'Apex'
ON CONFLICT DO NOTHING;

-- MOT Indicator
INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'MOT Indicator ' || at.name
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id
JOIN account_sizes sz ON sz.label = 'N/A'
WHERE pf.name = 'MOT Indicator'
ON CONFLICT DO NOTHING;

"""

with psycopg2.connect(DATABASE_URL, sslmode="require") as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()

print("✅ FULL prize_catalog seeded successfully")
