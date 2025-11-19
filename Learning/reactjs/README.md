# ⚛️ React.js Learning Path

Master React.js from fundamentals to building modern, production-ready web applications!

---

## 📖 What is React.js?

React is a JavaScript library for building user interfaces, created and maintained by Facebook (Meta). It's component-based, declarative, and makes building interactive UIs simple.

### Why React?

✅ **Component-Based** - Build encapsulated components  
✅ **Declarative** - Design simple views for each state  
✅ **Learn Once, Write Anywhere** - React Native for mobile  
✅ **Virtual DOM** - Fast and efficient rendering  
✅ **Huge Ecosystem** - Rich library of tools and packages  
✅ **Industry Standard** - Used by Facebook, Netflix, Airbnb, Instagram  

---

## 🗺️ Learning Path

### Phase 1: Beginner (2-3 weeks)
**Goal:** Understand React fundamentals and build simple apps

**Topics:**
- JSX syntax
- Components and Props
- State and lifecycle
- Event handling
- Lists and keys
- Forms and controlled components

**👉 Start:** [`01-beginner/README.md`](01-beginner/README.md)

---

### Phase 2: Intermediate (3-4 weeks)
**Goal:** Build complex, interactive applications

**Topics:**
- React Hooks (useState, useEffect, useContext)
- Custom hooks
- React Router
- API integration
- State management basics
- Styling solutions
- Form validation

**👉 Continue:** [`02-intermediate/README.md`](02-intermediate/README.md)

---

### Phase 3: Advanced (3-4 weeks)
**Goal:** Master advanced patterns and production deployment

**Topics:**
- Advanced hooks (useReducer, useMemo, useCallback)
- Context API and Redux
- Performance optimization
- TypeScript with React
- Testing (Jest, React Testing Library)
- Next.js (SSR/SSG)
- Deployment and CI/CD

**👉 Master:** [`03-advanced/README.md`](03-advanced/README.md)

---

## 🎯 Quick Start (30 Minutes)

### Prerequisites

```bash
# Node.js installed (v14 or higher)
node -v

# NPM installed
npm -v
```

### Create Your First React App

```bash
# Create new React app
npx create-react-app my-first-app

# Navigate to folder
cd my-first-app

# Start development server
npm start

# App opens at http://localhost:3000
```

### Your First Component

**src/App.js**
```javascript
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Hello, React! ⚛️</h1>
      <p>Welcome to your first React application!</p>
    </div>
  );
}

export default App;
```

### Component with State

```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
      <button onClick={() => setCount(0)}>
        Reset
      </button>
    </div>
  );
}

export default Counter;
```

### Interactive Todo App

```javascript
import React, { useState } from 'react';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
      setInput('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div style={{ padding: '20px', maxWidth: '500px', margin: '0 auto' }}>
      <h1>📝 Todo List</h1>
      
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          placeholder="Enter a todo..."
          style={{ padding: '10px', width: '70%' }}
        />
        <button onClick={addTodo} style={{ padding: '10px 20px', marginLeft: '10px' }}>
          Add
        </button>
      </div>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {todos.map(todo => (
          <li key={todo.id} style={{ marginBottom: '10px', padding: '10px', background: '#f0f0f0', borderRadius: '5px' }}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span style={{ 
              marginLeft: '10px', 
              textDecoration: todo.completed ? 'line-through' : 'none' 
            }}>
              {todo.text}
            </span>
            <button 
              onClick={() => deleteTodo(todo.id)}
              style={{ float: 'right', padding: '5px 10px', background: '#ff4444', color: 'white', border: 'none', borderRadius: '3px' }}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
```

✅ **You just built an interactive Todo app in React!**

---

## 📚 Course Structure

### Week-by-Week Plan

**Week 1-2: React Fundamentals**
- Day 1-2: Setup and JSX
- Day 3-4: Components and Props
- Day 5-6: State and events
- Day 7: First React app

**Week 3-4: Hooks & APIs**
- Day 8-9: useState and useEffect
- Day 10-11: API integration
- Day 12-13: React Router
- Day 14: Multi-page app

**Week 5-6: State Management**
- Day 15-16: Context API
- Day 17-18: useReducer
- Day 19-20: Redux basics
- Day 21: State management project

**Week 7-8: Advanced & Production**
- Day 22-23: Performance optimization
- Day 24-25: Testing
- Day 26-27: Deployment
- Day 28: Final project

---

## 🔧 Essential Tools & Libraries

### Must-Have Tools
```bash
# React Dev Tools (Browser extension)
# Available for Chrome and Firefox

# VS Code Extensions:
# - ES7+ React/Redux/React-Native snippets
# - Prettier - Code formatter
# - ESLint
```

### Popular React Libraries

```bash
# Routing
npm install react-router-dom

# HTTP Client
npm install axios

# UI Components
npm install @mui/material @emotion/react @emotion/styled

# Forms
npm install react-hook-form

# State Management
npm install redux react-redux @reduxjs/toolkit

# Icons
npm install react-icons

# Charts
npm install recharts

# Dates
npm install date-fns
```

---

## 🎯 Projects

### Beginner Projects
1. **Counter App** - State management basics
2. **Todo List** - CRUD operations
3. **Weather App** - API integration
4. **Calculator** - Complex state logic

### Intermediate Projects
1. **Movie Search** - API + routing
2. **E-commerce Store** - Context + routing
3. **Blog Platform** - Full CRUD with backend
4. **Social Media Feed** - Real-time updates

### Advanced Projects
1. **Dashboard** - Complex data visualization
2. **Chat Application** - WebSocket integration
3. **Video Platform** - Advanced media handling
4. **Full Stack App** - React + Node.js + MongoDB

**👉 See:** [`projects/`](projects/) folder

---

## 💡 React Best Practices

### Component Structure

```javascript
// Good: Functional component with clear structure
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function UserCard({ user, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    // Effect logic
  }, [user]);

  const handleSave = () => {
    onUpdate(user);
    setIsEditing(false);
  };

  return (
    <div className="user-card">
      {isEditing ? (
        // Edit mode
        <EditForm user={user} onSave={handleSave} />
      ) : (
        // View mode
        <UserInfo user={user} onEdit={() => setIsEditing(true)} />
      )}
    </div>
  );
}

UserCard.propTypes = {
  user: PropTypes.object.isRequired,
  onUpdate: PropTypes.func.isRequired
};

export default UserCard;
```

### Folder Structure

```
src/
├── components/
│   ├── common/
│   │   ├── Button.jsx
│   │   └── Input.jsx
│   ├── layout/
│   │   ├── Header.jsx
│   │   └── Footer.jsx
│   └── features/
│       └── UserProfile.jsx
├── pages/
│   ├── Home.jsx
│   ├── About.jsx
│   └── Dashboard.jsx
├── hooks/
│   └── useAuth.js
├── context/
│   └── AuthContext.js
├── services/
│   └── api.js
├── utils/
│   └── helpers.js
├── styles/
│   └── global.css
├── App.js
└── index.js
```

### State Management Patterns

```javascript
// Simple state
const [count, setCount] = useState(0);

// Object state
const [user, setUser] = useState({ name: '', email: '' });

// Update object state correctly
setUser(prev => ({ ...prev, name: 'John' }));

// Array state
const [items, setItems] = useState([]);

// Add to array
setItems(prev => [...prev, newItem]);

// Remove from array
setItems(prev => prev.filter(item => item.id !== id));
```

---

## 🏆 Career Outcomes

### Job Roles
- **Frontend Developer** - $75K-$120K
- **React Developer** - $80K-$130K
- **Full Stack Developer** - $90K-$150K
- **UI/UX Engineer** - $85K-$135K

### Skills You'll Master
- Modern JavaScript (ES6+)
- Component-based architecture
- State management
- API integration
- Responsive design
- Testing and debugging
- Production deployment

---

## ✅ Beginner Checklist

Before moving to intermediate:
- [ ] Set up React development environment
- [ ] Understand JSX syntax
- [ ] Can create functional components
- [ ] Understand props and state
- [ ] Handle events and forms
- [ ] Built at least 2 projects
- [ ] Know how to debug React apps

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

## 🎓 Learning Resources

### Official Documentation
- [React Docs](https://react.dev/)
- [React Tutorial](https://react.dev/learn)
- [React Patterns](https://reactpatterns.com/)

### Recommended Courses
- [React - The Complete Guide](https://www.udemy.com/course/react-the-complete-guide/)
- [Epic React](https://epicreact.dev/)
- [Full Stack Open](https://fullstackopen.com/)

### Books
- "Learning React" by Alex Banks & Eve Porcello
- "React Quickly" by Azat Mardan
- "Fullstack React" by Anthony Accomazzo

---

## 🚀 Start Learning

**Ready to begin your React journey?**

👉 **[Start with Beginner Guide →](01-beginner/README.md)**

---

**Happy Coding with React! ⚛️**

