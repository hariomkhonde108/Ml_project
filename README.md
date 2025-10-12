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
   ```

4. Launch Jupyter Notebook:

   ```powershell
   jupyter notebook
   ```

## Files & Notebooks

- `PuuOo.csv`, `puuoo_earthquakes.csv`, `KilaueaHypocentersANSS.csv` — data files used in analysis.
- `Data Exploration.ipynb`, `Random_forest.ipynb`, `DEEP PEEVED.ipynb`, `RunMLTests.ipynb` — notebooks with EDA and modeling.
- `util/datautil.py` — utility functions for loading and preprocessing data.

## Workflow Summary

1. Data Preparation: use utilities in `util/` to load and preprocess data.
2. Exploration: visualize spatial, temporal, and magnitude distributions in `Data Exploration.ipynb`.
3. Feature Engineering: add earthquake/eruption features such as rates and time-to-eruption.
4. Modeling: Random Forests, logistic regression, clustering, and deep learning models are provided across notebooks.

## Contributing & License

Contributions welcome — please open issues or PRs. This project is distributed under the MIT License.

## Notes

- The repository currently contains data CSVs and some Excel files. If you prefer not to include raw datasets in Git, remove them and add patterns to `.gitignore`. Consider using Git LFS for large files.

---

View this repository on GitHub: https://github.com/hariomkhonde108/ML_PROJECT

<<<<<<< HEAD
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
   ```
4. Launch Jupyter Notebook:
   ```powershell
   jupyter notebook
   ```

## Files & Notebooks
- `PuuOo.csv`, `puuoo_earthquakes.csv`, `KilaueaHypocentersANSS.csv` — data files used in analysis.
- `Data Exploration.ipynb`, `Random_forest.ipynb`, `DEEP PEEVED.ipynb`, `RunMLTests.ipynb` — notebooks with EDA and modeling.
- `util/datautil.py` — utility functions for loading and preprocessing data.

## Workflow Summary
1. Data Preparation: use utilities in `util/` to load and preprocess data.
2. Exploration: visualize spatial, temporal, and magnitude distributions in `Data Exploration.ipynb`.
3. Feature Engineering: add earthquake/eruption features such as rates and time-to-eruption.
4. Modeling: Random Forests, logistic regression, clustering, and deep learning models are provided across notebooks.

## Contributing & License
Contributions welcome — please open issues or PRs. This project is distributed under the MIT License.

## Notes
- The repository currently contains data CSVs and some Excel files. If you prefer not to include raw datasets in Git, remove them and add patterns to `.gitignore`. Consider using Git LFS for large files.

---

View this repository on GitHub: https://github.com/hariomkhonde108/ML_PROJECT

>>>>>>> 31f4a4b (Initial commit)
4. **Launch Jupyter Notebook**:
   ```powershell
   jupyter notebook
   ```

## File & Folder Descriptions

### Data Files
- **PuuOo.csv**: Eruption history for Puu Oo, with columns for date, repose, length, flow area, volume, rate, and location.
- **puuoo_earthquakes.csv**: Earthquake catalog for the region, with columns for date-time, latitude, longitude, depth, magnitude, type, and more.
- **train.txt, dev.txt, test.txt**: Index files for splitting data into training, validation, and test sets.
- **KilaueaHypocentersANSS.csv**: Additional earthquake catalog (ANSS format).
- **kilauea_eruptionHistory.xlsx, puuoo_earthquakes.xlsx**: Excel versions of eruption and earthquake data.

### Notebooks
- **Data Exploration.ipynb**: Initial exploration and visualization of earthquake and eruption data.
- **Random_forest.ipynb**: Feature engineering, classification, and regression using Random Forests. Includes hyperparameter tuning and feature importance analysis.
- **RunMLTests.ipynb**: End-to-end ML workflow, including data preparation, logistic regression, K-Means clustering, and evaluation.
- **DEEP PEEVED.ipynb**: Deep learning models (neural networks) for eruption prediction using PyTorch.
- **EQrates.ipynb**: Earthquake rate calculations and related visualizations.
- **AddFeaturesToEQs.ipynb**: Feature engineering and augmentation for earthquake datasets.

### Utility Scripts
- **util/datautil.py**: Functions for loading, parsing, and processing earthquake and eruption data. Includes:
  - `load_hypocenters`, `load_puuoo_eqs`: Load CSV data into arrays.
  - `PuuOo`: Class for handling eruption history.
  - `GetTimeToEruption`, `GetTimeSinceEruption`, `GetEQRates`: Feature engineering utilities.
- **util/__init__.py**: Imports main utility functions for use in notebooks.

### ML & Analysis Outputs
- **.png files**: Plots and figures generated by notebooks (feature importance, clustering, regression, etc).

### Configuration
- **requirements.txt**: Python dependencies for the project (numpy, matplotlib, scikit-learn, seaborn, jupyter).

## Workflow Summary
1. **Data Preparation**: Use utility functions to load and preprocess earthquake and eruption data.
2. **Exploration**: Visualize spatial, temporal, and magnitude distributions in `Data Exploration.ipynb`.
3. **Feature Engineering**: Add features such as earthquake rates, time to/since eruption, and select East Rift Zone events.
4. **ML Modeling**:
   - **Random Forests**: Classification and regression in `Random_forest.ipynb`.
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

