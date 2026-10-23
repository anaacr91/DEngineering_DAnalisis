CREATE TABLE players (
    player_id INT PRIMARY KEY,
    player_name VARCHAR(255),
    position VARCHAR(100),
    salary_per_year DECIMAL(12,2),
    contract_time INT
);

CREATE TABLE teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(255),
    country VARCHAR(100)
);

CREATE TABLE pickup (
    pickup_id INT PRIMARY KEY,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    `date` DATE,
    CONSTRAINT fk_pickup_player
        FOREIGN KEY (player_id) REFERENCES players(player_id),
    CONSTRAINT fk_pickup_team
        FOREIGN KEY (team_id) REFERENCES teams(team_id)
);
