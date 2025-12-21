# Centralized vs Distributed VCS

## 🏢 Centralized Version Control System (CVCS)

A **single central server** stores the complete codebase. All developers connect to this server to commit and update code.

### Key Characteristics
- One main server controls entire project history
- Developers get only working copies (not full history)
- All operations require server connection
- If central server fails, version history becomes inaccessible

### Examples
- **Subversion (SVN)**
- **CVS (Concurrent Versions System)**
- **Perforce**

## 🌐 Distributed Version Control System (DVCS)

Every developer has a **full copy** of the repository including complete history on their local machine.

### Key Characteristics
- All operations (commit, log, diff) run locally
- Servers used mainly for collaboration and sharing
- If server fails, any developer can restore the repository
- Works offline completely

### Examples
- **Git** (most popular)
- **Mercurial**
- **Bazaar**

## ⚖️ Detailed Comparison

| Feature | Centralized VCS | Distributed VCS |
|---------|----------------|-----------------|
| **Repository Location** | Single central server | Every developer's machine |
| **History Access** | Server required | Available locally |
| **Offline Work** | Limited | Full functionality |
| **Backup** | Single point of failure | Multiple complete backups |
| **Speed** | Network dependent | Local operations are fast |
| **Branching** | Complex/expensive | Easy and lightweight |
| **Merging** | Server-side conflicts | Local conflict resolution |
| **Collaboration** | Through central server | Peer-to-peer + server |

## 🔄 Workflow Comparison

### Centralized Workflow
```bash
# Developer A
svn checkout http://server/repo  # Get working copy
# Edit files
svn commit -m "Changes"          # Send to server

# Developer B  
svn update                       # Get latest from server
# Edit files
svn commit -m "More changes"     # Send to server
```

### Distributed Workflow
```bash
# Developer A
git clone https://github.com/user/repo  # Get full repository
# Edit files
git add .
git commit -m "Changes"                  # Local commit
git push origin main                     # Share with others

# Developer B
git pull origin main                     # Get latest changes
# Edit files  
git add .
git commit -m "More changes"             # Local commit
git push origin main                     # Share with others
```

## ✅ Advantages of Distributed VCS

### 🚀 Performance
- **Fast operations**: No network latency for common tasks
- **Local branching**: Create branches instantly
- **Quick commits**: Save work without network delays

### 🛡️ Reliability  
- **No single point of failure**: Every clone is a backup
- **Work offline**: Full functionality without internet
- **Data integrity**: Cryptographic checksums prevent corruption

### 🤝 Flexibility
- **Multiple workflows**: Centralized, feature-branch, forking
- **Easy experimentation**: Branch and merge without fear
- **Selective sharing**: Choose what and when to share

## ❗ When to Use Each

### Use Centralized VCS When:
- Simple, linear development process
- Strong need for access control
- Large binary files (though Git LFS helps)
- Team prefers centralized workflow

### Use Distributed VCS When:
- Multiple developers working simultaneously
- Need for offline development
- Complex branching and merging
- Open source or distributed teams

## 🧩 Quick Recap

✅ **Centralized**: Single server, simple but limited  
✅ **Distributed**: Full local copies, flexible and robust  
✅ **Git**: Most popular distributed VCS  
✅ **Better offline work** and **faster operations** with DVCS  

---

**[← Previous: GitHub Overview](02_GitHub_Overview.md) | [Next → Core Git Concepts](04_Core_Git_Concepts.md)**