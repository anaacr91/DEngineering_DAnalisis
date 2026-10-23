SELECT t.team_name, p.player_name
FROM teams AS t
LEFT JOIN pickup AS pu ON pu.team_id = t.team_id
LEFT JOIN players AS p ON p.player_id = pu.player_id

UNION

SELECT t.team_name, NULL AS player_name
FROM teams AS t
LEFT JOIN pickup AS pu ON pu.team_id = t.team_id
WHERE pu.pickup_id IS NULL;
