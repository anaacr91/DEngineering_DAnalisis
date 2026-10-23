CREATE TABLE songs (
    name VARCHAR(255),
    genre VARCHAR(100),
    rate DECIMAL(3,1),
    `year` INT
);

SELECT name AS Titles
FROM songs;
