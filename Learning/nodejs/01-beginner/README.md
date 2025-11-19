# 🟢 Node.js Beginner Guide

Learn Node.js fundamentals and build your first backend applications!

---

## 📖 Introduction to Node.js

Node.js allows you to run JavaScript outside the browser, making it perfect for building backend applications, APIs, and command-line tools.

### Key Features

- **JavaScript Runtime** - Run JS on the server
- **Event-Driven** - Non-blocking I/O operations
- **Single-Threaded** - But handles concurrency efficiently
- **NPM** - World's largest package registry
- **Cross-Platform** - Works on Windows, Mac, Linux

---

## 🚀 Getting Started

### Installation

**Download & Install:**
1. Visit [nodejs.org](https://nodejs.org/)
2. Download LTS (Long Term Support) version
3. Run installer with default settings

**Verify Installation:**
```bash
node -v
# Output: v20.10.0 (or similar)

npm -v
# Output: 10.2.3 (or similar)
```

---

## 📝 Your First Node.js Program

### Hello World

```javascript
// hello.js
console.log('Hello, World!');
console.log('Welcome to Node.js!');
```

**Run it:**
```bash
node hello.js
```

### Working with Variables

```javascript
// variables.js
const name = 'John';
let age = 25;
const isStudent = true;

console.log(`Name: ${name}`);
console.log(`Age: ${age}`);
console.log(`Is Student: ${isStudent}`);

// Node.js global objects
console.log('Current directory:', __dirname);
console.log('Current file:', __filename);
console.log('Node version:', process.version);
console.log('Platform:', process.platform);
```

---

## 📦 Node.js Modules

### Built-in Modules

Node.js comes with many built-in modules:

#### 1. File System (fs)

```javascript
// file-operations.js
const fs = require('fs');

// Write to file (synchronous)
fs.writeFileSync('hello.txt', 'Hello from Node.js!');
console.log('File created!');

// Read from file (synchronous)
const data = fs.readFileSync('hello.txt', 'utf8');
console.log('File content:', data);

// Write to file (asynchronous - better!)
fs.writeFile('async.txt', 'Async write!', (err) => {
    if (err) throw err;
    console.log('Async file created!');
});

// Read from file (asynchronous)
fs.readFile('async.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log('Async file content:', data);
});
```

#### 2. Path Module

```javascript
// path-demo.js
const path = require('path');

const filePath = '/users/john/documents/file.txt';

console.log('Directory name:', path.dirname(filePath));
console.log('Base name:', path.basename(filePath));
console.log('Extension:', path.extname(filePath));

// Join paths
const newPath = path.join('/users', 'john', 'documents', 'newfile.txt');
console.log('Joined path:', newPath);

// Resolve path
const absolutePath = path.resolve('documents', 'file.txt');
console.log('Absolute path:', absolutePath);
```

#### 3. OS Module

```javascript
// os-info.js
const os = require('os');

console.log('Platform:', os.platform());
console.log('Architecture:', os.arch());
console.log('CPUs:', os.cpus().length);
console.log('Free memory:', os.freemem() / 1024 / 1024 / 1024, 'GB');
console.log('Total memory:', os.totalmem() / 1024 / 1024 / 1024, 'GB');
console.log('Home directory:', os.homedir());
console.log('Username:', os.userInfo().username);
```

---

## 🔧 Creating Custom Modules

### Exporting and Importing

**math.js** (Custom module)
```javascript
// math.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;
const divide = (a, b) => a / b;

// Export single function
module.exports.add = add;

// Export multiple
module.exports = {
    add,
    subtract,
    multiply,
    divide
};
```

**app.js** (Using the module)
```javascript
// app.js
const math = require('./math');

console.log('Add:', math.add(10, 5));        // 15
console.log('Subtract:', math.subtract(10, 5)); // 5
console.log('Multiply:', math.multiply(10, 5)); // 50
console.log('Divide:', math.divide(10, 5));   // 2
```

---

## 🌐 Creating an HTTP Server

### Basic HTTP Server

```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    // Set response header
    res.writeHead(200, { 'Content-Type': 'text/html' });
    
    // Send response
    res.write('<h1>Hello from Node.js Server!</h1>');
    res.write('<p>This is my first web server</p>');
    res.end();
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Server with Routing

```javascript
// server-routing.js
const http = require('http');

const server = http.createServer((req, res) => {
    const url = req.url;
    
    if (url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<h1>Home Page</h1>');
        res.end();
    } else if (url === '/about') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<h1>About Page</h1>');
        res.end();
    } else if (url === '/api/users') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        const users = [
            { id: 1, name: 'John' },
            { id: 2, name: 'Jane' }
        ];
        res.end(JSON.stringify(users));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.write('<h1>404 - Page Not Found</h1>');
        res.end();
    }
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

## 🎯 NPM (Node Package Manager)

### Understanding package.json

```bash
# Create package.json
npm init

# Create with defaults
npm init -y
```

**package.json**
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My Node.js application",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "keywords": ["node", "api"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {}
}
```

### Installing Packages

```bash
# Install package (saves to dependencies)
npm install express

# Install as dev dependency
npm install --save-dev nodemon

# Install globally
npm install -g nodemon

# Install specific version
npm install express@4.18.0

# Install all dependencies
npm install

# Uninstall package
npm uninstall express
```

### Useful Packages for Beginners

```bash
# Nodemon - Auto-restart on file changes
npm install --save-dev nodemon

# Dotenv - Environment variables
npm install dotenv

# Colors - Colorful console output
npm install colors

# Moment - Date/time manipulation
npm install moment

# Axios - HTTP client
npm install axios
```

---

## ⚡ Asynchronous JavaScript

### Callbacks

```javascript
// callback-example.js
const fs = require('fs');

console.log('1. Starting...');

fs.readFile('data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log('2. File content:', data);
});

console.log('3. Continuing...');

// Output:
// 1. Starting...
// 3. Continuing...
// 2. File content: [file data]
```

### Promises

```javascript
// promise-example.js
const fs = require('fs').promises;

console.log('1. Starting...');

fs.readFile('data.txt', 'utf8')
    .then(data => {
        console.log('2. File content:', data);
        return fs.writeFile('output.txt', data.toUpperCase());
    })
    .then(() => {
        console.log('3. Output file created!');
    })
    .catch(err => {
        console.error('Error:', err);
    });

console.log('4. Continuing...');
```

### Async/Await (Modern Way)

```javascript
// async-await-example.js
const fs = require('fs').promises;

async function readAndProcess() {
    try {
        console.log('1. Starting...');
        
        // Read file
        const data = await fs.readFile('data.txt', 'utf8');
        console.log('2. File content:', data);
        
        // Process and write
        const processed = data.toUpperCase();
        await fs.writeFile('output.txt', processed);
        console.log('3. Output file created!');
        
    } catch (err) {
        console.error('Error:', err);
    }
}

readAndProcess();
console.log('4. Function called...');
```

---

## 🎯 Hands-On Exercises

### Exercise 1: File Manager

Create a simple file manager CLI:

```javascript
// file-manager.js
const fs = require('fs');
const path = require('path');

class FileManager {
    createFile(filename, content) {
        fs.writeFileSync(filename, content);
        console.log(`✅ File '${filename}' created`);
    }
    
    readFile(filename) {
        try {
            const content = fs.readFileSync(filename, 'utf8');
            console.log(`📄 Content of '${filename}':`);
            console.log(content);
        } catch (err) {
            console.log(`❌ Error reading file: ${err.message}`);
        }
    }
    
    deleteFile(filename) {
        try {
            fs.unlinkSync(filename);
            console.log(`🗑️  File '${filename}' deleted`);
        } catch (err) {
            console.log(`❌ Error deleting file: ${err.message}`);
        }
    }
    
    listFiles() {
        const files = fs.readdirSync('.');
        console.log('📁 Files in current directory:');
        files.forEach(file => console.log(`  - ${file}`));
    }
}

// Usage
const fm = new FileManager();
fm.createFile('test.txt', 'Hello, File Manager!');
fm.readFile('test.txt');
fm.listFiles();
// fm.deleteFile('test.txt');
```

### Exercise 2: Simple Web Server

Create a web server with multiple routes:

```javascript
// web-server.js
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>Welcome Home!</h1><a href="/about">About</a>');
    } 
    else if (req.url === '/about') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>About Us</h1><a href="/">Home</a>');
    }
    else if (req.url === '/api/time') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
            time: new Date().toLocaleTimeString(),
            date: new Date().toLocaleDateString()
        }));
    }
    else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 - Not Found</h1>');
    }
});

server.listen(3000, () => {
    console.log('Server running: http://localhost:3000');
});
```

### Exercise 3: Data Processor

Read, process, and save data:

```javascript
// data-processor.js
const fs = require('fs').promises;

async function processData() {
    try {
        // Read data
        const data = await fs.readFile('students.json', 'utf8');
        const students = JSON.parse(data);
        
        // Process data
        const passed = students.filter(s => s.grade >= 60);
        const failed = students.filter(s => s.grade < 60);
        
        const results = {
            total: students.length,
            passed: passed.length,
            failed: failed.length,
            passRate: (passed.length / students.length * 100).toFixed(2) + '%',
            students: {
                passed,
                failed
            }
        };
        
        // Save results
        await fs.writeFile('results.json', JSON.stringify(results, null, 2));
        console.log('✅ Results saved to results.json');
        console.log(`Pass rate: ${results.passRate}`);
        
    } catch (err) {
        console.error('❌ Error:', err.message);
    }
}

processData();
```

---

## 🎓 Practice Projects

### Project 1: Todo List CLI

Build a command-line todo list application:
- Add todos
- List todos
- Mark as complete
- Delete todos
- Save to file

### Project 2: Weather App

Fetch weather data from an API:
- Use Axios or node-fetch
- Get weather for a city
- Display formatted output
- Handle errors

### Project 3: File Watcher

Monitor a directory for changes:
- Watch for new files
- Log file changes
- Auto-backup files
- Send notifications

---

## ✅ Beginner Checklist

- [ ] Installed Node.js and NPM
- [ ] Ran first JavaScript file
- [ ] Used built-in modules (fs, path, os)
- [ ] Created custom modules
- [ ] Built an HTTP server
- [ ] Understand package.json
- [ ] Installed NPM packages
- [ ] Understand async/await
- [ ] Completed at least 2 projects

---

## 🚀 Next Steps

Once you've mastered the basics:

1. **Practice** - Build more small projects
2. **Learn Express** - Move to intermediate guide
3. **Database** - Learn MongoDB
4. **Build APIs** - Create RESTful services

👉 **[Continue to Intermediate →](../02-intermediate/README.md)**

---

**Keep coding! 🟢**

