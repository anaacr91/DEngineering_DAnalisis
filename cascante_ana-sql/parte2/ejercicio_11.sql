SELECT category,
       COUNT(*) AS restaurant_count,
       ROUND(AVG(rate), 2) AS average_rate,
       ROUND(AVG(price), 2) AS average_price,
       SUM(positive_reviews) AS total_positive_reviews,
       SUM(negative_reviews) AS total_negative_reviews
FROM restaurants
GROUP BY category
ORDER BY restaurant_count DESC;
