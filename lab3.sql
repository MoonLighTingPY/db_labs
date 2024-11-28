CREATE DATABASE IF NOT EXISTS `mydb`;
USE `mydb`;

DROP TABLE IF EXISTS panel_production;
DROP TABLE IF EXISTS panel_angle;
DROP TABLE IF EXISTS solar_panel;
DROP TABLE IF EXISTS panel_type;
DROP TABLE IF EXISTS battery_level;
DROP TABLE IF EXISTS battery;
DROP TABLE IF EXISTS owner_has_station;
DROP TABLE IF EXISTS energy_sale;
DROP TABLE IF EXISTS station;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS `owner`;

CREATE TABLE panel_type (
  `id` INT NOT NULL AUTO_INCREMENT KEY,
  `type_name` VARCHAR(45) NOT NULL,
  `description` MEDIUMTEXT NULL
) ENGINE = InnoDB;

CREATE TABLE location (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `city` VARCHAR(45) NOT NULL,
  `street` VARCHAR(45) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE station (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `total_capacity` DECIMAL(10,2) NOT NULL,
  `installation_date` DATE NOT NULL,
  `location_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE solar_panel (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `installation_date` DATE NOT NULL,
  `panel_type_id` INT NOT NULL,
  `station_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE battery (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `capacity` VARCHAR(45) NOT NULL,
  `installation_date` DATE NOT NULL,
  `station_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE battery_level (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `date_time` DATETIME NOT NULL,
  `charge_level` DECIMAL(5,2) NOT NULL,
  `battery_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE panel_angle (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `date_time` DATETIME NOT NULL,
  `angle` DECIMAL(5,2) NOT NULL,
  `solar_panel_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE panel_production (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `date_time` DATETIME NOT NULL,
  `production` DECIMAL(10,2) NOT NULL,
  `solar_panel_id` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE `owner` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `contact_number` INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE owner_has_station (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `owner_id` INT NOT NULL,
  `station_id` INT NOT NULL,
  `ownership_percentage` DECIMAL(5,2) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE energy_sale (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `energy_sold` DECIMAL(10,2) NOT NULL,
  `price_per_kwh` DECIMAL(5,2) NOT NULL,
  `date_time` DATETIME NOT NULL,
  `station_id` INT NOT NULL
) ENGINE = InnoDB;

ALTER TABLE station 
  ADD INDEX `fk_station_location1_idx` (`location_id`),
  ADD CONSTRAINT `fk_station_location1`
    FOREIGN KEY (`location_id`)
    REFERENCES `location` (`id`);

ALTER TABLE solar_panel 
  ADD INDEX `fk_solar_panel_panel_type_idx` (`panel_type_id`),
  ADD INDEX `fk_solar_panel_station1_idx` (`station_id`),
  ADD CONSTRAINT `fk_solar_panel_panel_type`
    FOREIGN KEY (`panel_type_id`)
    REFERENCES `panel_type` (`id`),
  ADD CONSTRAINT `fk_solar_panel_station1`
    FOREIGN KEY (`station_id`)
    REFERENCES `station` (`id`);

ALTER TABLE battery 
  ADD INDEX `fk_battery_station1_idx` (`station_id`),
  ADD CONSTRAINT `fk_battery_station1`
    FOREIGN KEY (`station_id`)
    REFERENCES `station` (`id`);
    
/*ALTER TABLE battery
	ADD COLUMN maker VARCHAR(20);
    
ALTER TABLE battery
    MODIFY COLUMN maker CHAR(50);
    
ALTER TABLE battery
    DROP COLUMN maker;*/

ALTER TABLE battery_level 
  ADD INDEX `fk_battery_level_battery1_idx` (`battery_id`),
  ADD CONSTRAINT `fk_battery_level_battery1`
    FOREIGN KEY (`battery_id`)
    REFERENCES `battery` (`id`);

ALTER TABLE panel_angle 
  ADD INDEX `fk_panel_angle_solar_panel1_idx` (`solar_panel_id`),
  ADD CONSTRAINT `fk_panel_angle_solar_panel1`
    FOREIGN KEY (`solar_panel_id`)
    REFERENCES `solar_panel` (`id`);

ALTER TABLE panel_production 
  ADD INDEX `fk_panel_production_solar_panel1_idx` (`solar_panel_id`),
  ADD CONSTRAINT `fk_panel_production_solar_panel1`
    FOREIGN KEY (`solar_panel_id`)
    REFERENCES `solar_panel` (`id`);

ALTER TABLE owner_has_station 
  ADD INDEX `fk_owner_has_station_station1_idx` (`station_id`),
  ADD INDEX `fk_owner_has_station_owner1_idx` (`owner_id`),
  ADD CONSTRAINT `fk_owner_has_station_owner1`
    FOREIGN KEY (`owner_id`)
    REFERENCES `owner` (`id`),
  ADD CONSTRAINT `fk_owner_has_station_station1`
    FOREIGN KEY (`station_id`)
    REFERENCES `station` (`id`);

ALTER TABLE energy_sale 
  ADD INDEX `fk_energy_sale_station1_idx` (`station_id`),
  ADD CONSTRAINT `fk_energy_sale_station1`
    FOREIGN KEY (`station_id`)
    REFERENCES `station` (`id`);

INSERT INTO panel_type (type_name, description) VALUES
('Monocrystalline', 'High efficiency and longevity'),
('Polycrystalline', 'Good efficiency, affordable'),
('Thin Film', 'Lightweight and flexible'),
('Bifacial', 'Double-sided energy production'),
('PERC', 'High performance in low light'),
('IBC', 'High efficiency, lower losses'),
('Hybrid', 'Efficient under different conditions'),
('Organic', 'Eco-friendly materials'),
('Flexible', 'Ideal for portable devices'),
('CdTe', 'Thin film technology'),
('CIGS', 'Thin film, robust performance'),
('DSSC', 'Transparent and colorful'),
('Amorphous Silicon', 'Cost-effective thin film'),
('Multijunction', 'Very high efficiency'),
('Concentrated PV', 'High efficiency with lenses');

INSERT INTO location (city, street) VALUES
('Kyiv', 'Shevchenka St.'),
('Lviv', 'Halytska St.'), 
('Odessa', 'Deribasivska St.'),
('Dnipro', 'Yavornytskoho Ave.'), 
('Kharkiv', 'Sumska St.'), 
('Cherkasy', 'Khreshchatyk St.'),
('Ivano-Frankivsk', 'Nezalezhnosti St.'), 
('Uzhhorod', 'Korzo St.'), 
('Poltava', 'Strytenska St.'),
('Zhytomyr', 'Peremohy St.'), 
('Chernihiv', 'Shchorsa St.'), 
('Vinnytsia', 'Soborna St.'),
('Chernivtsi', 'Holovna St.'), 
('Kropyvnytskyi', 'Arsenichuka St.'), 
('Rivne', 'Soborna St.');

INSERT INTO station (total_capacity, installation_date, location_id) VALUES
(5000.00, '2022-01-15', 1), 
(7000.00, '2022-02-20', 2), 
(3000.00, '2022-03-05', 3),
(2500.00, '2022-04-10', 4), 
(8000.00, '2022-05-15', 5), 
(6000.00, '2022-06-20', 6),
(4500.00, '2022-07-25', 7), 
(7500.00, '2022-08-30', 8), 
(9000.00, '2022-09-15', 9),
(5500.00, '2022-10-20', 10), 
(3500.00, '2022-11-25', 11), 
(9500.00, '2022-12-30', 12),
(4200.00, '2023-01-15', 13), 
(6200.00, '2023-02-20', 14), 
(7800.00, '2023-03-25', 15);

INSERT INTO solar_panel (installation_date, panel_type_id, station_id) VALUES
('2022-01-01', 3, 7),
('2022-01-10', 5, 9),
('2022-01-20', 7, 1),
('2022-02-01', 2, 6),
('2022-02-10', 6, 2),
('2022-02-20', 9, 8),
('2022-03-01', 7, 5),
('2022-03-10', 3, 4),
('2022-03-20', 6, 12),
('2022-04-01', 4, 11),
('2022-04-10', 13, 6),
('2022-04-20', 10, 4),
('2022-05-01', 5, 4),
('2022-05-10', 12, 13),
('2022-05-20', 15, 1);

INSERT INTO battery (capacity, installation_date, station_id) VALUES
('1000', '2022-01-05', 1), 
('1200', '2022-02-10', 2), 
('900', '2022-03-15', 6),
('1100', '2022-04-20', 4), 
('1300', '2022-05-25', 8), 
('1400', '2022-06-30', 6),
('1500', '2022-07-05', 5), 
('1600', '2022-08-10', 8), 
('1700', '2022-09-15', 9),
('1800', '2022-10-20', 10), 
('1900', '2022-11-25', 4), 
('2000', '2022-12-30', 1),
('2100', '2023-01-04', 6), 
('2200', '2023-02-09', 2), 
('2300', '2023-03-14', 15);

INSERT INTO battery_level (date_time, charge_level, battery_id) VALUES
('2022-01-05 10:00:00', 75.00, 1),
('2022-02-10 11:00:00', 80.00, 2),
('2022-03-15 12:00:00', 85.00, 3),
('2022-04-20 13:00:00', 70.00, 4), 
('2022-05-25 14:00:00', 65.00, 5), 
('2022-06-30 15:00:00', 60.00, 6),
('2022-07-05 16:00:00', 95.00, 7), 
('2022-08-10 17:00:00', 90.00, 8), 
('2022-09-15 18:00:00', 85.00, 9),
('2022-10-20 19:00:00', 80.00, 10), 
('2022-11-25 20:00:00', 75.00, 11), 
('2022-12-30 21:00:00', 70.00, 12),
('2023-01-04 22:00:00', 65.00, 13), 
('2023-02-09 23:00:00', 60.00, 14), 
('2023-03-14 00:00:00', 55.00, 15);

INSERT INTO panel_angle (date_time, angle, solar_panel_id) VALUES
('2022-01-01 10:00:00', 45.00, 1), 
('2022-01-10 11:00:00', 50.00, 2), 
('2022-01-20 12:00:00', 55.00, 3),
('2022-02-01 13:00:00', 60.00, 4), 
('2022-02-10 14:00:00', 65.00, 5), 
('2022-02-20 15:00:00', 70.00, 6),
('2022-03-01 16:00:00', 75.00, 7), 
('2022-03-10 17:00:00', 80.00, 8), 
('2022-03-20 18:00:00', 85.00, 9),
('2022-04-01 19:00:00', 90.00, 10), 
('2022-04-10 20:00:00', 95.00, 11), 
('2022-04-20 21:00:00', 100.00, 12),
('2022-05-01 22:00:00', 105.00, 13),
('2022-05-10 23:00:00', 110.00, 14), 
('2022-05-20 00:00:00', 115.00, 15);

INSERT INTO panel_production (date_time, production, solar_panel_id) VALUES
('2022-01-01 10:00:00', 500.00, 1), 
('2022-01-10 11:00:00', 600.00, 2), 
('2022-01-20 12:00:00', 700.00, 3),
('2022-02-01 13:00:00', 800.00, 4), 
('2022-02-10 14:00:00', 900.00, 5), 
('2022-02-20 15:00:00', 1000.00, 6),
('2022-03-01 16:00:00', 1100.00, 7), 
('2022-03-10 17:00:00', 1200.00, 8), 
('2022-03-20 18:00:00', 1300.00, 9),
('2022-04-01 19:00:00', 1400.00, 10), 
('2022-04-10 20:00:00', 1500.00, 11), 
('2022-04-20 21:00:00', 1600.00, 12),
('2022-05-01 22:00:00', 1700.00, 13), 
('2022-05-10 23:00:00', 1800.00, 14), 
('2022-05-20 00:00:00', 1900.00, 15);

INSERT INTO `owner` (name, surname, contact_number) VALUES
('John', 'Doe', 123456789),
('Jane', 'Smith', 234567890),
('Michael', 'Johnson', 345678901),
('Emily', 'Davis', 456789012),
('David', 'Martinez', 567890123),
('Sarah', 'Lopez', 678901234),
('Chris', 'Brown', 789012345),
('Amanda', 'Wilson', 890123456),
('Brian', 'Taylor', 901234567),
('Lisa', 'Anderson', 102345678),
('Paul', 'Thomas', 112345678),
('Megan', 'Jackson', 122345678),
('Laura', 'White', 132345678),
('Daniel', 'Harris', 142345678),
('Emma', 'Martin', 152345678);

INSERT INTO owner_has_station (owner_id, station_id, ownership_percentage) VALUES
(1, 1, 50.00),
(2, 2, 75.00),
(3, 3, 100.00),
(6, 4, 60.00),
(5, 5, 80.00),
(6, 6, 90.00),
(10, 7, 70.00),
(8, 8, 85.00),
(2, 9, 65.00),
(10, 10, 55.00),
(5, 11, 50.00),
(12, 12, 45.00),
(5, 13, 95.00),
(14, 14, 100.00),
(15, 15, 75.00);

INSERT INTO energy_sale (energy_sold, price_per_kwh, date_time, station_id) VALUES
(100.50, 0.15, '2023-01-01 10:00:00', 1),
(200.75, 0.18, '2023-01-02 12:00:00', 2),
(150.60, 0.14, '2023-01-03 14:00:00', 3),
(175.80, 0.17, '2023-01-04 09:00:00', 4),
(180.30, 0.16, '2023-01-05 11:00:00', 5),
(190.25, 0.15, '2023-01-06 08:00:00', 6),
(210.45, 0.19, '2023-01-07 13:00:00', 7),
(220.70, 0.17, '2023-01-08 15:00:00', 8),
(230.95, 0.18, '2023-01-09 16:00:00', 9),
(240.10, 0.14, '2023-01-10 10:00:00', 10),
(250.35, 0.15, '2023-01-11 12:00:00', 11),
(260.40, 0.16, '2023-01-12 14:00:00', 12),
(270.55, 0.18, '2023-01-13 09:00:00', 13),
(280.75, 0.19, '2023-01-14 11:00:00', 14),
(290.90, 0.17, '2023-01-15 13:00:00', 15);

CREATE INDEX idx_battery_capacity ON battery(`capacity`);
CREATE INDEX idx_station_installation_date ON station(`installation_date`);

