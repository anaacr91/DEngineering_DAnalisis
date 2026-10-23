SELECT r.name,
       SUM(c.number_awards) AS total_chef_awards
FROM restaurants AS r
JOIN chefs AS c ON c.restaurant_id = r.id
GROUP BY r.id, r.name
HAVING SUM(c.number_awards) > 10;
