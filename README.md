# Earthquake & Eruption ML Analysis

## Overview

This repository holds the **UE23CS352A Machine Learning Mini-Project**, focused on analyzing seismic signals and their relationship to eruptive activity at **Kilauea Volcano** (specifically the East Rift Zone and Pu'u 'Ō'ō crater). We apply a hybrid machine learning approach to test the predictive power of earthquake data alone.

The methods and features are derived from the project's accompanying research paper, **"Predicting Eruptive Events at Volcanoes from Earthquake Data."**

## Problem Statement

The project's goal is to use Kilauea's earthquake catalog to address two distinct challenges:

1. **Classification Task:** Predict whether the volcano is **contemporaneously erupting** (1) or in **repose** (0) at the time of an earthquake.
2. **Regression Task:** **Forecast the time** until an eruption commences.

The models rely on engineered features, primarily **short-term earthquake rates**, which serve as a proxy for physical unrest preceding an eruption.

## Key Results (Summary)

* The **Random Forest** model was the best overall performer for both tasks.
* **Classification:** Achieved a **Cohen's Kappa of 0.52** and an **AUROC of 0.71** on the test set, indicating moderate agreement in classifying the eruptive state.
* **Regression:** Forecasting was weak, with the best model (Random Forest) achieving an **R² of 0.38** on the test set.
* **Feature Importance:** **Monthly and Weekly Earthquake Rates** were identified as the most important predictors for volcanic activity.

## Quick Start (Windows PowerShell)

The following steps set up the environment required to run all Jupyter notebooks.

1. **Clone the repository and enter it:**

   ```powershell
   git clone https://github.com/hariomkhonde108/Ml_project.git
   cd Ml_project
   ```

2. **Create and activate a virtual environment and install dependencies:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook to run notebooks:**

   ```powershell
   jupyter notebook
   ```

## Files & Folders

| File/Folder | Purpose |
| :--- | :--- |
| `KilaueaHypocentersANSS.csv` | The **raw earthquake catalog** used for all feature engineering. |
| `kilauea_eruptionHistory.xlsx - Eruptions.csv` | **Historical eruption records** used to generate the target (label) variables. |
| `PuuOo.csv`, `kilauea_eruptionHistory.xlsx - Intrusions.csv` | Auxiliary data related to the specific vent and magma intrusions. |
| `dev.txt` | The **development (validation) set** used for hyperparameter tuning. |
| `Data Exploration.ipynb` | Notebook for initial data visualization, spatial filtering, and temporal checks. |
| `EQrates.ipynb`, `AddFeaturesToEQs.ipynb` | Notebooks dedicated to **Feature Engineering**, primarily the calculation and scaling of earthquake rate features (Daily, Weekly, Monthly) and the Time-to-Eruption label. |
| `DEEP.ipynb` | Notebook implementing the **Neural Network** and possibly the final consolidated testing of models. |
| `requirements.txt` | Python dependencies (e.g., scikit-learn, pandas, numpy, PyTorch). |

## Workflow Overview

To reproduce the project results, follow the notebooks sequentially:

1. **Data Preparation and Exploration:** Run `Data Exploration.ipynb` to load, clean, and spatially filter the earthquake and eruption data.

2. **Feature Engineering:** Execute `AddFeaturesToEQs.ipynb` and `EQrates.ipynb` to calculate **earthquake rates**, generate the **Time-to-Eruption label**, and perform feature **scaling** (standardization).

3. **Model Training and Tuning:** Utilize the remaining notebooks (e.g., `DEEP.ipynb`, `Random_forest.ipynb`) to:
   * Train and tune all four models: Logistic Regression, K-Means Clustering, Random Forest, and Neural Network.
   * Tune hyperparameters (e.g., Random Forest Max Depth) using the **development set**.

4. **Final Evaluation:** Evaluate the models on the unseen **test set** using appropriate metrics (κ, AUROC, RMSE, R²).

## Models Used

- **Logistic Regression:** Baseline linear classifier
- **K-Means Clustering:** Unsupervised learning approach for pattern detection
- **Random Forest:** Ensemble method (Best performer)
- **Neural Network:** Deep learning approach for complex pattern recognition

## Technologies & Dependencies

- Python 3.x
- scikit-learn
- pandas
- numpy
- PyTorch
- Jupyter Notebook
- matplotlib/seaborn (for visualizations)

Install all dependencies via:
```powershell
pip install -r requirements.txt
```

## Contact

For questions regarding the code or analysis, please contact: mr.hariomsrk@gmail.com

## License

This project is part of the UE23CS352A Machine Learning course. Please cite appropriately if using this work.