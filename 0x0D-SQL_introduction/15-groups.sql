-- Selecting a number 
SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY DESC;