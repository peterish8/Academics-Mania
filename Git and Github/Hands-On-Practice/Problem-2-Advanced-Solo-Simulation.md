# 🎭 Problem 2: Advanced Solo Simulation (Multi-Developer Scenario)

## 📋 Problem Statement

**Scenario**: You're simulating a **real-world development team** working on a **Task Management App**. You'll play the role of **3 different developers** (Frontend Dev, Backend Dev, and DevOps Engineer) by switching between different branches and repositories. This advanced exercise will test your understanding of complex Git workflows, multiple merge conflicts, reset operations, and advanced collaboration patterns.

**Goal**: Experience advanced Git scenarios including complex merges, reset operations, branch management, and simulate real team conflicts that happen in professional development.

---

## 🎯 What You'll Master
- ✅ Advanced branching strategies
- ✅ Complex merge conflict resolution
- ✅ All three reset types (soft, mixed, hard)
- ✅ Multiple remote repositories
- ✅ Git history manipulation
- ✅ Professional workflow simulation
- ✅ Crisis management (recovering from mistakes)

---

## 🏗️ Project Overview

You'll build a **Task Management App** with these components:
- **Frontend**: HTML/CSS/JavaScript interface
- **Backend**: API configuration and data files
- **DevOps**: Deployment scripts and configuration
- **Documentation**: README and setup guides

---

## 🚀 Complete Step-by-Step Guide

### 🎬 Setup Phase: Create the Simulation Environment

#### Step 1: Create Main Repository
```bash
# Create project directory
mkdir task-management-app
cd task-management-app

# Initialize Git repository
git init

# Create initial project structure
echo "# Task Management App

A collaborative task management application built by a distributed team.

## Team Members
- Frontend Developer: UI/UX and client-side logic
- Backend Developer: API and data management  
- DevOps Engineer: Deployment and infrastructure

## Project Status
🚧 In Development" > README.md

# Create basic project structure
mkdir frontend backend devops docs

echo "<!-- Frontend placeholder -->" > frontend/index.html
echo "# Backend API" > backend/api.md
echo "# Deployment Guide" > devops/deploy.md
echo "# Project Documentation" > docs/setup.md

# Initial commit
git add .
git commit -m "Initial project setup with team structure"

# Create GitHub repository (optional but recommended)
# Go to GitHub, create new repo, then:
# git remote add origin https://github.com/YOUR-USERNAME/task-management-app.git
# git push -u origin main
```

---

### 👨‍💻 Act as Frontend Developer

#### Step 2: Frontend Development Branch
```bash
# Create and switch to frontend branch
git checkout -b feature/frontend-ui

# Create the main HTML structure
echo "<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Task Manager</title>
    <link rel='stylesheet' href='styles.css'>
</head>
<body>
    <header>
        <h1>Task Management App</h1>
        <nav>
            <button id='add-task'>Add Task</button>
            <button id='view-all'>View All</button>
        </nav>
    </header>
    
    <main>
        <div id='task-container'>
            <div class='task-item'>
                <h3>Sample Task</h3>
                <p>This is a sample task created by Frontend Dev</p>
                <span class='status pending'>Pending</span>
            </div>
        </div>
    </main>
    
    <script src='app.js'></script>
</body>
</html>" > frontend/index.html

# Create CSS styling
echo "/* Task Manager Styles - Frontend Dev */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    margin-left: 0.5rem;
    border-radius: 4px;
    cursor: pointer;
}

nav button:hover {
    background-color: #2980b9;
}

#task-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.task-item {
    background: white;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #3498db;
}

.status {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: bold;
}

.status.pending {
    background-color: #f39c12;
    color: white;
}" > frontend/styles.css

# Create JavaScript functionality
echo "// Task Manager JavaScript - Frontend Dev
class TaskManager {
    constructor() {
        this.tasks = [];
        this.init();
    }
    
    init() {
        console.log('Task Manager initialized by Frontend Dev');
        this.loadSampleTasks();
        this.bindEvents();
    }
    
    loadSampleTasks() {
        this.tasks = [
            {
                id: 1,
                title: 'Design UI Components',
                description: 'Create reusable UI components',
                status: 'pending',
                assignee: 'Frontend Dev'
            },
            {
                id: 2,
                title: 'Implement Task Creation',
                description: 'Add functionality to create new tasks',
                status: 'in-progress',
                assignee: 'Frontend Dev'
            }
        ];
        this.renderTasks();
    }
    
    bindEvents() {
        document.getElementById('add-task').addEventListener('click', () => {
            this.addTask();
        });
        
        document.getElementById('view-all').addEventListener('click', () => {
            this.renderTasks();
        });
    }
    
    addTask() {
        // Placeholder for add task functionality
        console.log('Add task functionality - Frontend Dev implementation');
    }
    
    renderTasks() {
        const container = document.getElementById('task-container');
        container.innerHTML = this.tasks.map(task => \`
            <div class='task-item'>
                <h3>\${task.title}</h3>
                <p>\${task.description}</p>
                <span class='status \${task.status}'>\${task.status}</span>
                <small>Assigned to: \${task.assignee}</small>
            </div>
        \`).join('');
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TaskManager();
});" > frontend/app.js

# Commit frontend work
git add .
git commit -m "Implement frontend UI with task display and styling

- Add responsive HTML structure
- Create modern CSS styling with task cards
- Implement basic JavaScript task management
- Add sample tasks for testing"

# Push frontend branch (if using GitHub)
# git push -u origin feature/frontend-ui
```

---

### 👨‍💼 Act as Backend Developer

#### Step 3: Switch to Backend Development
```bash
# Switch back to main branch
git checkout main

# Create backend development branch
git checkout -b feature/backend-api

# Create API configuration
echo "{
  \"api\": {
    \"version\": \"1.0.0\",
    \"name\": \"Task Management API\",
    \"description\": \"RESTful API for task management - Backend Dev\",
    \"endpoints\": {
      \"tasks\": {
        \"GET /api/tasks\": \"Get all tasks\",
        \"POST /api/tasks\": \"Create new task\",
        \"PUT /api/tasks/:id\": \"Update task\",
        \"DELETE /api/tasks/:id\": \"Delete task\"
      },
      \"users\": {
        \"GET /api/users\": \"Get all users\",
        \"POST /api/users\": \"Create user\"
      }
    }
  },
  \"database\": {
    \"type\": \"JSON\",
    \"location\": \"./data/tasks.json\"
  }
}" > backend/api-config.json

# Create sample data structure
mkdir backend/data
echo "[
  {
    \"id\": 1,
    \"title\": \"Setup Database Schema\",
    \"description\": \"Design and implement database structure for tasks\",
    \"status\": \"completed\",
    \"priority\": \"high\",
    \"assignee\": \"Backend Dev\",
    \"created_at\": \"2024-01-15T10:00:00Z\",
    \"updated_at\": \"2024-01-15T14:30:00Z\"
  },
  {
    \"id\": 2,
    \"title\": \"Implement API Endpoints\",
    \"description\": \"Create RESTful API endpoints for task operations\",
    \"status\": \"in-progress\",
    \"priority\": \"high\",
    \"assignee\": \"Backend Dev\",
    \"created_at\": \"2024-01-15T11:00:00Z\",
    \"updated_at\": \"2024-01-15T15:00:00Z\"
  },
  {
    \"id\": 3,
    \"title\": \"Add Authentication\",
    \"description\": \"Implement user authentication and authorization\",
    \"status\": \"pending\",
    \"priority\": \"medium\",
    \"assignee\": \"Backend Dev\",
    \"created_at\": \"2024-01-15T12:00:00Z\",
    \"updated_at\": \"2024-01-15T12:00:00Z\"
  }
]" > backend/data/tasks.json

# Create API documentation
echo "# Task Management API Documentation

## Overview
RESTful API for managing tasks and users - Built by Backend Developer

## Authentication
- JWT tokens for user authentication
- API key required for all requests

## Endpoints

### Tasks
\`\`\`
GET    /api/tasks           - Get all tasks
POST   /api/tasks           - Create new task
GET    /api/tasks/:id       - Get specific task
PUT    /api/tasks/:id       - Update task
DELETE /api/tasks/:id       - Delete task
\`\`\`

### Users
\`\`\`
GET    /api/users           - Get all users
POST   /api/users           - Create user
GET    /api/users/:id       - Get specific user
\`\`\`

## Data Models

### Task Model
\`\`\`json
{
  \"id\": \"number\",
  \"title\": \"string\",
  \"description\": \"string\",
  \"status\": \"pending|in-progress|completed\",
  \"priority\": \"low|medium|high\",
  \"assignee\": \"string\",
  \"created_at\": \"ISO 8601 date\",
  \"updated_at\": \"ISO 8601 date\"
}
\`\`\`

## Error Handling
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error" > backend/README.md

# Commit backend work
git add .
git commit -m "Implement backend API structure and documentation

- Add API configuration with endpoint definitions
- Create sample task data with proper schema
- Implement comprehensive API documentation
- Setup data directory structure"
```

---

### 🔧 Act as DevOps Engineer

#### Step 4: Switch to DevOps Development
```bash
# Switch back to main
git checkout main

# Create DevOps branch
git checkout -b feature/devops-deployment

# Create deployment scripts
echo "#!/bin/bash
# Deployment script for Task Management App - DevOps Engineer

echo \"🚀 Starting deployment process...\"

# Build frontend
echo \"📦 Building frontend assets...\"
cd frontend
# In real scenario: npm run build
echo \"Frontend build completed\"

# Setup backend
echo \"⚙️ Setting up backend services...\"
cd ../backend
# In real scenario: npm install, database setup
echo \"Backend services configured\"

# Run tests
echo \"🧪 Running tests...\"
# In real scenario: npm test
echo \"All tests passed\"

# Deploy to server
echo \"🌐 Deploying to production server...\"
# In real scenario: rsync, docker deploy, etc.
echo \"Deployment completed successfully\"

echo \"✅ Task Management App deployed successfully!\"
echo \"📊 Deployment by: DevOps Engineer\"
echo \"🕒 Deployed at: \$(date)\"" > devops/deploy.sh

# Create Docker configuration
echo "# Task Management App - Docker Configuration
# Created by DevOps Engineer

version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - \"3000:3000\"
    environment:
      - NODE_ENV=production
    depends_on:
      - backend
      
  backend:
    build: ./backend
    ports:
      - \"5000:5000\"
    environment:
      - NODE_ENV=production
      - DB_HOST=database
    depends_on:
      - database
      
  database:
    image: postgres:13
    environment:
      - POSTGRES_DB=taskmanager
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secure_password
    volumes:
      - db_data:/var/lib/postgresql/data
      
volumes:
  db_data:" > devops/docker-compose.yml

# Create environment configuration
echo "# Environment Configuration - DevOps Engineer
# Production Environment Variables

# Application Settings
APP_NAME=TaskManagementApp
APP_VERSION=1.0.0
NODE_ENV=production

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=taskmanager
DB_USER=admin
DB_PASSWORD=secure_password

# API Configuration
API_PORT=5000
API_BASE_URL=/api/v1

# Frontend Configuration
FRONTEND_PORT=3000
FRONTEND_BUILD_PATH=./dist

# Security Settings
JWT_SECRET=your_jwt_secret_here
API_KEY=your_api_key_here

# Monitoring
LOG_LEVEL=info
ENABLE_MONITORING=true" > devops/.env.production

# Create monitoring configuration
echo "# Monitoring and Logging Configuration
# Setup by DevOps Engineer

## Application Monitoring
- Health checks every 30 seconds
- Performance metrics collection
- Error tracking and alerting

## Logging Strategy
- Application logs: /var/log/taskmanager/app.log
- Error logs: /var/log/taskmanager/error.log
- Access logs: /var/log/taskmanager/access.log

## Backup Strategy
- Database backup: Daily at 2 AM UTC
- File backup: Weekly on Sundays
- Retention: 30 days for daily, 12 weeks for weekly

## Security Measures
- SSL/TLS encryption
- Regular security updates
- Access control and authentication
- Rate limiting on API endpoints" > devops/monitoring.md

# Commit DevOps work
git add .
git commit -m "Setup DevOps infrastructure and deployment pipeline

- Add automated deployment script with build process
- Create Docker configuration for containerized deployment
- Setup environment variables for different stages
- Implement monitoring and logging strategy"
```

---

### 🔥 Create Intentional Conflicts (The Fun Part!)

#### Step 5: Merge Conflicts Simulation
```bash
# Switch to main and merge frontend first
git checkout main
git merge feature/frontend-ui

# Now merge backend (this should work fine)
git merge feature/backend-api

# Now let's create a conflict by modifying the same file from different branches
# Go back to frontend branch and modify README
git checkout feature/frontend-ui
echo "# Task Management App

A modern, responsive task management application.

## Frontend Features (by Frontend Dev)
- ✅ Responsive design
- ✅ Interactive task cards  
- ✅ Modern CSS styling
- ✅ JavaScript task management
- 🚧 Real-time updates (coming soon)

## Technology Stack
- HTML5 & CSS3
- Vanilla JavaScript
- Modern ES6+ features

## Setup Instructions
1. Open frontend/index.html in browser
2. No build process required
3. Works offline

Built with ❤️ by Frontend Developer" > README.md

git add .
git commit -m "Update README with frontend-focused information"

# Switch to DevOps branch and modify same README differently
git checkout feature/devops-deployment
echo "# Task Management App

Enterprise-grade task management solution with full DevOps pipeline.

## DevOps Features (by DevOps Engineer)
- ✅ Docker containerization
- ✅ Automated deployment pipeline
- ✅ Environment configuration management
- ✅ Monitoring and logging setup
- 🚧 Kubernetes orchestration (coming soon)

## Infrastructure
- Docker & Docker Compose
- Production-ready configuration
- Automated backup strategy
- Security best practices

## Deployment
\`\`\`bash
chmod +x devops/deploy.sh
./devops/deploy.sh
\`\`\`

## Monitoring
- Health checks
- Performance metrics
- Error tracking
- Log aggregation

Built for scale by DevOps Engineer" > README.md

git add .
git commit -m "Update README with DevOps and infrastructure focus"

# Now try to merge DevOps into main - this will create a conflict!
git checkout main
git merge feature/devops-deployment
```

**🚨 CONFLICT ALERT!** You should now see a merge conflict in README.md.

#### Step 6: Resolve the Complex Conflict
```bash
# Check the conflict
git status
# You'll see: both modified: README.md

# Open README.md in your editor
# You'll see something like:
# <<<<<<< HEAD
# Frontend version content
# =======  
# DevOps version content
# >>>>>>> feature/devops-deployment

# Resolve by creating a comprehensive README that includes both perspectives
```

**Create this combined README.md:**
```markdown
# Task Management App

A collaborative, enterprise-grade task management application built by a distributed development team.

## 🎯 Project Overview
Modern task management solution combining responsive frontend design with robust backend API and professional DevOps practices.

## 👥 Team Contributions

### Frontend Features (by Frontend Developer)
- ✅ Responsive design with modern CSS
- ✅ Interactive task cards and UI components
- ✅ JavaScript task management system
- ✅ User-friendly interface
- 🚧 Real-time updates (coming soon)

### Backend Features (by Backend Developer)  
- ✅ RESTful API with comprehensive endpoints
- ✅ JSON-based data storage
- ✅ Task CRUD operations
- ✅ User management system
- 🚧 Authentication system (coming soon)

### DevOps Features (by DevOps Engineer)
- ✅ Docker containerization
- ✅ Automated deployment pipeline
- ✅ Environment configuration management
- ✅ Monitoring and logging setup
- 🚧 Kubernetes orchestration (coming soon)

## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: RESTful API, JSON data storage
- **DevOps**: Docker, Docker Compose, Bash scripting
- **Infrastructure**: Production-ready configuration

## 🚀 Quick Start

### Development Setup
1. Clone the repository
2. Open `frontend/index.html` in browser for UI
3. Check `backend/README.md` for API documentation

### Production Deployment
```bash
chmod +x devops/deploy.sh
./devops/deploy.sh
```

## 📊 Project Structure
```
task-management-app/
├── frontend/          # UI components and styling
├── backend/           # API and data management
├── devops/           # Deployment and infrastructure
└── docs/             # Project documentation
```

## 🔧 Monitoring & Maintenance
- Health checks and performance metrics
- Automated backup strategy
- Security best practices
- Error tracking and logging

---
**Built collaboratively by Frontend Dev, Backend Dev, and DevOps Engineer** 🤝
```

```bash
# After resolving the conflict
git add README.md
git commit -m "Resolve merge conflict: combine frontend and DevOps documentation

- Integrate frontend features and UI information
- Include DevOps deployment and infrastructure details  
- Create comprehensive project overview
- Maintain contributions from all team members"
```

---

### 🎭 Advanced Git Operations Practice

#### Step 7: Practice Reset Operations
```bash
# Let's practice different reset types
# First, make some changes we'll reset

echo "// Emergency hotfix - critical bug found!
console.log('HOTFIX: Temporary debug code');
// TODO: Remove this debug code before production" >> frontend/app.js

git add .
git commit -m "HOTFIX: Add temporary debug code for critical bug"

# Oops! We committed debug code. Let's practice reset types:

# 1. Soft reset - undo commit but keep changes staged
git reset --soft HEAD~1
git status  # Changes should be staged
echo "✅ Soft reset: Commit undone, changes still staged"

# Recommit with better message
git commit -m "Add debugging utilities for development"

# 2. Mixed reset - undo commit and unstage changes
git reset HEAD~1  # This is --mixed by default
git status  # Changes should be unstaged but still in files
echo "✅ Mixed reset: Commit undone, changes unstaged but preserved"

# 3. Let's commit again and try hard reset
git add .
git commit -m "Add debugging code again"

# Hard reset - DANGEROUS! Completely removes changes
echo "⚠️  About to do HARD reset - this will delete changes!"
git reset --hard HEAD~1
git status  # Should be clean, changes completely gone
echo "✅ Hard reset: Commit and changes completely removed"
```

#### Step 8: Practice Advanced History Management
```bash
# Create some commits to practice with
echo "Feature 1" > feature1.txt
git add .
git commit -m "Add feature 1"

echo "Feature 2" > feature2.txt  
git add .
git commit -m "Add feature 2"

echo "Bug fix" > bugfix.txt
git add .
git commit -m "Fix critical bug"

# View history
git log --oneline -5

# Practice viewing specific commits
git show HEAD~2  # Show feature 1 commit
git diff HEAD~3..HEAD  # Compare current with 3 commits ago

# Practice branch management
git branch -a  # List all branches
git branch feature/cleanup  # Create new branch
git checkout feature/cleanup

# Clean up temporary files
rm -f feature1.txt feature2.txt bugfix.txt
git add .
git commit -m "Clean up temporary development files"

# Switch back and merge
git checkout main
git merge feature/cleanup

# Clean up branches
git branch -d feature/cleanup
git branch -d feature/frontend-ui
git branch -d feature/backend-api  
git branch -d feature/devops-deployment
```

---

## 🎯 Advanced Challenges (Optional)

### Challenge 1: Simulate Emergency Hotfix
```bash
# Simulate production emergency
git checkout -b hotfix/security-patch

echo "// SECURITY PATCH - Immediate deployment required
// Fix for potential XSS vulnerability
function sanitizeInput(input) {
    return input.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
}

// Apply sanitization to all user inputs
document.addEventListener('DOMContentLoaded', () => {
    console.log('Security patch applied - XSS protection enabled');
});" > frontend/security-patch.js

# Update HTML to include security patch
sed -i 's/<script src="app.js"><\/script>/<script src="security-patch.js"><\/script>\n    <script src="app.js"><\/script>/' frontend/index.html

git add .
git commit -m "SECURITY HOTFIX: Add XSS protection

- Implement input sanitization function
- Apply protection to all user inputs  
- Critical security vulnerability patched
- Requires immediate deployment"

# Merge hotfix directly to main (emergency process)
git checkout main
git merge hotfix/security-patch
git branch -d hotfix/security-patch

echo "🚨 Emergency hotfix deployed successfully!"
```

### Challenge 2: Simulate Rollback Scenario
```bash
# Simulate a bad deployment that needs rollback
echo "// BROKEN FEATURE - DO NOT USE
function brokenFeature() {
    // This code has serious bugs
    undefined.someMethod(); // This will crash!
}" >> frontend/app.js

git add .
git commit -m "Add new feature with advanced functionality"

# Oops! The feature is broken and causing crashes
# Practice rollback using revert (safe for shared repos)
git revert HEAD

# Check that the broken code is gone
cat frontend/app.js | grep "brokenFeature" || echo "✅ Broken code successfully reverted"
```

---

## 🏆 Success Criteria

You've mastered advanced Git when you can:

### ✅ Repository Management
- [x] Created complex project structure
- [x] Managed multiple feature branches
- [x] Simulated multi-developer workflow

### ✅ Conflict Resolution
- [x] Created intentional merge conflicts
- [x] Resolved complex conflicts involving multiple files
- [x] Combined different perspectives in conflict resolution

### ✅ Reset Mastery
- [x] Used soft reset to fix commit messages
- [x] Used mixed reset to modify commits
- [x] Understood dangers of hard reset
- [x] Applied appropriate reset type for each scenario

### ✅ Advanced Operations
- [x] Managed complex Git history
- [x] Performed emergency hotfixes
- [x] Executed safe rollbacks with revert
- [x] Cleaned up branches and maintained repository

### ✅ Professional Workflow
- [x] Simulated real-world development scenarios
- [x] Practiced crisis management
- [x] Understood team collaboration patterns
- [x] Applied Git best practices consistently

---

## 🎓 Reflection Questions

After completing this exercise, consider:

1. **Workflow Understanding**: Which Git workflow felt most natural? Why?

2. **Conflict Resolution**: What strategies worked best for resolving complex conflicts?

3. **Reset Operations**: When would you use each type of reset in real projects?

4. **Team Simulation**: How did simulating multiple developers help your understanding?

5. **Crisis Management**: How would you handle similar emergencies in real projects?

6. **Best Practices**: What Git practices will you adopt in future projects?

---

## 🚀 Next Level Challenges

Ready for more? Try these advanced scenarios:

### 🔥 Expert Level
- **Rebase Practice**: Learn interactive rebase to clean up commit history
- **Cherry-picking**: Practice selecting specific commits between branches  
- **Submodules**: Manage dependencies with Git submodules
- **Hooks**: Implement Git hooks for automated testing
- **Bisect**: Use Git bisect to find bug-introducing commits

### 🌟 Professional Level
- **GitFlow**: Implement GitFlow branching strategy
- **Semantic Versioning**: Practice proper version tagging
- **CI/CD Integration**: Connect Git with continuous integration
- **Code Review**: Practice thorough code review processes
- **Open Source**: Contribute to real open source projects

---

## 🎉 Congratulations!

You've successfully completed an advanced Git simulation that mirrors real-world development scenarios. You now have the skills to:

- Handle complex team collaborations
- Resolve challenging merge conflicts  
- Use Git reset operations safely and effectively
- Manage professional development workflows
- Recover from common Git mistakes

**You're now ready for professional Git usage! 🎊**

---

## 📚 Additional Resources

- **Git Documentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **Interactive Practice**: [learngitbranching.js.org](https://learngitbranching.js.org/)
- **Advanced Git**: [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials/advanced-overview)
- **Professional Workflows**: [GitHub Flow](https://guides.github.com/introduction/flow/)

**Keep practicing and happy coding! 🚀**