-- Active: 1728127464192@@127.0.0.1@3306@child_behavior_index
CREATE DATABASE shg_database;

USE shg_database;

CREATE TABLE shg_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    caste VARCHAR(100),
    education VARCHAR(100),
    marital_status VARCHAR(100),
    household_size INT,
    year_joined INT,
    role_in_shg VARCHAR(100),
    meeting_frequency VARCHAR(100),
    savings_amount VARCHAR(100),
    loan_details TEXT,
    financial_training TEXT,
    income_increased VARCHAR(10),
    income_source VARCHAR(255),
    skill_development TEXT,
    household_decision VARCHAR(10),
    village_meeting VARCHAR(10),
    independent_travel VARCHAR(10),
    confidence VARCHAR(10),
    social_support VARCHAR(10),
    leadership TEXT,
    group_issues TEXT,
    training_needs TEXT,
    suggestions TEXT
);
