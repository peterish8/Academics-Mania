# 05 Installing Git & Configuration

## 💾 Installing Git

### Download Git
Visit the official Git website: **[https://git-scm.com](https://git-scm.com)**

### Platform-Specific Installation

#### Windows
1. Download Git for Windows installer
2. Run the `.exe` file
3. Follow installation wizard (default settings are fine)
4. Git Bash will be available for command line

#### macOS
```bash
# Using Homebrew (recommended)
brew install git

# Or download from git-scm.com
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
```

#### Linux (CentOS/RHEL)
```bash
sudo yum install git
# or for newer versions
sudo dnf install git
```

## ✅ Verify Installation

Check if Git is properly installed:

```bash
# Check Git version
git --version

# Expected output example:
# git version 2.40.1
```

If you see a version number, Git is successfully installed!

## ⚙️ Basic Git Configuration

After installation, configure Git with your identity. This information will be attached to your commits.

### Set Your Identity

```bash
# Set your name (use your real name)
git config --global user.name "Your Full Name"

# Set your email (use same email as GitHub account)
git config --global user.email "your.email@example.com"
```

### 💡 Configuration Examples

```bash
# Example configuration
git config --global user.name "John Smith"
git config --global user.email "john.smith@gmail.com"
```

## 🔍 Check Your Configuration

View all your Git settings:

```bash
# List all configuration settings
git config --list

# Check specific settings
git config user.name
git config user.email
```

### Sample Output
```
user.name=John Smith
user.email=john.smith@gmail.com
core.autocrlf=true
core.editor=notepad
```

## 🛠️ Additional Useful Configurations

### Set Default Text Editor
```bash
# Set VS Code as default editor
git config --global core.editor "code --wait"

# Set Notepad (Windows)
git config --global core.editor "notepad"

# Set Vim (Linux/Mac)
git config --global core.editor "vim"
```

### Configure Line Endings
```bash
# Windows (converts LF to CRLF on checkout)
git config --global core.autocrlf true

# Mac/Linux (converts CRLF to LF on commit)
git config --global core.autocrlf input
```

### Set Default Branch Name
```bash
# Set 'main' as default branch name for new repositories
git config --global init.defaultBranch main
```

## 📋 Configuration Levels

Git has three levels of configuration:

| Level | Scope | Command Flag | File Location |
|-------|-------|--------------|---------------|
| **System** | All users | `--system` | `/etc/gitconfig` |
| **Global** | Current user | `--global` | `~/.gitconfig` |
| **Local** | Current repo | `--local` | `.git/config` |

### Priority Order
Local → Global → System (Local overrides Global, Global overrides System)

## 🔧 Essential Configuration Commands

```bash
# View configuration with locations
git config --list --show-origin

# Edit global config file directly
git config --global --edit

# Remove a configuration
git config --global --unset user.name

# Set configuration for current repository only
git config --local user.email "work.email@company.com"
```

## ❗ Common Configuration Issues

### Issue: Wrong Email Address
```bash
# Problem: Used personal email for work project
# Solution: Set local config for work repository
cd /path/to/work/project
git config --local user.email "work.email@company.com"
```

### Issue: Line Ending Problems
```bash
# Problem: Mixed line endings causing issues
# Solution: Configure autocrlf properly
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # Mac/Linux
```

## 🎯 Quick Setup Checklist

After installing Git, run these commands:

```bash
# 1. Verify installation
git --version

# 2. Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 3. Set default branch name
git config --global init.defaultBranch main

# 4. Set editor (optional)
git config --global core.editor "code --wait"

# 5. Verify configuration
git config --list
```

## 🧩 Quick Recap

✅ **Download**: Get Git from [git-scm.com](https://git-scm.com)  
✅ **Verify**: Check installation with `git --version`  
✅ **Configure**: Set name and email with `git config --global`  
✅ **Check**: View settings with `git config --list`  
✅ **Ready**: Git is now configured for your projects  

---

**[← Previous: Core Git Concepts](04_Core_Git_Concepts.md) | [Next → Creating New Projects](06_Creating_New_Projects.md)**