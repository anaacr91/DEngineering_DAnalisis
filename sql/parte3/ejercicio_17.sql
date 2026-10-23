SELECT t.team_name, COUNT(pu.pickup_id) AS pickup_count
FROM teams AS t
LEFT JOIN pickup AS pu ON pu.team_id = t.team_id
GROUP BY t.team_id, t.team_name;
