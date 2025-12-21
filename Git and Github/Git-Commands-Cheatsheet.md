# 🚀 Git Commands Cheatsheet

## 📋 Basic Git Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git init` | Initialize a new Git repository | `git init` |
| `git clone <url>` | Clone a repository from remote | `git clone https://github.com/user/repo.git` |
| `git status` | Show working directory status | `git status` |
| `git add <file>` | Add file to staging area | `git add index.html` |
| `git add .` | Add all files to staging area | `git add .` |
| `git commit -m "message"` | Commit staged changes | `git commit -m "Initial commit"` |
| `git log` | Show commit history | `git log` |
| `git log --oneline` | Show compact commit history | `git log --oneline` |

## 🌐 Remote Repository Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git remote add origin <url>` | Add remote repository | `git remote add origin https://github.com/user/repo.git` |
| `git remote -v` | Show remote repositories | `git remote -v` |
| `git push` | Push commits to remote | `git push` |
| `git push -u origin main` | Push and set upstream | `git push -u origin main` |
| `git pull` | Pull latest changes from remote | `git pull` |
| `git fetch` | Fetch changes without merging | `git fetch` |

## 🌿 Branch Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git branch` | List all branches | `git branch` |
| `git branch <name>` | Create new branch | `git branch feature-login` |
| `git checkout <branch>` | Switch to branch | `git checkout main` |
| `git checkout -b <name>` | Create and switch to new branch | `git checkout -b feature-signup` |
| `git switch <branch>` | Switch to branch (newer syntax) | `git switch main` |
| `git switch -c <name>` | Create and switch to new branch | `git switch -c feature-dashboard` |
| `git branch -d <name>` | Delete branch | `git branch -d feature-login` |
| `git branch -D <name>` | Force delete branch | `git branch -D feature-broken` |

## 🔀 Merge & Rebase Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git merge <branch>` | Merge branch into current branch | `git merge feature-login` |
| `git merge --abort` | Abort ongoing merge | `git merge --abort` |
| `git rebase <branch>` | Rebase current branch onto another | `git rebase main` |
| `git rebase --continue` | Continue rebase after resolving conflicts | `git rebase --continue` |
| `git rebase --abort` | Abort ongoing rebase | `git rebase --abort` |

## 🍒 Cherry-pick Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git cherry-pick <commit>` | Apply specific commit to current branch | `git cherry-pick a7d39b2` |
| `git cherry-pick <commit1> <commit2>` | Apply multiple commits | `git cherry-pick a7d39b2 f4e12ab` |
| `git cherry-pick --abort` | Abort cherry-pick operation | `git cherry-pick --abort` |
| `git cherry-pick --continue` | Continue after resolving conflicts | `git cherry-pick --continue` |

## 🔄 Reset & Revert Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git reset HEAD~` | Undo last commit (keep changes) | `git reset HEAD~` |
| `git reset --soft HEAD~` | Undo commit (keep staged) | `git reset --soft HEAD~` |
| `git reset --hard HEAD~` | Undo commit (delete changes) | `git reset --hard HEAD~` |
| `git revert <commit>` | Create new commit that undoes changes | `git revert a7d39b2` |
| `git clean -f` | Remove untracked files | `git clean -f` |
| `git clean -fd` | Remove untracked files and directories | `git clean -fd` |

## 🏷️ Stash Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git stash` | Stash current changes | `git stash` |
| `git stash save "message"` | Stash with custom message | `git stash save "work in progress"` |
| `git stash list` | List all stashes | `git stash list` |
| `git stash pop` | Apply and remove latest stash | `git stash pop` |
| `git stash apply` | Apply stash without removing | `git stash apply` |
| `git stash drop` | Delete latest stash | `git stash drop` |
| `git stash clear` | Delete all stashes | `git stash clear` |

## 🔍 Inspection Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git diff` | Show unstaged changes | `git diff` |
| `git diff --staged` | Show staged changes | `git diff --staged` |
| `git diff <branch1> <branch2>` | Compare branches | `git diff main feature-login` |
| `git show <commit>` | Show commit details | `git show a7d39b2` |
| `git blame <file>` | Show who changed each line | `git blame index.html` |
| `git log --graph` | Show commit graph | `git log --graph` |
| `git log --author="name"` | Show commits by author | `git log --author="John"` |

## 🏷️ Tag Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git tag` | List all tags | `git tag` |
| `git tag <name>` | Create lightweight tag | `git tag v1.0` |
| `git tag -a <name> -m "message"` | Create annotated tag | `git tag -a v1.0 -m "Version 1.0"` |
| `git push origin <tag>` | Push specific tag | `git push origin v1.0` |
| `git push origin --tags` | Push all tags | `git push origin --tags` |
| `git tag -d <name>` | Delete local tag | `git tag -d v1.0` |

## ⚙️ Configuration Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git config --global user.name "name"` | Set global username | `git config --global user.name "John Doe"` |
| `git config --global user.email "email"` | Set global email | `git config --global user.email "john@example.com"` |
| `git config --list` | Show all configurations | `git config --list` |
| `git config user.name` | Show current username | `git config user.name` |
| `git config --global init.defaultBranch main` | Set default branch name | `git config --global init.defaultBranch main` |

## 🔧 Advanced Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git reflog` | Show reference log | `git reflog` |
| `git bisect start` | Start binary search for bug | `git bisect start` |
| `git worktree add <path> <branch>` | Create new worktree | `git worktree add ../feature feature-branch` |
| `git submodule add <url>` | Add submodule | `git submodule add https://github.com/user/lib.git` |
| `git archive --format=zip HEAD > project.zip` | Create archive | `git archive --format=zip HEAD > project.zip` |

## 🚨 Emergency Commands

| 💻 Command | 📝 Description | 🎯 Example |
|:-----------|:---------------|:-----------|
| `git reset --hard HEAD` | Discard all local changes | `git reset --hard HEAD` |
| `git checkout -- <file>` | Discard changes in specific file | `git checkout -- index.html` |
| `git restore <file>` | Restore file to last commit | `git restore index.html` |
| `git restore --staged <file>` | Unstage file | `git restore --staged index.html` |
| `git commit --amend` | Modify last commit | `git commit --amend` |
| `git push --force-with-lease` | Force push safely | `git push --force-with-lease` |

## 📊 Useful Aliases

| 💻 Alias Setup | 📝 Description |
|:---------------|:---------------|
| `git config --global alias.st status` | `git st` for status |
| `git config --global alias.co checkout` | `git co` for checkout |
| `git config --global alias.br branch` | `git br` for branch |
| `git config --global alias.ci commit` | `git ci` for commit |
| `git config --global alias.unstage 'reset HEAD --'` | `git unstage` to unstage files |
| `git config --global alias.last 'log -1 HEAD'` | `git last` for last commit |
| `git config --global alias.visual '!gitk'` | `git visual` for GUI |