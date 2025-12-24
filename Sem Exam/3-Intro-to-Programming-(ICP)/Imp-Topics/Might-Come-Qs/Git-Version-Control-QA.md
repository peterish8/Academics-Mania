# 🎯 Git & Version Control - Exam Q&A (2.5 Marks)

> [!TIP] Click on the green boxes to reveal answers!

---

## 📌 Part 1: Core Theory Questions

### Q1: Define Version Control System (VCS). Why is it essential?

> [!SUCCESS]- Answer
> **Version Control System (VCS)** is a software tool that tracks and manages changes to files over time.
> 
> **Why Essential:**
> - 📜 Maintains complete history of changes
> - 🔄 Allows reverting to previous versions
> - 👥 Enables team collaboration
> - 🌿 Supports parallel development via branches
> - 🔒 Provides backup and recovery

---

### Q2: Centralized vs Distributed VCS - Explain the difference.

> [!SUCCESS]- Answer
> | Feature | Centralized (SVN) | Distributed (Git) |
> |---------|-------------------|-------------------|
> | **Storage** | Single central server | Every user has full copy |
> | **Offline work** | ❌ Needs server | ✅ Works offline |
> | **Speed** | Slower (server calls) | Faster (local) |
> | **Single point of failure** | ✅ Yes | ❌ No |
> | **Example** | SVN, CVS | Git, Mercurial |

---

### Q3: Explain the Three States of Git.

> [!SUCCESS]- Answer
> 1. **Working Directory** - Your actual files where you edit code
> 2. **Staging Area (Index)** - Files marked for next commit (`git add`)
> 3. **Git Directory (Repository)** - Where Git stores history (`.git` folder)
> 
> **Flow:** Working → Staging → Repository
> ```
> Edit file → git add → git commit
> ```

---

### Q4: What causes a Merge Conflict? How to resolve?

> [!SUCCESS]- Answer
> **Cause:** Two branches modify the same line in a file differently.
> 
> **Resolution Steps:**
> 1. Open conflicted file
> 2. Look for conflict markers:
> ```
> <<<<<<< HEAD
> your changes
> =======
> their changes
> >>>>>>> branch-name
> ```
> 3. Manually edit to keep correct code
> 4. Remove conflict markers
> 5. `git add <file>` and `git commit`

---

### Q5: Benefits of using branches for development?

> [!SUCCESS]- Answer
> - 🧪 **Isolation** - Work on features without affecting main code
> - 👥 **Parallel Development** - Multiple features at same time
> - 🐛 **Bug Fixes** - Hotfix branches for urgent fixes
> - 🔒 **Stable Main** - Main branch always deployable
> - 📋 **Code Review** - Review before merging

---

### Q6: Outline Git Workflow (init to push)

> [!SUCCESS]- Answer
> ```bash
> git init                    # Initialize repo
> git add .                   # Stage files
> git commit -m "message"     # Commit locally
> git remote add origin URL   # Connect to remote
> git push -u origin main     # Push to remote
> ```

---

## 📌 Part 2: Commands & Concepts

### Q7: What does `git add` do?

> [!SUCCESS]- Answer
> Moves files from **Working Directory** to **Staging Area**.
> ```bash
> git add file.txt     # Stage single file
> git add .            # Stage all files
> git add *.py         # Stage all Python files
> ```

---

### Q8: What does `git commit` do?

> [!SUCCESS]- Answer
> Saves staged changes to the **local repository** with a message.
> ```bash
> git commit -m "Add login feature"
> git commit -am "Quick commit"  # Add + Commit
> ```

---

### Q9: How to switch branches?

> [!SUCCESS]- Answer
> ```bash
> git checkout branch-name     # Old way
> git switch branch-name       # New way (Git 2.23+)
> git checkout -b new-branch   # Create + switch
> git switch -c new-branch     # Create + switch (new)
> ```

---

### Q10: What does `git merge` do?

> [!SUCCESS]- Answer
> Combines changes from one branch into another.
> ```bash
> git checkout main        # Go to target branch
> git merge feature        # Merge feature into main
> ```

---

### Q11: Difference between `git fetch` and `git pull`?

> [!SUCCESS]- Answer
> | Command | Action |
> |---------|--------|
> | `git fetch` | Downloads changes but doesn't merge |
> | `git pull` | Downloads + automatically merges |
> 
> `git pull` = `git fetch` + `git merge`

---

### Q12: How to push code to remote?

> [!SUCCESS]- Answer
> ```bash
> git push origin main           # Push to main
> git push -u origin main        # Set upstream + push
> git push                       # After setting upstream
> ```

---

### Q13: What is a Remote Repository?

> [!SUCCESS]- Answer
> A **version of your repository hosted on the internet** (GitHub, GitLab).
> - `origin` is the default remote name
> - Allows sharing code with team

---

### Q14: How to add a remote?

> [!SUCCESS]- Answer
> ```bash
> git remote add origin https://github.com/user/repo.git
> git remote -v                  # View remotes
> git remote remove origin       # Remove remote
> ```

---

### Q15: What is a Pull Request (PR)?

> [!SUCCESS]- Answer
> A **request to merge your branch** into another branch (usually main).
> - Used for code review before merging
> - Shows diff of changes
> - Team can comment and approve

---

### Q16: Why use main branch?

> [!SUCCESS]- Answer
> - 🔒 **Stable code** - Always deployable
> - 📋 **Production ready** - What users see
> - 🌿 **Base for branches** - All features branch from here

---

### Q17: What is `git log`?

> [!SUCCESS]- Answer
> Shows commit history.
> ```bash
> git log                    # Full log
> git log --oneline          # Compact view
> git log -n 5               # Last 5 commits
> git log --graph            # Visual branch tree
> ```

---

### Q18: How to check differences?

> [!SUCCESS]- Answer
> ```bash
> git diff                   # Working vs Staging
> git diff --staged          # Staging vs Last commit
> git diff branch1 branch2   # Between branches
> ```

---

### Q19: What is `git stash`?

> [!SUCCESS]- Answer
> **Temporarily saves uncommitted changes** without committing.
> ```bash
> git stash                  # Save changes
> git stash pop              # Restore + delete stash
> git stash list             # View all stashes
> git stash apply            # Restore but keep stash
> ```

---

### Q20: What are Git Tags?

> [!SUCCESS]- Answer
> **Markers for specific commits** (usually releases).
> ```bash
> git tag v1.0.0             # Create tag
> git tag -a v1.0 -m "msg"   # Annotated tag
> git push origin --tags     # Push tags
> ```

---

### Q21: What is `.gitignore` file?

> [!SUCCESS]- Answer
> Specifies files Git should **ignore** (not track).
> ```
> # .gitignore example
> *.pyc              # Ignore all .pyc files
> __pycache__/       # Ignore folder
> .env               # Ignore secrets
> node_modules/      # Ignore dependencies
> ```

---

### Q22: Difference between Git and GitHub?

> [!SUCCESS]- Answer
> | Git | GitHub |
> |-----|--------|
> | Version control **software** | **Hosting platform** for Git repos |
> | Works locally | Works online |
> | Command-line tool | Web interface + features |
> | Free & open source | Free + paid plans |

---

### Q23: What is Open Source?

> [!SUCCESS]- Answer
> Software with **publicly available source code** that anyone can view, modify, and distribute.
> - Examples: Linux, Git, VS Code
> - Encourages community contribution

---

### Q24: How to contribute to Open Source?

> [!SUCCESS]- Answer
> 1. **Fork** the repository
> 2. **Clone** your fork locally
> 3. Create a **branch** for changes
> 4. Make changes and **commit**
> 5. **Push** to your fork
> 6. Create a **Pull Request**

---

### Q25: Command to initialize a repo?

> [!SUCCESS]- Answer
> ```bash
> git init                   # Create new repo
> git init project-name      # Create in new folder
> ```

---

### Q26: Command to clone a repo?

> [!SUCCESS]- Answer
> ```bash
> git clone https://github.com/user/repo.git
> git clone URL folder-name  # Clone into specific folder
> ```

---

### Q27: What is Staging?

> [!SUCCESS]- Answer
> The **intermediate area** where you prepare files for commit.
> - Files must be staged before committing
> - Allows selective commits

---

### Q28: What does `git help` do?

> [!SUCCESS]- Answer
> Shows help documentation.
> ```bash
> git help              # General help
> git help commit       # Help for specific command
> git commit --help     # Same as above
> ```

---

### Q29: Remote vs Local Repository?

> [!SUCCESS]- Answer
> | Local | Remote |
> |-------|--------|
> | On your computer | On server (GitHub) |
> | You work here | Team shares here |
> | Full history | Full history |
> | `git commit` | `git push/pull` |

---

### Q30: What is Cloning?

> [!SUCCESS]- Answer
> **Creating a complete copy** of a remote repository on your computer.
> - Downloads all files + history
> - Sets up remote connection automatically

---

### Q31: What is Semantic Versioning?

> [!SUCCESS]- Answer
> Version format: **MAJOR.MINOR.PATCH** (e.g., 2.1.3)
> - **MAJOR** - Breaking changes
> - **MINOR** - New features (backward compatible)
> - **PATCH** - Bug fixes

---

### Q32: Rebase vs Merge - Difference?

> [!SUCCESS]- Answer
> | Merge | Rebase |
> |-------|--------|
> | Creates merge commit | Rewrites commit history |
> | Preserves history | Linear history |
> | Safer for shared branches | Cleaner but risky |

---

### Q33: How to list all branches?

> [!SUCCESS]- Answer
> ```bash
> git branch             # Local branches
> git branch -a          # All (local + remote)
> git branch -r          # Remote only
> ```

---

### Q34: What is GPL? Full form?

> [!SUCCESS]- Answer
> **GNU General Public License**
> - Open source license
> - **Requires:** If you modify and distribute, you must share source code
> - Ensures software stays free

---

### Q35: What does GPL require?

> [!SUCCESS]- Answer
> - 📖 **Source code must be available**
> - 🔄 **Derivatives must use same license**
> - 📝 **Include license and copyright**
> - ❌ **Cannot make it proprietary**

---

## 🧠 Quick Command Reference

| Action | Command |
|--------|---------|
| Initialize | `git init` |
| Clone | `git clone URL` |
| Stage | `git add .` |
| Commit | `git commit -m "msg"` |
| Push | `git push origin main` |
| Pull | `git pull` |
| Branch | `git branch name` |
| Switch | `git switch name` |
| Merge | `git merge branch` |
| Stash | `git stash` |
| Log | `git log --oneline` |

---

[[Imp-Topics-Hub|← Back to Hub]]
