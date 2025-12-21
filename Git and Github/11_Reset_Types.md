# 11 Reset Types (soft, mixed, hard)

## 🔄 Understanding Git Reset

**Git reset** moves the HEAD pointer to a different commit, effectively "undoing" commits. The key difference between reset types is what happens to your changes after the reset.

## 📍 Understanding HEAD and HEAD~

### HEAD Pointer
- **HEAD**: Points to your current latest commit (where you are now)
- **HEAD~1** or **HEAD~**: The commit just before the latest
- **HEAD~2**: Two commits before the latest
- **HEAD~3**: Three commits before the latest

### Visual Example
```bash
# Commit history:
A --- B --- C --- D (HEAD)

# HEAD~1 = commit C
# HEAD~2 = commit B  
# HEAD~3 = commit A
```

## 🎯 The Three Types of Reset

| Reset Type | Commit History | Staging Area | Working Directory |
|------------|----------------|--------------|-------------------|
| **--soft** | ✅ Moved | ✅ Preserved | ✅ Preserved |
| **--mixed** (default) | ✅ Moved | ❌ Cleared | ✅ Preserved |
| **--hard** | ✅ Moved | ❌ Cleared | ❌ Cleared |

## 🟢 Soft Reset (--soft)

**Purpose**: Undo commits but keep all changes staged and ready to commit again.

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1
```

### What Happens:
- ✅ **Commit removed** from history
- ✅ **Changes remain staged** (in staging area)
- ✅ **Files unchanged** in working directory

### Use Case Example:
```bash
# You made a commit with wrong message
git commit -m "bad commit message"

# Undo commit but keep changes staged
git reset --soft HEAD~1

# Now recommit with better message
git commit -m "Add user authentication feature"
```

### Before and After Soft Reset:
```bash
# Before:
# Working Directory: Clean
# Staging Area: Empty  
# Repository: A -> B -> C (HEAD)

# After git reset --soft HEAD~1:
# Working Directory: Clean
# Staging Area: Contains changes from commit C
# Repository: A -> B (HEAD)
```

## 🟡 Mixed Reset (--mixed) - Default

**Purpose**: Undo commits and unstage changes, but keep files modified in working directory.

```bash
# Undo last commit, unstage changes (default behavior)
git reset HEAD~1
# Same as:
git reset --mixed HEAD~1
```

### What Happens:
- ✅ **Commit removed** from history
- ❌ **Changes unstaged** (removed from staging area)
- ✅ **Files remain modified** in working directory

### Use Case Example:
```bash
# You want to modify your last commit
git reset HEAD~1

# Files are now modified but unstaged
# Edit files as needed
echo "Additional changes" >> file.txt

# Stage and commit everything together
git add .
git commit -m "Improved feature with additional changes"
```

### Before and After Mixed Reset:
```bash
# Before:
# Working Directory: Clean
# Staging Area: Empty
# Repository: A -> B -> C (HEAD)

# After git reset HEAD~1:
# Working Directory: Contains changes from commit C (modified files)
# Staging Area: Empty
# Repository: A -> B (HEAD)
```

## 🔴 Hard Reset (--hard) - DANGEROUS

**Purpose**: Completely undo commits and permanently delete all changes.

```bash
# Completely remove last commit and all its changes
git reset --hard HEAD~1
```

### What Happens:
- ✅ **Commit removed** from history
- ❌ **Changes deleted** from staging area
- ❌ **Changes deleted** from working directory

### ⚠️ WARNING: This is DESTRUCTIVE!
- All uncommitted changes are **permanently lost**
- Cannot be easily recovered
- Use with extreme caution

### Use Case Example:
```bash
# You want to completely abandon recent work
git reset --hard HEAD~2

# Everything from last 2 commits is gone forever
```

## 📊 Practical Examples

### Example 1: Fix Commit Message (Soft Reset)
```bash
# Current state:
git log --oneline -3
# a1b2c3d Fix typo in header
# b2c3d4e Add navigation menu  
# c3d4e5f Initial setup

# Oops, commit message should be more descriptive
git reset --soft HEAD~1

# Check status - changes are still staged
git status
# Changes to be committed:
#   modified: header.html

# Recommit with better message
git commit -m "Fix typo in header navigation text"
```

### Example 2: Modify Last Commit (Mixed Reset)
```bash
# You forgot to add a file to your last commit
git log --oneline -1
# a1b2c3d Add user registration

# Reset to modify the commit
git reset HEAD~1

# Add the forgotten file
git add forgotten-file.js

# Add all changes and commit together
git add .
git commit -m "Add user registration with validation"
```

### Example 3: Abandon Recent Work (Hard Reset)
```bash
# You've been experimenting and want to start over
git log --oneline -3
# a1b2c3d Experimental feature attempt
# b2c3d4e Another experiment
# c3d4e5f Last good version

# Go back to last good version, lose all experiments
git reset --hard c3d4e5f

# All experimental work is now gone
```

## 🛡️ Safety Considerations

### Before Using Reset
```bash
# Always check what you're about to reset
git log --oneline -5

# See what changes would be affected
git diff HEAD~1

# Consider creating a backup branch
git branch backup-before-reset
```

### Recovery Options
```bash
# If you accidentally used --hard, try to recover
git reflog

# Find the commit you want to restore
git reset --hard commit-hash-from-reflog
```

### Safer Alternatives
```bash
# Instead of reset --hard, consider:
git stash  # Save changes temporarily
git checkout -- filename  # Discard changes to specific file
git clean -fd  # Remove untracked files
```

## 🚫 When NOT to Use Reset

### Don't Reset if Already Pushed
```bash
# BAD: Don't reset commits that are already on GitHub
git push
git reset --hard HEAD~1  # This will cause problems!

# GOOD: Use revert instead for pushed commits
git revert HEAD  # Creates new commit that undoes changes
```

### Alternative: Git Revert
```bash
# Safely undo a pushed commit
git revert HEAD

# This creates a new commit that undoes the previous one
# Safe for shared repositories
```

## 🎯 Reset Decision Tree

```
Do you want to undo commits?
├── Yes
│   ├── Are commits already pushed to remote?
│   │   ├── Yes → Use `git revert` (safer)
│   │   └── No → Continue with reset
│   ├── Do you want to keep changes for editing?
│   │   ├── Yes, keep staged → `git reset --soft`
│   │   ├── Yes, but unstaged → `git reset --mixed`
│   │   └── No, delete everything → `git reset --hard`
└── No → Don't use reset
```

## 🧩 Quick Command Reference

```bash
# Reset types
git reset --soft HEAD~1     # Undo commit, keep staged
git reset HEAD~1            # Undo commit, unstage changes  
git reset --hard HEAD~1     # Undo commit, delete changes

# Safety commands
git reflog                  # See reset history
git branch backup          # Create backup before reset
git stash                  # Save changes temporarily

# Information
git log --oneline -5       # See recent commits
git status                 # Check current state
git diff HEAD~1           # See what would change
```

## 🧩 Quick Recap

✅ **--soft**: Undo commits, keep changes staged  
✅ **--mixed**: Undo commits, unstage changes, keep files modified  
✅ **--hard**: Undo commits, delete all changes (DANGEROUS)  
✅ **HEAD~**: Reference to previous commits  
✅ **Safety first**: Don't reset pushed commits, use revert instead  

---

**[← Previous: Git Merge and Conflicts](10_Git_Merge_Conflicts.md) | [Next → Merge Conflict Resolution](12_Merge_Conflict_Resolution.md)**