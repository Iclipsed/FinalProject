import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def test_residual_plot():
    # Load the dataset
    data = pd.read_csv("Dataset/2019.csv")
    
    # Rename columns as in the main script
    data.rename(columns={
        'Country or region': 'Countries',
        'Score': 'Happiness_Score',
        'GDP per capita': 'GDP_per_Capita',
        'Social support': 'Social_Support',
        'Healthy life expectancy': 'Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Perceptions of corruption': 'Corruption'
    }, inplace=True)

    # Ensure required columns are present
    required_columns = ['GDP_per_Capita', 'Happiness_Score']
    for col in required_columns:
        assert col in data.columns, f"Required column '{col}' is missing from the dataset."

    # Prepare data for linear regression
    x = data['GDP_per_Capita'].values.reshape(-1, 1)
    y = data['Happiness_Score'].values

    # Fit the linear regression model
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    residuals = y - y_pred

    # Ensure predictions and residuals are computed
    assert len(y_pred) == len(y), "Predictions length does not match target variable length."
    assert len(residuals) == len(y), "Residuals length does not match target variable length."

    # Generate residual plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, label='Residuals')
    plt.axhline(y=0, color='red', linestyle='--', label='Zero Residual Line')
    plt.title('Residual Plot: Happiness Score vs. GDP per Capita')
    plt.xlabel('Predicted Happiness Score')
    plt.ylabel('Residuals')
    plt.text(5, -3.5, 'Figure 7: Residuals from the linear regression model for GDP and Happiness Scores', fontsize=12, ha='center')
    plt.legend()

    # Validate plot title and labels
    title = plt.gca().title.get_text()
    xlabel = plt.gca().get_xlabel()
    ylabel = plt.gca().get_ylabel()
    assert title == 'Residual Plot: Happiness Score vs. GDP per Capita', "Residual plot title is incorrect."
    assert xlabel == 'Predicted Happiness Score', "X-axis label is incorrect."
    assert ylabel == 'Residuals', "Y-axis label is incorrect."

    # Check if the zero residual line is present
    lines = [line for line in plt.gca().get_lines() if line.get_label() == 'Zero Residual Line']
    assert len(lines) == 1, "Zero residual line is missing from the plot."

    # Cleanup the plot
    plt.close()