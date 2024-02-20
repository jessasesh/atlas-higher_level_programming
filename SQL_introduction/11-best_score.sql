-- Lists all records with specified parameters from specific database
SELECT `score`, `name` 
FROM `second_table` WHERE `score` >= 10 
ORDER BY `score` DESC;