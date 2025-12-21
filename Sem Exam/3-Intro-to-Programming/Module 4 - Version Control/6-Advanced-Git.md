# 🚀 Advanced Git (Rebase, Stash, Reset)

## 📌 1. Rebase vs Merge
- **Merge**: Creates a specific "merge commit". Preserves history exactly as it happened. Good for `main` branch history.
- **Rebase**: Moves your branch to the tip of another. Rewrites history to make it linear. Good for cleaning up feature branches before merging.

`git rebase main`

## 🎒 2. Stash
Save your uncommitted changes temporarily without committing.
- `git stash`: Save changes.
- `git stash pop`: Apply saved changes back.

## ⏪ 3. Reset
Undo changes.
- `git reset --soft HEAD~1`: Undo commit, keep changes staged.
- `git reset --hard HEAD~1`: Undo commit and **delete** changes (Dangerous!).

## 🍒 4. Cherry-Pick
Pick a specific commit from another branch and apply it to yours.
`git cherry-pick <commit-hash>`

---
> [[Sem Exam/3-Intro-to-Programming/Module 4 - Version Control/README|🔙 Back to Module 4 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
