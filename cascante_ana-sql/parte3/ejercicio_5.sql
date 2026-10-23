SELECT pu.*, p.*
FROM pickup AS pu
JOIN players AS p ON p.player_id = pu.player_id
WHERE p.position = 'portero';
