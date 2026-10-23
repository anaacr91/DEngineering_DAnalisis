SELECT p.player_name
FROM players AS p
LEFT JOIN pickup AS pu ON pu.player_id = p.player_id
WHERE pu.pickup_id IS NULL;
