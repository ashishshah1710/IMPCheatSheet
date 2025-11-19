# 🟢 Node.js Cheat Sheet

Quick reference for Node.js commands, modules, and patterns.

---

## 🚀 Basic Commands

```bash
# Run JavaScript file
node app.js

# Run with nodemon (auto-restart)
nodemon app.js

# Node REPL
node

# Check version
node -v
npm -v

# Get help
node --help
```

---

## 📦 NPM Commands

```bash
# Initialize project
npm init
npm init -y  # Skip questions

# Install packages
npm install package-name
npm i package-name  # Short form
npm install --save-dev package-name  # Dev dependency
npm install -g package-name  # Global install

# Install from package.json
npm install

# Uninstall
npm uninstall package-name

# Update
npm update
npm update package-name

# List installed
npm list
npm list -g  # Global packages

# Run scripts
npm start
npm test
npm run scriptname

# Check outdated
npm outdated
```

---

## 📝 Common Modules

### File System (fs)

```javascript
const fs = require('fs');

// Read file (sync)
const data = fs.readFileSync('file.txt', 'utf8');

// Write file (sync)
fs.writeFileSync('file.txt', 'Hello World');

// Read file (async)
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Write file (async)
fs.writeFile('file.txt', 'Hello', (err) => {
  if (err) throw err;
});

// Promises API
const fsPromises = require('fs').promises;
const data = await fsPromises.readFile('file.txt', 'utf8');

// Check if exists
fs.existsSync('file.txt');

// Delete file
fs.unlinkSync('file.txt');

// Create directory
fs.mkdirSync('newdir');

// Read directory
fs.readdirSync('.');
```

### Path

```javascript
const path = require('path');

path.join('/users', 'john', 'file.txt');
path.resolve('file.txt');
path.dirname('/users/john/file.txt');  // /users/john
path.basename('/users/john/file.txt'); // file.txt
path.extname('file.txt');               // .txt
```

### HTTP

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Hello</h1>');
});

server.listen(3000);
```

### OS

```javascript
const os = require('os');

os.platform();     // Platform
os.arch();         // Architecture
os.cpus();         // CPU info
os.freemem();      // Free memory
os.totalmem();     // Total memory
os.homedir();      // Home directory
os.userInfo();     // User info
```

---

## 🔧 Express.js

### Setup

```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Start server
app.listen(3000, () => console.log('Server running'));
```

### Routes

```javascript
// GET
app.get('/', (req, res) => {
  res.send('Hello');
});

// POST
app.post('/api/users', (req, res) => {
  res.json(req.body);
});

// PUT
app.put('/api/users/:id', (req, res) => {
  res.json({ id: req.params.id });
});

// DELETE
app.delete('/api/users/:id', (req, res) => {
  res.status(204).send();
});

// Route parameters
app.get('/users/:id', (req, res) => {
  const id = req.params.id;
});

// Query parameters
app.get('/search', (req, res) => {
  const query = req.query.q;
});
```

### Middleware

```javascript
// Custom middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Error!');
});

// Route-specific middleware
app.get('/protected', authMiddleware, (req, res) => {
  res.send('Protected');
});
```

---

## 🗄️ MongoDB (Mongoose)

```javascript
const mongoose = require('mongoose');

// Connect
mongoose.connect('mongodb://localhost/mydb');

// Schema
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  age: Number,
  createdAt: { type: Date, default: Date.now }
});

// Model
const User = mongoose.model('User', userSchema);

// Create
const user = new User({ name: 'John', email: 'john@example.com' });
await user.save();

// Find
const users = await User.find();
const user = await User.findById(id);
const user = await User.findOne({ email: 'john@example.com' });

// Update
await User.findByIdAndUpdate(id, { name: 'Jane' });
await User.updateOne({ _id: id }, { name: 'Jane' });

// Delete
await User.findByIdAndDelete(id);
await User.deleteOne({ _id: id });
```

---

## 🔐 Authentication (JWT)

```javascript
const jwt = require('jsonwebtoken');

// Generate token
const token = jwt.sign(
  { userId: user._id },
  'your-secret-key',
  { expiresIn: '1h' }
);

// Verify token
try {
  const decoded = jwt.verify(token, 'your-secret-key');
  console.log(decoded.userId);
} catch (err) {
  console.log('Invalid token');
}

// Middleware
const auth = (req, res, next) => {
  const token = req.header('Authorization').replace('Bearer ', '');
  try {
    const decoded = jwt.verify(token, 'secret');
    req.userId = decoded.userId;
    next();
  } catch (err) {
    res.status(401).send('Please authenticate');
  }
};
```

---

## ⚡ Async Patterns

### Callbacks

```javascript
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```

### Promises

```javascript
const readFile = (path) => {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
};

readFile('file.txt')
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### Async/Await

```javascript
async function readAndProcess() {
  try {
    const data = await fsPromises.readFile('file.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

---

## 🌍 Environment Variables

```javascript
// Using dotenv
require('dotenv').config();

const PORT = process.env.PORT || 3000;
const DB_URL = process.env.DATABASE_URL;
const SECRET = process.env.JWT_SECRET;

// .env file
PORT=3000
DATABASE_URL=mongodb://localhost/mydb
JWT_SECRET=your-secret-key
```

---

## 🔍 Debugging

```javascript
// Console methods
console.log('Info');
console.error('Error');
console.warn('Warning');
console.table([{name: 'John', age: 30}]);
console.time('timer');
console.timeEnd('timer');

// Debug module
const debug = require('debug')('app');
debug('Debug message');

// Inspector
node inspect app.js
node --inspect app.js
```

---

## 📨 Common Packages

```javascript
// Axios - HTTP client
const axios = require('axios');
const response = await axios.get('https://api.example.com/data');

// Morgan - HTTP logger
const morgan = require('morgan');
app.use(morgan('dev'));

// Cors - Enable CORS
const cors = require('cors');
app.use(cors());

// Bcrypt - Password hashing
const bcrypt = require('bcrypt');
const hash = await bcrypt.hash(password, 10);
const isMatch = await bcrypt.compare(password, hash);

// Joi - Validation
const Joi = require('joi');
const schema = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required()
});

// Multer - File upload
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });
app.post('/upload', upload.single('file'), (req, res) => {
  console.log(req.file);
});
```

---

## 🧪 Testing (Jest)

```javascript
// test.js
const sum = (a, b) => a + b;

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

// Async testing
test('fetches user', async () => {
  const user = await getUser(1);
  expect(user.name).toBe('John');
});

// Run tests
npm test
```

---

## 📊 Useful Patterns

### Error Handling Wrapper

```javascript
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/users', asyncHandler(async (req, res) => {
  const users = await User.find();
  res.json(users);
}));
```

### API Response Format

```javascript
const sendResponse = (res, statusCode, data, message) => {
  res.status(statusCode).json({
    success: statusCode < 400,
    message,
    data
  });
};

sendResponse(res, 200, users, 'Users fetched successfully');
```

### Environment Check

```javascript
const isDev = process.env.NODE_ENV === 'development';
const isProd = process.env.NODE_ENV === 'production';

if (isDev) {
  app.use(morgan('dev'));
}
```

---

## 🚀 Quick Start Template

```javascript
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'API Running' });
});

// Database
mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB error:', err));

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

**Happy Node.js coding! 🟢**

