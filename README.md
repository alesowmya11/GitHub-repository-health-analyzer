# 🐙 GitHub Repository Health Analyzer
![GitHub Repository Health Analyzer Demo](screenshots/project-demo.png)
## 🚀 Live Demo

👉 [Try the GitHub Repository Health Analyzer](https://app-repository-health-analyzer-glehjz3fy9vc4l2whni6aq.streamlit.app/)

## 📌 Overview

GitHub Repository Health Analyzer is a Python-based web application that analyzes the overall health and quality of a GitHub repository.

The application takes a GitHub repository URL as input and collects repository information using the GitHub REST API.

It analyzes documentation, activity, contributors, commits, issues, pull requests, repository size, stars and forks.

The system generates a custom health score out of 100 and provides recommendations for improving the repository.

---

## 🎯 Objectives

* Analyze GitHub repository quality
* Check README and LICENSE availability
* Analyze repository activity
* Analyze contributors and commits
* Check open issues and pull requests
* Display repository statistics
* Generate a health score
* Provide improvement recommendations
* Present results using an interactive Streamlit dashboard

---

## 🚀 Features

### 📋 Repository Details

Displays:

* Repository name
* Description
* Main programming language
* Creation date
* Last updated date
* Repository visibility

### 📊 Repository Metrics

Analyzes:

* ⭐ Stars
* 🍴 Forks
* 🐛 Open Issues
* 👥 Contributors
* 🔄 Recent Commits
* 📦 Repository Size

### 📝 Documentation Analysis

Checks whether the repository contains:

* README
* LICENSE

### 🔄 Activity Analysis

Analyzes the repository's recent update activity and classifies it as:

* 🟢 Active
* 🟡 Moderately Active
* 🔴 Inactive

### 🐛 Issue Analysis

Analyzes the number of open issues and provides a health status.

### 🔀 Pull Request Analysis

Analyzes open pull requests and provides an activity status.

### 📈 Data Visualization

Displays charts for:

* Repository metrics
* Health score components

### ⭐ Health Score

The application generates a custom score out of 100 based on:

| Component | Maximum Score |
| --------- | ------------: |
| README    |            20 |
| LICENSE   |            15 |
| Activity  |            25 |
| Stars     |            20 |
| Forks     |            10 |
| Issues    |            10 |
| **Total** |       **100** |

> The health score is a custom analytical methodology created for this project and is not an official GitHub score.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* GitHub REST API
* Requests
* Python-dotenv

---

## 📁 Project Structure

```text
GitHub Repository Health Analyzer/
│
├── app.py
├── github_api.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd GitHub-Repository-Health-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 GitHub API Token

Create a `.env` file in the project folder.

Add:

```text
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

The token is used to authenticate GitHub API requests and avoid unauthenticated API rate limits.

Never upload your actual token to GitHub.

---

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 How It Works

```text
User enters GitHub URL
          ↓
Extract Repository Owner & Name
          ↓
GitHub REST API
          ↓
Collect Repository Information
          ↓
Analyze Repository Health
          ↓
Calculate Health Score
          ↓
Generate Charts
          ↓
Generate Recommendations
          ↓
Display Dashboard
```

---

## 📊 Example Analysis

The application can analyze:

* Repository documentation
* Repository activity
* Community participation
* Commit activity
* Open issues
* Pull requests
* Stars and forks
* Repository size

The final result provides a quick overview of repository health.

---

## 🔮 Future Enhancements

Possible future improvements include:

* GitHub Actions / CI detection
* Test coverage analysis
* Code quality analysis
* Security analysis
* Commit trend charts
* Historical health scores
* Repository comparison
* Export health reports as PDF
* Database storage
* Deployment using Streamlit Cloud

---

## 👩‍💻 Author

Developed as a Python and GitHub API based developer productivity project.

---

## ⭐ Conclusion

GitHub Repository Health Analyzer helps developers quickly understand the quality, activity and maintainability of a GitHub repository through automated analysis and visual reporting.