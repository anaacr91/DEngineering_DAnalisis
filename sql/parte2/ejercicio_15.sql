SELECT r.name AS restaurant_name,
       c.name AS chef_name,
       c.experience_years
FROM restaurants AS r
JOIN chefs AS c ON c.restaurant_id = r.id
WHERE r.rate > 4
ORDER BY c.experience_years;
