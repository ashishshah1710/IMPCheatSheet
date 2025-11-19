# 🚀 Git Advanced Topics

**Phase 4: Master Advanced Techniques (3-4 Days)**

---

## 📖 Overview

Learn advanced Git techniques for complex scenarios and troubleshooting.

---

## 🎯 Learning Objectives

✅ Interactive rebase mastery  
✅ Cherry-pick effectively  
✅ Use git stash  
✅ Create git hooks  
✅ Recover lost commits  
✅ Advanced troubleshooting  

---

## 📚 Core Topics

### 1. Interactive Rebase

**Clean Up Commits:**
```bash
# Interactive rebase last 5 commits
git rebase -i HEAD~5
```

**Options:**
```
pick    abc1234 Add feature A
reword  def5678 Fix typo          # Edit message
edit    ghi9012 Add feature B     # Stop to amend
squash  jkl3456 Update feature A  # Combine with previous
fixup   mno7890 Minor fix         # Combine, discard message
drop    pqr1234 Experimental      # Remove commit
```

**Example Workflow:**
```bash
# Before: 5 messy commits
# After: 2 clean commits

git rebase -i HEAD~5
# Squash related commits
# Reword messages
# Drop unnecessary commits
```

---

### 2. Git Stash

**Basic Stash:**
```bash
# Stash changes
git stash

# Stash with message
git stash save "Work in progress on feature X"

# Stash including untracked files
git stash -u

# List stashes
git stash list

# Apply latest stash
git stash apply

# Apply and remove stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

**Create Branch from Stash:**
```bash
git stash branch feature-from-stash
```

---

### 3. Cherry-Pick

**Pick Commits:**
```bash
# Pick single commit
git cherry-pick abc1234

# Pick multiple commits
git cherry-pick abc1234 def5678

# Pick range of commits
git cherry-pick abc1234^..def5678

# Pick without committing
git cherry-pick --no-commit abc1234

# Continue after conflict
git cherry-pick --continue

# Abort cherry-pick
git cherry-pick --abort
```

---

### 4. Git Hooks

**Hook Types:**
- `pre-commit`: Before commit
- `commit-msg`: Validate commit message
- `pre-push`: Before push
- `post-merge`: After merge

**Example pre-commit Hook:**
```bash
#!/bin/sh
# .git/hooks/pre-commit

# Run tests
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit rejected."
    exit 1
fi

# Run linter
npm run lint
if [ $? -ne 0 ]; then
    echo "Linting failed. Commit rejected."
    exit 1
fi

exit 0
```

**Example commit-msg Hook:**
```bash
#!/bin/sh
# .git/hooks/commit-msg

# Validate commit message format
COMMIT_MSG=$(cat $1)

if ! echo "$COMMIT_MSG" | grep -qE "^(feat|fix|docs|style|refactor|test|chore):"; then
    echo "Invalid commit message format."
    echo "Use: feat|fix|docs|style|refactor|test|chore: message"
    exit 1
fi

exit 0
```

---

### 5. Git Reflog

**What is Reflog?**
Reference log - tracks all ref updates.

**Use Reflog:**
```bash
# Show reflog
git reflog

# Show reflog for branch
git reflog show main

# Recover lost commit
git reflog
git checkout abc1234

# Recover deleted branch
git reflog
git branch feature-recovered abc1234
```

**Example Recovery:**
```bash
# Oh no! Deleted important commit
git reset --hard HEAD~3

# Recover using reflog
git reflog
# HEAD@{1}: commit: Important change

git reset --hard HEAD@{1}
# Recovered!
```

---

### 6. Bisect (Find Bugs)

**Binary Search for Bugs:**
```bash
# Start bisect
git bisect start

# Mark current as bad
git bisect bad

# Mark known good commit
git bisect good abc1234

# Git checks out middle commit
# Test it, then mark:
git bisect good  # or
git bisect bad

# Repeat until found
# Git identifies first bad commit

# Reset
git bisect reset
```

---

### 7. Submodules

**Add Submodule:**
```bash
# Add submodule
git submodule add https://github.com/user/lib.git libs/lib

# Clone with submodules
git clone --recurse-submodules <repo-url>

# Update submodules
git submodule update --init --recursive

# Pull submodule updates
git submodule update --remote
```

---

### 8. Advanced Troubleshooting

**Find Who Changed Line:**
```bash
git blame file.txt
git blame -L 10,20 file.txt  # Specific lines
```

**Find Commit that Added/Removed Text:**
```bash
git log -S "search text"
git log --grep="pattern"
```

**Diff Between Branches:**
```bash
git diff main..feature
git diff main...feature  # Since diverged
```

**Find Lost Commits:**
```bash
git fsck --lost-found
```

**Rewrite History (Dangerous!):**
```bash
# Change author of last commit
git commit --amend --author="New Name <email@example.com>"

# Change author of multiple commits
git filter-branch --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "old@example.com" ]
then
    export GIT_COMMITTER_EMAIL="new@example.com"
    export GIT_COMMITTER_NAME="New Name"
fi
' -- --all
```

---

## 🎯 Interview Questions

### Q1: What is git reflog and when to use it?

**Answer:**
Reflog is a log of all reference updates. Use it to:
- Recover lost commits
- Undo git reset --hard
- Find deleted branches
- Track all HEAD movements

### Q2: How to find which commit introduced a bug?

**Answer:**
Use `git bisect`:
1. `git bisect start`
2. Mark current as bad: `git bisect bad`
3. Mark known good: `git bisect good <commit>`
4. Test each commit Git checks out
5. Mark as good/bad until found

### Q3: What are Git hooks?

**Answer:**
Scripts that run automatically on Git events:
- pre-commit: Before committing
- commit-msg: Validate commit message
- pre-push: Before pushing
- post-merge: After merging

Use for: testing, linting, validation.

### Q4: How to temporarily save changes without committing?

**Answer:**
```bash
git stash          # Save changes
git stash pop      # Restore changes
```

---

## ✅ Practice Exercises

- [ ] Clean commit history with interactive rebase
- [ ] Use git stash effectively
- [ ] Cherry-pick commits
- [ ] Create git hooks
- [ ] Recover lost commits with reflog
- [ ] Find bugs with bisect
- [ ] Work with submodules
- [ ] Practice troubleshooting

---

**👉 Next:** [Interview Questions →](../interview-questions/README.md)

