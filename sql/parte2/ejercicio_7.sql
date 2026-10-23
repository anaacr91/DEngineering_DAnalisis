SELECT price, COUNT(*) AS restaurant_count
FROM restaurants
WHERE positive_reviews > 1000
GROUP BY price;
