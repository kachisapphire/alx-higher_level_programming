#!/bin/bash
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Select avg
SELECT temperatures.city, AVG(temperatures.value) AS avg_temp FROM temperatures GROUP BY temperatures.city ORDER BY avg_temp DESC; 
