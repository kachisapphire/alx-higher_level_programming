#!/bin/bash
-- Write a script that creates the table id_not_null on your MySQL SERVER
-- Create table
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
