SELECT r.name,
       COALESCE(SUM(c.number_awards), 0) AS total_chef_awards
FROM restaurants AS r
LEFT JOIN chefs AS c ON c.restaurant_id = r.id
GROUP BY r.id, r.name
ORDER BY total_chef_awards DESC;
