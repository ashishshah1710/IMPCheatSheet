# 📦 Git - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master Git for professional software development and ace your technical interviews!

---

## 📖 Overview

Git is the most widely used version control system. Understanding Git deeply is essential for professional developers working in teams and managing code effectively.

### Why Git?

✅ **Version Control** - Track code changes  
✅ **Collaboration** - Work with teams effectively  
✅ **Branching** - Parallel development  
✅ **History** - Complete project history  
✅ **Distributed** - Every clone is a full backup  
✅ **Industry Standard** - Used by 95%+ development teams  

---

## 🎯 Learning Path

### Phase 1: Git Basics (2-3 days)
**Fundamental commands and concepts**

- Git initialization and configuration
- Basic workflow (add, commit, push, pull)
- Repository structure
- Working directory, staging area, repository
- Commit history and logs

**👉 Start:** [`01-basics/README.md`](01-basics/README.md)

---

### Phase 2: Branching & Merging (2-3 days)
**Master branch management**

- Creating and switching branches
- Merging strategies
- Resolving conflicts
- Rebase vs merge
- Branch management best practices

**👉 Continue:** [`02-branching/README.md`](02-branching/README.md)

---

### Phase 3: Collaboration (2-3 days)
**Team workflows and best practices**

- Remote repositories
- Pull requests
- Code review process
- Git workflows (GitFlow, GitHub Flow)
- Fork and pull model
- Team collaboration best practices

**👉 Master:** [`03-collaboration/README.md`](03-collaboration/README.md)

---

### Phase 4: Advanced Topics (3-4 days)
**Advanced Git techniques**

- Interactive rebase
- Cherry-pick
- Git stash
- Submodules and subtrees
- Git hooks
- Rewriting history
- Advanced troubleshooting

**👉 Advanced:** [`04-advanced/README.md`](04-advanced/README.md)

---

## 💼 Interview Preparation

### Common Git Interview Topics

**Basic Questions:**
- What is Git and how does it work?
- Difference between Git and GitHub?
- Explain staging area
- What is a commit?
- Git clone vs fork

**Branching:**
- What is a branch?
- Merge vs rebase - when to use which?
- How to resolve merge conflicts?
- Fast-forward merge vs three-way merge
- Branch naming conventions

**Collaboration:**
- Explain pull request workflow
- How to review code effectively?
- Git workflows you've used
- Handling large binary files
- Monorepo vs multi-repo

**Advanced:**
- What is cherry-pick?
- Interactive rebase use cases
- Git reflog - what and when?
- How to undo commits?
- Squashing commits

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 📚 Content Structure

```
git/
├── 01-basics/
│   ├── README.md                    # Git fundamentals
│   ├── setup-config.md             # Installation & config
│   ├── basic-commands.md           # Essential commands
│   └── understanding-git.md        # How Git works
│
├── 02-branching/
│   ├── README.md                    # Branching guide
│   ├── creating-branches.md        # Branch operations
│   ├── merging.md                  # Merge strategies
│   └── conflict-resolution.md      # Resolving conflicts
│
├── 03-collaboration/
│   ├── README.md                    # Team workflows
│   ├── remote-repos.md             # Working with remotes
│   ├── pull-requests.md            # PR workflow
│   └── git-workflows.md            # Popular workflows
│
├── 04-advanced/
│   ├── README.md                    # Advanced topics
│   ├── interactive-rebase.md       # Rewriting history
│   ├── cherry-pick.md              # Selective commits
│   ├── stash.md                    # Temporary storage
│   └── hooks.md                    # Automation
│
├── interview-questions/
│   ├── README.md                    # All questions
│   ├── basic-questions.md          # Fundamentals
│   ├── scenario-based.md           # Real scenarios
│   └── troubleshooting.md          # Fixing issues
│
└── CHEATSHEET.md                    # Quick reference
```

---

## 🎯 Quick Reference

### Most Used Commands

```bash
# Initialize
git init
git clone <url>

# Basic Workflow
git add <file>
git commit -m "message"
git push origin main
git pull origin main

# Branching
git branch <branch-name>
git checkout <branch-name>
git checkout -b <branch-name>
git merge <branch-name>

# Status & History
git status
git log
git log --oneline --graph --all

# Remote
git remote add origin <url>
git remote -v
git fetch origin
git push -u origin main

# Undo
git reset HEAD~1
git revert <commit>
git checkout -- <file>
```

---

## 🏆 For Experienced Developers

### What Interviewers Expect

**Technical Knowledge:**
- Deep understanding of Git internals
- Multiple workflow strategies
- Conflict resolution expertise
- Advanced commands usage
- Git best practices

**Real-World Experience:**
- Managing large repositories
- Team collaboration patterns
- Code review processes
- CI/CD integration
- Troubleshooting Git issues

**Problem-Solving:**
- Recovering lost commits
- Fixing merge conflicts
- Cleaning up commit history
- Managing releases
- Security considerations

---

## 📊 Interview Success Metrics

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Basic Commands | 🔴 Critical | 95% |
| Branching & Merging | 🔴 Critical | 90% |
| Merge Conflicts | 🔴 Critical | 85% |
| Pull Requests | 🟡 Important | 80% |
| Rebase vs Merge | 🟡 Important | 75% |
| Git Workflows | 🟡 Important | 70% |
| Cherry-pick | 🟢 Good to Know | 50% |
| Advanced Topics | 🟢 Good to Know | 40% |

---

## 🎓 Learning Resources

### Official Documentation
- [Git Official Docs](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Reference](https://git-scm.com/docs)

### Interactive Learning
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Immersion](https://gitimmersion.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

### Practice
- Create GitHub repositories
- Contribute to open source
- Practice conflict resolution
- Try different workflows

---

## ✅ Preparation Checklist

### Basics
- [ ] Understand Git architecture
- [ ] Master basic commands
- [ ] Know staging area concept
- [ ] Understand commits
- [ ] Read commit history

### Branching
- [ ] Create and delete branches
- [ ] Switch between branches
- [ ] Merge branches
- [ ] Resolve conflicts
- [ ] Understand rebase

### Collaboration
- [ ] Work with remotes
- [ ] Create pull requests
- [ ] Review code
- [ ] Know GitFlow
- [ ] Understand fork model

### Advanced
- [ ] Interactive rebase
- [ ] Cherry-pick commits
- [ ] Use git stash
- [ ] Create git hooks
- [ ] Recover lost commits

---

## 🚀 Career Impact

### Why Git Expertise Matters

**Job Requirements:**
- **100% of** software engineering jobs require Git
- **80%+** interview processes test Git knowledge
- **Team collaboration** relies on Git proficiency

**Career Benefits:**
- Faster code reviews
- Better collaboration
- Fewer conflicts
- Cleaner history
- Professional credibility

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Basics | [01-basics/README.md](01-basics/README.md) |
| Branching | [02-branching/README.md](02-branching/README.md) |
| Collaboration | [03-collaboration/README.md](03-collaboration/README.md) |
| Advanced | [04-advanced/README.md](04-advanced/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

## 🎯 Next Steps

1. **Learn Basics** - Start with [`01-basics/README.md`](01-basics/README.md)
2. **Practice Branching** - [`02-branching/README.md`](02-branching/README.md)
3. **Master Collaboration** - [`03-collaboration/README.md`](03-collaboration/README.md)
4. **Study Interview Questions** - [`interview-questions/README.md`](interview-questions/README.md)
5. **Practice Daily** - Use Git in all your projects

---

**Ready to master Git?** 📦

👉 **[Start with Basics →](01-basics/README.md)**

