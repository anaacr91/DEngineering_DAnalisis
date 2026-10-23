SELECT m.TITLE, a.name, a.awards
FROM movies AS m
JOIN actors AS a ON a.movie_id = m.ID
WHERE a.awards = (
    SELECT MAX(a2.awards)
    FROM actors AS a2
    WHERE a2.movie_id = a.movie_id
);
