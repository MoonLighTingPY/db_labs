use lab4;

DROP TRIGGER IF EXISTS insert_battery;
DROP TRIGGER IF EXISTS update_battery;
DROP TRIGGER IF EXISTS delete_airline;
DROP PROCEDURE IF EXISTS insert_location;
DROP PROCEDURE IF EXISTS insert_owner_has_station;
DROP PROCEDURE IF EXISTS insert_packet;
DROP PROCEDURE IF EXISTS get_energy_sold;
DROP FUNCTION IF EXISTS calculate_energy_sold;
DROP PROCEDURE IF EXISTS create_databases_and_tables;
DROP TRIGGER IF EXISTS delete_log;
DROP TRIGGER IF EXISTS prevent_deletion;
DROP TRIGGER IF EXISTS insert_format_type_name;
DROP TRIGGER IF EXISTS update_format_type_name;

DELIMITER //

CREATE TRIGGER insert_battery
BEFORE INSERT ON battery_producer
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM battery WHERE id = NEW.battery_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'battery_id does not exist in battery_producer table.';
    END IF;
END //

CREATE TRIGGER update_battery
BEFORE UPDATE ON battery_producer
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM battery WHERE id = NEW.battery_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'battery_id does not exist in battery_producer table.';
    END IF;
END //

CREATE TRIGGER delete_airline
BEFORE DELETE ON battery
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM battery_producer WHERE battery_id = OLD.id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'battery_id is referenced in battery_producer table.';
    END IF;
END //

CREATE PROCEDURE insert_location(
    IN city VARCHAR(45),
    IN street VARCHAR(45)
)
BEGIN
    INSERT INTO location (city, street) VALUES (city, street);
END //

CREATE PROCEDURE insert_owner_has_station(
    IN owner_id INT,
    IN station_id INT,
    IN ownership_percentage FLOAT
)
BEGIN
    INSERT INTO owner_has_station (owner_id, station_id, ownership_percentage) VALUES (owner_id, station_id, ownership_percentage);
END //


CREATE PROCEDURE insert_packet()
BEGIN
    DECLARE num INT DEFAULT 1;
    WHILE num <= 10 DO
        INSERT INTO panel_type (type_name, description) VALUE (CONCAT('Noname', num), "test");
        SET num = num + 1;
    END WHILE;
END //


CREATE FUNCTION calculate_energy_sold(type VARCHAR(10))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(10, 2);

    IF type = 'max' THEN
        SELECT MAX(energy_sold) INTO result FROM energy_sale;
    ELSEIF type = 'min' THEN
        SELECT MIN(energy_sold) INTO result FROM energy_sale;
    ELSEIF type = 'sum' THEN
        SELECT SUM(energy_sold) INTO result FROM energy_sale;
    ELSEIF type = 'avg' THEN
        SELECT AVG(energy_sold) INTO result FROM energy_sale;
    ELSE
        SET result = NULL;
    END IF;

    RETURN result;
END //


CREATE PROCEDURE get_energy_sold(type VARCHAR(10))
BEGIN
    SELECT calculate_energy_sold(type) AS result;
END //

CREATE PROCEDURE create_databases_and_tables()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE owner_name VARCHAR(45);
    DECLARE num_tables INT;
    DECLARE i INT;

    DECLARE owner_cursor CURSOR FOR SELECT name FROM owner;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN owner_cursor;

    read_loop: LOOP
        FETCH owner_cursor INTO owner_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @db_name = owner_name;
        SET @create_db_query = CONCAT('CREATE DATABASE IF NOT EXISTS ', @db_name);
        PREPARE stmt FROM @create_db_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET num_tables = FLOOR(1 + (RAND() * 9));
        SET i = 1;

        WHILE i <= num_tables DO
            SET @table_name = CONCAT(@db_name, '.', @db_name, i);
            SET @create_table_query = CONCAT('CREATE TABLE IF NOT EXISTS ', @table_name, ' (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255))');
            PREPARE stmt FROM @create_table_query;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
            SET i = i + 1;
        END WHILE;
    END LOOP;

    CLOSE owner_cursor;
END //

CREATE TRIGGER delete_log
AFTER DELETE ON battery_producer
FOR EACH ROW
BEGIN
    INSERT INTO battery_producer_log (battery_id, name, deleted_at)
    VALUES (OLD.battery_id, OLD.name, NOW());
END //

CREATE TRIGGER prevent_deletion
BEFORE DELETE ON energy_sale
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You cannot delete from this table.';
END //


CREATE TRIGGER insert_format_type_name
BEFORE INSERT ON panel_type
FOR EACH ROW
BEGIN
    DECLARE invalid_format BOOLEAN;
    SET invalid_format = NOT (NEW.type_name REGEXP '^[AMZ][0-9]{5}[A-Z]{2}$');

    IF invalid_format THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid format for type_name.';
    END IF;
END //


CREATE TRIGGER update_format_type_name
BEFORE UPDATE ON panel_type
FOR EACH ROW
BEGIN
    DECLARE invalid_format BOOLEAN;
    SET invalid_format = NOT (NEW.type_name REGEXP '^[AMZ][0-9]{5}[A-Z]{2}$');

    IF invalid_format THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid format for type_name.';
    END IF;
END //


DELIMITER ;




