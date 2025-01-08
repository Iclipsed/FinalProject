
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
}, inplace=True)#

print(data.info())


columns= ['Happiness_Score', 'GDP_per_Capita', 'Social_Support',
                  'Life_Expectancy', 'Freedom', 'Generosity', 'Corruption']
# Selecting only the relevant columns for this investigation

plt.figure(figsize=(10, 6))
correlation_matrix = data[columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# coolwarm suitable as cold and warms colours aligns with colour theory. Intuitive colours.
#2dp rounding used to display enough significant figures for a meaningful comparison of variables
plt.title('Correlation Heatmap: Happiness and Predictors')
plt.text(3.8, 10, 'Figure 2: A Correlation Matrix Heatmap that displays the correlation between all the columns in the dataset ', fontsize = 12, ha="center")
plt.show()



# https://matplotlib.org/stable/users/explain/colors/colormaps.html
# https://seaborn.pydata.org/generated/seaborn.heatmap.html



def test_correlation_heatmap():
    

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
