SELECT app_id, developer, a.title, rating
FROM shopify.apps a
JOIN shopify.key_benefits k
    ON a.id = k.app_id
WHERE (k.title LIKE '%security%') OR (k.description LIKE '%security%')
ORDER BY a.rating DESC