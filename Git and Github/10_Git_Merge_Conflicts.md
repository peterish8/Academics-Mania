# 10 Git Merge, Conflicts & Reset

## 🔄 What is Git Merge?

**Git merge** combines changes from one branch into another, integrating their histories while preserving all commits. It's essential for collaborative development and feature integration.

### Common Use Cases
- Merging feature branches into main branch
- Integrating bug fixes
- Combining work from multiple developers
- Updating feature branches with latest main changes

## 🛠️ Basic Merge Commands

### Standard Merge Process
```bash
# 1. Switch to target branch (where changes should go)
git checkout main

# 2. Merge source branch into current branch
git merge feature-branch

# 3. Push merged changes (if needed)
git push
```

### Merge Types

#### Fast-Forward Merge
When target branch hasn't changed since feature branch was created:
```bash
# Before merge:
# main:    A---B
# feature:     B---C---D

# After merge:
# main:    A---B---C---D (fast-forward)

git merge feature-branch
# No merge commit created
```

#### Three-Way Merge
When both branches have new commits:
```bash
# Before merge:
# main:    A---B---E---F
# feature:     B---C---D

# After merge:
# main:    A---B---E---F---M
#              \         /
# feature:      C---D---/

git merge feature-branch
# Creates merge commit M
```

## ⚠️ When Do Merge Conflicts Occur?

Conflicts happen when Git cannot automatically merge changes because:

1. **Same line modified**: Both branches edit the same line differently
2. **File deleted vs modified**: One branch deletes a file, another modifies it
3. **Binary file conflicts**: Two versions of binary files exist

### Conflict Example Scenario
```bash
# Developer A modifies line 5 in app.js:
console.log("Hello from Developer A");

# Developer B modifies same line 5 in app.js:
console.log("Hello from Developer B");

# When merging: CONFLICT!
```

## 🔍 How Git Shows Merge Conflicts

When conflicts occur, Git marks them in files with special markers:

```javascript
// app.js with conflict markers
function greetUser() {
<<<<<<< HEAD
    console.log("Hello from main branch");
=======
    console.log("Hello from feature branch");
>>>>>>> feature-branch
}
```

### Conflict Marker Explanation
- `<<<<<<< HEAD`: Start of your current branch version
- `=======`: Separator between versions
- `>>>>>>> branch-name`: End of incoming branch version

## 🛠️ Resolving Merge Conflicts

### Step-by-Step Resolution Process

#### 1. Identify Conflicted Files
```bash
# See which files have conflicts
git status

# Output shows:
# Unmerged paths:
#   both modified:   app.js
#   both modified:   styles.css
```

#### 2. Open and Edit Conflicted Files
Choose one of these resolution strategies:

**Option A: Keep Your Version**
```javascript
// Remove conflict markers, keep HEAD version
function greetUser() {
    console.log("Hello from main branch");
}
```

**Option B: Keep Incoming Version**
```javascript
// Remove conflict markers, keep incoming version
function greetUser() {
    console.log("Hello from feature branch");
}
```

**Option C: Combine Both Versions**
```javascript
// Remove conflict markers, combine logically
function greetUser() {
    console.log("Hello from main branch");
    console.log("Hello from feature branch");
}
```

**Option D: Write New Solution**
```javascript
// Remove conflict markers, create new solution
function greetUser() {
    console.log("Hello from merged branches");
}
```

#### 3. Mark Conflicts as Resolved
```bash
# After editing files, stage them
git add app.js
git add styles.css

# Or stage all resolved files
git add .
```

#### 4. Complete the Merge
```bash
# Commit the merge (Git provides default message)
git commit

# Or provide custom merge message
git commit -m "Merge feature-branch: resolve greeting conflicts"
```

## 🚨 Aborting a Merge

If conflicts are too complex or you want to start over:

```bash
# Cancel the merge and return to pre-merge state
git merge --abort

# This restores your branch to exactly how it was before merge attempt
```

## 🔧 Tools for Conflict Resolution

### Command Line Tools
```bash
# Use Git's built-in merge tool
git mergetool

# Configure your preferred merge tool
git config --global merge.tool vimdiff
git config --global merge.tool code  # VS Code
```

### VS Code Integration
1. **Conflict indicators**: VS Code highlights conflicts with colors
2. **Action buttons**: "Accept Current Change", "Accept Incoming Change", "Accept Both Changes"
3. **Side-by-side view**: Compare versions easily
4. **Integrated terminal**: Run Git commands directly

### Other Popular Tools
- **GitKraken**: Visual merge conflict resolution
- **SourceTree**: Atlassian's Git GUI with merge tools
- **Beyond Compare**: Professional file comparison tool
- **Meld**: Free visual merge tool

## 📊 Merge Conflict Resolution Strategies

| Strategy | When to Use | Command/Action |
|----------|-------------|----------------|
| **Accept Yours** | Your changes are correct | Keep `<<<<<<< HEAD` section |
| **Accept Theirs** | Incoming changes are correct | Keep `>>>>>>> branch` section |
| **Combine Both** | Both changes are needed | Merge both sections logically |
| **Rewrite** | Neither version is ideal | Write completely new solution |
| **Abort** | Too complex to resolve now | `git merge --abort` |

## 🎯 Best Practices for Avoiding Conflicts

### 1. Frequent Pulls
```bash
# Stay updated with main branch
git checkout main
git pull
git checkout feature-branch
git merge main  # or git rebase main
```

### 2. Small, Focused Commits
```bash
# Good: Small, logical commits
git commit -m "Add user validation"
git commit -m "Update error messages"

# Bad: Large, mixed commits
git commit -m "Add features and fix bugs and update styles"
```

### 3. Communication
- Coordinate with team on file ownership
- Use feature branches for experimental work
- Discuss major changes before implementation

### 4. File Organization
```bash
# Avoid conflicts by organizing code into separate files
# Instead of everyone editing app.js:
auth/
  login.js
  register.js
ui/
  header.js
  footer.js
```

## 🔍 Checking Merge Status

### Before Merging
```bash
# See what would be merged
git log HEAD..feature-branch --oneline

# Check if merge would create conflicts
git merge --no-commit --no-ff feature-branch
git merge --abort  # Cancel the test merge
```

### During Conflict Resolution
```bash
# List conflicted files
git status

# See conflict markers in files
git diff

# Check which files are staged for commit
git diff --cached
```

### After Merging
```bash
# Verify merge was successful
git log --oneline -5

# See the merge commit
git show HEAD
```

## 🧩 Quick Command Reference

```bash
# Merge commands
git merge branch-name           # Merge branch into current
git merge --no-ff branch-name   # Force merge commit
git merge --abort              # Cancel ongoing merge

# Conflict resolution
git status                     # See conflicted files
git add filename              # Mark conflict as resolved
git commit                    # Complete merge
git mergetool                 # Open merge tool

# Information commands
git log --merge               # Show commits causing conflict
git diff                      # See conflict markers
git ls-files -u              # List unmerged files
```

## 🧩 Quick Recap

✅ **Merge**: Combines changes from different branches  
✅ **Conflicts**: Occur when same lines are modified differently  
✅ **Resolution**: Edit files, remove markers, stage, commit  
✅ **Abort**: Use `git merge --abort` to cancel  
✅ **Prevention**: Frequent pulls, small commits, good communication  

---

**[← Previous: Git Log and History](09_Git_Log_History.md) | [Next → Reset Types](11_Reset_Types.md)**