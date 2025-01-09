# FinalProject

## Overview

This repository contains the code and the relevant analyses for the project **"The Pursuit of Happiness: Understanding the Key Drivers of Well-being"** The research seeks to provide an insight into ways in which we can improve global happiness, through looking at regional trends and factors. By doing this, data-driven suggestions can guide the implementation of different policies; targeted and contextual interventions can be made by policmakers such as the UN to make the world a better place.

### Research Hypothesis

The project is guided by the hypothesis:
> * “GDP per capita exerts the greatest influence on national happiness levels, with life expectancy contributing to it. Africa has the lowest score whilst Europe has the highest, reflecting the idea that GDP is the biggest driver of happiness.”*

---

## Project Structure

The repository is structured as follows:

- **`.circleci/`**: Configuration files for CircleCI integration for testing every commit.
  - `config.yml`: CircleCI configuration file.

- **`FinalProject/`**
  - **`Dataset/`**: Contains the dataset used for analysis.
    - `2019.csv`: Dataset containing detailed information on The Happiness Report (2019).

  - **`Visualisations/`**: Stores all visualisations and statistical summaries related to the analysis.
    - `Correlation_Heatmap.png`
    - `GDPvsHappiness.png`
    - `HappinessScoreByRegion.png`
    - `Residual_Analysis.png`
    - `T_Test.png`

  - **`Tests/`**: Contains all scripts for cleaning data, performing analysis, and generating visualisations.
    - `Python_Analysis.py` : The document where all the code is written
      
  - **`requirements.txt`**: Lists Python dependencies needed to run the scripts.

  - **`Tests/`**: Includes all test files to validate scripts and functionality.
    - `test_BarChart.py`
    - `test_cleaning.py`
    - `test_heatmap.py`
    - `test_loading.py`
    - `test_residuals.py`
    - `test_scatterplot.py`
    - `test_Ttest.py`

- **`README.md`**: Project documentation.

---

## Dataset Information

The analysis is based on a survey from the **World Happiness Report**, a yearly study conducted to understand why people are unhappy and where peopel are the most unhappy.

### Source: 

https://worldhappiness.report/ed/2019/


---

## How to Run

To clone and run the project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Iclipsed/FinalProject.git
cd FinalProject
```

### 2. Install Required Libraries
Ensure you have Python installed (version 3.8+ is recommended). Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### 3. Run the Scripts

- **Data Cleaning, Visualisations and Analysis**:  
  Execute the visualisation script in the `Graphs/` directory. Example:
  ```bash
  python -m Graphs/Python_Analysis.py
  ```

- **Tests**:  
  Run unit tests in terminal located in the `Tests/` directory to ensure functionality:
  ```bash
  python -m pytest Tests    
  ```

---

## Creator
This project was conducted by Ismael Rahman
Student ID: 230358184

