SELECT COUNT(*) AS comedy_movies
FROM movies
WHERE LOWER(GENRE) = 'comedy'
  AND RATE > 8;
