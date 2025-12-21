# 06 Creating New Projects

There are **two main ways** to start a Git project:
1. **Clone** an existing repository from GitHub
2. **Initialize** a new repository locally and link to GitHub

## 🔄 Method 1: Cloning from GitHub

Use this when you want to work on an existing project or start from a template.

### Basic Clone Command
```bash
# Clone a repository
git clone https://github.com/username/repository-name.git

# Clone into specific folder
git clone https://github.com/username/repository-name.git my-project

# Clone specific branch
git clone -b branch-name https://github.com/username/repository-name.git
```

### 💡 Real Example
```bash
# Clone a popular project
git clone https://github.com/microsoft/vscode.git

# This creates a 'vscode' folder with complete project history
```

### What Happens When You Clone?
- ✅ Downloads complete repository with full history
- ✅ Sets up remote connection to original repository  
- ✅ Creates local working directory
- ✅ Automatically configures Git tracking

### Useful Commands After Cloning
```bash
# Navigate to cloned directory
cd repository-name

# Check remote connections
git remote -v

# See project status
git status

# View commit history
git log --oneline
```

## 🆕 Method 2: Initialize Local Project

Use this when starting a completely new project from scratch.

### Step-by-Step Process

#### 1. Create Project Directory
```bash
# Create new folder
mkdir my-new-project

# Navigate into folder
cd my-new-project
```

#### 2. Initialize Git Repository
```bash
# Initialize Git in current directory
git init

# This creates a hidden .git folder
```

#### 3. Create Initial Files
```bash
# Create a README file
echo "# My New Project" >> README.md

# Create main project file
echo "<h1>Hello World</h1>" >> index.html
```

#### 4. Stage and Commit Files
```bash
# Add files to staging area
git add .

# Create first commit
git commit -m "Initial commit"
```

#### 5. Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New repository" (+ icon)
3. Enter repository name
4. Choose public/private
5. **Don't** initialize with README (you already have files)
6. Click "Create repository"

#### 6. Connect Local to GitHub
```bash
# Add remote connection (replace with your repository URL)
git remote add origin https://github.com/yourusername/my-new-project.git

# Push code to GitHub
git push -u origin main
```

## 🔗 Understanding Remotes

A **remote** is a connection between your local repository and a hosted repository (like GitHub).

### Common Remote Commands
```bash
# View remote connections
git remote -v

# Add new remote
git remote add origin https://github.com/user/repo.git

# Change remote URL
git remote set-url origin https://github.com/user/new-repo.git

# Remove remote
git remote remove origin
```

### 💡 Remote Naming Convention
- **origin**: Default name for main remote repository
- **upstream**: Often used for original repository when you fork
- **backup**: Sometimes used for backup repositories

## 📊 Method Comparison

| Aspect | Clone Method | Initialize Method |
|--------|--------------|-------------------|
| **Use Case** | Existing project | Brand new project |
| **Setup Speed** | Fast | More steps |
| **History** | Full history included | Starts fresh |
| **Remote** | Auto-configured | Manual setup required |
| **Best For** | Contributing to projects | Personal projects |

## 🛠️ Complete Example Workflows

### Workflow 1: Contributing to Open Source
```bash
# 1. Fork repository on GitHub (click Fork button)
# 2. Clone your fork
git clone https://github.com/yourusername/project.git
cd project

# 3. Add original repository as upstream
git remote add upstream https://github.com/original/project.git

# 4. Create feature branch
git checkout -b new-feature

# 5. Make changes and commit
git add .
git commit -m "Add new feature"

# 6. Push to your fork
git push origin new-feature

# 7. Create Pull Request on GitHub
```

### Workflow 2: Starting Personal Project
```bash
# 1. Create and setup local repository
mkdir my-website
cd my-website
git init

# 2. Create initial files
echo "# My Personal Website" >> README.md
echo "<!DOCTYPE html><html><body><h1>Coming Soon</h1></body></html>" >> index.html

# 3. First commit
git add .
git commit -m "Initial website structure"

# 4. Create GitHub repository (via web interface)
# 5. Connect and push
git remote add origin https://github.com/yourusername/my-website.git
git push -u origin main
```

## ⚙️ Pro Tips

### Tip 1: Use SSH for Easier Authentication
```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to GitHub account (copy public key)
cat ~/.ssh/id_ed25519.pub

# Clone using SSH
git clone git@github.com:username/repository.git
```

### Tip 2: Clone with Specific Depth
```bash
# Clone only recent commits (faster for large repositories)
git clone --depth 1 https://github.com/username/repository.git
```

### Tip 3: Template Repositories
```bash
# Use GitHub template feature for project starters
# Click "Use this template" on GitHub instead of cloning
```

## 🧩 Quick Recap

✅ **Clone Method**: Fast setup for existing projects  
✅ **Initialize Method**: Full control for new projects  
✅ **Remotes**: Connect local and cloud repositories  
✅ **First commit**: Always start with initial files  
✅ **Push**: Share your code with `git push`  

---

**[← Previous: Installing Git](05_Installing_Git.md) | [Next → Staging and Commit Workflow](07_Staging_Commit_Workflow.md)**