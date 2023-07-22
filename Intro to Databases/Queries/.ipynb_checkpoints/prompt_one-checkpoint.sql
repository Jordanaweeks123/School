SELECT app_id, developer, rating, a.reviews_count
FROM shopify.categories c
JOIN shopify.apps_categories ac
    ON c.id = ac.category_id
JOIN shopify.apps a
    ON (ac.app_id = a.id) AND (a.rating >= 4) AND (a.reviews_count >= 50) AND (c.title = 'Productivity')
ORDER BY a.rating DESC, a.reviews_count DESC