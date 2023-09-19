-- top temp in july and aug
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 8 or month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3
