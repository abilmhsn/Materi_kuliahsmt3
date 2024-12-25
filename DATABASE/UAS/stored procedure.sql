DELIMITER $$

CREATE PROCEDURE AddNewOrder(
    IN p_user_id INT,
    IN p_total_price DECIMAL(10,2),
    IN p_product_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE new_order_id INT;

    -- Mulai transaksi
    START TRANSACTION;

    -- Menambahkan entri ke tabel orders
    INSERT INTO orders (user_id, total_price)
    VALUES (p_user_id, p_total_price);

    -- Mengambil ID pesanan yang baru saja dimasukkan
    SET new_order_id = LAST_INSERT_ID();

    -- Menambahkan entri ke tabel order_items
    INSERT INTO order_items (order_id, product_id, quantity)
    VALUES (new_order_id, p_product_id, p_quantity);

    -- Komit transaksi
    COMMIT;
END $$

DELIMITER ;
