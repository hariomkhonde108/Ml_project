# Machine Learning Project - Solubility Prediction

## Overview
This project predicts the solubility (logS) of chemical compounds using machine learning. By leveraging molecular descriptors and regression models, the project aims to offer insights into compound solubility for research and development purposes.

## Features
- Loads and processes a dataset directly from a GitHub repository.
- Prepares data for model training with proper cleaning and formatting.
- Splits data into training and testing sets.
- Implements regression models (Linear Regression and Random Forest) for predictions.
- Visualizes predicted results against experimental values.

## Tech Stack
- Python
- Pandas
- Scikit-learn

# PEEVED: Earthquake & Eruption ML Analysis
## Overview

This repository contains code, data, and notebooks for machine learning and statistical analysis of volcanic earthquakes and eruptions, focused on the Puu Oo region of Kilauea volcano. It includes data exploration, feature engineering, classification, regression, clustering, and deep learning workflows.

## Setup
1. Clone the repository:

   ```powershell
   git clone https://github.com/hariomkhonde108/ML_PROJECT.git
   cd ML_PROJECT
   ```

2. Create and activate a Python virtual environment (recommended):

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   # PEEVED / ML_PROJECT — Earthquake & Eruption Machine Learning

   ## Overview

   This repository contains the UE23CS352A mini-project for machine learning analysis of volcanic earthquakes and eruptions (Puu Oo / Kilauea region). It includes data, notebooks, utility code, and the required deliverables (one-page write-up and slides).

   > Problem statement: [Paste a 1–2 sentence problem description here]

   ## Quick status

   - Repo visibility: private
   - Deliverables included: one-page write-up PDF, slides PDF
   - Datasets: included in the repository per your request (do not remove unless you want history rewritten)

   ## Quick start (Windows PowerShell)

   1. Create and activate a Python virtual environment (recommended):

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   # For PDF scripts (optional):
   venv\Scripts\python.exe -m pip install reportlab
   ```

   3. Run Jupyter notebooks locally:

   ```powershell
   jupyter notebook
   ```

   4. Generate deliverable PDFs (optional):

   ```powershell
   venv\Scripts\python.exe scripts\make_onepage_pdf.py
   venv\Scripts\python.exe scripts\make_slides_pdf.py
   # Outputs: deliverables\one_page_writeup.pdf, deliverables\slides.pdf
   ```

   ## Important files & folders

   - `deliverables/` — one-page writeup (markdown + PDF) and slides template (markdown + PDF)
   - `scripts/` — small helper scripts to convert the markdown templates into PDFs using ReportLab
   - `util/` — utility code (data loading, feature engineering)
   - Notebooks (`*.ipynb`) — exploration and modeling workflows (Random_forest.ipynb, Data Exploration.ipynb, DEEP PEEVED.ipynb, etc.)
   - Data files (`*.csv`, `*.xlsx`) — earthquake and eruption datasets used for analysis
   - `requirements.txt` — Python dependencies
   - `LICENSE` — MIT license

   ## Deliverables mapping (UE23CS352A)

   - Source code and notebooks: present in the repository
   - One-page write-up: `deliverables/one_page_writeup.md` + `deliverables/one_page_writeup.pdf`
   - Slides: `deliverables/slides_template.md` + `deliverables/slides.pdf`
   - README: this file explains how to run and reproduce results

   Deliverable checklist:

   - [x] Source code and notebooks in the repository
   - [x] One-page write-up PDF included
   - [x] Slides PDF included
   - [x] LICENSE added
   - [ ] (optional) Set up Git LFS for very large files

   ## Team & contact

   - Team members: TBD (please provide names and I will update this section)
   - Problem statement: TBD (paste 1–2 sentence summary above)
   - Contact: mr.hariomsrk@gmail.com

   If you want, I will:

   - Add the team names and short project summary when you provide them
   - Add faculty/TA GitHub usernames as collaborators (you'll need to supply their usernames)
   - Add a `CONTRIBUTING.md` or `USAGE.md` with step-by-step run examples

   ---

   When you're ready, paste the team member names, a one-line problem statement, and any GitHub usernames to add as collaborators and I'll update the README and add collaborators for you.

   - **Logistic Regression & Clustering**: In `RunMLTests.ipynb`, compare classifiers and use K-Means for unsupervised analysis.
   - **Deep Learning**: Neural network models in `DEEP PEEVED.ipynb`.
5. **Evaluation**: Use metrics (accuracy, confusion matrix, ROC AUC, R2) and visualizations to assess model performance.
6. **Reproducibility**: Index files (`train.txt`, `dev.txt`, `test.txt`) ensure consistent splits for experiments.

## Dataset Details
- **PuuOo.csv**: Eruption events, with timing and physical parameters.
- **puuoo_earthquakes.csv**: Earthquake events, with location, depth, magnitude, and type.
- **KilaueaHypocentersANSS.csv**: Broader catalog for Kilauea region.

## How to Use
1. Open any notebook in Jupyter and follow the workflow cells.
2. Use utility functions from `util/` for data loading and feature engineering.
3. Modify index files to change train/val/test splits if needed.
4. Generated plots are saved as PNGs for further analysis or publication.
>>>>>>> 31f4a4b (Initial commit)

