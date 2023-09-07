---
--- Create tables companies and vacancies
---

CREATE TABLE problems (
id SERIAL PRIMARY KEY,
contestId integer NOT NULL,
index VARCHAR(100) NOT NULL,
name VARCHAR(100),
points VARCHAR(100),
rating VARCHAR(100),
tags VARCHAR(1000),
type VARCHAR(100));

CREATE TABLE problemStatistics (
id SERIAL PRIMARY KEY,
contestId integer NOT NULL,
index VARCHAR(100) NOT NULL,
solvedCount integer);

--CREATE TABLE vacancies (
--vacancy_id SERIAL PRIMARY KEY,
--company_id INTEGER REFERENCES companies (company_id) ON DELETE CASCADE,
--vacancy_name VARCHAR(100) NOT NULL,
--vacancy_url VARCHAR(100) NOT NULL,
--vacancy_salary_from INT,
--vacancy_salary_to INT,
--vacancy_address VARCHAR(100),
--CONSTRAINT chk_salary_from CHECK(vacancy_salary_from >= 0),
--CONSTRAINT chk_salary_to CHECK(vacancy_salary_to >= 0)
--);