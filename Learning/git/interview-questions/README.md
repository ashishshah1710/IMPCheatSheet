# 💼 Git Interview Questions

**Comprehensive Interview Preparation**

---

## Basic Questions

### Q1: What is Git?

**Answer:** Git is a distributed version control system that tracks changes in source code. Key features:
- Distributed (every clone is full backup)
- Fast and efficient
- Branching and merging
- Complete history
- Open source

---

### Q2: Git vs GitHub/GitLab?

**Answer:**
- **Git**: Version control system (software)
- **GitHub/GitLab**: Hosting platforms for Git repositories (services)

---

### Q3: Explain Git workflow

**Answer:**
1. Modify files (Working Directory)
2. Stage changes (Staging Area): `git add`
3. Commit (Repository): `git commit`
4. Push to remote: `git push`

---

### Q4: What is staging area?

**Answer:** Intermediate area between working directory and repository. Allows selective committing of changes.

```
Working Dir → Stage → Repository
   (edit)   git add   git commit
```

---

## Branching Questions

### Q5: What is a branch?

**Answer:** A pointer to a commit. Allows parallel development without affecting main codebase.

---

### Q6: Merge vs Rebase?

**Answer:**

| Merge | Rebase |
|-------|--------|
| Preserves history | Rewrites history |
| Creates merge commit | Linear history |
| Use for public branches | Use for local cleanup |
| Safer | Riskier |

**Rule:** Never rebase public branches!

---

### Q7: Fast-forward vs three-way merge?

**Answer:**
- **Fast-forward**: Target hasn't diverged, just move pointer
- **Three-way**: Branches diverged, create merge commit

---

### Q8: How to resolve merge conflicts?

**Answer:**
1. `git status` - see conflicted files
2. Edit files (remove <<<<, ====, >>>>)
3. `git add` - stage resolved files
4. `git commit` - complete merge

---

## Collaboration Questions

### Q9: Git fetch vs Git pull?

**Answer:**
- `git fetch`: Download changes, don't merge
- `git pull`: Download and merge (fetch + merge)

---

### Q10: What is a Pull Request?

**Answer:** Request to merge changes. Enables:
- Code review
- Discussion
- CI/CD checks
- Approval workflow

---

### Q11: Fork vs Clone?

**Answer:**
- **Fork**: Create copy on GitHub (for contributing)
- **Clone**: Copy to local machine

---

## Advanced Questions

### Q12: What is HEAD?

**Answer:** Pointer to current branch/commit. Represents where you are.

```
HEAD        # Current
HEAD~1      # One before
HEAD~2      # Two before
```

---

### Q13: What is git reflog?

**Answer:** Log of all reference updates. Use to:
- Recover lost commits
- Undo hard resets
- Find deleted branches

---

### Q14: Git reset --soft vs --mixed vs --hard?

**Answer:**
```bash
--soft   # Keep changes staged
--mixed  # Keep changes unstaged (default)
--hard   # Discard all changes (dangerous!)
```

---

### Q15: What is cherry-pick?

**Answer:** Apply specific commit from one branch to another.

```bash
git cherry-pick abc1234
```

Use case: Port bugfix to multiple branches.

---

## Scenario-Based Questions

### Q16: Committed to wrong branch. How to fix?

**Answer:**
```bash
# If not pushed
git reset HEAD~1       # Undo commit
git stash              # Save changes
git checkout correct-branch
git stash pop          # Apply changes
git add .
git commit -m "message"
```

---

### Q17: Accidentally deleted branch. How to recover?

**Answer:**
```bash
git reflog
git checkout -b recovered-branch abc1234
```

---

### Q18: Need to undo last 3 commits

**Answer:**
```bash
# Keep changes
git reset HEAD~3

# Discard changes
git reset --hard HEAD~3

# If already pushed
git revert HEAD~3..HEAD
```

---

### Q19: Large file committed by mistake

**Answer:**
```bash
# Not pushed yet
git reset HEAD~1
git rm --cached large-file.zip
git commit -m "Remove large file"

# Already pushed
# Use git filter-branch or BFG Repo-Cleaner
```

---

### Q20: Merge conflict in multiple files

**Answer:**
```bash
# View conflicts
git status

# For each file:
# 1. Edit and resolve
# 2. git add file.txt

# Or use tools
git mergetool

# Complete merge
git commit
```

---

## Troubleshooting Questions

### Q21: Git push rejected

**Answer:**
```bash
# Fetch and merge first
git pull origin main

# Or rebase
git pull --rebase origin main

# Then push
git push origin main
```

---

### Q22: Detached HEAD state

**Answer:**
Checked out specific commit, not a branch.

```bash
# Create branch from here
git checkout -b new-branch

# Or go back to branch
git checkout main
```

---

### Q23: How to find commit that introduced bug?

**Answer:**
```bash
# Use bisect
git bisect start
git bisect bad
git bisect good <known-good-commit>
# Test each checkout
git bisect good/bad
# Identifies first bad commit
git bisect reset
```

---

## Best Practices Questions

### Q24: Good commit message format?

**Answer:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

Example:
```
feat(auth): add JWT authentication

Implement JWT-based authentication for API endpoints.
Includes token generation and validation.

Closes #123
```

Types: feat, fix, docs, style, refactor, test, chore

---

### Q25: Branch naming conventions?

**Answer:**
```
feature/feature-name
bugfix/bug-description
hotfix/urgent-fix
release/v1.2.0
```

---

### Q26: How often to commit?

**Answer:**
- Commit logical units of work
- Each commit should be working code
- Commit often (easier to undo)
- One feature per commit
- Use descriptive messages

---

### Q27: Git workflows you've used?

**Answer:**
- **GitHub Flow**: Simple, main + feature branches
- **GitFlow**: Complex, multiple branch types
- **Trunk-Based**: Frequent integration to main

Choose based on team size and release frequency.

---

## Quick Tips for Interviews

1. **Know the basics cold**: add, commit, push, pull, branch, merge
2. **Understand why**: Don't just memorize commands
3. **Real examples**: Share actual scenarios you've handled
4. **Troubleshooting**: Practice fixing common issues
5. **Best practices**: Show you write clean commit history

---

**[← Back to Main](../README.md)**

