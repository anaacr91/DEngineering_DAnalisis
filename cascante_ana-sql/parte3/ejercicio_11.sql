SELECT p.player_id,
       p.player_name,
       t.team_name
FROM players AS p
LEFT JOIN pickup AS pu ON pu.player_id = p.player_id
LEFT JOIN teams AS t ON t.team_id = pu.team_id;
