# 📦 Git Basics

**Phase 1: Master Git Fundamentals (2-3 Days)**

---

## 📖 Overview

Learn the essential Git commands and concepts needed for daily development work.

---

## 🎯 Learning Objectives

✅ Understand Git architecture  
✅ Configure Git properly  
✅ Master basic workflow  
✅ Track changes effectively  
✅ View and understand history  

---

## 📚 Core Topics

### 1. Git Installation & Configuration

**Install Git:**
```bash
# Windows: Download from https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt-get install git
```

**Initial Configuration:**
```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim

# View configuration
git config --list
git config user.name
```

**Configuration Levels:**
- `--system`: All users on the system
- `--global`: Current user
- `--local`: Current repository (default)

---

### 2. Git Architecture

**Three Areas:**

```
Working Directory  →  Staging Area  →  Repository
  (Modified)          (Staged)         (Committed)
      ↓                   ↓                 ↓
   git add          git commit         git push
```

**File States:**
- **Untracked**: New files not tracked by Git
- **Modified**: Changed but not staged
- **Staged**: Marked for next commit
- **Committed**: Stored in repository

---

### 3. Basic Workflow

**Initialize Repository:**
```bash
# Create new repository
git init

# Clone existing repository
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder-name
```

**Basic Commands:**
```bash
# Check status
git status
git status -s  # Short format

# Add files to staging
git add file.txt          # Single file
git add *.js             # All JavaScript files
git add .                # All files in current directory
git add -A               # All files in repository

# Commit changes
git commit -m "Add feature X"
git commit -am "Update feature X"  # Add and commit tracked files

# View history
git log
git log --oneline
git log --oneline --graph --all
git log --oneline -5      # Last 5 commits
```

---

### 4. Working with Files

**Track New Files:**
```bash
# Create and track file
echo "Hello Git" > README.md
git add README.md
git commit -m "Add README"
```

**Modify Files:**
```bash
# Edit file
echo "More content" >> README.md

# Check changes
git diff                  # Unstaged changes
git diff --staged         # Staged changes
git diff HEAD             # All changes

# Stage and commit
git add README.md
git commit -m "Update README"
```

**Remove Files:**
```bash
# Remove from Git and filesystem
git rm file.txt
git commit -m "Remove file.txt"

# Remove from Git only (keep in filesystem)
git rm --cached file.txt
git commit -m "Stop tracking file.txt"
```

**Rename Files:**
```bash
# Rename file
git mv old-name.txt new-name.txt
git commit -m "Rename file"

# Equivalent to:
# mv old-name.txt new-name.txt
# git rm old-name.txt
# git add new-name.txt
```

---

### 5. Viewing History

**Log Commands:**
```bash
# Basic log
git log

# One line per commit
git log --oneline

# With graph
git log --oneline --graph --all

# With file changes
git log --stat

# With actual changes
git log -p

# Last N commits
git log -5

# Filter by author
git log --author="John"

# Filter by date
git log --since="2024-01-01"
git log --until="2024-12-31"

# Filter by message
git log --grep="fix"

# Filter by file
git log -- file.txt
```

**Show Commit:**
```bash
# Show specific commit
git show <commit-hash>
git show HEAD
git show HEAD~1          # One commit before HEAD
git show HEAD~2          # Two commits before HEAD
```

---

### 6. Undoing Changes

**Discard Working Directory Changes:**
```bash
# Single file
git checkout -- file.txt
git restore file.txt     # New way

# All files
git checkout -- .
git restore .            # New way
```

**Unstage Files:**
```bash
# Single file
git reset HEAD file.txt
git restore --staged file.txt  # New way

# All files
git reset HEAD
git restore --staged .   # New way
```

**Amend Last Commit:**
```bash
# Change commit message
git commit --amend -m "New message"

# Add forgotten file
git add forgotten-file.txt
git commit --amend --no-edit
```

**Reset Commits:**
```bash
# Keep changes in working directory
git reset --soft HEAD~1

# Keep changes unstaged
git reset --mixed HEAD~1  # Default
git reset HEAD~1

# Discard all changes (DANGEROUS!)
git reset --hard HEAD~1
```

---

### 7. .gitignore

**Common Patterns:**
```
# .gitignore file

# Dependencies
node_modules/
vendor/

# Build output
dist/
build/
*.jar
*.war

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Environment
.env
.env.local

# Temporary files
*.tmp
temp/
```

**Ignore Rules:**
```
*.log          # All .log files
!important.log # Except important.log
/temp          # Only temp in root
temp/          # temp directory anywhere
**/logs        # logs anywhere
```

---

### 8. Git Aliases

**Common Aliases:**
```bash
# Create aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg 'log --oneline --graph --all'

# Use aliases
git st          # Same as: git status
git co main     # Same as: git checkout main
git lg          # Same as: git log --oneline --graph --all
```

---

## 💻 Complete Example Workflow

```bash
# 1. Initialize repository
mkdir my-project
cd my-project
git init

# 2. Configure (first time only)
git config user.name "John Doe"
git config user.email "john@example.com"

# 3. Create .gitignore
cat > .gitignore << EOF
node_modules/
.env
*.log
EOF

# 4. Create files
echo "# My Project" > README.md
echo "console.log('Hello');" > app.js

# 5. Check status
git status

# 6. Stage files
git add .

# 7. Commit
git commit -m "Initial commit"

# 8. Make changes
echo "New feature" >> README.md

# 9. View changes
git diff

# 10. Stage and commit
git add README.md
git commit -m "Update README"

# 11. View history
git log --oneline
```

---

## 🎯 Interview Questions

### Q1: Explain the three stages in Git

**Answer:**
1. **Working Directory**: Where you modify files
2. **Staging Area (Index)**: Where you prepare files for commit
3. **Repository**: Where commits are stored

Workflow: Modify → Stage (git add) → Commit (git commit)

---

### Q2: Difference between `git add .` and `git add -A`?

**Answer:**
- `git add .`: Adds files in current directory and subdirectories
- `git add -A`: Adds all files in entire repository

In Git 2.x+, both are equivalent when run from repository root.

---

### Q3: How to undo the last commit but keep changes?

**Answer:**
```bash
git reset --soft HEAD~1  # Keep changes staged
git reset HEAD~1         # Keep changes unstaged (default)
git reset --hard HEAD~1  # Discard changes (careful!)
```

---

### Q4: What is HEAD in Git?

**Answer:**
HEAD is a pointer to the current branch reference, which points to the last commit on that branch. It represents where you are in the repository.

```bash
HEAD           # Current commit
HEAD~1         # One commit before HEAD
HEAD~2         # Two commits before HEAD
HEAD^          # Parent of HEAD
```

---

## ✅ Practice Exercises

1. Create a new repository
2. Configure your name and email
3. Create multiple files
4. Use .gitignore for specific patterns
5. Make several commits
6. View history in different formats
7. Undo changes in various ways
8. Practice with git diff
9. Amend a commit
10. Create useful aliases

---

**👉 Next:** [Branching & Merging →](../02-branching/README.md)

---

**💡 Pro Tip:** Practice these commands daily. Muscle memory is key to Git proficiency!

