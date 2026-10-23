SELECT price,
       ROUND(AVG(positive_reviews), 0) AS average_positive_reviews,
       COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY price
HAVING COUNT(*) > 10;
