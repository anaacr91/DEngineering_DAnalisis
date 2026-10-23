SELECT t.team_name,
       YEAR(pu.`date`) AS pickup_year,
       COUNT(*) AS total_pickups
FROM pickup AS pu
JOIN teams AS t ON t.team_id = pu.team_id
GROUP BY t.team_id, t.team_name, YEAR(pu.`date`)
ORDER BY t.team_name, pickup_year;
