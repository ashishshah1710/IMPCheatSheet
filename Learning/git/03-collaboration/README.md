# 🤝 Git Collaboration

**Phase 3: Team Workflows (2-3 Days)**

---

## 📖 Overview

Learn how to collaborate effectively with teams using Git and platforms like GitHub/GitLab.

---

## 🎯 Learning Objectives

✅ Work with remote repositories  
✅ Create pull requests  
✅ Review code effectively  
✅ Understand Git workflows  
✅ Collaborate in teams  

---

## 📚 Core Topics

### 1. Remote Repositories

**Add Remote:**
```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# List remotes
git remote -v

# Show remote details
git remote show origin

# Rename remote
git remote rename origin upstream

# Remove remote
git remote remove origin
```

**Clone Repository:**
```bash
# Clone with HTTPS
git clone https://github.com/user/repo.git

# Clone with SSH
git clone git@github.com:user/repo.git

# Clone specific branch
git clone -b develop https://github.com/user/repo.git

# Shallow clone (last commit only)
git clone --depth 1 https://github.com/user/repo.git
```

---

### 2. Push & Pull

**Push Changes:**
```bash
# Push to remote
git push origin main

# Push and set upstream
git push -u origin main

# Push all branches
git push --all origin

# Push tags
git push --tags origin

# Force push (careful!)
git push --force origin main
git push --force-with-lease origin main  # Safer
```

**Pull Changes:**
```bash
# Fetch and merge
git pull origin main

# Fetch only
git fetch origin

# Pull with rebase
git pull --rebase origin main
```

---

### 3. Pull Requests (PRs)

**PR Workflow:**

1. **Create Branch:**
```bash
git checkout -b feature/add-login
```

2. **Make Changes & Commit:**
```bash
git add .
git commit -m "Add login functionality"
```

3. **Push to Remote:**
```bash
git push -u origin feature/add-login
```

4. **Create PR on GitHub/GitLab**
5. **Code Review**
6. **Address Feedback:**
```bash
git commit -m "Address review comments"
git push origin feature/add-login
```

7. **Merge PR**
8. **Delete Branch:**
```bash
git branch -d feature/add-login
git push origin --delete feature/add-login
```

---

### 4. Code Review Best Practices

**As Reviewer:**
- ✅ Review promptly
- ✅ Be constructive
- ✅ Check tests
- ✅ Verify functionality
- ✅ Look for edge cases

**As Author:**
- ✅ Keep PRs small
- ✅ Write clear descriptions
- ✅ Add tests
- ✅ Respond to feedback
- ✅ Keep commits clean

**PR Description Template:**
```markdown
## What
Brief description of changes

## Why
Reason for changes

## How
Technical approach

## Testing
How to test changes

## Screenshots
(if applicable)
```

---

### 5. Git Workflows

#### GitHub Flow
```
main (always deployable)
  ↓
Create feature branch
  ↓
Make commits
  ↓
Open Pull Request
  ↓
Review & Discussion
  ↓
Merge to main
  ↓
Deploy
```

#### GitFlow
```
main        # Production releases
  ↓
develop     # Integration branch
  ↓
feature/*   # New features (from develop)
hotfix/*    # Urgent fixes (from main)
release/*   # Release prep (from develop)
```

**GitFlow Commands:**
```bash
# Start feature
git checkout -b feature/new-feature develop

# Finish feature
git checkout develop
git merge --no-ff feature/new-feature
git branch -d feature/new-feature

# Start release
git checkout -b release/1.2.0 develop

# Finish release
git checkout main
git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Version 1.2.0"
git checkout develop
git merge --no-ff release/1.2.0
git branch -d release/1.2.0
```

---

### 6. Forking Workflow

**Fork & Clone:**
```bash
# 1. Fork on GitHub

# 2. Clone your fork
git clone https://github.com/your-username/repo.git

# 3. Add upstream
git remote add upstream https://github.com/original/repo.git

# 4. Verify remotes
git remote -v
```

**Keep Fork Updated:**
```bash
# Fetch upstream
git fetch upstream

# Merge upstream changes
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

**Contribute:**
```bash
# 1. Create branch
git checkout -b feature/contribution

# 2. Make changes
git add .
git commit -m "Add contribution"

# 3. Push to fork
git push origin feature/contribution

# 4. Create Pull Request on GitHub
```

---

### 7. Tags & Releases

**Create Tags:**
```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag specific commit
git tag -a v1.0.0 abc1234 -m "Release 1.0.0"

# List tags
git tag
git tag -l "v1.*"

# Show tag
git show v1.0.0

# Push tags
git push origin v1.0.0
git push origin --tags

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

**Semantic Versioning:**
```
MAJOR.MINOR.PATCH

v1.0.0 → v2.0.0  # Major (breaking changes)
v1.0.0 → v1.1.0  # Minor (new features)
v1.0.0 → v1.0.1  # Patch (bug fixes)
```

---

## 🎯 Interview Questions

### Q1: Git pull vs Git fetch?

**Answer:**
- `git fetch`: Downloads changes but doesn't merge
- `git pull`: Downloads and merges (fetch + merge)

Use fetch when you want to review changes before merging.

### Q2: Explain fork vs clone

**Answer:**
- **Clone**: Copy repository to local machine
- **Fork**: Create personal copy on GitHub

Fork is used for contributing to projects you don't own.

### Q3: What is a Pull Request?

**Answer:**
A Pull Request (PR) is a request to merge changes from one branch to another. It enables:
- Code review
- Discussion
- Continuous Integration checks
- Approval workflow

### Q4: How to keep fork updated?

**Answer:**
```bash
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main
git push origin main
```

---

## ✅ Practice Checklist

- [ ] Clone repositories
- [ ] Push and pull changes
- [ ] Create pull requests
- [ ] Review code
- [ ] Fork repositories
- [ ] Keep fork synced
- [ ] Create tags
- [ ] Practice Git workflows

---

**👉 Next:** [Advanced Topics →](../04-advanced/README.md)


---

## 💡 Simple Explanation (In Plain English)

Team Git uses a **remote** (`origin`), **`git fetch`** downloads commits without merging, **`git pull`** fetch+merge, **`git push`** uploads. **Pull requests** are code review before merge. **Fork** copies someone else's repo to your account; **upstream** sync keeps your fork current.

---

## 🎯 Interview Quick Prep

### 1. Fetch vs pull?

**Simple Answer:** `git fetch` updates remote-tracking branches only—you inspect before merging. `git pull` is fetch plus merge (or rebase), which can surprise you if you have not reviewed incoming commits.

### 2. What is a pull request?

**Simple Answer:** A request to merge your branch into another (usually `main`), with review comments and CI checks. It is a collaboration gate, not a Git core command.

### 3. How resolve "rejected push"?

**Simple Answer:** Someone pushed first—`git pull --rebase` (or pull then push) integrates their work, resolve conflicts, then push again.

### 4. Fork workflow?

**Simple Answer:** Fork on GitHub, clone your fork, push branches to your fork, open PR to upstream. Maintainers merge; you sync fork from upstream periodically.

### 5. What is `origin`?

**Simple Answer:** Default name for the remote you cloned from—usually the team's GitHub repo URL for push/pull.
