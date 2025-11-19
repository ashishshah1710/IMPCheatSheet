# 🐍 Python Programming

## Overview
Python is a versatile, beginner-friendly language widely used in web development, data science, automation, and more. Essential for modern software engineering.

---

## Why Learn Python?

### ✅ Benefits
- **Easy to learn**: Clear, readable syntax
- **Versatile**: Web, data science, ML, automation
- **In-demand**: Top language in job market
- **Large ecosystem**: Millions of packages (PyPI)
- **Great for interviews**: Concise code

### 📊 Use Cases
- **Web Development**: Django, Flask
- **Data Science**: Pandas, NumPy, Matplotlib
- **Machine Learning**: TensorFlow, PyTorch, scikit-learn
- **Automation**: Scripting, testing, DevOps
- **APIs**: REST, FastAPI

---

## Getting Started

### Installation
```bash
# Check if installed
python --version

# Install Python 3.11+
# Windows: Download from python.org
# Mac: brew install python
# Linux: sudo apt install python3
```

### Hello World
```python
# hello.py
print("Hello, World!")

# Run
python hello.py
```

---

## Core Python

### 1. **Variables & Data Types**
```python
# Numbers
age = 25
price = 99.99
is_active = True

# Strings
name = "John Doe"
message = f"Hello, {name}!"  # f-strings

# Lists (mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")

# Tuples (immutable)
coordinates = (10, 20)

# Dictionaries
user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Sets (unique values)
tags = {"python", "java", "javascript"}
```

### 2. **Control Flow**
```python
# If-else
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# For loop
for fruit in fruits:
    print(fruit)

for i in range(5):  # 0 to 4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```

### 3. **Functions**
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# *args, **kwargs
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda (anonymous functions)
square = lambda x: x ** 2
add = lambda x, y: x + y

# Decorators
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### 4. **Object-Oriented Programming**
```python
class User:
    # Class variable
    count = 0
    
    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.count += 1
    
    # Instance method
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # Class method
    @classmethod
    def get_count(cls):
        return cls.count
    
    # Static method
    @staticmethod
    def is_valid_email(email):
        return "@" in email
    
    # String representation
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

# Inheritance
class Admin(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def delete_user(self, user):
        print(f"{self.name} deleted {user.name}")
```

---

## Web Development with Python

### Flask (Microframework)
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI (Modern, Fast)
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

users: List[User] = []

@app.get("/api/users")
async def get_users():
    return users

@app.post("/api/users", status_code=201)
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    if 0 <= user_id < len(users):
        return users[user_id]
    raise HTTPException(status_code=404, detail="User not found")

# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
```

### Django (Full-stack Framework)
```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import User

@require_http_methods(["GET"])
def get_users(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.get_users),
]
```

---

## Data Science Basics

### NumPy (Numerical Computing)
```python
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Operations
print(arr * 2)  # [2, 4, 6, 8, 10]
print(arr.mean())  # 3.0
print(matrix.shape)  # (3, 2)

# Slicing
print(arr[1:4])  # [2, 3, 4]
```

### Pandas (Data Analysis)
```python
import pandas as pd

# DataFrame
data = {
    'name': ['John', 'Jane', 'Bob'],
    'age': [25, 30, 35],
    'city': ['NY', 'LA', 'Chicago']
}
df = pd.DataFrame(data)

# Operations
print(df.head())
print(df.describe())
print(df[df['age'] > 25])  # Filter
print(df.groupby('city')['age'].mean())  # Group by

# Read/Write CSV
df.to_csv('users.csv', index=False)
df = pd.read_csv('users.csv')
```

---

## Common Python Libraries

### File I/O
```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()
    lines = f.readlines()

# Write file
with open('output.txt', 'w') as f:
    f.write("Hello, World!")

# JSON
import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### Requests (HTTP Client)
```python
import requests

# GET request
response = requests.get('https://api.example.com/users')
users = response.json()

# POST request
new_user = {"name": "John", "email": "john@example.com"}
response = requests.post('https://api.example.com/users', json=new_user)

# With headers and authentication
headers = {"Authorization": "Bearer token123"}
response = requests.get('https://api.example.com/protected', headers=headers)
```

### Date/Time
```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Arithmetic
tomorrow = now + timedelta(days=1)
week_ago = now - timedelta(weeks=1)

# Parsing
date = datetime.strptime("2024-01-15", "%Y-%m-%d")
```

---

## Testing

### unittest
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_add_strings(self):
        with self.assertRaises(TypeError):
            add("2", 3)

if __name__ == '__main__':
    unittest.main()
```

### pytest (Popular)
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

# Run: pytest test_math.py
```

---

## Virtual Environments

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install packages
pip install requests flask pandas

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

---

## Common Interview Questions

### Easy
1. Reverse a string
2. Check if palindrome
3. Find duplicates in list
4. Fibonacci sequence
5. FizzBuzz

### Medium
6. Two Sum
7. Merge intervals
8. Group anagrams
9. Implement LRU Cache
10. Binary search

### Python-Specific
11. What is the difference between list and tuple?
12. Explain decorators
13. What is `*args` and `**kwargs`?
14. Difference between `==` and `is`
15. What is a generator?

---

## Best Practices

✅ Follow PEP 8 (style guide)  
✅ Use virtual environments  
✅ Write docstrings  
✅ Use type hints (Python 3.5+)  
✅ Handle exceptions properly  
✅ Use list comprehensions (when readable)  
✅ Use `with` for file operations  

```python
# Type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

from typing import List, Dict, Optional

def process_users(users: List[Dict[str, str]]) -> Optional[int]:
    if not users:
        return None
    return len(users)
```

---

## Resources

### Books
- **"Python Crash Course"** by Eric Matthes
- **"Fluent Python"** by Luciano Ramalho
- **"Automate the Boring Stuff with Python"** by Al Sweigart

### Online
- **python.org**: Official docs
- **Real Python**: Tutorials
- **Python Weekly**: Newsletter

### Practice
- **LeetCode**: Python tag
- **HackerRank**: Python track
- **Codewars**: Python katas

---

## Project Ideas

1. **Web Scraper**: BeautifulSoup + Requests
2. **REST API**: Flask/FastAPI + SQLAlchemy
3. **Data Dashboard**: Streamlit + Pandas
4. **Automation Script**: File processing, email automation
5. **CLI Tool**: Click/Argparse

---

## Next Steps

- Build a project with Flask/FastAPI
- Learn Django for full-stack
- Explore data science with Pandas
- Practice algorithms in Python
- Contribute to open source

---

**💡 Pro Tip**: Python is excellent for rapid prototyping and interviews. Master the basics, then specialize in web dev or data science based on your interests!

