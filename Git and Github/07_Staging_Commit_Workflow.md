# 07 Understanding Staging and Commit Workflow

## 🔄 The Three States of Git

Git manages files through three distinct areas, creating a powerful workflow for tracking changes.

| State | Location | Description | VS Code Indicator |
|-------|----------|-------------|-------------------|
| **Working Directory** | Your project folder | Where you edit files | File explorer |
| **Staging Area** | Git index | Pre-commit preparation zone | Source Control panel |
| **Repository** | .git folder | Permanent commit history | Git History |

## 📁 File States in Detail

Every file in your Git project exists in one of these states:

### 1. Untracked
- **Meaning**: Git doesn't know about this file yet
- **VS Code**: `U` symbol in Source Control
- **Action**: Use `git add` to start tracking

### 2. Tracked (Unmodified)
- **Meaning**: File is in Git but hasn't changed
- **VS Code**: No symbol (clean state)
- **Action**: Edit file to make it modified

### 3. Modified
- **Meaning**: File changed but not staged for commit
- **VS Code**: `M` symbol in Source Control
- **Action**: Use `git add` to stage changes

### 4. Staged
- **Meaning**: Changes marked for next commit
- **VS Code**: `A` (new) or `M` (modified) in staged section
- **Action**: Use `git commit` to save permanently

## 🎯 Complete Workflow Example

Let's walk through a real project workflow:

### Step 1: Create and Edit Files
```bash
# Create a new file
echo "# My Project" >> README.md
echo "console.log('Hello World');" >> app.js

# Check status
git status
```

**Output:**
```
Untracked files:
  README.md
  app.js
```

### Step 2: Stage Files
```bash
# Stage specific file
git add README.md

# Stage all files
git add .

# Check status after staging
git status
```

**Output:**
```
Changes to be committed:
  new file:   README.md
  new file:   app.js
```

### Step 3: Commit Changes
```bash
# Create commit with descriptive message
git commit -m "Add initial project files

- Create README with project description
- Add basic JavaScript application file"
```

### Step 4: Modify Existing Files
```bash
# Edit existing file
echo "## Installation" >> README.md

# Check what changed
git status
git diff
```

**Output:**
```
Changes not staged for commit:
  modified:   README.md
```

## 🛠️ Essential Staging Commands

### Adding Files to Staging
```bash
# Stage specific file
git add filename.txt

# Stage multiple files
git add file1.txt file2.txt

# Stage all changes in current directory
git add .

# Stage all changes in repository
git add -A

# Stage only modified files (not new files)
git add -u
```

### Removing from Staging
```bash
# Unstage specific file (keeps changes in working directory)
git reset filename.txt

# Unstage all files
git reset

# Remove file from staging and working directory
git rm filename.txt

# Remove file from Git but keep in working directory
git rm --cached filename.txt
```

## 📊 Staging Area Benefits

### 1. Selective Commits
```bash
# You modified 3 files but only want to commit 2
git add file1.txt file2.txt
git commit -m "Implement user authentication"

# file3.txt remains modified but uncommitted
```

### 2. Quality Control
```bash
# Review staged changes before committing
git diff --staged

# Make sure everything looks correct
git status

# Then commit
git commit -m "Add user login feature"
```

### 3. Logical Grouping
```bash
# Group related changes together
git add login.js auth.css
git commit -m "Add login functionality"

git add profile.js profile.css  
git commit -m "Add user profile page"
```

## 🔍 Checking Your Work

### View File States
```bash
# See overall status
git status

# Short status format
git status -s
```

**Short Status Symbols:**
- `??` = Untracked
- `A` = Added (staged)
- `M` = Modified
- `D` = Deleted
- `R` = Renamed

### View Changes
```bash
# See unstaged changes
git diff

# See staged changes
git diff --staged

# See changes in specific file
git diff filename.txt
```

## 💡 Advanced Staging Techniques

### Interactive Staging
```bash
# Choose what to stage interactively
git add -i

# Stage parts of a file (patch mode)
git add -p filename.txt
```

### Staging Hunks
When you use `git add -p`, Git shows you chunks of changes:
- `y` = stage this hunk
- `n` = don't stage this hunk  
- `s` = split into smaller hunks
- `q` = quit

## 🎨 VS Code Integration

### Source Control Panel
1. **Changes section**: Modified files (unstaged)
2. **Staged Changes section**: Files ready for commit
3. **+ button**: Stage individual files
4. **- button**: Unstage files
5. **Commit message box**: Write commit message
6. **✓ Commit button**: Create commit

### Keyboard Shortcuts
- `Ctrl+Shift+G`: Open Source Control
- `Ctrl+Enter`: Commit staged changes
- `Ctrl+Shift+P` → "Git: Stage All Changes"

## ⚠️ Common Mistakes to Avoid

### Mistake 1: Committing Too Much
```bash
# Bad: Committing unrelated changes together
git add .
git commit -m "Various fixes"

# Good: Separate logical commits
git add login.js
git commit -m "Fix login validation"
git add styles.css  
git commit -m "Update button styling"
```

### Mistake 2: Poor Commit Messages
```bash
# Bad commit messages
git commit -m "fix"
git commit -m "update stuff"
git commit -m "asdf"

# Good commit messages
git commit -m "Fix user authentication timeout issue"
git commit -m "Update navigation menu styling for mobile"
git commit -m "Add input validation for registration form"
```

### Mistake 3: Forgetting to Stage
```bash
# You made changes but forgot to stage
git commit -m "Add new feature"  # This commits nothing!

# Always check status first
git status
git add .
git commit -m "Add new feature"
```

## 🧩 Quick Recap

✅ **Three States**: Working Directory → Staging Area → Repository  
✅ **File States**: Untracked → Modified → Staged → Committed  
✅ **Staging Benefits**: Selective commits, quality control, logical grouping  
✅ **Essential Commands**: `git add`, `git commit`, `git status`, `git diff`  
✅ **Best Practice**: Review changes before committing  

---

**[← Previous: Creating New Projects](06_Creating_New_Projects.md) | [Next → Pushing and Pulling](08_Pushing_Pulling.md)**