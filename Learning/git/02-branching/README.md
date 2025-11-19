# 🌿 Git Branching & Merging

**Phase 2: Master Branch Management (2-3 Days)**

---

## 📖 Overview

Learn how to work with branches effectively, merge changes, and resolve conflicts.

---

## 🎯 Learning Objectives

✅ Create and manage branches  
✅ Switch between branches  
✅ Merge branches effectively  
✅ Resolve merge conflicts  
✅ Understand rebase  

---

## 📚 Core Topics

### 1. Understanding Branches

**What is a Branch?**
A branch is a pointer to a commit. It allows parallel development without affecting the main codebase.

```
main:     A---B---C---D
                   \
feature:            E---F
```

**Why Branches?**
- ✅ Isolate features
- ✅ Experiment safely
- ✅ Collaborate efficiently
- ✅ Organize work

---

### 2. Branch Operations

**Create Branch:**
```bash
# Create branch
git branch feature-login

# Create and switch
git checkout -b feature-login
git switch -c feature-login  # New way

# Create from specific commit
git branch feature-x abc1234
```

**List Branches:**
```bash
# Local branches
git branch

# Remote branches
git branch -r

# All branches
git branch -a

# With last commit
git branch -v

# Merged branches
git branch --merged

# Not merged branches
git branch --no-merged
```

**Switch Branches:**
```bash
# Switch to existing branch
git checkout feature-login
git switch feature-login    # New way

# Switch to previous branch
git checkout -
git switch -
```

**Delete Branch:**
```bash
# Delete merged branch
git branch -d feature-login

# Force delete (even if not merged)
git branch -D feature-login

# Delete remote branch
git push origin --delete feature-login
```

---

### 3. Merging Branches

**Fast-Forward Merge:**
```bash
# When no divergent commits
main:     A---B---C
                   \
feature:            D---E

# After merge:
main:     A---B---C---D---E

# Command:
git checkout main
git merge feature
```

**Three-Way Merge:**
```bash
# When branches diverged
main:     A---B---C---F
                   \
feature:            D---E

# After merge (creates merge commit M):
main:     A---B---C---F---M
                   \     /
feature:            D---E

# Command:
git checkout main
git merge feature
```

**Merge Commands:**
```bash
# Regular merge
git merge feature-branch

# No fast-forward (always create merge commit)
git merge --no-ff feature-branch

# Squash commits
git merge --squash feature-branch

# Abort merge
git merge --abort
```

---

### 4. Resolving Conflicts

**When Conflicts Occur:**
```
<<<<<<< HEAD
Current branch content
=======
Merging branch content
>>>>>>> feature-branch
```

**Resolution Steps:**
```bash
# 1. Identify conflicted files
git status

# 2. Open files and edit
# Remove conflict markers
# Keep desired changes

# 3. Stage resolved files
git add conflicted-file.txt

# 4. Complete merge
git commit -m "Merge feature-branch, resolve conflicts"
```

**Conflict Resolution Tools:**
```bash
# Use merge tool
git mergetool

# Accept ours (current branch)
git checkout --ours file.txt

# Accept theirs (merging branch)
git checkout --theirs file.txt
```

---

### 5. Rebase

**What is Rebase?**
Rebase moves or combines commits to a new base.

```
# Before rebase:
main:     A---B---C---F
                   \
feature:            D---E

# After rebase:
main:     A---B---C---F
                       \
feature:                D'---E'
```

**Rebase Commands:**
```bash
# Rebase feature onto main
git checkout feature
git rebase main

# Rebase interactively
git rebase -i main

# Continue after resolving conflicts
git rebase --continue

# Skip current commit
git rebase --skip

# Abort rebase
git rebase --abort
```

**Rebase vs Merge:**

| Aspect | Merge | Rebase |
|--------|-------|--------|
| History | Preserves history | Rewrites history |
| Commits | Creates merge commit | No merge commit |
| Use Case | Public branches | Local cleanup |
| Safety | Safer | Riskier |

**Golden Rule:** Never rebase public branches!

---

### 6. Interactive Rebase

**Use Cases:**
- Squash commits
- Edit commit messages
- Reorder commits
- Split commits
- Delete commits

**Commands:**
```bash
# Interactive rebase last 3 commits
git rebase -i HEAD~3
```

**Interactive Options:**
```
pick    # Use commit
reword  # Use commit but edit message
edit    # Use commit and stop for amending
squash  # Combine with previous commit
fixup   # Combine with previous (discard message)
drop    # Remove commit
```

**Example:**
```bash
# Original:
pick abc1234 Add feature A
pick def5678 Fix typo
pick ghi9012 Add feature B

# Squash:
pick abc1234 Add feature A
squash def5678 Fix typo
pick ghi9012 Add feature B

# Result: 2 commits instead of 3
```

---

### 7. Cherry-Pick

**What is Cherry-Pick?**
Apply specific commits from one branch to another.

```bash
# Pick single commit
git cherry-pick abc1234

# Pick multiple commits
git cherry-pick abc1234 def5678

# Pick without committing
git cherry-pick --no-commit abc1234

# Abort cherry-pick
git cherry-pick --abort
```

---

### 8. Branch Management Best Practices

**Naming Conventions:**
```
feature/login-page
bugfix/fix-payment-error
hotfix/security-patch
release/v1.2.0
```

**Branch Strategy:**
```
main         # Production-ready code
develop      # Integration branch
feature/*    # New features
hotfix/*     # Critical fixes
release/*    # Release preparation
```

**Clean Up:**
```bash
# Delete merged branches
git branch --merged | grep -v main | xargs git branch -d

# Prune remote branches
git fetch --prune
git remote prune origin
```

---

## 💻 Complete Example

```bash
# 1. Create feature branch
git checkout -b feature-user-auth

# 2. Make changes
echo "// Auth code" > auth.js
git add auth.js
git commit -m "Add authentication"

# 3. More changes
echo "// More auth" >> auth.js
git commit -am "Complete authentication"

# 4. Update from main
git checkout main
git pull origin main

# 5. Merge main into feature (stay updated)
git checkout feature-user-auth
git merge main
# Or rebase:
git rebase main

# 6. Resolve conflicts if any
# Edit files, then:
git add .
git rebase --continue

# 7. Merge feature into main
git checkout main
git merge feature-user-auth

# 8. Push changes
git push origin main

# 9. Delete feature branch
git branch -d feature-user-auth
```

---

## 🎯 Interview Questions

### Q1: Merge vs Rebase - when to use which?

**Answer:**
- **Merge**: Use for public/shared branches, preserves history
- **Rebase**: Use for local cleanup, creates linear history

Never rebase public branches!

### Q2: How to resolve merge conflicts?

**Answer:**
1. `git status` to see conflicted files
2. Open files and edit (remove <<<<, ====, >>>>)
3. `git add` resolved files
4. `git commit` to complete merge

### Q3: What is fast-forward merge?

**Answer:**
When target branch hasn't diverged, Git simply moves pointer forward. No merge commit created.

### Q4: How to undo a merge?

**Answer:**
```bash
# If not pushed yet
git reset --hard HEAD~1

# If already pushed
git revert -m 1 <merge-commit-hash>
```

---

## ✅ Practice Exercises

1. Create multiple branches
2. Switch between branches
3. Merge branches
4. Create merge conflicts intentionally
5. Resolve conflicts
6. Practice rebase
7. Use interactive rebase
8. Cherry-pick commits
9. Delete old branches
10. Practice branch strategies

---

**👉 Next:** [Collaboration →](../03-collaboration/README.md)

