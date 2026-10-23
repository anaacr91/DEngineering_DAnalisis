SELECT t.team_name,
       MAX(p.salary_per_year) AS maximum_salary,
       MIN(p.salary_per_year) AS minimum_salary,
       AVG(p.salary_per_year) AS average_salary
FROM teams AS t
LEFT JOIN pickup AS pu ON pu.team_id = t.team_id
LEFT JOIN players AS p ON p.player_id = pu.player_id
GROUP BY t.team_id, t.team_name;
