# 🟢 Node.js Learning Path

Master Node.js from fundamentals to building production-ready backend applications!

---

## 📖 What is Node.js?

Node.js is a JavaScript runtime built on Chrome's V8 engine that allows you to run JavaScript on the server side.

### Why Node.js?

✅ **JavaScript Everywhere** - Use JS for frontend and backend  
✅ **Non-blocking I/O** - Handle thousands of concurrent connections  
✅ **NPM Ecosystem** - Millions of packages available  
✅ **Fast & Scalable** - Built for high-performance applications  
✅ **Active Community** - Huge support and resources  
✅ **Enterprise Ready** - Used by Netflix, Uber, PayPal, LinkedIn  

---

## 🗺️ Learning Path

### Phase 1: Beginner (2-3 weeks)
**Goal:** Understand Node.js fundamentals and build simple applications

**Topics:**
- Node.js basics and installation
- Modules and require system
- NPM and package.json
- File system operations
- Basic HTTP server
- Asynchronous JavaScript

**👉 Start:** [`01-beginner/README.md`](01-beginner/README.md)

---

### Phase 2: Intermediate (3-4 weeks)
**Goal:** Build REST APIs and work with databases

**Topics:**
- Express.js framework
- REST API design
- Middleware and routing
- MongoDB integration
- Authentication & JWT
- Error handling
- Environment variables

**👉 Continue:** [`02-intermediate/README.md`](02-intermediate/README.md)

---

### Phase 3: Advanced (3-4 weeks)
**Goal:** Build production-ready, scalable applications

**Topics:**
- Microservices architecture
- WebSockets and real-time features
- Testing (Jest, Mocha)
- Performance optimization
- Security best practices
- Docker deployment
- Logging and monitoring

**👉 Master:** [`03-advanced/README.md`](03-advanced/README.md)

---

## 🎯 Quick Start (30 Minutes)

### Install Node.js

```bash
# Download from: https://nodejs.org/
# Choose LTS version

# Verify installation
node -v
# Output: v20.x.x

npm -v
# Output: 10.x.x
```

### Your First Node.js Program

```javascript
// hello.js
console.log('Hello, Node.js!');
console.log('Node version:', process.version);
```

**Run it:**
```bash
node hello.js
```

### Your First HTTP Server

```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Node.js server!');
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

**Run it:**
```bash
node server.js
# Visit: http://localhost:3000
```

### Your First Express API

```bash
# Create project
mkdir my-first-api
cd my-first-api
npm init -y

# Install Express
npm install express

# Create app.js
```

```javascript
// app.js
const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.json({ message: 'Welcome to Node.js API!' });
});

app.get('/api/users', (req, res) => {
    const users = [
        { id: 1, name: 'John Doe' },
        { id: 2, name: 'Jane Smith' }
    ];
    res.json(users);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`API running on http://localhost:${PORT}`);
});
```

**Run it:**
```bash
node app.js
# Test: http://localhost:3000/api/users
```

✅ **You just created your first REST API!**

---

## 📚 Course Structure

### Week-by-Week Plan

**Week 1-2: Node.js Fundamentals**
- Day 1-2: Installation and basics
- Day 3-4: Modules and NPM
- Day 5-6: File system and async
- Day 7: First HTTP server project

**Week 3-4: Express.js & APIs**
- Day 8-9: Express basics
- Day 10-11: REST API design
- Day 12-13: Middleware and routing
- Day 14: CRUD API project

**Week 5-6: Databases**
- Day 15-16: MongoDB basics
- Day 17-18: Mongoose ODM
- Day 19-20: Authentication with JWT
- Day 21: Full-stack CRUD app

**Week 7-8: Advanced Topics**
- Day 22-23: WebSockets
- Day 24-25: Testing
- Day 26-27: Deployment
- Day 28: Final project

---

## 🎓 Learning Resources

### Official Documentation
- [Node.js Docs](https://nodejs.org/docs/)
- [NPM Docs](https://docs.npmjs.com/)
- [Express.js Guide](https://expressjs.com/)

### Recommended Books
- "Node.js Design Patterns" by Mario Casciaro
- "Learning Node.js" by Marc Wandschneider
- "Node.js 8 the Right Way" by Jim Wilson

### Online Courses
- [Node.js - The Complete Guide](https://www.udemy.com/course/nodejs-the-complete-guide/)
- [Complete Node.js Developer](https://www.udemy.com/course/complete-nodejs-developer-zero-to-mastery/)

---

## 🔧 Essential Tools

### Development Tools
- **VS Code** - Recommended editor
- **Postman** - API testing
- **MongoDB Compass** - Database GUI
- **Nodemon** - Auto-restart on changes

### NPM Packages (Must Know)
```bash
# Framework
npm install express

# Database
npm install mongoose mongodb

# Authentication
npm install jsonwebtoken bcrypt

# Environment variables
npm install dotenv

# Validation
npm install joi express-validator

# Logging
npm install morgan winston

# Testing
npm install --save-dev jest supertest mocha chai
```

---

## 🎯 Projects

### Beginner Projects
1. **File Manager** - CLI tool for file operations
2. **Todo API** - Simple CRUD API
3. **Weather App** - Fetch and display weather data
4. **URL Shortener** - Create short URLs

### Intermediate Projects
1. **Blog Platform** - Full REST API with auth
2. **E-commerce API** - Products, cart, orders
3. **Chat Application** - Real-time messaging
4. **Task Manager** - Project management API

### Advanced Projects
1. **Microservices** - Multiple services architecture
2. **Social Media API** - Complex relationships
3. **Video Streaming** - File upload and streaming
4. **Real-time Analytics** - WebSocket dashboard

**👉 See:** [`projects/`](projects/) folder

---

## 💡 Best Practices

### Code Structure
```
my-node-app/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── utils/
│   └── app.js
├── tests/
├── config/
├── .env
├── .gitignore
├── package.json
└── README.md
```

### Environment Variables
```javascript
// .env
PORT=3000
MONGODB_URI=mongodb://localhost:27017/mydb
JWT_SECRET=your-secret-key

// app.js
require('dotenv').config();
const port = process.env.PORT || 3000;
```

### Error Handling
```javascript
// Global error handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        error: 'Something went wrong!',
        message: err.message
    });
});
```

### Async/Await
```javascript
// Good practice
const getUser = async (id) => {
    try {
        const user = await User.findById(id);
        return user;
    } catch (error) {
        throw new Error('User not found');
    }
};
```

---

## 🏆 Career Outcomes

### Job Roles
- **Backend Developer** - $80K-$130K
- **Node.js Developer** - $85K-$140K
- **Full Stack Developer** - $90K-$150K
- **API Developer** - $85K-$135K

### Skills You'll Master
- REST API development
- Database integration
- Authentication & security
- Real-time applications
- Microservices architecture
- Testing and deployment

---

## ✅ Beginner Checklist

Before moving to intermediate:
- [ ] Installed Node.js and NPM
- [ ] Understand modules and require
- [ ] Can work with file system
- [ ] Built basic HTTP server
- [ ] Understand async/await
- [ ] Completed beginner projects

---

## 📞 Quick Links

| Topic | Link |
|-------|------|
| Beginner Guide | [01-beginner/README.md](01-beginner/README.md) |
| Intermediate Guide | [02-intermediate/README.md](02-intermediate/README.md) |
| Advanced Guide | [03-advanced/README.md](03-advanced/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |
| Projects | [projects/](projects/) |

---

## 🚀 Start Learning

**Ready to begin?**

👉 **[Start with Beginner Guide →](01-beginner/README.md)**

---

**Happy Coding with Node.js! 🟢**

