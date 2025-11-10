# Solar Challenge Week 0

This repository contains the setup for the Week 0 Solar Data Analysis Challenge.

## Project Overview
This project is part of the 10 Academy 12-week training program. The goal of this week is to set up the development environment, version control, and prepare for data exploration and analysis of solar farm data from Benin, Sierra Leone, and Togo.

## Environment Setup
To reproduce the environment locally:

1. **Clone the repository**
```bash
git clone https://github.com/life412/solar-challenge-week0.git
cd solar-challenge-week0

Create and activate a Python virtual environment

# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt

Folder Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── notebooks/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── tests/
│   │   ├── __init__.py
│   └── scripts/
│       ├── __init__.py
│       └── README.md
└── app/
    ├── __init__.py
    ├── main.py
    └── utils.py

Git Workflow

Create branches for tasks, e.g.:

git checkout -b setup-task


Commit changes with descriptive messages:

git add .
git commit -m "chore: setup Python environment and .gitignore"


Merge task branch into main via Pull Request on GitHub.

Key Files

.gitignore: Ignored files and folders (Python, virtual environments, Jupyter checkpoints, etc.)

requirements.txt: Lists all Python packages needed for this project.

.github/workflows/ci.yml: CI workflow to test environment setup.
