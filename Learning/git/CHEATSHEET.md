# 📦 Git Cheat Sheet

**Quick Reference Guide**

---

## Setup & Config

```bash
# Configure
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git config --list

# Initialize
git init
git clone <url>
```

---

## Basic Commands

```bash
# Status
git status
git status -s

# Add
git add file.txt
git add .
git add -A

# Commit
git commit -m "message"
git commit -am "message"

# History
git log
git log --oneline
git log --oneline --graph --all
```

---

## Branching

```bash
# Create
git branch feature-name
git checkout -b feature-name

# Switch
git checkout feature-name
git switch feature-name

# List
git branch
git branch -a

# Delete
git branch -d feature-name
git branch -D feature-name

# Merge
git merge feature-name
git merge --no-ff feature-name
```

---

## Remote

```bash
# Add remote
git remote add origin <url>
git remote -v

# Push
git push origin main
git push -u origin main

# Pull
git pull origin main
git pull --rebase origin main

# Fetch
git fetch origin
```

---

## Undo Changes

```bash
# Discard changes
git checkout -- file.txt
git restore file.txt

# Unstage
git reset HEAD file.txt
git restore --staged file.txt

# Undo commit
git reset HEAD~1         # Keep changes
git reset --hard HEAD~1  # Discard changes

# Revert commit
git revert <commit-hash>
```

---

## Stash

```bash
# Stash changes
git stash
git stash save "message"

# List stashes
git stash list

# Apply stash
git stash apply
git stash pop

# Drop stash
git stash drop
git stash clear
```

---

## Rebase

```bash
# Rebase
git rebase main
git rebase -i HEAD~3

# Continue/abort
git rebase --continue
git rebase --abort
```

---

## Tags

```bash
# Create tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0"

# List tags
git tag

# Push tags
git push origin v1.0.0
git push --tags

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## Advanced

```bash
# Cherry-pick
git cherry-pick <commit-hash>

# Reflog
git reflog

# Blame
git blame file.txt

# Bisect
git bisect start
git bisect bad
git bisect good <commit>
```

---

## Common Workflows

### Feature Branch
```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add feature"
git push -u origin feature/new-feature
# Create PR
# Merge on GitHub
git checkout main
git pull origin main
git branch -d feature/new-feature
```

### Hotfix
```bash
git checkout -b hotfix/critical-bug main
git add .
git commit -m "Fix critical bug"
git checkout main
git merge --no-ff hotfix/critical-bug
git push origin main
git tag -a v1.0.1 -m "Hotfix release"
git push --tags
```

---

## Useful Aliases

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.lg 'log --oneline --graph --all'
```

---

## .gitignore Patterns

```
# Dependencies
node_modules/
vendor/

# Build
dist/
build/
*.jar

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Environment
.env
*.log
```

---

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Example:**
```
feat(auth): add JWT authentication

Implement JWT-based auth for API endpoints

Closes #123
```

---

## Emergency Commands

```bash
# Undo last commit (not pushed)
git reset --soft HEAD~1

# Recover deleted branch
git reflog
git checkout -b recovered abc1234

# Remove large file from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch large-file.zip' \
  --prune-empty --tag-name-filter cat -- --all
```

---

**Happy Git-ing! 📦**

