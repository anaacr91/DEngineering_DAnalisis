SELECT COALESCE(SUM(awards), 0) AS total_awards
FROM restaurants
WHERE price < 20;
