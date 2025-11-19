# 📘 TypeScript

## Overview
TypeScript is JavaScript with types - a strongly typed superset of JavaScript that compiles to plain JavaScript. Essential for modern web development.

---

## Why TypeScript?

### ✅ Benefits
- **Type Safety**: Catch errors at compile time
- **Better IDE Support**: Autocomplete, refactoring
- **Improved Readability**: Self-documenting code
- **Scalability**: Better for large codebases
- **Modern JS Features**: ES6+ support

### Companies Using TypeScript
- Microsoft, Google, Airbnb, Slack, Netflix, Spotify

---

## Getting Started

### Installation
```bash
# Install globally
npm install -g typescript

# Check version
tsc --version

# Initialize project
tsc --init  # Creates tsconfig.json
```

### Hello World
```typescript
// hello.ts
function greet(name: string): string {
    return `Hello, ${name}!`;
}

console.log(greet("World"));

// Compile
tsc hello.ts  # Produces hello.js

// Run
node hello.js
```

---

## Basic Types

```typescript
// Primitives
let age: number = 25;
let name: string = "John";
let isActive: boolean = true;

// Arrays
let numbers: number[] = [1, 2, 3, 4];
let names: Array<string> = ["John", "Jane"];

// Tuple (fixed-length array with specific types)
let person: [string, number] = ["John", 30];

// Enum
enum Color {
    Red,
    Green,
    Blue
}
let favoriteColor: Color = Color.Blue;

enum Status {
    Active = "ACTIVE",
    Inactive = "INACTIVE"
}

// Any (avoid when possible)
let anything: any = "string";
anything = 42;
anything = true;

// Unknown (safer than any)
let value: unknown = "hello";
if (typeof value === "string") {
    console.log(value.toUpperCase());
}

// Void (no return value)
function logMessage(message: string): void {
    console.log(message);
}

// Never (never returns)
function throwError(message: string): never {
    throw new Error(message);
}

// Null and undefined
let nullable: null = null;
let undefinedValue: undefined = undefined;

// Union types
let id: number | string;
id = 123;
id = "abc123";

// Literal types
let direction: "up" | "down" | "left" | "right";
direction = "up";  // ✓
// direction = "forward";  // ✗ Error
```

---

## Interfaces

```typescript
// Basic interface
interface User {
    id: number;
    name: string;
    email: string;
    age?: number;  // Optional property
    readonly createdAt: Date;  // Readonly
}

const user: User = {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    createdAt: new Date()
};

// user.createdAt = new Date();  // Error: readonly

// Extending interfaces
interface Admin extends User {
    role: string;
    permissions: string[];
}

const admin: Admin = {
    id: 1,
    name: "Admin User",
    email: "admin@example.com",
    createdAt: new Date(),
    role: "admin",
    permissions: ["read", "write", "delete"]
};

// Function types in interfaces
interface MathOperation {
    (a: number, b: number): number;
}

const add: MathOperation = (a, b) => a + b;
const subtract: MathOperation = (a, b) => a - b;

// Index signatures
interface StringMap {
    [key: string]: string;
}

const config: StringMap = {
    apiUrl: "https://api.example.com",
    apiKey: "abc123"
};
```

---

## Type Aliases

```typescript
// Type alias
type ID = number | string;
type UserRole = "admin" | "user" | "guest";

// Object type
type User = {
    id: ID;
    name: string;
    role: UserRole;
};

// Function type
type GreetFunction = (name: string) => string;

const greet: GreetFunction = (name) => `Hello, ${name}!`;

// Union types
type Success = { status: 200; data: any };
type Error = { status: 400 | 500; error: string };
type Response = Success | Error;

function handleResponse(response: Response) {
    if (response.status === 200) {
        console.log(response.data);
    } else {
        console.error(response.error);
    }
}

// Intersection types
type Person = {
    name: string;
    age: number;
};

type Employee = {
    employeeId: number;
    department: string;
};

type EmployeePerson = Person & Employee;

const employee: EmployeePerson = {
    name: "John",
    age: 30,
    employeeId: 12345,
    department: "Engineering"
};
```

---

## Functions

```typescript
// Typed parameters and return
function add(a: number, b: number): number {
    return a + b;
}

// Optional parameters
function greet(name: string, greeting?: string): string {
    return `${greeting || "Hello"}, ${name}!`;
}

// Default parameters
function power(base: number, exponent: number = 2): number {
    return Math.pow(base, exponent);
}

// Rest parameters
function sum(...numbers: number[]): number {
    return numbers.reduce((acc, n) => acc + n, 0);
}

// Function overloading
function format(value: string): string;
function format(value: number): string;
function format(value: boolean): string;
function format(value: string | number | boolean): string {
    return String(value);
}

// Arrow functions
const multiply = (a: number, b: number): number => a * b;

// Generic functions
function identity<T>(arg: T): T {
    return arg;
}

const num = identity<number>(42);
const str = identity<string>("hello");
```

---

## Classes

```typescript
class User {
    // Properties
    private id: number;
    public name: string;
    protected email: string;
    readonly createdAt: Date;
    
    // Constructor
    constructor(id: number, name: string, email: string) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.createdAt = new Date();
    }
    
    // Methods
    public greet(): string {
        return `Hello, I'm ${this.name}`;
    }
    
    // Getter
    get userId(): number {
        return this.id;
    }
    
    // Setter
    set userName(name: string) {
        if (name.length < 3) {
            throw new Error("Name too short");
        }
        this.name = name;
    }
    
    // Static method
    static createGuest(): User {
        return new User(0, "Guest", "guest@example.com");
    }
}

// Shorthand constructor
class Product {
    constructor(
        public id: number,
        public name: string,
        public price: number
    ) {}
}

// Inheritance
class Admin extends User {
    constructor(
        id: number,
        name: string,
        email: string,
        public role: string
    ) {
        super(id, name, email);
    }
    
    public deleteUser(userId: number): void {
        console.log(`Deleting user ${userId}`);
    }
}

// Abstract class
abstract class Animal {
    abstract makeSound(): void;
    
    move(): void {
        console.log("Moving...");
    }
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

// Implementing interfaces
interface Printable {
    print(): void;
}

class Document implements Printable {
    print(): void {
        console.log("Printing document...");
    }
}
```

---

## Generics

```typescript
// Generic function
function getFirst<T>(array: T[]): T | undefined {
    return array[0];
}

const firstNumber = getFirst<number>([1, 2, 3]);  // number
const firstName = getFirst<string>(["a", "b"]);   // string

// Generic interface
interface Response<T> {
    status: number;
    data: T;
}

const userResponse: Response<User> = {
    status: 200,
    data: { id: 1, name: "John", email: "john@example.com" }
};

// Generic class
class Box<T> {
    private value: T;
    
    constructor(value: T) {
        this.value = value;
    }
    
    getValue(): T {
        return this.value;
    }
    
    setValue(value: T): void {
        this.value = value;
    }
}

const numberBox = new Box<number>(42);
const stringBox = new Box<string>("hello");

// Generic constraints
interface Lengthwise {
    length: number;
}

function logLength<T extends Lengthwise>(arg: T): void {
    console.log(arg.length);
}

logLength("hello");  // ✓
logLength([1, 2, 3]);  // ✓
// logLength(42);  // ✗ Error: number doesn't have length
```

---

## Type Guards & Narrowing

```typescript
// typeof guard
function print(value: string | number) {
    if (typeof value === "string") {
        console.log(value.toUpperCase());
    } else {
        console.log(value.toFixed(2));
    }
}

// instanceof guard
class Dog {
    bark() { console.log("Woof!"); }
}

class Cat {
    meow() { console.log("Meow!"); }
}

function makeSound(animal: Dog | Cat) {
    if (animal instanceof Dog) {
        animal.bark();
    } else {
        animal.meow();
    }
}

// Custom type guard
interface Fish {
    swim: () => void;
}

interface Bird {
    fly: () => void;
}

function isFish(pet: Fish | Bird): pet is Fish {
    return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
    if (isFish(pet)) {
        pet.swim();
    } else {
        pet.fly();
    }
}

// Discriminated unions
type Success = { kind: "success"; data: any };
type Error = { kind: "error"; message: string };
type Result = Success | Error;

function handleResult(result: Result) {
    switch (result.kind) {
        case "success":
            console.log(result.data);
            break;
        case "error":
            console.error(result.message);
            break;
    }
}
```

---

## Utility Types

```typescript
// Partial (all properties optional)
interface User {
    id: number;
    name: string;
    email: string;
}

type PartialUser = Partial<User>;
// { id?: number; name?: string; email?: string; }

// Required (all properties required)
type RequiredUser = Required<PartialUser>;

// Readonly (all properties readonly)
type ReadonlyUser = Readonly<User>;

// Pick (select specific properties)
type UserPreview = Pick<User, "id" | "name">;
// { id: number; name: string; }

// Omit (exclude specific properties)
type UserWithoutEmail = Omit<User, "email">;
// { id: number; name: string; }

// Record (create object type with keys)
type UserRoles = Record<string, string>;
// { [key: string]: string; }

// ReturnType (extract return type)
function getUser() {
    return { id: 1, name: "John" };
}
type User = ReturnType<typeof getUser>;

// Parameters (extract parameter types)
function createUser(name: string, age: number) {}
type CreateUserParams = Parameters<typeof createUser>;
// [string, number]
```

---

## TypeScript with React

```typescript
import React, { useState, useEffect } from 'react';

// Props interface
interface UserCardProps {
    user: {
        id: number;
        name: string;
        email: string;
    };
    onDelete?: (id: number) => void;
}

// Functional component
const UserCard: React.FC<UserCardProps> = ({ user, onDelete }) => {
    return (
        <div>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
            {onDelete && (
                <button onClick={() => onDelete(user.id)}>Delete</button>
            )}
        </div>
    );
};

// useState with TypeScript
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);
const [users, setUsers] = useState<User[]>([]);

// useEffect
useEffect(() => {
    fetchUsers();
}, []);

// Event handlers
const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    console.log(event.currentTarget);
};

const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value);
};
```

---

## tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "jsx": "react",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## Best Practices

✅ Enable `strict` mode in tsconfig.json  
✅ Avoid `any` - use `unknown` if needed  
✅ Use interfaces for objects, type aliases for unions  
✅ Leverage type inference (don't over-annotate)  
✅ Use discriminated unions for better type narrowing  
✅ Write reusable generic types  
✅ Use readonly and const assertions  

---

## Resources

### Official
- **typescriptlang.org**: Official docs
- **TypeScript Handbook**: Comprehensive guide

### Learning
- **TypeScript Deep Dive**: Free online book
- **Execute Program**: Interactive lessons

### Practice
- **TypeScript Exercises**: github.com/typescript-exercises
- **Type Challenges**: github.com/type-challenges

---

**💡 Pro Tip**: Start by adding TypeScript to an existing JavaScript project incrementally. Enable `allowJs` in tsconfig and gradually migrate files!

