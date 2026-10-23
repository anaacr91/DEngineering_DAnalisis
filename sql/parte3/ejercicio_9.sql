WITH previus_query AS (
    SELECT player_id, COUNT(*) AS n_pickups
    FROM pickup
    GROUP BY player_id
)
SELECT *
FROM previus_query;
