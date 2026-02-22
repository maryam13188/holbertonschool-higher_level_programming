# SQL - Introduction

![MySQL](https://img.shields.io/badge/mysql-8.0-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)

## 📋 Description
This project is an introduction to SQL and MySQL. It covers the basics of databases, SQL queries, and MySQL operations.

## 🎯 Learning Objectives
- What is a database
- What is a relational database
- What does SQL stand for
- What is MySQL
- How to create a database in MySQL
- What are DDL and DML
- How to CREATE and ALTER tables
- How to SELECT data from a table
- How to INSERT, UPDATE, and DELETE data
- What are subqueries
- How to use MySQL functions

## 🛠️ Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Ubuntu 22.04 LTS
- MySQL 8.0.25
- All files end with a new line
- All SQL queries have a comment before them
- All SQL keywords in uppercase (SELECT, WHERE, etc.)
- A README.md file is mandatory

## 📁 Files Description

| File Name | Description |
|-----------|-------------|
| `0-list_databases.sql` | Lists all databases in MySQL server |
| `1-create_database_if_missing.sql` | Creates database `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Deletes database `hbtn_0c_0` if exists |
| `3-list_tables.sql` | Lists all tables in a database |
| `4-first_table.sql` | Creates `first_table` with id and name columns |
| `5-full_table.sql` | Shows full description of `first_table` |
| `6-list_values.sql` | Lists all rows in `first_table` |
| `7-insert_value.sql` | Inserts a new row in `first_table` |
| `8-count_89.sql` | Counts records with id = 89 |
| `9-full_creation.sql` | Creates `second_table` and adds multiple rows |
| `10-top_score.sql` | Lists records ordered by score (top first) |
| `11-best_score.sql` | Lists records with score >= 10 |
| `12-no_cheating.sql` | Updates Bob's score to 10 |
| `13-change_class.sql` | Removes records with score <= 5 |
| `14-average.sql` | Computes average score |
| `15-groups.sql` | Groups records by score |
| `16-no_link.sql` | Lists records with name (no NULL or empty) |

## 🚀 How to Use

### 1. Start MySQL Service
```bash
service mysql start
```
## Run SQL Scripts
# List all databases
```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

# Create database
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

# Use a specific database
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
## 📝 Examples
## Task 0: List databases
```
-- 0-list_databases.sql
SHOW DATABASES;
```
```
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
sys 
```
## Task 7: Insert value
```
-- 7-insert_value.sql
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```
## ✨ Author:

Maryam
