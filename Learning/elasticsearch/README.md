# 🔍 Elasticsearch

## Overview
Elasticsearch is a distributed, RESTful search and analytics engine built on Apache Lucene. It's designed for horizontal scalability, reliability, and real-time search capabilities.

---

## Why Elasticsearch?

### ✅ Benefits
- **Full-Text Search**: Powerful text search with relevance scoring
- **Fast**: Near real-time search and indexing
- **Scalable**: Distributed architecture, petabyte-scale
- **RESTful API**: Easy HTTP-based operations
- **Schema-Free**: JSON documents, flexible structure
- **Analytics**: Aggregations for data analysis

### 🎯 Use Cases
- **Search Engines**: Product search, site search
- **Logging & Monitoring**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Analytics**: Business intelligence, metrics
- **Security**: SIEM (Security Information and Event Management)
- **E-commerce**: Product catalogs, recommendations
- **Content Management**: Document search, media libraries

### Companies Using Elasticsearch
- Netflix, Uber, Slack, GitHub, Stack Overflow, Medium

---

## Core Concepts

### 1. **Index**
Like a database - collection of documents

```json
Index: "products"
├── Document 1 (Laptop)
├── Document 2 (Phone)
└── Document 3 (Tablet)
```

### 2. **Document**
JSON object - the data you store

```json
{
  "_index": "products",
  "_id": "1",
  "_source": {
    "name": "MacBook Pro",
    "price": 2399,
    "category": "laptops",
    "description": "Powerful laptop for professionals"
  }
}
```

### 3. **Mapping**
Schema definition - how documents are indexed

```json
{
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "price": { "type": "float" },
      "category": { "type": "keyword" },
      "created_at": { "type": "date" }
    }
  }
}
```

### 4. **Shard**
Subdivision of an index for horizontal scaling

### 5. **Replica**
Copy of a shard for fault tolerance

---

## Installation

### Docker (Easiest)
```bash
# Single node
docker run -d \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.11.0

# Verify
curl http://localhost:9200
```

### Linux
```bash
# Download and extract
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.11.0-linux-x86_64.tar.gz
tar -xzf elasticsearch-8.11.0-linux-x86_64.tar.gz
cd elasticsearch-8.11.0

# Start
./bin/elasticsearch
```

### Mac
```bash
brew install elasticsearch
brew services start elasticsearch

# Verify
curl http://localhost:9200
```

---

## Basic Operations (CRUD)

### Create Index
```bash
# Create index with settings
curl -X PUT "localhost:9200/products" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "description": { "type": "text" },
      "price": { "type": "float" },
      "category": { "type": "keyword" },
      "tags": { "type": "keyword" },
      "in_stock": { "type": "boolean" },
      "created_at": { "type": "date" }
    }
  }
}
'
```

### Index Document (Create/Update)
```bash
# Index with auto-generated ID
curl -X POST "localhost:9200/products/_doc" -H 'Content-Type: application/json' -d'
{
  "name": "MacBook Pro",
  "description": "Powerful laptop with M3 chip",
  "price": 2399.99,
  "category": "laptops",
  "tags": ["apple", "laptop", "premium"],
  "in_stock": true,
  "created_at": "2024-01-15"
}
'

# Index with specific ID
curl -X PUT "localhost:9200/products/_doc/1" -H 'Content-Type: application/json' -d'
{
  "name": "iPhone 15 Pro",
  "description": "Latest iPhone with A17 Pro chip",
  "price": 999.99,
  "category": "phones",
  "tags": ["apple", "phone", "5g"],
  "in_stock": true,
  "created_at": "2024-01-15"
}
'
```

### Get Document
```bash
# Get by ID
curl -X GET "localhost:9200/products/_doc/1"

# Get only source
curl -X GET "localhost:9200/products/_doc/1/_source"
```

### Update Document
```bash
# Partial update
curl -X POST "localhost:9200/products/_update/1" -H 'Content-Type: application/json' -d'
{
  "doc": {
    "price": 899.99,
    "in_stock": false
  }
}
'

# Update with script
curl -X POST "localhost:9200/products/_update/1" -H 'Content-Type: application/json' -d'
{
  "script": {
    "source": "ctx._source.price -= params.discount",
    "params": {
      "discount": 100
    }
  }
}
'
```

### Delete Document
```bash
# Delete by ID
curl -X DELETE "localhost:9200/products/_doc/1"

# Delete by query
curl -X POST "localhost:9200/products/_delete_by_query" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "category": "phones"
    }
  }
}
'
```

---

## Search Queries

### 1. **Match All**
```json
GET /products/_search
{
  "query": {
    "match_all": {}
  }
}
```

### 2. **Match Query** (Full-Text Search)
```json
GET /products/_search
{
  "query": {
    "match": {
      "description": "powerful laptop"
    }
  }
}
```

### 3. **Term Query** (Exact Match)
```json
GET /products/_search
{
  "query": {
    "term": {
      "category": "laptops"
    }
  }
}
```

### 4. **Multi-Match** (Search Multiple Fields)
```json
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "apple",
      "fields": ["name^3", "description", "tags"]
    }
  }
}
```
*Note: `^3` boosts the `name` field by 3x*

### 5. **Bool Query** (Combine Conditions)
```json
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "category": "laptops" } }
      ],
      "filter": [
        { "range": { "price": { "gte": 1000, "lte": 3000 } } },
        { "term": { "in_stock": true } }
      ],
      "should": [
        { "match": { "tags": "premium" } }
      ],
      "must_not": [
        { "match": { "name": "refurbished" } }
      ]
    }
  }
}
```

**Bool Clauses:**
- `must`: Document must match (affects score)
- `filter`: Document must match (no scoring, faster)
- `should`: Nice to have (boosts score)
- `must_not`: Document must not match

### 6. **Range Query**
```json
GET /products/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 500,
        "lte": 2000
      }
    }
  }
}

// Date range
GET /products/_search
{
  "query": {
    "range": {
      "created_at": {
        "gte": "2024-01-01",
        "lte": "2024-12-31"
      }
    }
  }
}
```

### 7. **Wildcard & Fuzzy Search**
```json
// Wildcard
GET /products/_search
{
  "query": {
    "wildcard": {
      "name": "mac*"
    }
  }
}

// Fuzzy (typo tolerance)
GET /products/_search
{
  "query": {
    "fuzzy": {
      "name": {
        "value": "mackbook",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

### 8. **Prefix Search**
```json
GET /products/_search
{
  "query": {
    "prefix": {
      "name": "iphone"
    }
  }
}
```

### 9. **Exists Query**
```json
GET /products/_search
{
  "query": {
    "exists": {
      "field": "discount"
    }
  }
}
```

---

## Advanced Search Features

### 1. **Pagination**
```json
GET /products/_search
{
  "from": 0,
  "size": 10,
  "query": {
    "match_all": {}
  }
}

// Deep pagination (use search_after for performance)
GET /products/_search
{
  "size": 10,
  "query": { "match_all": {} },
  "search_after": [1463538857, "654323"],
  "sort": [
    { "created_at": "asc" },
    { "_id": "asc" }
  ]
}
```

### 2. **Sorting**
```json
GET /products/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "price": "asc" },
    { "_score": "desc" }
  ]
}
```

### 3. **Source Filtering**
```json
// Include specific fields
GET /products/_search
{
  "_source": ["name", "price"],
  "query": { "match_all": {} }
}

// Exclude fields
GET /products/_search
{
  "_source": {
    "excludes": ["description"]
  },
  "query": { "match_all": {} }
}
```

### 4. **Highlighting**
```json
GET /products/_search
{
  "query": {
    "match": {
      "description": "powerful"
    }
  },
  "highlight": {
    "fields": {
      "description": {}
    }
  }
}
```

### 5. **Autocomplete (Suggestions)**
```json
// Create index with completion field
PUT /products
{
  "mappings": {
    "properties": {
      "suggest": {
        "type": "completion"
      }
    }
  }
}

// Query suggestions
POST /products/_search
{
  "suggest": {
    "product-suggest": {
      "prefix": "mac",
      "completion": {
        "field": "suggest"
      }
    }
  }
}
```

---

## Aggregations (Analytics)

### 1. **Metrics Aggregations**
```json
// Average price
GET /products/_search
{
  "size": 0,
  "aggs": {
    "avg_price": {
      "avg": {
        "field": "price"
      }
    }
  }
}

// Multiple metrics
GET /products/_search
{
  "size": 0,
  "aggs": {
    "stats": {
      "stats": {
        "field": "price"
      }
    }
  }
}
// Returns: min, max, avg, sum, count
```

### 2. **Bucket Aggregations**
```json
// Group by category
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_category": {
      "terms": {
        "field": "category",
        "size": 10
      }
    }
  }
}

// Price ranges
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "to": 500 },
          { "from": 500, "to": 1000 },
          { "from": 1000, "to": 2000 },
          { "from": 2000 }
        ]
      }
    }
  }
}

// Date histogram
GET /products/_search
{
  "size": 0,
  "aggs": {
    "sales_over_time": {
      "date_histogram": {
        "field": "created_at",
        "calendar_interval": "month"
      }
    }
  }
}
```

### 3. **Nested Aggregations**
```json
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_category": {
      "terms": {
        "field": "category"
      },
      "aggs": {
        "avg_price": {
          "avg": {
            "field": "price"
          }
        }
      }
    }
  }
}
```

---

## Integration with Applications

### Python (elasticsearch-py)
```python
from elasticsearch import Elasticsearch

# Connect
es = Elasticsearch(['http://localhost:9200'])

# Index document
doc = {
    'name': 'MacBook Pro',
    'price': 2399.99,
    'category': 'laptops'
}
es.index(index='products', id=1, document=doc)

# Search
resp = es.search(index='products', query={
    'match': {
        'name': 'macbook'
    }
})

for hit in resp['hits']['hits']:
    print(hit['_source'])

# Update
es.update(index='products', id=1, doc={
    'price': 2199.99
})

# Delete
es.delete(index='products', id=1)

# Bulk operations
from elasticsearch.helpers import bulk

actions = [
    {
        '_index': 'products',
        '_id': i,
        '_source': {
            'name': f'Product {i}',
            'price': i * 100
        }
    }
    for i in range(1000)
]
bulk(es, actions)
```

### Node.js (@elastic/elasticsearch)
```javascript
const { Client } = require('@elastic/elasticsearch');
const client = new Client({ node: 'http://localhost:9200' });

// Index document
await client.index({
  index: 'products',
  id: '1',
  document: {
    name: 'MacBook Pro',
    price: 2399.99,
    category: 'laptops'
  }
});

// Search
const result = await client.search({
  index: 'products',
  query: {
    match: {
      name: 'macbook'
    }
  }
});

console.log(result.hits.hits);

// Update
await client.update({
  index: 'products',
  id: '1',
  doc: {
    price: 2199.99
  }
});

// Delete
await client.delete({
  index: 'products',
  id: '1'
});
```

### Java (High Level REST Client)
```java
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.builder.SearchSourceBuilder;

// Connect
RestHighLevelClient client = new RestHighLevelClient(
    RestClient.builder(new HttpHost("localhost", 9200, "http"))
);

// Index document
IndexRequest request = new IndexRequest("products")
    .id("1")
    .source("name", "MacBook Pro",
            "price", 2399.99,
            "category", "laptops");
client.index(request, RequestOptions.DEFAULT);

// Search
SearchRequest searchRequest = new SearchRequest("products");
SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();
sourceBuilder.query(QueryBuilders.matchQuery("name", "macbook"));
searchRequest.source(sourceBuilder);

SearchResponse response = client.search(searchRequest, RequestOptions.DEFAULT);

// Close
client.close();
```

---

## Real-World Use Cases

### 1. **E-Commerce Product Search**
```json
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "multi_match": {
            "query": "wireless headphones",
            "fields": ["name^3", "description", "brand^2"]
          }
        }
      ],
      "filter": [
        { "range": { "price": { "lte": 200 } } },
        { "term": { "in_stock": true } },
        { "terms": { "brand": ["sony", "bose", "apple"] } }
      ]
    }
  },
  "aggs": {
    "brands": {
      "terms": { "field": "brand" }
    },
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "to": 50 },
          { "from": 50, "to": 100 },
          { "from": 100, "to": 200 },
          { "from": 200 }
        ]
      }
    }
  },
  "sort": [
    { "_score": "desc" },
    { "popularity": "desc" }
  ]
}
```

### 2. **Log Analysis (ELK Stack)**
```json
// Index logs
PUT /logs/_doc/1
{
  "timestamp": "2024-01-15T10:30:00",
  "level": "ERROR",
  "message": "Database connection timeout",
  "service": "order-service",
  "user_id": 12345
}

// Search errors in last hour
GET /logs/_search
{
  "query": {
    "bool": {
      "must": [
        { "term": { "level": "ERROR" } }
      ],
      "filter": [
        {
          "range": {
            "timestamp": {
              "gte": "now-1h"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "errors_by_service": {
      "terms": { "field": "service" }
    }
  }
}
```

### 3. **Geospatial Search**
```json
// Create index with geo_point
PUT /locations
{
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "location": { "type": "geo_point" }
    }
  }
}

// Index locations
PUT /locations/_doc/1
{
  "name": "Central Park",
  "location": {
    "lat": 40.785091,
    "lon": -73.968285
  }
}

// Find nearby locations (within 5km)
GET /locations/_search
{
  "query": {
    "geo_distance": {
      "distance": "5km",
      "location": {
        "lat": 40.7831,
        "lon": -73.9712
      }
    }
  }
}
```

---

## Performance Optimization

### 1. **Index Settings**
```json
PUT /products
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "refresh_interval": "30s",  // Default: 1s (less frequent = faster indexing)
    "index.max_result_window": 10000
  }
}
```

### 2. **Bulk Indexing**
```bash
# Better performance than individual requests
curl -X POST "localhost:9200/_bulk" -H 'Content-Type: application/json' -d'
{ "index": { "_index": "products", "_id": "1" } }
{ "name": "Product 1", "price": 100 }
{ "index": { "_index": "products", "_id": "2" } }
{ "name": "Product 2", "price": 200 }
'
```

### 3. **Use Filters Over Queries**
```json
// Filter (cacheable, no scoring)
{
  "query": {
    "bool": {
      "filter": [
        { "term": { "category": "laptops" } }
      ]
    }
  }
}

// Query (scoring, slower)
{
  "query": {
    "term": { "category": "laptops" }
  }
}
```

### 4. **Optimize Mappings**
```json
{
  "mappings": {
    "properties": {
      "id": { "type": "keyword" },  // Use keyword for exact match
      "email": { "type": "keyword" },
      "description": {
        "type": "text",
        "index": false  // Don't index if you never search on it
      }
    }
  }
}
```

---

## Best Practices

### ✅ Do's
- Use `keyword` type for exact matches (IDs, emails, statuses)
- Use `text` type for full-text search
- Set appropriate `refresh_interval` for your use case
- Use bulk API for multiple operations
- Use filters for non-scoring queries
- Monitor cluster health regularly
- Use aliases for zero-downtime reindexing
- Implement proper security (authentication, encryption)

### ❌ Don'ts
- Don't use wildcard queries on large datasets
- Don't store unnecessary data
- Don't use too many shards (overhead)
- Don't fetch large result sets (use pagination)
- Don't use nested/parent-child unless necessary
- Don't ignore index lifecycle management

---

## Monitoring & Management

### Cluster Health
```bash
GET /_cluster/health

GET /_cat/indices?v

GET /_cat/nodes?v
```

### Index Management
```bash
# Create alias
POST /_aliases
{
  "actions": [
    { "add": { "index": "products_v1", "alias": "products" } }
  ]
}

# Reindex
POST /_reindex
{
  "source": { "index": "products_old" },
  "dest": { "index": "products_new" }
}

# Delete index
DELETE /products
```

---

## Common Interview Questions

1. **What is the difference between `match` and `term` queries?**
   - `match`: Full-text search, analyzed
   - `term`: Exact match, not analyzed

2. **Explain shards and replicas**
   - Shards: Horizontal scaling (split data)
   - Replicas: Fault tolerance (copy data)

3. **How does Elasticsearch achieve near real-time search?**
   - In-memory indexing with periodic refresh (default 1s)

4. **What is inverted index?**
   - Maps terms to documents (like a book index)

5. **Difference between `should` and `must` in bool query?**
   - `must`: Required, affects scoring
   - `should`: Optional, boosts scoring

---

## Resources

### Official
- **elastic.co/docs**: Official documentation
- **elastic.co/training**: Free courses

### Tools
- **Kibana**: Visualization and management UI
- **Logstash**: Data ingestion pipeline
- **Beats**: Lightweight data shippers

### Practice
- Set up ELK stack locally
- Index real datasets (e.g., movie database)
- Build a search application

---

## Quick Reference

```bash
# Health check
GET /_cluster/health

# List indices
GET /_cat/indices?v

# Create index
PUT /myindex

# Index document
POST /myindex/_doc
{ "field": "value" }

# Search
GET /myindex/_search
{ "query": { "match_all": {} } }

# Update
POST /myindex/_update/1
{ "doc": { "field": "new_value" } }

# Delete
DELETE /myindex/_doc/1

# Delete index
DELETE /myindex
```

---

**💡 Pro Tip**: Start with simple queries (match_all, match, term) and gradually move to complex bool queries with aggregations. Use Kibana Dev Tools for interactive learning!

