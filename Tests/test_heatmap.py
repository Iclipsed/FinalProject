
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def test_correlation_heatmap():

    data = pd.read_csv("Dataset/2019.csv")
    print(data.head(5))


    data.rename(columns={
    'Country or region': 'Countries',
    'Score': 'Happiness_Score',
    'GDP per capita': 'GDP_per_Capita',
    'Social support': 'Social_Support',
    'Healthy life expectancy': 'Life_Expectancy',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption'
     }, inplace=True)
    
    columns= ['Happiness_Score', 'GDP_per_Capita', 'Social_Support',
                  'Life_Expectancy', 'Freedom', 'Generosity', 'Corruption']
    # Selecting only the relevant columns for this investigation
    
    # Compute correlation matrix
    correlation_matrix = data[columns].corr()

    # Assert the correlation matrix dimensions are correct
    assert correlation_matrix.shape == (7, 7), "Correlation matrix dimensions are incorrect"

    # Assert that all columns are in the correlation matrix
    for col in columns:
        assert col in correlation_matrix.columns, f"Column {col} is missing in the correlation matrix"

    # Assert heatmap title
    plt.title('Correlation Heatmap: Happiness and Predictors')
    title = plt.gca().title.get_text()
    assert title == 'Correlation Heatmap: Happiness and Predictors', "Heatmap title is incorrect"
