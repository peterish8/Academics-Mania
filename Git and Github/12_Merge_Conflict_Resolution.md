# 12 Merge Conflicts (Detection, Resolution, Abort)

## 🔍 Detecting Merge Conflicts

Merge conflicts are Git's way of asking for your help when it can't automatically combine changes. Understanding how to detect, resolve, and manage conflicts is crucial for collaborative development.

## 🚨 When Conflicts Occur

### Common Conflict Scenarios

#### 1. Same Line, Different Changes
```javascript
// Developer A changes line 5:
console.log("Hello from Team A");

// Developer B changes same line 5:
console.log("Hello from Team B");

// Result: CONFLICT when merging
```

#### 2. File Deleted vs Modified
```bash
# Developer A deletes file
git rm config.txt

# Developer B modifies same file
echo "new config" >> config.txt

# Result: CONFLICT when merging
```

#### 3. Binary File Conflicts
```bash
# Both developers modify same image file
# Git cannot merge binary files automatically
# Result: CONFLICT requiring manual resolution
```

## 🔍 Conflict Detection Process

### Step 1: Attempt Merge
```bash
# Try to merge feature branch
git checkout main
git merge feature-branch
```

### Step 2: Git Reports Conflicts
```bash
# Git output when conflicts occur:
Auto-merging app.js
CONFLICT (content): Merge conflict in app.js
Auto-merging styles.css
CONFLICT (content): Merge conflict in styles.css
Automatic merge failed; fix conflicts and then commit the result.
```

### Step 3: Check Conflict Status
```bash
# See which files have conflicts
git status

# Output shows:
Unmerged paths:
  (use "git add <file>..." to mark resolution)
    both modified:   app.js
    both modified:   styles.css
    deleted by us:   config.txt
    added by them:   new-feature.js
```

## 🛠️ Understanding Conflict Markers

When Git detects conflicts, it adds special markers to show conflicting sections:

### Basic Conflict Structure
```javascript
// app.js with conflict
function getUserName() {
<<<<<<< HEAD
    return "User from main branch";
=======
    return "User from feature branch";
>>>>>>> feature-branch
}
```

### Conflict Marker Breakdown
- `<<<<<<< HEAD`: Start of your current branch (HEAD) version
- `=======`: Divider between conflicting versions
- `>>>>>>> branch-name`: End of incoming branch version
- Everything between markers needs manual resolution

### Complex Conflict Example
```css
/* styles.css with multiple conflicts */
.header {
<<<<<<< HEAD
    background-color: blue;
    font-size: 24px;
=======
    background-color: red;
    font-size: 20px;
    border: 1px solid black;
>>>>>>> feature-styling
}

.navigation {
<<<<<<< HEAD
    display: flex;
=======
    display: grid;
    grid-template-columns: repeat(3, 1fr);
>>>>>>> feature-styling
}
```

## 🔧 Resolution Strategies

### Strategy 1: Accept Current Changes (HEAD)
```javascript
// Keep only the HEAD version
function getUserName() {
    return "User from main branch";
}
```

### Strategy 2: Accept Incoming Changes
```javascript
// Keep only the incoming version
function getUserName() {
    return "User from feature branch";
}
```

### Strategy 3: Combine Both Changes
```javascript
// Merge both versions logically
function getUserName() {
    const mainUser = "User from main branch";
    const featureUser = "User from feature branch";
    return `${mainUser} and ${featureUser}`;
}
```

### Strategy 4: Create New Solution
```javascript
// Write completely new code
function getUserName() {
    return "Merged user from both branches";
}
```

## 📝 Step-by-Step Resolution Process

### Step 1: Identify All Conflicted Files
```bash
# List files with conflicts
git status

# See conflict details
git diff
```

### Step 2: Open and Edit Each Conflicted File
```bash
# Open file in your editor
code app.js  # VS Code
vim app.js   # Vim
nano app.js  # Nano
```

### Step 3: Resolve Conflicts
1. **Find conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`)
2. **Decide resolution strategy** (keep yours, theirs, combine, or rewrite)
3. **Remove all conflict markers**
4. **Test your resolution** (if possible)

### Step 4: Mark Files as Resolved
```bash
# Stage resolved files
git add app.js
git add styles.css

# Or stage all resolved files
git add .
```

### Step 5: Complete the Merge
```bash
# Commit the merge (Git provides default message)
git commit

# Or provide custom message
git commit -m "Resolve merge conflicts between main and feature-branch

- Keep main branch styling for header
- Combine navigation approaches
- Update user functions to handle both cases"
```

## 🛠️ Tools for Conflict Resolution

### VS Code Built-in Tools
VS Code provides excellent conflict resolution features:

1. **Visual Indicators**: Conflicts highlighted with colors
2. **Action Buttons**:
   - "Accept Current Change" (keep HEAD)
   - "Accept Incoming Change" (keep incoming)
   - "Accept Both Changes" (combine)
   - "Compare Changes" (side-by-side view)

### Command Line Merge Tools
```bash
# Configure and use Git's merge tool
git config --global merge.tool vimdiff
git mergetool

# Other popular merge tools:
git config --global merge.tool meld
git config --global merge.tool kdiff3
git config --global merge.tool p4merge
```

### External GUI Tools
- **GitKraken**: Visual merge conflict resolution
- **SourceTree**: Atlassian's Git GUI
- **Beyond Compare**: Professional comparison tool
- **Meld**: Free visual diff and merge tool

## 🚫 Aborting a Merge

Sometimes conflicts are too complex or you need to approach differently:

### Abort Current Merge
```bash
# Cancel the merge and return to pre-merge state
git merge --abort

# This command:
# - Cancels the ongoing merge
# - Removes conflict markers from files
# - Returns branch to exact state before merge attempt
# - Preserves any uncommitted changes you had before merge
```

### When to Abort
- **Too many conflicts**: More conflicts than expected
- **Wrong branch**: Realized you're merging wrong branches
- **Need preparation**: Want to coordinate with team first
- **Complex resolution**: Need more time to understand changes

### After Aborting
```bash
# Check that abort worked
git status
# Should show "nothing to commit, working tree clean"

# Plan your approach:
# 1. Communicate with team
# 2. Review changes more carefully
# 3. Consider alternative merge strategies
# 4. Try merge again when ready
```

## 🎯 Advanced Conflict Resolution

### Partial File Resolution
```bash
# Stage parts of files during conflict resolution
git add -p filename.txt

# This allows you to:
# - Stage resolved hunks
# - Leave unresolved hunks for later
# - Gradually work through complex conflicts
```

### Using Git Attributes for Merge Strategies
```bash
# Create .gitattributes file for custom merge behavior
echo "*.generated merge=ours" >> .gitattributes

# This tells Git to always use "our" version for generated files
```

### Three-Way Merge Information
```bash
# See all three versions during conflict
git show :1:filename.txt  # Common ancestor
git show :2:filename.txt  # HEAD (current branch)
git show :3:filename.txt  # Incoming branch
```

## 📊 Conflict Resolution Checklist

### Before Resolution
- [ ] Understand what each branch was trying to accomplish
- [ ] Identify all conflicted files with `git status`
- [ ] Back up current state if needed
- [ ] Communicate with team members if their changes are involved

### During Resolution
- [ ] Open each conflicted file
- [ ] Understand both versions of changes
- [ ] Choose appropriate resolution strategy
- [ ] Remove ALL conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- [ ] Test resolution if possible
- [ ] Stage resolved files with `git add`

### After Resolution
- [ ] Verify all conflicts resolved with `git status`
- [ ] Review changes with `git diff --cached`
- [ ] Commit with descriptive message
- [ ] Test merged code thoroughly
- [ ] Push to remote if appropriate

## 🧩 Quick Command Reference

```bash
# Conflict detection
git status                    # See conflicted files
git diff                      # See conflict markers
git ls-files -u              # List unmerged files

# Resolution process
git add filename             # Mark file as resolved
git add .                    # Stage all resolved files
git commit                   # Complete merge
git commit -m "message"      # Complete with custom message

# Merge management
git merge --abort            # Cancel ongoing merge
git mergetool               # Open merge tool
git merge --continue        # Continue after resolving

# Information commands
git log --merge             # Show conflicting commits
git show :2:filename        # Show HEAD version
git show :3:filename        # Show incoming version
```

## 🧩 Quick Recap

✅ **Detection**: Git stops merge and marks conflicts in files  
✅ **Markers**: `<<<<<<<`, `=======`, `>>>>>>>` show conflicting sections  
✅ **Resolution**: Edit files, remove markers, stage, commit  
✅ **Tools**: VS Code, merge tools, or manual editing  
✅ **Abort**: Use `git merge --abort` to cancel and start over  

---

**[← Previous: Reset Types](11_Reset_Types.md) | [Next → Practice and Recap](13_Practice_Recap.md)**