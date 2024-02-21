-- Lists all cities within specified database in ascending order 
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` 
FROM `cities`, `states` 
WHERE `cities`.`state_id` = `states`.`id` 
ORDER BY `cities`.`id`;