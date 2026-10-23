WITH previus_query AS (
    SELECT player_id, COUNT(*) AS n_pickups
    FROM pickup
    GROUP BY player_id
)
SELECT p.player_name, pq.n_pickups
FROM previus_query AS pq
JOIN players AS p ON p.player_id = pq.player_id
ORDER BY pq.n_pickups DESC;
