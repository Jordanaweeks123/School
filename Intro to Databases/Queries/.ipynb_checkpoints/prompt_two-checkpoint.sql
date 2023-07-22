SELECT COUNT(*)
FROM shopify.apps a
FULL OUTER JOIN shopify.pricing_plans p
    ON a.id = p.id
WHERE (a.id IS NULL) OR (p.id IS NULL)