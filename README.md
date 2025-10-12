# Earthquake & Eruption ML Analysis

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
3. Launch Jupyter Notebook to run notebooks:

```powershell
jupyter notebook
```


## Files & folders (important)

- `data/` or root CSVs: earthquake and eruption catalogs (e.g. `PuuOo.csv`, `puuoo_earthquakes.csv`, `KilaueaHypocentersANSS.csv`)
- `util/` — utility functions for loading and processing datasets (`util/datautil.py`)
- `*.ipynb` — notebooks: `Data Exploration.ipynb`, `Random_forest.ipynb`, `RunMLTests.ipynb`, `DEEP PEEVED.ipynb`, `EQrates.ipynb`, `AddFeaturesToEQs.ipynb`
- `requirements.txt` — Python dependencies

## Workflow overview

1. Data preparation: use `util/datautil.py` to load and preprocess earthquake and eruption data.
2. Feature engineering: compute earthquake rates (1-day, 7-day, 30-day), time since/to eruption, and other spatial/temporal features.
3. Modeling: train logistic regression, random forest, k-means clustering, and simple neural networks for classification and regression tasks.
4. Evaluation: use AUROC, Cohen's Kappa for classification and RMSE/R2 for regression. Visualize results and feature importance.


## Contact

For questions: mr.hariomsrk@gmail.com
