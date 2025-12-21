# 04 Core Git Concepts

## 🗂️ Key Git Components

Understanding these four core concepts is essential for mastering Git workflow.

| **Concept**           | **Description**                                                                                                                                                                    | **Purpose**                                                                                                           | **Example / Analogy**                                                                               |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Repository**        | The Git **database** that stores your entire project history — every commit, branch, and file version. It exists both **locally** (on your computer) and **remotely** (on GitHub). | Acts as the **central storage** for all versions of your code. Lets you track history, revert, or collaborate easily. | 🏦 *Like a cloud drive that keeps every past version of your project — not just the latest one.*    |
| **Working Directory** | The **actual folder** on your system where you create, edit, and delete files.                                                                                                     | It's your **active workspace** where you make real changes to your code.                                              | 💻 *Like writing or editing a document on your desk before saving it.*                              |
| **Staging Area**      | A **temporary zone** (also called the **index**) where Git keeps track of changes you want to include in your next commit.                                                         | It's a **pre-commit review area**, letting you choose which modifications are ready to be saved.                      | 🧾 *Like collecting and reviewing your homework before submitting it.*                              |
| **Commit**            | A **snapshot** of all staged files, saved permanently in the repository. Each commit has an ID and message describing the changes.                                                 | Serves as a **save point in project history**, allowing you to go back or compare versions anytime.                   | 📸 *Like taking a picture of your work at a particular stage — you can always revisit that moment.* |

## 📁 Repository (Repo)

A **repository** is the complete storage of your project including:
- All files and folders
- Complete change history
- Branch information
- Configuration settings

```bash
# Initialize a new repository
git init

# Clone existing repository
git clone https://github.com/user/project.git
```

### Types of Repositories
- **Local Repository**: On your computer
- **Remote Repository**: On GitHub, GitLab, etc.
- **Bare Repository**: Server-side, no working directory

## 💼 Working Directory

The **working directory** is your project folder where you:
- Edit files
- Add new files
- Delete files
- Organize project structure

```bash
# Check working directory status
git status

# See what files changed
git diff
```

### File States in Working Directory
- **Untracked**: New files Git doesn't know about
- **Modified**: Changed files that Git is tracking
- **Deleted**: Removed files that were previously tracked

## 🎭 Staging Area (Index)

The **staging area** is a preparation zone where you:
- Select which changes to include in next commit
- Review changes before making them permanent
- Group related changes together

```bash
# Add specific file to staging
git add filename.txt

# Add all changes to staging
git add .

# Remove from staging (keep changes in working directory)
git reset filename.txt
```

### 💡 Why Use Staging Area?
- **Selective commits**: Choose exactly what to save
- **Quality control**: Review before committing
- **Logical grouping**: Combine related changes
- **Partial commits**: Commit some changes, keep others for later

## 📸 Commit

A **commit** is a permanent snapshot that includes:
- All staged changes
- Commit message describing changes
- Author information
- Timestamp
- Unique identifier (hash)

```bash
# Create commit with message
git commit -m "Add user login functionality"

# Commit with detailed message
git commit -m "Add user login

- Implement login form validation
- Add password encryption
- Create session management
- Add logout functionality"
```

### 🎯 Good Commit Practices
- **Clear messages**: Describe what and why
- **Atomic commits**: One logical change per commit
- **Present tense**: "Add feature" not "Added feature"
- **Imperative mood**: "Fix bug" not "Fixes bug"

## 🔄 Git Workflow Visualization

```
Working Directory  →  Staging Area  →  Repository
     (edit)           (git add)        (git commit)
       ↓                  ↓               ↓
   file.txt          file.txt        Commit ABC123
   (modified)        (staged)        "Add new feature"
```

## 📊 Three States of Git

Every file in your Git repository exists in one of these states:

### 1. Modified
- File has been changed in working directory
- Changes not yet staged for commit
- **VS Code indicator**: `M` (modified)

### 2. Staged  
- File changes are marked for next commit
- Changes are in staging area
- **VS Code indicator**: `A` (added) or `M` (modified staged)

### 3. Committed
- Changes are safely stored in repository
- File is clean in working directory
- **VS Code indicator**: No indicator (clean state)

## 🛠️ Essential Commands Summary

```bash
# Repository operations
git init                    # Initialize new repo
git clone <url>            # Copy remote repo

# Working directory
git status                 # Check file states
git diff                   # See unstaged changes
git diff --staged          # See staged changes

# Staging area
git add <file>             # Stage specific file
git add .                  # Stage all changes
git reset <file>           # Unstage file

# Commits
git commit -m "message"    # Create commit
git log                    # View commit history
git log --oneline          # Compact history view
```

## 🧩 Quick Recap

✅ **Repository**: Complete project storage with history  
✅ **Working Directory**: Where you edit files  
✅ **Staging Area**: Preparation zone for commits  
✅ **Commit**: Permanent snapshot with message  
✅ **Three states**: Modified → Staged → Committed  

---

**[← Previous: VCS Comparison](03_VCS_Comparison.md) | [Next → Installing Git](05_Installing_Git.md)**