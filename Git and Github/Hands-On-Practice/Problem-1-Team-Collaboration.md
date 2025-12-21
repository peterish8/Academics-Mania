# 🤝 Problem 1: Team Collaboration Project

## 📋 Problem Statement

**Scenario**: You and your partner are building a simple **Recipe Sharing Website**. Person A will work on the homepage and navigation, while Person B will work on the recipe display and user features. You need to collaborate using Git and GitHub, handle merge conflicts, and practice the complete workflow.

**Goal**: Create a functional website with both team members contributing, experience real collaboration workflows, resolve conflicts, and use Pull Requests.

---

## 🎯 What You'll Practice
- ✅ Repository setup and cloning
- ✅ Branch creation and management  
- ✅ Collaborative development
- ✅ Merge conflicts (intentional)
- ✅ Pull Requests and code review
- ✅ Git history and tracking

---

## 👥 Team Setup

### Prerequisites
- Both partners have Git installed and configured
- Both have GitHub accounts
- Both have VS Code or preferred editor
- Good communication (Discord, Slack, or in-person)

---

## 🚀 Step-by-Step Instructions

### 🅰️ PERSON A INSTRUCTIONS (Repository Owner)

#### Step 1: Create Repository on GitHub
1. Go to [GitHub.com](https://github.com)
2. Click "New repository" (+ icon)
3. Repository name: `recipe-sharing-website`
4. Description: `A collaborative recipe sharing website built with HTML/CSS/JS`
5. Make it **Public**
6. ✅ Check "Add a README file"
7. Click "Create repository"

#### Step 2: Clone Repository Locally
```bash
# Clone the repository to your computer
git clone https://github.com/YOUR-USERNAME/recipe-sharing-website.git

# Navigate into the project
cd recipe-sharing-website

# Check status
git status
```

#### Step 3: Create Initial Project Structure
```bash
# Create basic files
echo "<!DOCTYPE html>
<html>
<head>
    <title>Recipe Sharing - Home</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <h1>Welcome to Recipe Sharing</h1>
    <p>Person A created this homepage</p>
</body>
</html>" > index.html

echo "/* Person A's CSS */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
}" > styles.css

# Stage and commit
git add .
git commit -m "Add initial homepage and basic styling"

# Push to GitHub
git push
```

#### Step 4: Add Partner as Collaborator
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Click "Collaborators" in left sidebar
4. Click "Add people"
5. Enter Person B's GitHub username
6. Send invitation

#### Step 5: Create Your Feature Branch
```bash
# Create branch for navigation feature
git checkout -b feature/navigation

# Add navigation to index.html
echo "<!DOCTYPE html>
<html>
<head>
    <title>Recipe Sharing - Home</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <nav>
        <ul>
            <li><a href='index.html'>Home</a></li>
            <li><a href='recipes.html'>Recipes</a></li>
            <li><a href='about.html'>About</a></li>
        </ul>
    </nav>
    <h1>Welcome to Recipe Sharing</h1>
    <p>Person A created this homepage with navigation</p>
</body>
</html>" > index.html

# Update CSS for navigation
echo "/* Person A's CSS */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

nav ul {
    list-style-type: none;
    padding: 0;
    background-color: #f0f0f0;
    margin: 0 0 20px 0;
}

nav li {
    display: inline;
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
}

h1 {
    color: #333;
}" > styles.css

# Commit changes
git add .
git commit -m "Add navigation menu to homepage"

# Push feature branch
git push -u origin feature/navigation
```

#### Step 6: Wait for Person B to Set Up
**⏳ WAIT**: Let Person B complete their setup (Steps 1-4) before continuing.

#### Step 7: Create Pull Request
1. Go to your repository on GitHub
2. You'll see "Compare & pull request" button for your branch
3. Click it
4. Title: `Add Navigation Menu`
5. Description: `Added navigation menu with Home, Recipes, and About links`
6. Click "Create pull request"
7. **DON'T MERGE YET** - wait for Person B's work

#### Step 8: Continue Development (Create Conflict)
```bash
# Switch back to main and pull latest
git checkout main
git pull

# Create another branch for footer
git checkout -b feature/footer

# Modify styles.css (this will create conflict with Person B)
echo "/* Person A's CSS - Updated */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f9f9f9;
}

nav ul {
    list-style-type: none;
    padding: 0;
    background-color: #f0f0f0;
    margin: 0 0 20px 0;
}

nav li {
    display: inline;
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
}

h1 {
    color: #333;
    text-align: center;
}

footer {
    margin-top: 50px;
    text-align: center;
    color: #666;
    border-top: 1px solid #ddd;
    padding-top: 20px;
}" > styles.css

# Add footer to index.html
echo "<!DOCTYPE html>
<html>
<head>
    <title>Recipe Sharing - Home</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <nav>
        <ul>
            <li><a href='index.html'>Home</a></li>
            <li><a href='recipes.html'>Recipes</a></li>
            <li><a href='about.html'>About</a></li>
        </ul>
    </nav>
    <h1>Welcome to Recipe Sharing</h1>
    <p>Person A created this homepage with navigation</p>
    <footer>
        <p>&copy; 2024 Recipe Sharing Website - Built by Person A & Person B</p>
    </footer>
</body>
</html>" > index.html

# Commit and push
git add .
git commit -m "Add footer and update styling"
git push -u origin feature/footer
```

#### Step 9: Merge Person B's Work First
1. Go to GitHub and merge Person B's Pull Request
2. Pull the updated main branch:
```bash
git checkout main
git pull
```

#### Step 10: Handle Merge Conflict
```bash
# Try to merge your footer branch
git merge feature/footer

# You'll get a conflict! Don't panic.
# Open styles.css in VS Code
# You'll see conflict markers like:
# <<<<<<< HEAD
# Person B's changes
# =======
# Your changes  
# >>>>>>> feature/footer

# Resolve by combining both changes logically
# Remove conflict markers and keep the best of both
```

#### Step 11: Complete the Project
```bash
# After resolving conflicts
git add .
git commit -m "Resolve merge conflict: combine footer and recipe styling"
git push
```

---

### 🅱️ PERSON B INSTRUCTIONS (Collaborator)

#### Step 1: Accept Collaboration Invitation
1. Check your email for GitHub invitation
2. Click "Accept invitation"
3. You now have access to Person A's repository

#### Step 2: Clone Repository
```bash
# Clone Person A's repository
git clone https://github.com/PERSON-A-USERNAME/recipe-sharing-website.git

# Navigate into project
cd recipe-sharing-website

# Check the current state
git status
git log --oneline
```

#### Step 3: Create Your Feature Branch
```bash
# Create branch for recipe features
git checkout -b feature/recipes

# Create recipes page
echo "<!DOCTYPE html>
<html>
<head>
    <title>Recipe Sharing - Recipes</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <h1>Our Recipes</h1>
    <div class='recipe-card'>
        <h3>Chocolate Chip Cookies</h3>
        <p>Delicious homemade cookies - Person B's favorite!</p>
        <p><strong>Prep time:</strong> 15 minutes</p>
    </div>
    <div class='recipe-card'>
        <h3>Pasta Carbonara</h3>
        <p>Classic Italian pasta dish</p>
        <p><strong>Prep time:</strong> 20 minutes</p>
    </div>
</body>
</html>" > recipes.html

# Update CSS (this will conflict with Person A later)
echo "/* Person A's CSS */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
}

/* Person B's additions */
.recipe-card {
    border: 1px solid #ddd;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
    background-color: #fff;
}

.recipe-card h3 {
    color: #e74c3c;
    margin-top: 0;
}

.recipe-card p {
    margin: 5px 0;
}" > styles.css

# Commit your work
git add .
git commit -m "Add recipes page with recipe cards styling"

# Push your branch
git push -u origin feature/recipes
```

#### Step 4: Create Pull Request
1. Go to the repository on GitHub
2. Click "Compare & pull request" for your branch
3. Title: `Add Recipes Page`
4. Description: `Created recipes page with sample recipes and card styling`
5. Click "Create pull request"

#### Step 5: Continue Development (More Features)
```bash
# Create about page
git checkout -b feature/about

echo "<!DOCTYPE html>
<html>
<head>
    <title>Recipe Sharing - About</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <h1>About Recipe Sharing</h1>
    <p>This website was built collaboratively by Person A and Person B using Git and GitHub!</p>
    <h2>Our Mission</h2>
    <p>To share delicious recipes with the world and practice Git collaboration.</p>
    <h2>Contributors</h2>
    <ul>
        <li>Person A - Homepage and Navigation</li>
        <li>Person B - Recipes and About Page</li>
    </ul>
</body>
</html>" > about.html

# Commit and push
git add .
git commit -m "Add about page with project information"
git push -u origin feature/about
```

#### Step 6: Review Person A's Pull Request
1. Go to Person A's Pull Request on GitHub
2. Click "Files changed" tab
3. Review the code changes
4. Add comments if needed
5. Click "Review changes" → "Approve" → "Submit review"

#### Step 7: Merge Your First PR
1. Merge your recipes Pull Request on GitHub
2. Delete the feature branch after merging

#### Step 8: Handle the Merge Conflict (When Person A Merges)
```bash
# Pull latest changes
git checkout main
git pull

# You'll see Person A's navigation changes
# Now when Person A tries to merge their footer branch,
# there will be conflicts in styles.css because you both modified it

# Help Person A resolve conflicts by communicating about:
# - What changes you made
# - What changes they made  
# - How to combine them logically
```

---

## 🎯 Expected Learning Outcomes

### After Completing This Exercise:

#### ✅ Repository Management
- Created and cloned repositories
- Added collaborators
- Managed remote connections

#### ✅ Branching Workflow
- Created feature branches
- Switched between branches
- Merged branches

#### ✅ Collaboration
- Made Pull Requests
- Reviewed code
- Communicated about changes

#### ✅ Conflict Resolution
- Encountered real merge conflicts
- Resolved conflicts manually
- Understood conflict markers

#### ✅ Git History
- Tracked project evolution
- Used git log effectively
- Understood commit messages

---

## 🚨 Troubleshooting Guide

### Problem: Can't Push to Repository
```bash
# Solution: Make sure you're added as collaborator
git remote -v  # Check remote URL
git push -u origin branch-name  # Set upstream
```

### Problem: Merge Conflicts Seem Overwhelming
```bash
# Solution: Communicate with partner
git merge --abort  # Cancel merge
# Discuss changes with partner
# Try merge again with better understanding
```

### Problem: Lost Track of Changes
```bash
# Solution: Use Git history
git log --oneline --graph --all  # See all branches
git status  # Check current state
git diff  # See what changed
```

---

## 🎉 Success Criteria

You've successfully completed this exercise when:

- ✅ Both partners contributed code to the repository
- ✅ At least 2 Pull Requests were created and merged
- ✅ You encountered and resolved at least 1 merge conflict
- ✅ The final website has content from both contributors
- ✅ You can explain the Git workflow you used
- ✅ Both partners understand branching and merging

---

## 🔄 Next Steps

After completing this exercise:
1. **Experiment more**: Try different branching strategies
2. **Add features**: Continue building the website
3. **Practice regularly**: Use this workflow in other projects
4. **Learn advanced Git**: Explore rebasing, cherry-picking
5. **Move to Problem 2**: Try the advanced solo exercise

**Great job on your first collaborative Git project! 🎊**