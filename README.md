#  Git Version Control Project — Python Calculator

##  Introduction
This project demonstrates complete end-to-end usage of **Git** and **GitHub** for version control.  
The objective was to create a simple Python-based calculator program and use Git to track changes, commit updates, create multiple branches, resolve conflicts, and finally push the repository to GitHub.

This README includes all Git commands used, screenshots placeholder sections, challenges faced, and a conclusion summarizing the learning outcomes.

## 📝 Project Description

The project contains two Python files:

### **1. utils.py**
Contains the core mathematical functions:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b) with zero-division handling

### **2. calculator.py**
Implements:
- menu display  
- user input  
- calling functions from utils.py  
- complete calculator program loop


# Git Commands Used

### **1. Initialize Repository**
```
git init
```
### **2. Add Files**
```
git add .
git commit -m "Initial project setup"
```
### **3. Create Branches**
```
git branch feature
git branch test
git branch bugfix
git branch experiment
```
### **4. Switch Between Branches**
```
git checkout feature
```
### **5. Merge Branches**
```
git checkout main
git merge feature
```
### **6. Merge Conflict Demo**
Edit same line in two branches → merge → resolve → commit.
### **7. Add Remote GitHub Repo**
```
git remote add origin https://github.com/YourUsername/git-python-project.git
```
### **8. Push Changes**
```
git push -u origin main
```
---
## Screenshots
### image 1
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000246.png?raw=true)

### image 2
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000422.png?raw=true)

### image 3
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000448.png?raw=true)

### image 4
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000503.png?raw=true)

### image 5
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000516.png?raw=true)

### image 6
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000545.png?raw=true)
### image 7
![image alt](https://github.com/anujrawat47/git-python-project/blob/main/Screenshot%202025-12-01%20000611.png?raw=true)

### **Conclusion**

This project helped me understand essential Git concepts:

- Working directory vs staging area
- Committing changes
- Creating and switching branches
- Merging and resolving conflicts
- Setting up GitHub remote and pushing code
- Writing documentation using Markdown
