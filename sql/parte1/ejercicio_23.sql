SELECT name,
       CASE
           WHEN genre = 'rock&roll' AND rate > 8 THEN 'Energy'
           WHEN genre = 'techno' AND rate > 7 THEN 'Intense'
           ELSE 'Nice'
       END AS Mood
FROM songs;
