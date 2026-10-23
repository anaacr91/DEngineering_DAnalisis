SELECT DISTINCT r.name
FROM restaurants AS r
JOIN chefs AS c ON c.restaurant_id = r.id
WHERE c.experience_years > 10;
