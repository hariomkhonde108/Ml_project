# Kilauea Eruption Prediction: Machine Learning Analysis

## 🌋 Overview

This repository hosts the code and analysis for the **UE23CS352A Machine Learning Mini-Project**. The project applies various machine learning algorithms to historical earthquake data from Kilauea Volcano (specifically the East Rift Zone and Pu'u 'Ō'ō crater) to predict its eruptive state.

The methodology is based on the research paper, *"Predicting Eruptive Events at Volcanoes from Earthquake Data"*. The primary hypothesis is that **engineered earthquake rate features** can capture the increased seismic unrest that precedes a volcanic eruption.

## 🎯 Problem Statement

The goal is to test the predictive capabilities of the Kilauea earthquake catalog by solving two distinct machine learning tasks:

1. **Contemporaneous Eruption Classification:** A binary classification task to predict if the volcano is currently erupting (1) or in a repose period (0) at the time of an earthquake.

2. **Time to Eruption Regression (Forecasting):** A regression task to forecast the continuous time (in scaled units) until the next eruption commences.

## 🚀 Quick Start

To set up the environment and run the analysis notebooks, follow these steps:

### Windows PowerShell

1. **Clone the repository:**
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

### Linux/macOS

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hariomkhonde108/Ml_project.git
   cd Ml_project
   ```

2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

*The notebooks should be executed in sequential order starting with data exploration and feature engineering.*

## 📊 Results and Performance

All models were evaluated using a stratified **70% Train / 20% Development / 10% Test split**.

### 1. Classification Task Performance

Due to significant **class imbalance** (~80% Repose labels), performance was measured using **Cohen's Kappa (κ)** (agreement beyond chance) and **AUROC** (Area Under the Receiver Operating Characteristic Curve).

| Algorithm | Dataset | Kappa (κ) | AUROC |
|:----------|:--------|:----------|:------|
| **Random Forest** | **Test** | **0.52** | **0.71** |
| Logistic Regression | Test | 0.28 | 0.60 |
| K-Means | Test | 0.24 | 0.63 |
| Neural Network | Test | 0.29 | 0.61 |

**Conclusion:** The **Random Forest** was the best classifier, demonstrating **moderate agreement** (κ=0.52) and strong discriminatory power (AUROC=0.71).

### 2. Regression Task Performance

Performance for the Time-to-Eruption task was assessed using **Root Mean Squared Error (RMSE)** and the **R² value** (coefficient of determination).

| Algorithm | RMSE (Train/Dev/Test) | R² (Train/Dev/Test) |
|:----------|:---------------------|:--------------------|
| **Random Forest** | 0.16 / 0.68 / **0.64** | 0.82 / 0.37 / **0.38** |
| Neural Network | 0.86 / 0.92 / 0.90 | 0.26 / 0.15 / 0.19 |
| K-Means | 0.95 / 0.95 / 1.02 | 0.097 / 0.059 / 0.037 |

**Conclusion:** The Random Forest again performed best, but the **R² value of 0.38** indicates a **weak correlation** between predicted and observed times to eruption.

### 3. Feature Importance

For the Random Forest Regression model, the most important features were:

1. **Monthly Rate** (Earthquake count over 30 days)
2. **Weekly Rate** (Earthquake count over 7 days)
3. **Latitude (Y coordinate)**

## 🛠️ Workflow and Files

The project follows a sequential workflow across its key notebooks:

| File/Folder | Purpose |
|:------------|:--------|
| `KilaueaHypocentersANSS.csv` | **Raw Data:** The primary earthquake catalog input |
| `kilauea_eruptionHistory.xlsx - Eruptions.csv` | **Label Data:** Provides eruption start/end times for label generation |
| `PuuOo.csv` | Auxiliary data related to the specific vent |
| `kilauea_eruptionHistory.xlsx - Intrusions.csv` | Magma intrusion data |
| `dev.txt` | The **development (validation) set** used for hyperparameter tuning |
| **`Data Exploration.ipynb`** | Initial cleaning, visualization, and spatial filtering to the East Rift Zone |
| **`AddFeaturesToEQs.ipynb`** | **Feature Engineering:** Calculates the time-to-eruption label and derives earthquake rate features (Daily, Weekly, Monthly) |
| **`EQrates.ipynb`** | **Data Processing:** Finalizes features, scales the data, and prepares the train/dev/test sets |
| **`DEEP PEEVED.ipynb`** (or `DEEP.ipynb`) | Implementation and training of the **Neural Network** and consolidated testing of all models |
| `requirements.txt` | Python dependencies |

### Execution Order

To reproduce the project results, follow the notebooks sequentially:

1. **Data Preparation and Exploration:** Run `Data Exploration.ipynb` to load, clean, and spatially filter the earthquake and eruption data.

2. **Feature Engineering:** Execute `AddFeaturesToEQs.ipynb` and `EQrates.ipynb` to:
   - Calculate **earthquake rates** (Daily, Weekly, Monthly)
   - Generate the **Time-to-Eruption label**
   - Perform feature **scaling** (standardization)

3. **Model Training and Tuning:** Utilize the remaining notebooks to:
   - Train and tune all four models: Logistic Regression, K-Means Clustering, Random Forest, and Neural Network
   - Tune hyperparameters (e.g., Random Forest Max Depth) using the **development set**

4. **Final Evaluation:** Evaluate the models on the unseen **test set** using appropriate metrics (κ, AUROC, RMSE, R²)

## 🤖 Models Used

- **Logistic Regression:** Baseline linear classifier
- **K-Means Clustering:** Unsupervised learning approach for pattern detection
- **Random Forest:** Ensemble method (Best performer)
- **Neural Network:** Deep learning approach for complex pattern recognition

## 🔧 Technologies & Dependencies

- Python 3.x
- scikit-learn
- pandas
- numpy
- PyTorch
- Jupyter Notebook
- matplotlib/seaborn (for visualizations)

Install all dependencies via:
```bash
pip install -r requirements.txt
```

## 📧 Contact

For questions regarding the code or analysis, please contact: mr.hariomsrk@gmail.com

## 📄 License

This project is part of the UE23CS352A Machine Learning course. Please cite appropriately if using this work.

## 🙏 Acknowledgments

This project is based on the research methodology from *"Predicting Eruptive Events at Volcanoes from Earthquake Data"* and utilizes earthquake catalog data from ANSS (Advanced National Seismic System) for Kilauea Volcano.
