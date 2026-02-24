# SQL - More Queries

![MySQL](https://img.shields.io/badge/mysql-8.0-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-orange)

## 📋 Description
This project dives deeper into SQL and MySQL, focusing on user management, privileges, constraints, and complex queries using JOINs and subqueries.

## 🎯 Learning Objectives
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## 🛠️ Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Ubuntu 20.04 LTS
- MySQL 8.0.25
- All files end with a new line
- All SQL queries have a comment before them
- All SQL keywords in uppercase (SELECT, WHERE, etc.)
- A README.md file is mandatory

## 📁 Files Description

| File Name | Description |
|-----------|-------------|
| `0-privileges.sql` | Lists all privileges of users user_0d_1 and user_0d_2 |
| `1-create_user.sql` | Creates user user_0d_1 with all privileges |
| `2-create_read_user.sql` | Creates database hbtn_0d_2 and user user_0d_2 with SELECT privilege |
| `3-force_name.sql` | Creates table force_name with NOT NULL constraint on name |
| `4-never_empty.sql` | Creates table id_not_null with default value 1 on id |
| `5-unique_id.sql` | Creates table unique_id with UNIQUE constraint on id |
| `6-states.sql` | Creates database hbtn_0d_usa and table states with PRIMARY KEY |
| `7-cities.sql` | Creates table cities with FOREIGN KEY referencing states |
| `8-cities_of_california_subquery.sql` | Lists all cities of California using subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state names using JOIN |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre linked (INNER JOIN) |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre ids (LEFT JOIN) |
| `12-no_genre.sql` | Lists shows without a genre linked |
| `13-count_shows_by_genre.sql` | Counts number of shows linked to each genre |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres (with NULL if no genre) |

## 🚀 How to Use

### 1. Start MySQL Service
```bash
service mysql start
```

## 2. Import Database Dump (for tasks 10-16)
```
# Create database
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -hlocalhost -uroot -p

# Import data
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

## 3. Run SQL Scripts
```
# List user privileges
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

# Create user
cat 1-create_user.sql | mysql -hlocalhost -uroot -p

# Run scripts with specific database
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
# Run scripts with specific database
```


## 📝 Examples
Task 0: My privileges!
```
-- 0-privileges.sql
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
```
```
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000): There is no such grant defined for user 'user_0d_1' on host 'localhost'
```
## Task 7: Cities table
```
-- 7-cities.sql
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```
## Task 16: List shows and genres
```
-- 16-shows_by_genre.sql
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
```
```
$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title               name
Better Call Saul    NULL
Breaking Bad        Crime
Breaking Bad        Drama
```
## 🔑 Key Concepts
## User Management
```
-- Create user
CREATE USER IF NOT EXISTS 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
GRANT SELECT ON database_name.* TO 'username'@'localhost';

-- Show grants
SHOW GRANTS FOR 'username'@'localhost';
```
## Constraints
```
-- NOT NULL
name VARCHAR(256) NOT NULL

-- DEFAULT
id INT DEFAULT 1

-- UNIQUE
id INT UNIQUE

-- PRIMARY KEY
id INT PRIMARY KEY AUTO_INCREMENT

-- FOREIGN KEY
FOREIGN KEY (state_id) REFERENCES states(id)
```
## JOIN Types
```
-- INNER JOIN (only matching records)
SELECT * FROM table1 JOIN table2 ON table1.id = table2.foreign_id;

-- LEFT JOIN (all records from left table)
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.foreign_id;
```
## ✨ Author
Maryam
