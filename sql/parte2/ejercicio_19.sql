SELECT r.name,
       AVG(c.number_awards) AS average_chef_awards
FROM restaurants AS r
JOIN chefs AS c ON c.restaurant_id = r.id
GROUP BY r.id, r.name
ORDER BY average_chef_awards DESC;
