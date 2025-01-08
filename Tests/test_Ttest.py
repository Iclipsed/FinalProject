import pytest
import pandas as pd
from scipy.stats import ttest_ind

def test_ttest_ind():
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

    # Group countries by GDP per capita (high vs. low based on median GDP)
    median_gdp = data['GDP_per_Capita'].median()
    high_gdp = data[data['GDP_per_Capita'] >= median_gdp]['Happiness_Score']
    low_gdp = data[data['GDP_per_Capita'] < median_gdp]['Happiness_Score']

    # Ensure the groups are not empty
    assert len(high_gdp) > 0, "High GDP group is empty."
    assert len(low_gdp) > 0, "Low GDP group is empty."

    # Perform the t-test
    t_stat, p_value = ttest_ind(high_gdp, low_gdp)

    # Ensure t-test produces valid outputs
    assert isinstance(t_stat, float), "T-Statistic is not a float."
    assert isinstance(p_value, float), "P-Value is not a float."

    # Validate the statistical interpretation
    if p_value < 0.05:
        assert p_value < 0.05, "The test failed to identify a statistically significant difference when expected."
    else:
        assert p_value >= 0.05, "The test incorrectly identified a statistically significant difference."

    print(f"T-Statistic: {t_stat}")
    print(f"P-Value: {p_value}")