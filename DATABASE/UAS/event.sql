DELIMITER $$

CREATE EVENT delete_old_orders
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    DELETE FROM orders
    WHERE order_date < NOW() - INTERVAL 30 DAY
    AND status = 'Pending';
END $$

DELIMITER ;
