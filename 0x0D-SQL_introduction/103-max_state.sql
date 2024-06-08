#!/bin/bash
-- Write a script that displays the max temperature of each state 
-- Order by
SELECT temperatures.state, MAX(temperatures.value) AS max_temp FROM temperatures GROUP BY temperatures.state ORDER BY temperatures.state;
