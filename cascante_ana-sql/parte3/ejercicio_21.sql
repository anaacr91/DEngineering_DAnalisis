SELECT t.country,
       COUNT(DISTINCT pu.player_id) AS player_count
FROM teams AS t
JOIN pickup AS pu ON pu.team_id = t.team_id
GROUP BY t.country;
