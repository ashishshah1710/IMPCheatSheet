# ⚛️ React.js Cheat Sheet

Quick reference for React components, hooks, and patterns.

---

## 🚀 Setup

```bash
# Create new app
npx create-react-app my-app
cd my-app
npm start

# With TypeScript
npx create-react-app my-app --template typescript

# Vite (faster alternative)
npm create vite@latest my-app -- --template react
```

---

## 🧩 Components

### Functional Component

```javascript
// Basic component
function Welcome() {
  return <h1>Hello!</h1>;
}

// With props
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Arrow function
const Button = ({ text, onClick }) => {
  return <button onClick={onClick}>{text}</button>;
};

// Export
export default Welcome;
```

---

## 📝 JSX

```javascript
// Basic JSX
const element = <h1>Hello</h1>;

// Expressions
const name = 'John';
const element = <h1>Hello, {name}!</h1>;

// Attributes
<img src={url} alt="Description" />
<button className="btn" onClick={handleClick}>Click</button>

// Inline styles
<div style={{ color: 'red', fontSize: '20px' }}>Text</div>

// Conditional rendering
{isLoggedIn ? <Dashboard /> : <Login />}
{isVisible && <Component />}

// Lists
{items.map(item => <li key={item.id}>{item.name}</li>)}

// Fragments
<>
  <h1>Title</h1>
  <p>Paragraph</p>
</>
```

---

## 🎣 Hooks

### useState

```javascript
import { useState } from 'react';

// Basic usage
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const [isActive, setIsActive] = useState(false);

// Update state
setCount(count + 1);
setCount(prev => prev + 1);  // Functional update

// Object state
const [user, setUser] = useState({ name: '', email: '' });
setUser(prev => ({ ...prev, name: 'John' }));

// Array state
const [items, setItems] = useState([]);
setItems(prev => [...prev, newItem]);
setItems(prev => prev.filter(item => item.id !== id));
```

### useEffect

```javascript
import { useEffect } from 'react';

// Run on every render
useEffect(() => {
  console.log('Component rendered');
});

// Run once (on mount)
useEffect(() => {
  console.log('Component mounted');
}, []);

// Run when dependency changes
useEffect(() => {
  console.log('Count changed:', count);
}, [count]);

// Cleanup
useEffect(() => {
  const timer = setTimeout(() => console.log('Timer'), 1000);
  return () => clearTimeout(timer);  // Cleanup
}, []);

// Fetch data
useEffect(() => {
  const fetchData = async () => {
    const response = await fetch('/api/data');
    const data = await response.json();
    setData(data);
  };
  fetchData();
}, []);
```

### useContext

```javascript
import { createContext, useContext } from 'react';

// Create context
const ThemeContext = createContext('light');

// Provider
function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

// Consumer
function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Button</button>;
}
```

### useRef

```javascript
import { useRef } from 'react';

// DOM reference
const inputRef = useRef(null);

const focusInput = () => {
  inputRef.current.focus();
};

return <input ref={inputRef} />;

// Mutable value (persists across renders)
const countRef = useRef(0);
countRef.current += 1;
```

### useReducer

```javascript
import { useReducer } from 'react';

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  
  return (
    <>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </>
  );
}
```

### useMemo

```javascript
import { useMemo } from 'react';

// Memoize expensive calculation
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(a, b);
}, [a, b]);

// Memoize filtered list
const filteredList = useMemo(() => {
  return items.filter(item => item.active);
}, [items]);
```

### useCallback

```javascript
import { useCallback } from 'react';

// Memoize function
const handleClick = useCallback(() => {
  console.log('Clicked', count);
}, [count]);

// Pass to child to prevent re-renders
<ChildComponent onClick={handleClick} />
```

---

## 🎨 Event Handling

```javascript
// Click
<button onClick={handleClick}>Click</button>
<button onClick={() => handleClick(id)}>Click with param</button>

// Form
<form onSubmit={handleSubmit}>
  <input onChange={handleChange} />
</form>

// Input
<input 
  value={text} 
  onChange={(e) => setText(e.target.value)}
/>

// Keyboard
<input onKeyDown={handleKeyDown} />
<input onKeyPress={(e) => e.key === 'Enter' && handleSubmit()} />

// Mouse
<div 
  onMouseEnter={handleMouseEnter}
  onMouseLeave={handleMouseLeave}
/>

// Prevent default
const handleSubmit = (e) => {
  e.preventDefault();
  // Your code
};
```

---

## 📋 Forms

### Controlled Components

```javascript
function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ name, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Multiple Inputs

```javascript
const [formData, setFormData] = useState({
  name: '',
  email: '',
  password: ''
});

const handleChange = (e) => {
  const { name, value } = e.target;
  setFormData(prev => ({
    ...prev,
    [name]: value
  }));
};

<input name="name" value={formData.name} onChange={handleChange} />
<input name="email" value={formData.email} onChange={handleChange} />
```

---

## 🎨 Styling

### Inline Styles

```javascript
<div style={{ color: 'red', fontSize: '20px' }}>Text</div>

const styles = {
  container: {
    padding: '20px',
    backgroundColor: '#f0f0f0'
  }
};

<div style={styles.container}>Content</div>
```

### CSS Modules

```javascript
// Component.module.css
.container {
  padding: 20px;
}

// Component.jsx
import styles from './Component.module.css';
<div className={styles.container}>Content</div>
```

### Styled Components

```javascript
import styled from 'styled-components';

const Button = styled.button`
  background: blue;
  color: white;
  padding: 10px 20px;
  &:hover {
    background: darkblue;
  }
`;

<Button>Click Me</Button>
```

---

## 🧭 React Router

```javascript
import { BrowserRouter, Routes, Route, Link, useNavigate, useParams } from 'react-router-dom';

// Setup
function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/users/:id" element={<User />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

// Navigation
function Component() {
  const navigate = useNavigate();
  return <button onClick={() => navigate('/about')}>Go to About</button>;
}

// Params
function User() {
  const { id } = useParams();
  return <h1>User ID: {id}</h1>;
}
```

---

## 📡 API Calls

### Fetch

```javascript
useEffect(() => {
  fetch('https://api.example.com/data')
    .then(res => res.json())
    .then(data => setData(data))
    .catch(err => console.error(err));
}, []);

// Async/await
useEffect(() => {
  const fetchData = async () => {
    try {
      const response = await fetch('https://api.example.com/data');
      const data = await response.json();
      setData(data);
    } catch (err) {
      console.error(err);
    }
  };
  fetchData();
}, []);
```

### Axios

```javascript
import axios from 'axios';

useEffect(() => {
  axios.get('https://api.example.com/data')
    .then(response => setData(response.data))
    .catch(error => console.error(error));
}, []);

// Async/await
useEffect(() => {
  const fetchData = async () => {
    try {
      const { data } = await axios.get('https://api.example.com/data');
      setData(data);
    } catch (error) {
      console.error(error);
    }
  };
  fetchData();
}, []);
```

---

## 🔐 Conditional Rendering

```javascript
// If/Else with ternary
{isLoggedIn ? <Dashboard /> : <Login />}

// Logical AND
{isVisible && <Component />}

// Multiple conditions
{isLoading ? (
  <Spinner />
) : error ? (
  <Error message={error} />
) : (
  <Data data={data} />
)}

// Switch/Case pattern
const renderContent = () => {
  switch (status) {
    case 'loading': return <Spinner />;
    case 'error': return <Error />;
    case 'success': return <Data />;
    default: return null;
  }
};
```

---

## 📋 Lists

```javascript
// Basic list
{items.map(item => (
  <div key={item.id}>{item.name}</div>
))}

// With index (avoid if list can change)
{items.map((item, index) => (
  <div key={index}>{item}</div>
))}

// With components
{users.map(user => (
  <UserCard key={user.id} user={user} />
))}

// Empty state
{items.length === 0 ? (
  <p>No items found</p>
) : (
  items.map(item => <Item key={item.id} {...item} />)
)}
```

---

## 🎯 Common Patterns

### Loading State

```javascript
function DataComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch('/api/data');
        const data = await response.json();
        setData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

### Custom Hook

```javascript
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const data = await response.json();
        setData(data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [url]);

  return { data, loading, error };
}

// Usage
const { data, loading, error } = useFetch('/api/users');
```

### Debounce

```javascript
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
}

// Usage
const [searchTerm, setSearchTerm] = useState('');
const debouncedSearch = useDebounce(searchTerm, 500);

useEffect(() => {
  // API call with debouncedSearch
}, [debouncedSearch]);
```

---

## 🧪 Testing

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import Component from './Component';

test('renders component', () => {
  render(<Component />);
  expect(screen.getByText('Hello')).toBeInTheDocument();
});

test('handles click', () => {
  render(<Component />);
  const button = screen.getByRole('button');
  fireEvent.click(button);
  expect(screen.getByText('Clicked')).toBeInTheDocument();
});
```

---

## 📦 Prop Types

```javascript
import PropTypes from 'prop-types';

function User({ name, age, email }) {
  return <div>{name}, {age}, {email}</div>;
}

User.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number,
  email: PropTypes.string.isRequired
};

User.defaultProps = {
  age: 0
};
```

---

## 🚀 Quick Start Template

```javascript
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="App">
      <h1>My React App</h1>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}

export default App;
```

---

**Happy React coding! ⚛️**

