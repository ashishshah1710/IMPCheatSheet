# 🚀 Get Started - Full Stack Java Development

Start your journey to becoming a Full Stack Java Developer in just 30 minutes!

---

## ✅ Environment Setup (20 minutes)

### Step 1: Install Java JDK (5 minutes)

**Download & Install:**
- Visit [Adoptium](https://adoptium.net/)
- Download JDK 17 (LTS)
- Run installer
- Follow default options

**Verify Installation:**
```bash
java -version
# Output: openjdk version "17.0.x"

javac -version
# Output: javac 17.0.x
```

**Set JAVA_HOME (if needed):**

**Windows:**
```powershell
# Add to System Environment Variables
JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.x.x
Path=%JAVA_HOME%\bin
```

**Mac/Linux:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export JAVA_HOME=/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH
```

---

### Step 2: Install IDE (5 minutes)

**Option A: IntelliJ IDEA (Recommended)**
- Download: [IntelliJ IDEA Community](https://www.jetbrains.com/idea/download/)
- Free and powerful
- Best for Java/Spring development

**Option B: Eclipse**
- Download: [Eclipse IDE](https://www.eclipse.org/downloads/)
- Free and lightweight
- Good alternative

**Option C: VS Code**
- Download: [VS Code](https://code.visualstudio.com/)
- Install Java Extension Pack
- Good for polyglot development

---

### Step 3: Install Build Tools (3 minutes)

**Maven:**
```bash
# Windows (using Chocolatey)
choco install maven

# Mac
brew install maven

# Linux
sudo apt install maven

# Verify
mvn -version
```

**Gradle (Optional):**
```bash
# Windows
choco install gradle

# Mac
brew install gradle

# Verify
gradle -version
```

---

### Step 4: Install Node.js (3 minutes)

For full-stack development:

```bash
# Download from: https://nodejs.org/
# Choose LTS version

# Verify
node -v
# Output: v20.x.x

npm -v
# Output: 10.x.x
```

---

### Step 5: Install MongoDB (4 minutes)

**Download:**
- Visit [MongoDB Downloads](https://www.mongodb.com/try/download/community)
- Choose Community Edition
- Install with default settings

**Verify:**
```bash
mongosh --version
# Output: 2.x.x

# Start MongoDB
# Windows: mongod
# Mac: brew services start mongodb-community
# Linux: sudo systemctl start mongod
```

---

## 🎯 Your First 30 Minutes

### Minutes 1-10: Hello World in Java

```java
// Create: HelloWorld.java

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Full Stack Java Developer! 🚀");
        
        // Java 17 features
        String name = "Student";
        System.out.println("Welcome, " + name + "!");
    }
}
```

**Compile and Run:**
```bash
# Compile
javac HelloWorld.java

# Run
java HelloWorld

# Output: Hello, Full Stack Java Developer! 🚀
```

✅ **You just wrote and ran your first Java program!**

---

### Minutes 11-20: Create Spring Boot Application

**Using Spring Initializr:**

1. Visit [start.spring.io](https://start.spring.io)
2. Configure:
   - Project: Maven
   - Language: Java
   - Spring Boot: 3.2.x
   - Java: 17
   - Dependencies: Spring Web
3. Click "Generate"
4. Extract ZIP file

**Or use command line:**
```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d baseDir=my-first-spring-app \
  -o my-first-spring-app.zip

unzip my-first-spring-app.zip
cd my-first-spring-app
```

**Create a REST endpoint:**

```java
// src/main/java/.../controller/HelloController.java

package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class HelloController {
    
    @GetMapping("/hello")
    public String hello() {
        return "Hello from Spring Boot! 🎉";
    }
    
    @GetMapping("/greet/{name}")
    public String greet(@PathVariable String name) {
        return "Hello, " + name + "! Welcome to Spring Boot!";
    }
}
```

**Run the application:**
```bash
# Using Maven
./mvnw spring-boot:run

# Or if Maven is installed globally
mvn spring-boot:run
```

**Test it:**
```bash
# Open browser to:
http://localhost:8080/api/hello
http://localhost:8080/api/greet/YourName

# Or use curl
curl http://localhost:8080/api/hello
```

✅ **You just created your first REST API!**

---

### Minutes 21-30: First React Component

**Create React App:**
```bash
npx create-react-app my-first-react-app
cd my-first-react-app
```

**Create a component:**
```javascript
// src/App.js

import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [name, setName] = useState('');

  const fetchGreeting = async () => {
    try {
      // Connect to Spring Boot API
      const response = await fetch(`http://localhost:8080/api/greet/${name || 'Guest'}`);
      const data = await response.text();
      setMessage(data);
    } catch (error) {
      setMessage('Error connecting to backend');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 Full Stack Java Developer</h1>
        <input 
          type="text" 
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{ padding: '10px', fontSize: '16px', marginBottom: '10px' }}
        />
        <button onClick={fetchGreeting} style={{ padding: '10px 20px', fontSize: '16px' }}>
          Get Greeting from Spring Boot
        </button>
        {message && <p style={{ marginTop: '20px', fontSize: '20px' }}>{message}</p>}
      </header>
    </div>
  );
}

export default App;
```

**Run React app:**
```bash
npm start
# Opens http://localhost:3000
```

**Enable CORS in Spring Boot:**
```java
// Add to HelloController.java
@CrossOrigin(origins = "http://localhost:3000")
```

✅ **You just connected React to Spring Boot!**

---

## 📊 Skill Assessment

Before diving deep, assess your current level:

### Complete Beginner (Start at Week 1)
- [ ] No programming experience
- [ ] Never used Java
- [ ] Don't know what OOP means
- [ ] Haven't built any applications

**Start:** `01-dsa/README.md` → Learn programming fundamentals

---

### Basic Programming (Start at Week 2)
- [x] Know basic programming (any language)
- [x] Understand variables, loops, functions
- [ ] Haven't used Java much
- [ ] Never built web applications

**Start:** `02-core-java/01-beginner/`

---

### Java Developer (Start at Week 6)
- [x] Know Core Java well
- [x] Understand OOP concepts
- [x] Built simple Java applications
- [ ] Haven't used Spring/Spring Boot

**Start:** `04-spring/01-spring-core/`

---

### Experienced Developer (Start at Week 10)
- [x] Experienced with Java & Spring
- [x] Built REST APIs
- [ ] Want to learn NoSQL/Kafka/React
- [ ] Want to improve system design

**Start:** `05-databases/` or `08-reactjs/`

---

## 🎯 Choose Your Learning Path

### Path 1: Complete Beginner → Full Stack (24 weeks)

**Perfect for:** Career changers, fresh graduates

**Week 1-4:** DSA & Core Java fundamentals  
**Week 5-8:** Advanced Java & Collections  
**Week 9-14:** Spring Boot & REST APIs  
**Week 15-18:** Databases (MongoDB, SQL)  
**Week 19-20:** Kafka messaging  
**Week 21-24:** React.js & Full Stack projects  

**Daily commitment:** 2-3 hours  
**Expected outcome:** Junior Full Stack Developer role

---

### Path 2: Backend Specialist (16 weeks)

**Perfect for:** Focus on backend/microservices

**Week 1-3:** DSA essentials  
**Week 4-6:** Core Java review  
**Week 7-10:** Spring Boot deep dive  
**Week 11-13:** Databases (MongoDB, Couchbase)  
**Week 14-15:** Kafka & Event-driven architecture  
**Week 16:** Microservices project  

**Daily commitment:** 2-3 hours  
**Expected outcome:** Backend Java Developer

---

### Path 3: Fast Track (12 weeks - Intensive)

**Perfect for:** Career transition, bootcamp style

**Prerequisite:** Basic programming knowledge

**Week 1-2:** Java fundamentals (intensive)  
**Week 3-5:** Spring Boot & REST API  
**Week 6-7:** MongoDB & Kafka basics  
**Week 8-10:** React.js fundamentals  
**Week 11-12:** Full stack project & deployment  

**Daily commitment:** 5-6 hours  
**Expected outcome:** Full Stack Developer (entry level)

---

### Path 4: MERN → Java (8 weeks)

**Perfect for:** JavaScript developers learning Java

**Week 1-2:** Java syntax & OOP  
**Week 3-5:** Spring Boot (compare to Express)  
**Week 6-7:** MongoDB with Java (vs Mongoose)  
**Week 8:** Integration project  

**Daily commitment:** 2-3 hours  
**Expected outcome:** Full Stack with Java backend

---

## 📚 Essential Tools Setup

### Development Tools

**1. Postman (API Testing)**
```bash
# Download from: https://www.postman.com/downloads/
# Essential for testing REST APIs
```

**2. Git**
```bash
# Windows
choco install git

# Mac
brew install git

# Linux
sudo apt install git

# Configure
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**3. Docker (Optional but recommended)**
```bash
# Download Docker Desktop
# https://www.docker.com/products/docker-desktop

# Useful for running databases locally
docker run -d -p 27017:27017 mongo
docker run -d -p 9092:9092 apache/kafka
```

---

### IDE Extensions

**IntelliJ IDEA Plugins:**
- Lombok
- Spring Boot Assistant
- Maven Helper
- Rainbow Brackets
- Key Promoter X

**VS Code Extensions:**
- Java Extension Pack
- Spring Boot Extension Pack
- ES7+ React/Redux/React-Native snippets
- ESLint
- Prettier

---

## 🎓 First Week Goals

### Day 1: Environment Setup
- [ ] Install all required software
- [ ] Complete "First 30 Minutes" above
- [ ] Create GitHub account
- [ ] Set up Git locally

**Time:** 2-3 hours

---

### Day 2: Java Basics
- [ ] Read: `02-core-java/01-beginner/README.md`
- [ ] Learn: Variables, data types, operators
- [ ] Practice: Write 5 simple programs
- [ ] Exercise: Calculator program

**Time:** 2-3 hours

---

### Day 3: Control Flow
- [ ] Learn: if-else, switch, loops
- [ ] Practice: Pattern printing programs
- [ ] Exercise: Number guessing game
- [ ] Quiz: Test your knowledge

**Time:** 2-3 hours

---

### Day 4: Functions & Arrays
- [ ] Learn: Methods, parameters, return values
- [ ] Learn: Arrays and array operations
- [ ] Practice: Array manipulation exercises
- [ ] Exercise: Array sorting program

**Time:** 2-3 hours

---

### Day 5: Object-Oriented Programming
- [ ] Learn: Classes and objects
- [ ] Learn: Constructors and methods
- [ ] Practice: Create class hierarchies
- [ ] Exercise: Student management system

**Time:** 3 hours

---

### Day 6-7: Weekend Project
- [ ] Project: Console-based application
- [ ] Options: Library system, Bank account, Todo list
- [ ] Use OOP principles
- [ ] Push to GitHub

**Time:** 4-6 hours

---

## 💡 Learning Best Practices

### 1. Code Every Day
```java
// Even 30 minutes counts!
// Consistency > Intensity

public class DailyPractice {
    public static void main(String[] args) {
        System.out.println("Day " + dayNumber + " of learning!");
        // Your code here
    }
}
```

### 2. Build Projects, Not Just Tutorials
- **Bad:** Watch 10 tutorials
- **Good:** Build 3 projects

### 3. Debug, Don't Give Up
```java
// When you see an error:
// 1. Read the error message carefully
// 2. Google the exact error
// 3. Check Stack Overflow
// 4. Try to fix it yourself
// 5. Ask for help if stuck > 30 min
```

### 4. Use Version Control
```bash
# From day one!
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 5. Document Your Learning
```markdown
# Create a learning journal
## Day 1: Java Basics
- Learned: Variables, data types
- Built: Calculator program
- Struggled with: Loops
- Tomorrow: Practice more loop problems
```

---

## 📈 30-Day Challenge

Can you build momentum in your first month?

### Week 1: Java Fundamentals
- Day 1: Setup & Hello World
- Day 2-4: Basic syntax
- Day 5-7: OOP basics + Project

### Week 2: Core Java
- Day 8-10: Collections Framework
- Day 11-12: Exception Handling
- Day 13-14: File I/O + Project

### Week 3: Spring Boot Intro
- Day 15-16: Spring Boot setup
- Day 17-18: REST APIs
- Day 19-21: CRUD application

### Week 4: Database Integration
- Day 22-24: MongoDB with Java
- Day 25-26: Spring Data
- Day 27-30: Full CRUD app with database

**Daily commitment:** 2 hours  
**Result:** Strong foundation + 4 projects

---

## 🎯 Quick Wins

Start with these to build confidence:

### Quick Win #1: FizzBuzz (15 minutes)
```java
public class FizzBuzz {
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            if (i % 15 == 0) System.out.println("FizzBuzz");
            else if (i % 3 == 0) System.out.println("Fizz");
            else if (i % 5 == 0) System.out.println("Buzz");
            else System.out.println(i);
        }
    }
}
```

### Quick Win #2: REST API (20 minutes)
Use Spring Initializr + One controller = Working API

### Quick Win #3: React Hello World (15 minutes)
`create-react-app` + Modify App.js = Working UI

---

## 🆘 Stuck? Quick Troubleshooting

### Java won't compile
```bash
# Check Java is installed
java -version

# Check file name matches class name
// File: HelloWorld.java
public class HelloWorld { ... }

# Compile from correct directory
javac HelloWorld.java
```

### Spring Boot won't start
```bash
# Check port 8080 is free
# Windows: netstat -ano | findstr :8080
# Mac/Linux: lsof -i :8080

# Use different port
java -jar app.jar --server.port=8081
```

### MongoDB connection fails
```bash
# Check MongoDB is running
mongosh

# Check connection string
mongodb://localhost:27017/mydb
```

---

## 📞 Next Steps

**Today:**
1. ✅ Complete environment setup
2. ✅ Run Hello World
3. ✅ Create Spring Boot app
4. ✅ Choose your learning path

**This Week:**
1. Read `STUDY-PLAN.md` for detailed schedule
2. Start `02-core-java/01-beginner/`
3. Join communities (Reddit, Discord)
4. Set up GitHub portfolio

**This Month:**
1. Complete Java fundamentals
2. Build 3-4 small projects
3. Start Spring Boot
4. Solve 20 DSA problems

---

## 🌟 Inspiration

**Remember:**
- Every expert was once a beginner
- Small daily progress compounds
- Projects > Perfection
- Community helps you grow

**Your journey starts NOW!** 🚀

---

**Ready? Open `02-core-java/01-beginner/README.md` and let's code!** 💪

