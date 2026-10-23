SELECT category, SUM(negative_reviews) AS total_negative_reviews
FROM restaurants
GROUP BY category;
