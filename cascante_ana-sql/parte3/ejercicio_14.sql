SELECT t.team_name, p.player_name, pu.`date`
FROM pickup AS pu
JOIN players AS p ON p.player_id = pu.player_id
JOIN teams AS t ON t.team_id = pu.team_id
WHERE YEAR(pu.`date`) = 2023;
