SELECT YEAR(`date`) AS pickup_year,
       COUNT(*) AS total_pickups
FROM pickup
GROUP BY YEAR(`date`)
ORDER BY pickup_year;
