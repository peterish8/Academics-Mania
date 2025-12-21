# 09 Git Log & History

## 📜 Understanding Git History

Git maintains a complete history of all changes made to your project. The `git log` command is your window into this history, showing commits, authors, dates, and messages.

## 🔍 Basic Log Commands

### Standard Log View
```bash
# Show full commit history
git log

# Sample output:
# commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
# Author: John Smith <john@example.com>
# Date:   Mon Oct 23 14:30:25 2023 -0400
#
#     Add user authentication feature
#
#     - Implement login form validation
#     - Add password encryption
#     - Create session management
```

### Compact Log View
```bash
# One line per commit (most useful)
git log --oneline

# Sample output:
# a1b2c3d Add user authentication feature
# b2c3d4e Fix navigation menu bug
# c3d4e5f Update homepage styling
# d4e5f6g Initial project setup
```

## 🎨 Customizing Log Output

### Limit Number of Commits
```bash
# Show last 5 commits
git log -5

# Show last 10 commits in oneline format
git log --oneline -10
```

### Filter by Author
```bash
# Show commits by specific author
git log --author="John Smith"

# Show commits by current user
git log --author="$(git config user.name)"
```

### Filter by Date
```bash
# Show commits since specific date
git log --since="2023-10-01"

# Show commits in date range
git log --since="2023-10-01" --until="2023-10-31"

# Show commits from last week
git log --since="1 week ago"
```

### Filter by Message
```bash
# Search commit messages for keyword
git log --grep="bug"

# Search for multiple keywords
git log --grep="feature" --grep="add"
```

## 📊 Visual Log Formats

### Graph View
```bash
# Show branch and merge history
git log --graph --oneline

# Detailed graph with all branches
git log --graph --all --decorate --oneline
```

### Pretty Formats
```bash
# Custom format with colors
git log --pretty=format:"%h - %an, %ar : %s"

# Output:
# a1b2c3d - John Smith, 2 hours ago : Add user authentication
# b2c3d4e - Jane Doe, 1 day ago : Fix navigation bug

# Predefined pretty formats
git log --pretty=short
git log --pretty=full
git log --pretty=fuller
```

## 🔎 Examining Specific Commits

### Show Commit Details
```bash
# Show specific commit with changes
git show a1b2c3d

# Show commit without diff
git show --name-only a1b2c3d

# Show only files changed
git show --stat a1b2c3d
```

### Compare Commits
```bash
# Compare two commits
git diff a1b2c3d..b2c3d4e

# Compare with previous commit
git diff HEAD~1

# Compare current with 3 commits ago
git diff HEAD~3
```

## 📁 File-Specific History

### Track File Changes
```bash
# Show history of specific file
git log filename.txt

# Show changes made to file
git log -p filename.txt

# Show when file was moved/renamed
git log --follow filename.txt
```

### File at Specific Commit
```bash
# Show file content at specific commit
git show a1b2c3d:filename.txt

# Show file names changed in commit
git show --name-only a1b2c3d
```

## 🌿 Branch History

### View Branch Information
```bash
# Show commits on current branch only
git log --first-parent

# Show commits not in main branch
git log main..feature-branch

# Show commits in feature branch but not main
git log --oneline main..feature-branch
```

### Merge History
```bash
# Show merge commits only
git log --merges

# Show non-merge commits only
git log --no-merges

# Show branch topology
git log --graph --all --oneline --decorate
```

## 🛠️ Advanced Log Techniques

### Interactive Log Exploration
```bash
# Browse commits interactively
git log --oneline | head -20

# Use with grep for searching
git log --oneline | grep "feature"
```

### Statistics and Analysis
```bash
# Show commit statistics
git log --stat

# Show short statistics
git log --shortstat

# Count commits by author
git shortlog -sn
```

### Performance Analysis
```bash
# Show commits that changed specific lines
git log -L 10,20:filename.txt

# Show commits affecting function
git log -L :functionName:filename.js
```

## 📋 Useful Log Aliases

Add these to your Git configuration for quick access:

```bash
# Set up useful aliases
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
git config --global alias.last "log -1 HEAD --stat"

# Usage:
git lg      # Beautiful graph view
git hist    # Formatted history
git last    # Last commit details
```

## 🔍 Finding Specific Information

### Find When Bug Was Introduced
```bash
# Use git bisect to find problematic commit
git bisect start
git bisect bad                    # Current version has bug
git bisect good a1b2c3d          # This commit was good
# Git will checkout middle commit for testing
# Mark as good or bad, repeat until found
```

### Search Code History
```bash
# Find when specific code was added/removed
git log -S "function_name" --oneline

# Find when regex pattern was changed
git log -G "regex_pattern" --oneline
```

## 📊 Log Output Examples

### Comprehensive Project Overview
```bash
# Get project overview
git log --oneline --graph --all --decorate -10

# Sample output:
# * a1b2c3d (HEAD -> main, origin/main) Add user auth
# * b2c3d4e Fix navigation bug  
# |\  
# | * c3d4e5f (feature/login) Implement login
# | * d4e5f6g Add login form
# |/  
# * e5f6g7h Update styling
# * f6g7h8i Initial commit
```

### Detailed Change Summary
```bash
# Show what changed in each commit
git log --stat --oneline -5

# Sample output:
# a1b2c3d Add user authentication
#  auth.js     | 45 ++++++++++++++++++++++++++++++++++++++++++
#  login.html  | 23 +++++++++++++++++++++++
#  2 files changed, 68 insertions(+)
```

## 🧩 Quick Command Reference

```bash
# Essential log commands
git log                          # Full history
git log --oneline               # Compact view
git log -5                      # Last 5 commits
git log --author="Name"         # Filter by author
git log --since="1 week ago"    # Recent commits
git log --grep="keyword"        # Search messages
git log --graph --all           # Visual branch history
git show commit-hash            # Specific commit details
```

## 🧩 Quick Recap

✅ **git log**: View complete project history  
✅ **--oneline**: Compact, readable format  
✅ **--graph**: Visual branch representation  
✅ **Filtering**: By author, date, message, file  
✅ **git show**: Detailed view of specific commits  

---

**[← Previous: Pushing and Pulling](08_Pushing_Pulling.md) | [Next → Git Merge and Conflicts](10_Git_Merge_Conflicts.md)**