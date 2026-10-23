SELECT p.player_name, p.salary_per_year
FROM players AS p
JOIN pickup AS pu ON pu.player_id = p.player_id
JOIN teams AS t ON t.team_id = pu.team_id
WHERE p.position = 'delantero'
  AND t.country = 'España'
ORDER BY p.salary_per_year DESC
LIMIT 1;
