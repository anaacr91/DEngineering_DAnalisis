SELECT ROUND(AVG(price), 0) AS rounded_average_menu_price
FROM restaurants
WHERE `year` BETWEEN 1990 AND 1999;
