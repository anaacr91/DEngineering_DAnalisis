SELECT p.player_name, pu.`date`
FROM players AS p
LEFT JOIN pickup AS pu ON pu.player_id = p.player_id;
