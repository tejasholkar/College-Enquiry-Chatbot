-- MySQL database setup for CRCE Bot
-- Run this file in your MySQL database to create the necessary tables

CREATE DATABASE IF NOT EXISTS register;
USE register;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create suggestion table
CREATE TABLE IF NOT EXISTS suggestion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verify tables
SELECT 'Tables created successfully!' AS Status;

