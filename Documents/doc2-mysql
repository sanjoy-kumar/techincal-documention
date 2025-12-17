# MySQL – Step-by-Step Complete Guide (Brief but All Aspects)
## STEP 1: What is MySQL?
    - MySQL is a Relational Database Management System (RDBMS)
    - Data is stored in tables
    - Uses SQL (Structured Query Language)

## STEP 2: Database Basics
### Create Database
CREATE DATABASE company_db;

### Use Database
USE company_db;

### Show Databases
SHOW DATABASES;


## STEP 3: Tables & Data Types

### Common Data Types
| Type | Example |
| ----------- | ----------- |
| INT | 1, 100 |
| VARCHAR | 'John' |
| TEXT | long text |
| DATE | '2025-01-01' |
| DATETIME | '2025-01-01 10:30:00' |
| DECIMAL | 10.50 |
| BOOLEAN | 0 / 1 |


### Create Table
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    salary DECIMAL(10,2),
    joining_date DATE,
    is_active BOOLEAN DEFAULT 1
);
```

## STEP 4: CRUD Operations (Core of MySQL)
### INSERT (Create)
```sql
INSERT INTO employees (name, email, salary, joining_date)
VALUES ('Sanjoy', 'sanjoy@test.com', 60000, '2024-06-01');
```

### SELECT (Read)
```sql
SELECT * FROM employees;
```

### Specific columns:
```sql
SELECT name, salary FROM employees;
```

### With condition:
```sql
SELECT * FROM employees WHERE salary > 50000;
```

### UPDATE
```sql
UPDATE employees
SET salary = 65000
WHERE id = 1;
```

### DELETE
```sql
DELETE FROM employees WHERE id = 1;
```

**⚠️ Always use WHERE with UPDATE/DELETE.**

## STEP 5: WHERE, AND, OR, IN, BETWEEN
```sql
SELECT * FROM employees
WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees
WHERE name IN ('Sanjoy', 'Rahul');
```

## STEP 6: Sorting & Limiting
### ORDER BY
```sql
SELECT * FROM employees ORDER BY salary DESC;
```

### LIMIT
```sql
SELECT * FROM employees LIMIT 5;
```

### Pagination:
```sql
SELECT * FROM employees LIMIT 5 OFFSET 10;
```

## STEP 7: Aggregate Functions
| Function | Use |
| ---------- | ---------- |
| COUNT() | Total rows |
| SUM() | Total |
| AVG() | Average |
| MIN(), MAX() | Min/Max |

```sql
SELECT COUNT(*) FROM employees;

SELECT AVG(salary) FROM employees;
```

## STEP 8: GROUP BY & HAVING
```sql
SELECT is_active, COUNT(*) 
FROM employees
GROUP BY is_active;
```

### With condition:
```sql
SELECT is_active, COUNT(*)
FROM employees
GROUP BY is_active
HAVING COUNT(*) > 2;
```

## STEP 9: Relationships (Very Important)
### One-to-Many Example
```sql
CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

```sql
ALTER TABLE employees
ADD department_id INT,
ADD FOREIGN KEY (department_id) REFERENCES departments(id);
```

## STEP 10: JOINs (Critical Skill)
### INNER JOIN

```sql
SELECT e.name, d.name AS department
FROM employees e
JOIN departments d ON e.department_id = d.id;
```
## LEFT JOIN
```sql
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

## STEP 11: Indexes (Performance)
```sql
CREATE INDEX idx_email ON employees(email);
```

### Use index when:
- Searching large tables
- Using WHERE / JOIN columns

## STEP 12: Constraints
| Constraint | Purpose |
| PRIMARY KEY | Unique ID |
| FOREIGN KEY | Relationship |
| UNIQUE | No duplicate |
| NOT NULL | Required |
| DEFAULT | Default value |

Example:
```text
email VARCHAR(150) UNIQUE NOT NULL
```

## STEP 13: Transactions (Safety)
```sql
START TRANSACTION;

UPDATE employees SET salary = salary - 5000 WHERE id = 1;
UPDATE employees SET salary = salary + 5000 WHERE id = 2;

COMMIT;

Rollback:
ROLLBACK;
```

## STEP 14: Views
```sql
CREATE VIEW active_employees AS
SELECT name, email
FROM employees
WHERE is_active = 1;

SELECT * FROM active_employees;
```

## STEP 15: Stored Procedures (Intro)
```sql
DELIMITER //

CREATE PROCEDURE getEmployees()
BEGIN
    SELECT * FROM employees;
END //

DELIMITER ;
```
### Call:
```sql
CALL getEmployees();
```

## STEP 16: Security & Users
```sql
CREATE USER 'app_user'@'%' IDENTIFIED BY 'password';

GRANT SELECT, INSERT ON company_db.* TO 'app_user'@'%';
```

## STEP 17: Backup & Restore (Real-World)
### Backup:
```sql
mysqldump -u root -p company_db > backup.sql
```
### Restore:
```sql
mysql -u root -p company_db < backup.sql
```

## STEP 18: MySQL with Python (You Use This)
### SQLAlchemy Example
```sql
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://user:password@localhost/company_db"
)
```

## STEP 19: Best Practices

- ✅ Always use indexes
- ✅ Avoid SELECT * in production
- ✅ Use transactions
- ✅ Normalize data
- ✅ Backup regularly

