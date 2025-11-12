Solar Challenge Week 0
Project Overview

This repository contains the data analysis and visualization workflow for the Solar Challenge Week 0 project.
It includes exploratory data analysis (EDA) for Benin, Sierra Leone, and Togo, cross-country comparisons, and optional Streamlit dashboard development.

Objectives:

Clean and preprocess solar data (GHI, DNI, DHI, weather parameters).

Handle missing values and outliers using Z-score method.

Perform EDA for Benin.

Compare solar potential across countries.

(Optional) Build a Streamlit dashboard for interactive visualization.

Folder Structure
solar-challenge-week0/
├── app/                  # Streamlit dashboard
│   ├── main.py           # Main Streamlit script
│   └── utils.py          # Helper functions for data loading/visualization
├── data/
│   ├── raw/              # Original datasets
│   │   ├── benin.csv
│   │   ├── sierraleone.csv
│   │   └── togo.csv
│   └── clean/            # Cleaned datasets
│       ├── benin_clean.csv
│       ├── sierraleone_clean.csv
│       └── togo_clean.csv
├── notebooks/            # Jupyter notebooks for EDA and analysis
│   ├── eda_benin.ipynb
│   └── compare_countries.ipynb
├── .github/              # CI workflow
│   └── workflows/
│       └── python-app.yml
├── .gitignore
├── requirements.txt
└── README.md

Environment Setup
1. Clone Repository
git clone https://github.com/yourusername/solar-challenge-week0.git
cd solar-challenge-week0

2. Create Virtual Environment
python -m venv venv

3. Activate Virtual Environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

Usage
1. Jupyter Notebooks

EDA for Benin: notebooks/eda_benin.ipynb

Cross-Country Comparison: notebooks/compare_countries.ipynb
Run each notebook step-by-step to view data cleaning, visualizations, and analysis.

2. Streamlit Dashboard (Optional)
streamlit run app/main.py


Features:

Interactive selection of countries

Boxplots for GHI, DNI, DHI

Summary tables of solar metrics

(Optional) Visual ranking by average GHI

Data Cleaning and Analysis Highlights

Missing values handled with column mean imputation.

Outliers identified and treated using Z-score method.

Summary statistics computed for GHI, DNI, DHI.

Comparative analysis across Benin, Sierra Leone, and Togo with boxplots and ANOVA/Kruskal–Wallis tests.

CI/CD Workflow

GitHub Actions workflow automatically runs tests and checks on every pull request.

Workflow file: .github/workflows/python-app.yml

Git Workflow

Feature branches: eda-benin, compare-countries, dashboard-dev

Commit messages: Use descriptive messages like feat: add GHI summary stats

Pull Requests: Always merge feature branches into main after review.

Requirements

Python 3.10+

pandas, numpy, matplotlib, seaborn, streamlit

Example requirements.txt:

pandas
numpy
matplotlib
seaborn
streamlit
scipy

Notes

Keep data/clean in .gitignore to avoid pushing large CSVs.

Always document new notebooks and scripts in the README.

Optional Streamlit dashboard enhances visualization but is not mandatory for core submission.
