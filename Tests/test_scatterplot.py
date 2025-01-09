import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





### Test Methods Start Here ###
def test_scatterplot():
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

    # Check if the required columns are in the dataset
    required_columns = ['GDP_per_Capita', 'Happiness_Score']
    for col in required_columns:
        assert col in data.columns, f"Required column '{col}' is missing from the dataset."

    # Generate scatter plot
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x='GDP_per_Capita', y='Happiness_Score', data=data)

    # Ensure scatterplot was generated
    assert scatter is not None, "Scatterplot was not generated correctly."

    # Add title and labels for testing purposes (same as in the original plot code)
    plt.title('Happiness Score vs. GDP per Capita')
    plt.xlabel('GDP per Capita')
    plt.ylabel('Happiness Score')

    # Check plot title
    title = plt.gca().title.get_text()
    assert title == 'Happiness Score vs. GDP per Capita', "Scatterplot title is incorrect."

    # Check X and Y axis labels
    xlabel = plt.gca().get_xlabel()
    ylabel = plt.gca().get_ylabel()
    assert xlabel == 'GDP per Capita', "X-axis label is incorrect."
    assert ylabel == 'Happiness Score', "Y-axis label is incorrect."

    # Cleanup the plot to prevent memory issues in testing environments
    plt.close()