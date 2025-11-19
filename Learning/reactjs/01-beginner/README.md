# ⚛️ React.js Beginner Guide

Learn React from scratch and build your first interactive web applications!

---

## 📖 What is React?

React is a JavaScript library for building user interfaces. Instead of manipulating the DOM directly, you describe what your UI should look like, and React handles the updates efficiently.

### Key Concepts

- **Components** - Reusable UI pieces
- **JSX** - JavaScript + HTML syntax
- **Props** - Data passed to components
- **State** - Component's memory
- **Virtual DOM** - Fast rendering

---

## 🚀 Setup & Installation

### Prerequisites

```bash
# Check Node.js is installed
node -v  # Should be v14+

# Check NPM is installed
npm -v
```

### Create React App

```bash
# Create new React application
npx create-react-app my-app

# Navigate to directory
cd my-app

# Start development server
npm start

# App opens at http://localhost:3000
```

### Project Structure

```
my-app/
├── node_modules/          # Dependencies
├── public/
│   ├── index.html         # HTML template
│   └── favicon.ico
├── src/
│   ├── App.js             # Main component
│   ├── App.css            # Styles
│   ├── index.js           # Entry point
│   └── index.css
├── package.json           # Project config
└── README.md
```

---

## 📝 JSX - JavaScript XML

JSX lets you write HTML-like code in JavaScript:

```javascript
// JSX Example
const element = <h1>Hello, React!</h1>;

// Under the hood, it becomes:
const element = React.createElement('h1', null, 'Hello, React!');
```

### JSX Rules

```javascript
import React from 'react';

function JSXRules() {
  // 1. Return single parent element
  return (
    <div>
      <h1>Title</h1>
      <p>Paragraph</p>
    </div>
  );

  // 2. Use className instead of class
  return <div className="container">Content</div>;

  // 3. Close all tags
  return <img src="logo.png" alt="Logo" />;

  // 4. Use camelCase for attributes
  return <button onClick={handleClick}>Click Me</button>;

  // 5. Embed JavaScript with curly braces
  const name = "John";
  return <h1>Hello, {name}!</h1>;

  // 6. Conditional rendering
  return (
    <div>
      {isLoggedIn ? <p>Welcome!</p> : <p>Please log in</p>}
    </div>
  );
}
```

---

## 🧩 Components

### Functional Components

```javascript
// Simple component
function Welcome() {
  return <h1>Welcome to React!</h1>;
}

// Component with JSX
function Greeting() {
  const name = "Alice";
  const greeting = <h1>Hello, {name}!</h1>;
  return greeting;
}

// Component with logic
function CurrentTime() {
  const now = new Date().toLocaleTimeString();
  return (
    <div>
      <h2>Current Time</h2>
      <p>{now}</p>
    </div>
  );
}
```

### Using Components

```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import Greeting from './Greeting';

function App() {
  return (
    <div className="App">
      <Welcome />
      <Greeting />
      <Greeting />  {/* Can reuse! */}
    </div>
  );
}

export default App;
```

---

## 🎁 Props - Passing Data

Props allow you to pass data from parent to child components:

```javascript
// Child component receives props
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

// Parent component passes props
function App() {
  return (
    <div>
      <Welcome name="Alice" />
      <Welcome name="Bob" />
      <Welcome name="Charlie" />
    </div>
  );
}
```

### Destructuring Props

```javascript
// Instead of props.name, props.age
function UserCard({ name, age, email }) {
  return (
    <div className="user-card">
      <h2>{name}</h2>
      <p>Age: {age}</p>
      <p>Email: {email}</p>
    </div>
  );
}

// Usage
function App() {
  return (
    <UserCard 
      name="John Doe" 
      age={30} 
      email="john@example.com" 
    />
  );
}
```

### Props with Children

```javascript
// Button component
function Button({ children, onClick }) {
  return (
    <button onClick={onClick} className="custom-button">
      {children}
    </button>
  );
}

// Usage
function App() {
  return (
    <div>
      <Button onClick={() => alert('Clicked!')}>
        Click Me
      </Button>
      <Button onClick={() => console.log('Saved')}>
        💾 Save
      </Button>
    </div>
  );
}
```

---

## 🔄 State - Component Memory

State allows components to remember information:

```javascript
import React, { useState } from 'react';

function Counter() {
  // Declare state variable
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Count: {count}</h2>
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
```

### Multiple State Variables

```javascript
function UserForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ name, email, age });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input 
        type="email" 
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input 
        type="number" 
        value={age}
        onChange={(e) => setAge(e.target.value)}
        placeholder="Age"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### State with Objects

```javascript
function UserProfile() {
  const [user, setUser] = useState({
    name: 'John',
    age: 25,
    email: 'john@example.com'
  });

  const updateName = (newName) => {
    setUser(prevUser => ({
      ...prevUser,  // Keep other properties
      name: newName
    }));
  };

  return (
    <div>
      <p>Name: {user.name}</p>
      <p>Age: {user.age}</p>
      <p>Email: {user.email}</p>
      <button onClick={() => updateName('Jane')}>
        Change Name
      </button>
    </div>
  );
}
```

---

## 🎪 Event Handling

```javascript
function EventExamples() {
  const handleClick = () => {
    alert('Button clicked!');
  };

  const handleInput = (e) => {
    console.log('Input value:', e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();  // Prevent form submission
    console.log('Form submitted');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      console.log('Enter key pressed');
    }
  };

  return (
    <div>
      {/* Click event */}
      <button onClick={handleClick}>Click Me</button>

      {/* With inline arrow function */}
      <button onClick={() => console.log('Inline click')}>
        Inline
      </button>

      {/* With parameters */}
      <button onClick={() => handleClick('parameter')}>
        With Param
      </button>

      {/* Input event */}
      <input type="text" onChange={handleInput} />

      {/* Form submit */}
      <form onSubmit={handleSubmit}>
        <input type="text" onKeyPress={handleKeyPress} />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
```

---

## 📋 Lists and Keys

### Rendering Lists

```javascript
function UserList() {
  const users = [
    { id: 1, name: 'Alice', age: 25 },
    { id: 2, name: 'Bob', age: 30 },
    { id: 3, name: 'Charlie', age: 35 }
  ];

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.age} years old
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### Why Keys Matter

```javascript
// ❌ Bad: Using index as key (avoid if list can change)
{items.map((item, index) => (
  <li key={index}>{item}</li>
))}

// ✅ Good: Using unique ID
{items.map(item => (
  <li key={item.id}>{item.name}</li>
))}
```

---

## 📝 Forms and Controlled Components

### Controlled Input

```javascript
function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login:', { username, password });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Username:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button type="submit">Login</button>
    </form>
  );
}
```

### Multiple Inputs

```javascript
function RegistrationForm() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    country: 'USA'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Registration:', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="username"
        value={formData.username}
        onChange={handleChange}
        placeholder="Username"
      />
      <input
        name="email"
        type="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <input
        name="password"
        type="password"
        value={formData.password}
        onChange={handleChange}
        placeholder="Password"
      />
      <select name="country" value={formData.country} onChange={handleChange}>
        <option value="USA">USA</option>
        <option value="UK">UK</option>
        <option value="Canada">Canada</option>
      </select>
      <button type="submit">Register</button>
    </form>
  );
}
```

---

## 🎯 Complete Todo App Example

```javascript
import React, { useState } from 'react';
import './TodoApp.css';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  const addTodo = () => {
    if (input.trim()) {
      setTodos([
        ...todos,
        {
          id: Date.now(),
          text: input,
          completed: false
        }
      ]);
      setInput('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id 
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const getFilteredTodos = () => {
    switch(filter) {
      case 'active':
        return todos.filter(t => !t.completed);
      case 'completed':
        return todos.filter(t => t.completed);
      default:
        return todos;
    }
  };

  return (
    <div className="todo-app">
      <h1>📝 My Todo List</h1>
      
      <div className="add-todo">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          placeholder="What needs to be done?"
        />
        <button onClick={addTodo}>Add</button>
      </div>

      <div className="filters">
        <button onClick={() => setFilter('all')}>All ({todos.length})</button>
        <button onClick={() => setFilter('active')}>
          Active ({todos.filter(t => !t.completed).length})
        </button>
        <button onClick={() => setFilter('completed')}>
          Completed ({todos.filter(t => t.completed).length})
        </button>
      </div>

      <ul className="todo-list">
        {getFilteredTodos().map(todo => (
          <li key={todo.id} className={todo.completed ? 'completed' : ''}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => deleteTodo(todo.id)}>❌</button>
          </li>
        ))}
      </ul>

      {todos.length === 0 && (
        <p className="empty">No todos yet. Add one above!</p>
      )}
    </div>
  );
}

export default TodoApp;
```

---

## ✅ Beginner Checklist

- [ ] Created React app with create-react-app
- [ ] Understand JSX syntax
- [ ] Can create functional components
- [ ] Know how to pass props
- [ ] Understand useState hook
- [ ] Can handle events
- [ ] Can render lists with keys
- [ ] Built at least one form
- [ ] Created a complete Todo app

---

## 🎓 Practice Exercises

### Exercise 1: Profile Card
Create a component that displays user profile with name, avatar, bio, and social links.

### Exercise 2: Counter with Multiple Operations
Build a counter that can add, subtract, multiply, divide, and reset.

### Exercise 3: Shopping Cart
Create a shopping cart with add/remove items and total calculation.

### Exercise 4: Weather Display
Fetch weather data from an API and display it nicely.

---

## 🚀 Next Steps

Once you've mastered the basics:

1. **Practice** - Build more components and apps
2. **Learn Hooks** - useState, useEffect, custom hooks
3. **Routing** - React Router for multi-page apps
4. **API Integration** - Fetch data from backends

👉 **[Continue to Intermediate →](../02-intermediate/README.md)**

---

**Keep building! ⚛️**

