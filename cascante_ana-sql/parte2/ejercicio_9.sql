SELECT category, price, AVG(positive_reviews) AS average_positive_reviews
FROM restaurants
GROUP BY category, price;
