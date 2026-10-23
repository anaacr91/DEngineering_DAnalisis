CREATE TABLE actors (
    name VARCHAR(255),
    age INT,
    awards INT,
    movie_id INT,
    CONSTRAINT fk_actors_movie
        FOREIGN KEY (movie_id) REFERENCES movies(ID)
        ON DELETE CASCADE
);
