INSERT INTO prize_catalog (prop_firm_id, account_type_id, account_size_id, display_name)
SELECT pf.id, at.id, sz.id,
    'Alpha Futures ' || at.name || ' ' || sz.label
FROM prop_firms pf
JOIN account_types at ON at.prop_firm_id = pf.id AND at.name = 'Zero'
JOIN account_sizes sz ON sz.label IN ('25k','50k','100k')
WHERE pf.name = 'Alpha Futures'
ON CONFLICT DO NOTHING;
