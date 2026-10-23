SELECT py.y AS pickup_year,
       COUNT(pu.pickup_id) AS pickup_count
FROM pickup_years AS py
LEFT JOIN pickup AS pu ON YEAR(pu.`date`) = py.y
GROUP BY py.y
ORDER BY py.y;
