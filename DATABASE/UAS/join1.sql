SELECT
    p.name AS product_name,
    p.price,
    c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE c.name = 'Pakaian' AND p.price > 100
ORDER BY p.price DESC;
