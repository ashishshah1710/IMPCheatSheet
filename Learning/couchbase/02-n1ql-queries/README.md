# 🔍 Couchbase - N1QL & Advanced Queries

Master N1QL (SQL for JSON) and complex query patterns!

---

## 📚 Table of Contents

1. [N1QL Fundamentals](#n1ql-fundamentals)
2. [Complex Queries](#complex-queries)
3. [Joins](#joins)
4. [Subqueries](#subqueries)
5. [Array Operations](#array-operations)
6. [Full-Text Search](#full-text-search)
7. [Query Optimization](#query-optimization)
8. [Interview Questions](#interview-questions)

---

## 🎯 N1QL Fundamentals

### SELECT Queries

```sql
-- Basic SELECT
SELECT * FROM `travel-sample` 
WHERE type = 'airline' 
LIMIT 10;

-- Specific fields
SELECT name, country, callsign 
FROM `travel-sample` 
WHERE type = 'airline';

-- Computed fields
SELECT name, 
       LOWER(name) as lowercase_name,
       LENGTH(name) as name_length
FROM `travel-sample` 
WHERE type = 'airline';

-- DISTINCT
SELECT DISTINCT country 
FROM `travel-sample` 
WHERE type = 'airline';
```

### WHERE Clauses

```sql
-- Comparison operators
SELECT * FROM `travel-sample` 
WHERE type = 'hotel' AND reviews.ratings.Overall >= 4;

-- BETWEEN
SELECT * FROM `travel-sample` 
WHERE type = 'hotel' 
AND price BETWEEN 100 AND 300;

-- IN
SELECT * FROM `travel-sample` 
WHERE country IN ['United States', 'United Kingdom', 'France'];

-- LIKE (pattern matching)
SELECT * FROM `travel-sample` 
WHERE name LIKE '%Hotel%';

-- IS NULL / IS NOT NULL
SELECT * FROM `travel-sample` 
WHERE description IS NOT NULL;

-- CONTAINS (for arrays)
SELECT * FROM `travel-sample` 
WHERE type = 'hotel' 
AND CONTAINS(reviews, 'excellent');
```

---

## 🔄 Complex Queries

### Aggregations

```sql
-- COUNT
SELECT COUNT(*) as total 
FROM `travel-sample` 
WHERE type = 'airline';

-- SUM, AVG, MIN, MAX
SELECT 
    AVG(price) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price,
    SUM(price) as total_price
FROM `travel-sample` 
WHERE type = 'hotel';

-- GROUP BY
SELECT country, COUNT(*) as count 
FROM `travel-sample` 
WHERE type = 'airline' 
GROUP BY country 
ORDER BY count DESC;

-- HAVING
SELECT country, COUNT(*) as count 
FROM `travel-sample` 
WHERE type = 'airline' 
GROUP BY country 
HAVING COUNT(*) > 10 
ORDER BY count DESC;
```

### Window Functions

```sql
-- ROW_NUMBER
SELECT name, country,
       ROW_NUMBER() OVER (PARTITION BY country ORDER BY name) as row_num
FROM `travel-sample` 
WHERE type = 'airline';

-- RANK
SELECT name, country, callsign,
       RANK() OVER (PARTITION BY country ORDER BY name) as rank
FROM `travel-sample` 
WHERE type = 'airline';

-- LAG and LEAD
SELECT name, price,
       LAG(price) OVER (ORDER BY price) as prev_price,
       LEAD(price) OVER (ORDER BY price) as next_price
FROM `travel-sample` 
WHERE type = 'hotel';
```

---

## 🔗 Joins

### INNER JOIN

```sql
-- Join airlines with routes
SELECT r.airline, r.sourceairport, a.name as airline_name
FROM `travel-sample` r
INNER JOIN `travel-sample` a 
ON KEYS r.airlineid
WHERE r.type = 'route' 
AND a.type = 'airline'
LIMIT 10;
```

### LEFT JOIN

```sql
-- Join with optional match
SELECT a.name, r.sourceairport
FROM `travel-sample` a
LEFT JOIN `travel-sample` r 
ON KEYS ('route_' || a.iata)
WHERE a.type = 'airline'
LIMIT 10;
```

### NEST (Embedding Results)

```sql
-- Nest routes within airlines
SELECT a.name, 
       ARRAY_AGG(r) as routes
FROM `travel-sample` a
INNER JOIN `travel-sample` r 
ON KEYS r.airlineid
WHERE a.type = 'airline' 
AND r.type = 'route'
GROUP BY a.name
LIMIT 5;
```

### Lookup Joins

```sql
-- Join using document key
SELECT h.name, h.city, r.content
FROM `travel-sample` h
LEFT NEST `travel-sample` r 
ON KEY h.id || '::review'
WHERE h.type = 'hotel';
```

---

## 📦 Subqueries

### IN Subquery

```sql
-- Find airlines flying to specific airport
SELECT name 
FROM `travel-sample` 
WHERE type = 'airline'
AND id IN (
    SELECT RAW airlineid 
    FROM `travel-sample` 
    WHERE type = 'route' 
    AND sourceairport = 'SFO'
);
```

### EXISTS Subquery

```sql
-- Airlines that have at least one route
SELECT a.name 
FROM `travel-sample` a
WHERE a.type = 'airline'
AND EXISTS (
    SELECT 1 
    FROM `travel-sample` r 
    WHERE r.type = 'route' 
    AND r.airlineid = a.id
);
```

### Correlated Subquery

```sql
-- Hotels with above-average price in their city
SELECT h1.name, h1.city, h1.price
FROM `travel-sample` h1
WHERE h1.type = 'hotel'
AND h1.price > (
    SELECT AVG(h2.price)
    FROM `travel-sample` h2
    WHERE h2.type = 'hotel'
    AND h2.city = h1.city
);
```

---

## 📋 Array Operations

### UNNEST

```sql
-- Flatten array
SELECT h.name, review
FROM `travel-sample` h
UNNEST h.reviews as review
WHERE h.type = 'hotel';
```

### ARRAY

```sql
-- Transform array elements
SELECT name,
       ARRAY hobby FOR hobby IN hobbies END as hobby_list
FROM `travel-sample`
WHERE type = 'user';

-- Filter array elements
SELECT name,
       ARRAY r FOR r IN reviews WHEN r.rating > 4 END as good_reviews
FROM `travel-sample`
WHERE type = 'hotel';

-- Array with index
SELECT name,
       ARRAY {index: i, value: v} FOR v IN hobbies AT i END as indexed_hobbies
FROM `travel-sample`
WHERE type = 'user';
```

### ARRAY_AGG

```sql
-- Aggregate into array
SELECT country, 
       ARRAY_AGG(name) as airline_names
FROM `travel-sample`
WHERE type = 'airline'
GROUP BY country;

-- ARRAY_AGG with DISTINCT
SELECT country,
       ARRAY_AGG(DISTINCT city) as cities
FROM `travel-sample`
WHERE type = 'hotel'
GROUP BY country;
```

### Array Functions

```sql
-- ARRAY_LENGTH
SELECT name, ARRAY_LENGTH(reviews) as review_count
FROM `travel-sample`
WHERE type = 'hotel';

-- ARRAY_CONTAINS
SELECT name
FROM `travel-sample`
WHERE type = 'hotel'
AND ARRAY_CONTAINS(reviews[*].author, 'John');

-- ARRAY_CONCAT
SELECT ARRAY_CONCAT(['a', 'b'], ['c', 'd']) as combined;

-- ARRAY_REMOVE
SELECT ARRAY_REMOVE(['a', 'b', 'c'], 'b') as result;
```

---

## 🔎 Full-Text Search

### Creating FTS Index

```javascript
// Via Web Console or REST API
const ftsIndex = {
  "type": "fulltext-index",
  "name": "hotel-search",
  "sourceType": "couchbase",
  "sourceName": "travel-sample",
  "planParams": {
    "maxPartitionsPerPIndex": 171
  },
  "params": {
    "mapping": {
      "default_mapping": {
        "enabled": false
      },
      "types": {
        "hotel": {
          "enabled": true,
          "properties": {
            "name": {
              "enabled": true,
              "fields": [{
                "name": "name",
                "type": "text"
              }]
            },
            "description": {
              "enabled": true,
              "fields": [{
                "name": "description",
                "type": "text"
              }]
            }
          }
        }
      }
    }
  }
};
```

### FTS Queries

```sql
-- Simple search
SELECT name, description
FROM `travel-sample`
WHERE SEARCH(name, 'beach resort');

-- Match phrase
SELECT name
FROM `travel-sample`
WHERE SEARCH(`travel-sample`, {
  "query": {
    "match_phrase": "luxury hotel"
  }
});

-- Fuzzy search
SELECT name
FROM `travel-sample`
WHERE SEARCH(`travel-sample`, {
  "query": {
    "match": "hotl",
    "fuzziness": 1
  }
});

-- Boolean search
SELECT name
FROM `travel-sample`
WHERE SEARCH(`travel-sample`, {
  "query": {
    "conjuncts": [
      {"match": "hotel"},
      {"match": "beach"}
    ]
  }
});
```

---

## ⚡ Query Optimization

### EXPLAIN

```sql
-- Analyze query plan
EXPLAIN SELECT * FROM `travel-sample` 
WHERE type = 'airline' AND country = 'United States';

-- Check index usage
EXPLAIN SELECT name FROM `travel-sample` 
USE INDEX (idx_type)
WHERE type = 'airline';
```

### Index Hints

```sql
-- Force index usage
SELECT * FROM `travel-sample` 
USE INDEX (idx_type_country)
WHERE type = 'airline' AND country = 'United States';

-- Avoid specific index
SELECT * FROM `travel-sample` 
AVOID INDEX (idx_primary)
WHERE type = 'airline';
```

### Covering Indexes

```sql
-- Create covering index
CREATE INDEX idx_airline_covering 
ON `travel-sample`(type, name, country)
WHERE type = 'airline';

-- Query uses covering index (no document fetch needed)
SELECT name, country 
FROM `travel-sample` 
WHERE type = 'airline';
```

### Query Optimization Tips

```sql
-- 1. Use appropriate indexes
CREATE INDEX idx_type_country ON `travel-sample`(type, country);

-- 2. Limit result set
SELECT * FROM `travel-sample` 
WHERE type = 'airline' 
LIMIT 100;

-- 3. Use projections (select specific fields)
SELECT name, country FROM `travel-sample` 
WHERE type = 'airline';

-- 4. Avoid SELECT *
SELECT id, name, email FROM users;  -- Good
SELECT * FROM users;  -- Bad (fetches all fields)

-- 5. Use WHERE clauses efficiently
WHERE type = 'airline' AND country = 'USA'  -- Good (indexed fields first)

-- 6. Avoid wildcard at start of LIKE
LIKE 'hotel%'  -- Good (can use index)
LIKE '%hotel'  -- Bad (cannot use index)
```

---

## 🔍 Advanced Patterns

### Recursive CTE

```sql
-- Find all connected routes
WITH RECURSIVE route_chain(source, dest, path, depth) AS (
    SELECT sourceairport, destinationairport, 
           [sourceairport, destinationairport], 1
    FROM `travel-sample`
    WHERE type = 'route' AND sourceairport = 'SFO'
    
    UNION ALL
    
    SELECT rc.source, r.destinationairport,
           ARRAY_APPEND(rc.path, r.destinationairport), rc.depth + 1
    FROM route_chain rc
    JOIN `travel-sample` r ON r.sourceairport = rc.dest
    WHERE r.type = 'route' AND rc.depth < 3
)
SELECT * FROM route_chain;
```

### JSON Functions

```sql
-- JSON manipulation
SELECT name,
       OBJECT_ADD(meta(), 'timestamp', NOW_STR()) as enriched
FROM `travel-sample`
WHERE type = 'airline'
LIMIT 5;

-- JSON construction
SELECT OBJECT_CONSTRUCT(
    'airline', name,
    'country', country,
    'timestamp', NOW_STR()
) as result
FROM `travel-sample`
WHERE type = 'airline'
LIMIT 5;
```

---

## 🎯 Interview Questions

**Q: What is N1QL?**

**Answer:**
N1QL (pronounced "nickel") is Couchbase's query language - SQL for JSON. It extends SQL to work with JSON documents.

**Q: How do joins work in N1QL?**

**Answer:**
- **ON KEYS:** Join using document keys
- **ON:** Join using any condition
- **NEST:** Embed joined results as nested arrays
- **UNNEST:** Flatten arrays for joining

**Q: What are covering indexes?**

**Answer:**
Indexes that contain all fields needed by a query, eliminating the need to fetch documents. Significantly improves query performance.

---

**Continue to Performance & Scaling for optimization!** 🚀

