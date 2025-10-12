# PEEVED: Earthquake & Eruption ML Analysis

## Overview
This repository holds the UE23CS352A mini-project analyzing earthquake signals and their relationship to eruptive activity at Kilauea (Puu Oo). It includes data, utility code, Jupyter notebooks, and a small set of helper scripts to reproduce the deliverables.

## Problem statement
Use earthquake catalog features (location, depth, magnitude, and short-term earthquake rates) to (1) predict whether Kilauea is erupting at the time of an earthquake (classification) and (2) forecast time-to-eruption (regression) using machine learning methods.

## Quick start (Windows PowerShell)

1. Clone the repository and enter it:

```powershell
git clone https://github.com/hariomkhonde108/Ml_project.git
cd Ml_project
```

2. Create and activate a virtual environment and install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. (Optional) Install ReportLab for PDF helper scripts:

```powershell
venv\Scripts\python.exe -m pip install reportlab
```

4. Launch Jupyter Notebook to run notebooks:

```powershell
jupyter notebook
```

## Deliverables

- `deliverables/one_page_writeup.md` and `deliverables/one_page_writeup.pdf` — single-page summary
- `deliverables/slides_template.md` and `deliverables/slides.pdf` — slides for presentation
- `scripts/make_onepage_pdf.py` and `scripts/make_slides_pdf.py` — helpers that convert the markdown templates to PDFs (use ReportLab)

## Files & folders (important)

- `data/` or root CSVs: earthquake and eruption catalogs (e.g. `PuuOo.csv`, `puuoo_earthquakes.csv`, `KilaueaHypocentersANSS.csv`)
- `util/` — utility functions for loading and processing datasets (`util/datautil.py`)
- `*.ipynb` — notebooks: `Data Exploration.ipynb`, `Random_forest.ipynb`, `RunMLTests.ipynb`, `DEEP PEEVED.ipynb`, `EQrates.ipynb`, `AddFeaturesToEQs.ipynb`
- `deliverables/` — templates and generated PDFs for submission
- `scripts/` — simple helper scripts (PDF generation)
- `requirements.txt` — Python dependencies

## Workflow overview

1. Data preparation: use `util/datautil.py` to load and preprocess earthquake and eruption data.
2. Feature engineering: compute earthquake rates (1-day, 7-day, 30-day), time since/to eruption, and other spatial/temporal features.
3. Modeling: train logistic regression, random forest, k-means clustering, and simple neural networks for classification and regression tasks.
4. Evaluation: use AUROC, Cohen's Kappa for classification and RMSE/R2 for regression. Visualize results and feature importance.

## Reproduce deliverables (PDFs)

From an activated venv with `reportlab` installed you can run:

```powershell
venv\Scripts\python.exe scripts\make_onepage_pdf.py
venv\Scripts\python.exe scripts\make_slides_pdf.py
# outputs: deliverables\one_page_writeup.pdf, deliverables\slides.pdf
```

## Notes and next steps

- The repository currently includes datasets in the git history per your instruction. If you prefer to remove large files from history or track them with Git LFS, tell me and I'll help.
- If you provide team member names and a final short project summary I will add them to the README and the one-page writeup.

## Contact

For questions: mr.hariomsrk@gmail.com

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

   > Problem statement: Use earthquake catalog features (location, depth, magnitude and short-term earthquake rates) to predict whether Kilauea is erupting (classification) and to forecast time-to-eruption (regression) using machine learning methods such as logistic regression, random forests, k-means clustering and neural networks.

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

