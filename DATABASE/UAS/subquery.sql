SELECT
    p.product_id,
    p.name AS product_name,
    p.price
FROM products p
WHERE p.product_id NOT IN (
    SELECT oi.product_id
    FROM order_items oi
    GROUP BY oi.product_id
);
