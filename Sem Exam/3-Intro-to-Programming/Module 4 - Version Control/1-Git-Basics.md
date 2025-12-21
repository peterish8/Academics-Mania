# 🌱 Git Basics & Branching

## 📌 1. Essential Commands
Set up your identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### **Core Workflow**
1. **Init**: `git init` (Start a new repo)
2. **Clone**: `git clone <url>` (Download existing repo)
3. **Status**: `git status` (Check chanegs)
4. **Add**: `git add .` (Stage changes)
5. **Commit**: `git commit -m "Message"` (Save changes)
6. **Push**: `git push origin main` (Upload to remote)
7. **Pull**: `git pull origin main` (Download updates)

---

## 🌿 2. Branching & Merging
Branches allow you to work on features in isolation.

```bash
# Create and switch to a new branch
git checkout -b feature-login

# Switch back to main
git checkout main

# Merge feature into main
git merge feature-login
```

---

## 🧠 Practice Exercises
1. **Local Repo**: Initialize a git repo, create a file, commit it, create a new branch, change the file, commit again, and merge it back to main.

---
> [[Sem Exam/3-Intro-to-Programming/Module 4 - Version Control/README|🔙 Back to Module 4 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
