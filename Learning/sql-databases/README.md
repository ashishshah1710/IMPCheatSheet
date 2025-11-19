# 🗄️ SQL Databases (PostgreSQL & MySQL)

## Overview
Relational databases are the backbone of most applications. PostgreSQL and MySQL are the two most popular open-source SQL databases.

---

## PostgreSQL vs MySQL

| Feature | PostgreSQL | MySQL |
|---------|-----------|-------|
| **Type** | Object-relational | Relational |
| **ACID Compliance** | Full | Full (InnoDB) |
| **Performance** | Complex queries | Simple queries, reads |
| **Advanced Features** | JSON, Arrays, Full-text | Limited |
| **Replication** | Logical, streaming | Master-slave, group |
| **Use Cases** | Complex apps, analytics | Web apps, read-heavy |

### When to Use PostgreSQL
✅ Complex queries and joins  
✅ Data integrity critical  
✅ Advanced data types needed  
✅ OLAP (analytics) workloads  

### When to Use MySQL
✅ Simple CRUD operations  
✅ Read-heavy workloads  
✅ Easier setup and management  
✅ Wide hosting support  

---

## Installation

### PostgreSQL
```bash
# Ubuntu
sudo apt update
sudo apt install postgresql postgresql-contrib

# Mac
brew install postgresql
brew services start postgresql

# Connect
psql -U postgres
```

### MySQL
```bash
# Ubuntu
sudo apt install mysql-server

# Mac
brew install mysql
brew services start mysql

# Secure installation
sudo mysql_secure_installation

# Connect
mysql -u root -p
```

---

## Basic SQL Commands

### Database Operations
```sql
-- Create database
CREATE DATABASE myapp;

-- List databases
\l  -- PostgreSQL
SHOW DATABASES;  -- MySQL

-- Use database
\c myapp;  -- PostgreSQL
USE myapp;  -- MySQL

-- Drop database
DROP DATABASE myapp;
```

### Table Operations
```sql
-- Create table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- PostgreSQL
    -- id INT AUTO_INCREMENT PRIMARY KEY,  -- MySQL
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add column
ALTER TABLE users ADD COLUMN last_login TIMESTAMP;

-- Modify column
ALTER TABLE users ALTER COLUMN email TYPE VARCHAR(150);  -- PostgreSQL
ALTER TABLE users MODIFY email VARCHAR(150);  -- MySQL

-- Drop column
ALTER TABLE users DROP COLUMN last_login;

-- Drop table
DROP TABLE users;

-- Describe table
\d users;  -- PostgreSQL
DESCRIBE users;  -- MySQL
```

---

## CRUD Operations

### Create (INSERT)
```sql
-- Single insert
INSERT INTO users (username, email, age) 
VALUES ('john_doe', 'john@example.com', 30);

-- Multiple inserts
INSERT INTO users (username, email, age) VALUES
    ('jane_smith', 'jane@example.com', 25),
    ('bob_jones', 'bob@example.com', 35),
    ('alice_wilson', 'alice@example.com', 28);

-- Insert with RETURNING (PostgreSQL)
INSERT INTO users (username, email, age)
VALUES ('new_user', 'new@example.com', 22)
RETURNING id, username, created_at;
```

### Read (SELECT)
```sql
-- Select all
SELECT * FROM users;

-- Select specific columns
SELECT id, username, email FROM users;

-- Where clause
SELECT * FROM users WHERE age > 25;

-- Multiple conditions
SELECT * FROM users 
WHERE age > 25 AND is_active = TRUE;

-- OR condition
SELECT * FROM users 
WHERE age < 20 OR age > 60;

-- IN operator
SELECT * FROM users 
WHERE username IN ('john_doe', 'jane_smith');

-- LIKE operator (pattern matching)
SELECT * FROM users 
WHERE email LIKE '%@gmail.com';

-- BETWEEN
SELECT * FROM users 
WHERE age BETWEEN 25 AND 35;

-- ORDER BY
SELECT * FROM users 
ORDER BY created_at DESC;

-- LIMIT and OFFSET
SELECT * FROM users 
ORDER BY created_at DESC 
LIMIT 10 OFFSET 20;  -- Skip 20, get next 10

-- DISTINCT
SELECT DISTINCT age FROM users;
```

### Update (UPDATE)
```sql
-- Update single record
UPDATE users 
SET email = 'newemail@example.com' 
WHERE id = 1;

-- Update multiple columns
UPDATE users 
SET age = 31, is_active = FALSE 
WHERE username = 'john_doe';

-- Update with condition
UPDATE users 
SET is_active = FALSE 
WHERE last_login < NOW() - INTERVAL '1 year';

-- Update with RETURNING (PostgreSQL)
UPDATE users 
SET age = age + 1 
WHERE id = 1 
RETURNING *;
```

### Delete (DELETE)
```sql
-- Delete specific record
DELETE FROM users WHERE id = 1;

-- Delete with condition
DELETE FROM users WHERE is_active = FALSE;

-- Delete all records (dangerous!)
DELETE FROM users;

-- TRUNCATE (faster, resets auto-increment)
TRUNCATE TABLE users;
```

---

## Joins

```sql
-- Sample data
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product VARCHAR(100),
    amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INNER JOIN (matching records only)
SELECT users.username, orders.product, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN (all from left table)
SELECT users.username, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- RIGHT JOIN (all from right table)
SELECT users.username, orders.product
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;

-- FULL OUTER JOIN (all from both - PostgreSQL only)
SELECT users.username, orders.product
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;

-- Multiple joins
SELECT u.username, o.product, p.status
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN payments p ON o.id = p.order_id;
```

---

## Aggregate Functions

```sql
-- COUNT
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM users WHERE age > 30;

-- SUM
SELECT SUM(amount) FROM orders;

-- AVG
SELECT AVG(age) FROM users;

-- MIN and MAX
SELECT MIN(age), MAX(age) FROM users;

-- GROUP BY
SELECT age, COUNT(*) as count
FROM users
GROUP BY age
ORDER BY count DESC;

-- GROUP BY with JOIN
SELECT u.username, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.username;

-- HAVING (filter after GROUP BY)
SELECT age, COUNT(*) as count
FROM users
GROUP BY age
HAVING COUNT(*) > 5;
```

---

## Indexes

```sql
-- Create index
CREATE INDEX idx_users_email ON users(email);

-- Composite index
CREATE INDEX idx_users_age_created ON users(age, created_at);

-- Unique index
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- List indexes
\di  -- PostgreSQL
SHOW INDEX FROM users;  -- MySQL

-- Drop index
DROP INDEX idx_users_email;
```

---

## Constraints

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) CHECK (price > 0),
    category VARCHAR(50) DEFAULT 'General',
    sku VARCHAR(50) UNIQUE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE
);

-- Add constraint
ALTER TABLE products 
ADD CONSTRAINT check_positive_price 
CHECK (price > 0);

-- Drop constraint
ALTER TABLE products 
DROP CONSTRAINT check_positive_price;
```

---

## Transactions

```sql
-- Start transaction
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit (make permanent)
COMMIT;

-- Or rollback (undo)
ROLLBACK;

-- Savepoints
BEGIN;
UPDATE users SET age = 30 WHERE id = 1;
SAVEPOINT my_savepoint;
UPDATE users SET age = 35 WHERE id = 2;
ROLLBACK TO my_savepoint;  -- Undo second update
COMMIT;
```

---

## Advanced PostgreSQL Features

### JSON Support
```sql
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_data JSONB  -- JSONB is binary, faster
);

INSERT INTO events (event_data) VALUES
    ('{"type": "login", "user_id": 1, "timestamp": "2024-01-15"}'),
    ('{"type": "purchase", "user_id": 2, "amount": 99.99}');

-- Query JSON
SELECT event_data->>'type' as event_type FROM events;
SELECT * FROM events WHERE event_data->>'type' = 'login';
SELECT * FROM events WHERE event_data->>'amount' > '50';

-- JSON operators
SELECT event_data->'user_id' FROM events;  -- Returns JSON
SELECT event_data->>'user_id' FROM events;  -- Returns text
```

### Arrays
```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    tags TEXT[]
);

INSERT INTO posts (title, tags) VALUES
    ('First Post', ARRAY['tech', 'programming']),
    ('Second Post', ARRAY['life', 'travel', 'food']);

-- Query arrays
SELECT * FROM posts WHERE 'tech' = ANY(tags);
SELECT * FROM posts WHERE tags @> ARRAY['programming'];
```

### Full-Text Search
```sql
-- Create search column
ALTER TABLE posts ADD COLUMN search_vector tsvector;

-- Update search vector
UPDATE posts SET search_vector = 
    to_tsvector('english', title || ' ' || content);

-- Create index
CREATE INDEX idx_posts_search ON posts USING gin(search_vector);

-- Search
SELECT * FROM posts 
WHERE search_vector @@ to_tsquery('english', 'programming & java');
```

---

## Common Queries

### Pagination
```sql
-- Page 1 (records 1-10)
SELECT * FROM users LIMIT 10 OFFSET 0;

-- Page 2 (records 11-20)
SELECT * FROM users LIMIT 10 OFFSET 10;

-- Page N
SELECT * FROM users LIMIT 10 OFFSET ((N - 1) * 10);
```

### Find Duplicates
```sql
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;
```

### Running Totals
```sql
SELECT 
    created_at::DATE as date,
    amount,
    SUM(amount) OVER (ORDER BY created_at) as running_total
FROM orders;
```

### Ranking
```sql
SELECT 
    username,
    score,
    RANK() OVER (ORDER BY score DESC) as rank
FROM leaderboard;
```

---

## Performance Optimization

### EXPLAIN
```sql
-- See query plan
EXPLAIN SELECT * FROM users WHERE email = 'john@example.com';

-- With execution stats
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'john@example.com';
```

### Best Practices
✅ Use indexes on frequently queried columns  
✅ Avoid SELECT * (specify columns)  
✅ Use LIMIT for large result sets  
✅ Optimize JOINs (index foreign keys)  
✅ Use connection pooling  
✅ Normalize data (avoid redundancy)  
✅ Use prepared statements (prevent SQL injection)  

---

## Backup & Restore

### PostgreSQL
```bash
# Backup
pg_dump myapp > myapp_backup.sql
pg_dump -U postgres myapp > backup.sql

# Restore
psql myapp < myapp_backup.sql
psql -U postgres myapp < backup.sql
```

### MySQL
```bash
# Backup
mysqldump -u root -p myapp > myapp_backup.sql

# Restore
mysql -u root -p myapp < myapp_backup.sql
```

---

## SQL Injection Prevention

```sql
-- BAD (vulnerable)
query = "SELECT * FROM users WHERE username = '" + userInput + "'"

-- GOOD (parameterized)
-- Java
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE username = ?"
);
stmt.setString(1, userInput);

-- Python
cursor.execute("SELECT * FROM users WHERE username = %s", (userInput,))

-- Node.js
db.query("SELECT * FROM users WHERE username = $1", [userInput])
```

---

## Resources

### PostgreSQL
- **Official Docs**: postgresql.org/docs
- **Tutorial**: postgresqltutorial.com

### MySQL
- **Official Docs**: dev.mysql.com/doc
- **Tutorial**: mysqltutorial.org

### Practice
- **SQL Zoo**: Interactive SQL tutorial
- **LeetCode**: Database problems
- **HackerRank**: SQL challenges

---

**💡 Pro Tip**: Master the basics (CRUD, joins, indexes) first. Advanced features like JSON and full-text search come later!

