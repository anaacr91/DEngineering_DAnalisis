CREATE TABLE alumnos (
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255),
    edad INT,
    nota_media DECIMAL(4,2),
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE profesores (
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255),
    edad INT,
    `años_experiencia` INT,
    id INT AUTO_INCREMENT PRIMARY KEY
);
