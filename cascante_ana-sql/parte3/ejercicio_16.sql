SELECT position, COUNT(*) AS player_count
FROM players
GROUP BY position;
