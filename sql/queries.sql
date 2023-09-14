---
--- Create table problems
---

CREATE TABLE problems (
contestId VARCHAR PRIMARY KEY,
name VARCHAR(100),
points VARCHAR(100),
rating integer,
solvedCount integer,
tags VARCHAR(1000)
--type VARCHAR(100)
);