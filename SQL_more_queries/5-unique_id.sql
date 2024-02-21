-- -- Creates table with specified properties/values
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
	);