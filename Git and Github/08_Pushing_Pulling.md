# 08 Pushing & Pulling Changes

## 🔄 Understanding Push and Pull

**Push** and **Pull** are the fundamental commands for synchronizing your local repository with remote repositories (like GitHub).

| Command | Direction | Purpose |
|---------|-----------|---------|
| **git push** | Local → Remote | Upload your commits to GitHub |
| **git pull** | Remote → Local | Download latest changes from GitHub |

## 📤 Git Push: Uploading Changes

### Basic Push Command
```bash
# Push current branch to remote
git push

# Push specific branch to remote
git push origin main

# Push and set upstream (first time)
git push -u origin main
```

### What Happens During Push?
1. Git compares local commits with remote repository
2. Uploads new commits to remote repository
3. Updates remote branch pointer
4. Confirms successful upload

### 💡 First Push Example
```bash
# After creating commits locally
git add .
git commit -m "Add homepage design"

# Push to GitHub (first time)
git push -u origin main

# Subsequent pushes (after -u flag is set)
git push
```

## 📥 Git Pull: Downloading Changes

### Basic Pull Command
```bash
# Pull latest changes from remote
git pull

# Pull from specific remote and branch
git pull origin main
```

### What Happens During Pull?
1. Downloads new commits from remote repository
2. Merges changes into your current branch
3. Updates your working directory
4. May create merge commits if needed

### 💡 Pull Example
```bash
# Before starting work, get latest changes
git pull

# Make your changes
echo "New feature" >> feature.txt
git add .
git commit -m "Add new feature"

# Push your changes
git push
```

## 🔄 Complete Collaboration Workflow

### Scenario: Two Developers Working Together

#### Developer A's Workflow
```bash
# 1. Start with latest code
git pull

# 2. Make changes
echo "Feature A" >> app.js
git add .
git commit -m "Add Feature A"

# 3. Push changes
git push
```

#### Developer B's Workflow
```bash
# 1. Get Developer A's changes
git pull

# 2. Make different changes
echo "Feature B" >> app.js
git add .
git commit -m "Add Feature B"

# 3. Push changes
git push
```

## ⚠️ Common Push/Pull Scenarios

### Scenario 1: Push Rejected (Remote has newer commits)
```bash
# You try to push
git push

# Error message:
# ! [rejected] main -> main (fetch first)
# hint: Updates were rejected because the remote contains work that you do not have locally.

# Solution: Pull first, then push
git pull
git push
```

### Scenario 2: Merge Conflicts During Pull
```bash
# Pull creates conflicts
git pull

# Output:
# Auto-merging app.js
# CONFLICT (content): Merge conflict in app.js
# Automatic merge failed; fix conflicts and then commit the result.

# Fix conflicts in files, then:
git add .
git commit -m "Resolve merge conflicts"
git push
```

## 🛠️ Advanced Push/Pull Commands

### Push Variations
```bash
# Push all branches
git push --all

# Force push (dangerous - overwrites remote)
git push --force

# Safer force push (only if no one else pushed)
git push --force-with-lease

# Push tags
git push --tags

# Push new branch to remote
git push -u origin feature-branch
```

### Pull Variations
```bash
# Pull with rebase instead of merge
git pull --rebase

# Pull only (fetch without merge)
git fetch
git merge origin/main

# Pull from different remote
git pull upstream main
```

## 🔍 Checking Remote Status

### View Remote Information
```bash
# List remote repositories
git remote -v

# Show remote branch information
git branch -r

# Show all branches (local and remote)
git branch -a

# Check if local is behind/ahead of remote
git status
```

### Fetch vs Pull
```bash
# Fetch: Download changes but don't merge
git fetch origin

# See what was fetched
git log HEAD..origin/main

# Merge manually if desired
git merge origin/main

# Pull: Fetch + Merge in one command
git pull origin main
```

## 📊 Push/Pull Best Practices

### 1. Always Pull Before Push
```bash
# Good workflow
git pull          # Get latest changes
# Make your changes
git add .
git commit -m "Your changes"
git push          # Upload your changes
```

### 2. Commit Before Pull
```bash
# Ensure your work is saved before pulling
git add .
git commit -m "Work in progress"
git pull
```

### 3. Use Descriptive Branch Names
```bash
# Push feature branches
git checkout -b feature/user-authentication
git push -u origin feature/user-authentication

# Push bug fix branches  
git checkout -b fix/login-validation
git push -u origin fix/login-validation
```

## 🚨 Troubleshooting Common Issues

### Issue 1: Authentication Failed
```bash
# Problem: GitHub credentials not configured
# Solution: Use personal access token or SSH key

# For HTTPS (use token as password)
git remote set-url origin https://github.com/username/repo.git

# For SSH (after adding SSH key to GitHub)
git remote set-url origin git@github.com:username/repo.git
```

### Issue 2: Large File Push Fails
```bash
# Problem: File too large for GitHub
# Solution: Use Git LFS or remove large files

# Install Git LFS
git lfs install

# Track large files
git lfs track "*.zip"
git add .gitattributes
git commit -m "Add LFS tracking"
```

### Issue 3: Accidentally Pushed Sensitive Data
```bash
# Problem: Committed passwords or API keys
# Solution: Remove from history (if not shared yet)

# Remove file from history
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch secrets.txt' \
--prune-empty --tag-name-filter cat -- --all

# Force push to update remote
git push --force-with-lease
```

## 🎯 Quick Command Reference

```bash
# Essential push/pull commands
git push                    # Push current branch
git push -u origin main     # Push and set upstream
git pull                    # Pull latest changes
git pull --rebase          # Pull with rebase

# Status and information
git status                 # Check local vs remote status
git remote -v             # List remote repositories
git fetch                 # Download without merging
git log --oneline -5      # See recent commits
```

## 🧩 Quick Recap

✅ **Push**: Upload local commits to remote repository  
✅ **Pull**: Download and merge remote changes locally  
✅ **Always pull before push** to avoid conflicts  
✅ **Commit your work** before pulling changes  
✅ **Use -u flag** when pushing new branches  

---

**[← Previous: Staging and Commit Workflow](07_Staging_Commit_Workflow.md) | [Next → Git Log and History](09_Git_Log_History.md)**