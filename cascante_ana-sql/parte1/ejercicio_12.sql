SELECT m.TITLE, a.name, a.age
FROM movies AS m
JOIN actors AS a ON a.movie_id = m.ID
WHERE a.age = (
    SELECT MIN(a2.age)
    FROM actors AS a2
    WHERE a2.movie_id = a.movie_id
);
