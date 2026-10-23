CREATE TABLE restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    `year` INT,
    rate DECIMAL(3,1),
    price DECIMAL(5,2),
    awards INT,
    positive_reviews INT,
    negative_reviews INT,
    category ENUM('vegano', 'parrilla', 'buffet libre', 'paleolítico', 'paellas', 'asturiano')
);
