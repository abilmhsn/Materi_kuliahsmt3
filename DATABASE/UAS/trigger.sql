DELIMITER $$

CREATE TRIGGER update_order_total AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    DECLARE new_total DECIMAL(10,2);

    -- Menghitung ulang total harga untuk pesanan terkait
    SELECT SUM(oi.quantity * p.price) INTO new_total
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    WHERE oi.order_id = NEW.order_id;

    -- Memperbarui total harga pesanan di tabel orders
    UPDATE orders
    SET total_price = new_total
    WHERE order_id = NEW.order_id;
END $$

DELIMITER ;
