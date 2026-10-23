SELECT DISTINCT r.category
FROM restaurants AS r
JOIN chefs AS c ON c.restaurant_id = r.id
WHERE LOWER(c.speciality) = 'mediterránea';
