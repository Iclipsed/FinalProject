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

plt.figure(figsize=(10, 6))
sns.scatterplot(x='GDP_per_Capita', y='Happiness_Score', data= data)
sns.regplot(x='GDP_per_Capita', y='Happiness_Score', data= data, scatter=False, color='red')
plt.title('Happiness Score vs. GDP per Capita')
plt.text(0.9, 1.5,'Figure 3: Scatterplot with regression line showing the relationship between GDP per capita and happiness scores', fontsize=12, ha='center')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.show()

from sklearn.linear_model import LinearRegression
# Reference: https://www.geeksforgeeks.org/python-linear-regression-using-sklearn/

x = data['GDP_per_Capita'].values.reshape(-1, 1)  
y = data['Happiness_Score'].values  

# Fit a linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict values
y_pred = model.predict(x)
residuals = y - y_pred

# Reference https://stackoverflow.com/questions/62646058/how-does-the-predict-method-work-on-scikit-learn#:~:text=predict()%20must%20follow%20fit,new%20inputs%20to%20their%20labels.

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.6, label='Residuals')
plt.axhline(y=0, color='red', linestyle='--', label='Zero Residual Line')
plt.title('Residual Plot: Happiness Score vs. GDP per Capita')
plt.xlabel('Predicted Happiness Score')
plt.ylabel('Residuals')
plt.text(5, -3.5, 'Figure 7: Residuals from the linear regression model for GDP and Happiness Scores', fontsize=12, ha='center')
plt.legend()
plt.show()


from scipy.stats import ttest_ind


# Group countries by GDP per capita (high vs. low based on median GDP)
median_gdp = data['GDP_per_Capita'].median()
high_gdp = data[data['GDP_per_Capita'] >= median_gdp]['Happiness_Score']
low_gdp = data[data['GDP_per_Capita'] < median_gdp]['Happiness_Score']

# Perform the t-test
t_stat, p_value = ttest_ind(high_gdp, low_gdp)

# Display results
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("The difference in happiness scores between high and low GDP groups is statistically significant.")
else:
    print("No significant difference in happiness scores between high and low GDP groups.")


# Reference: https://neuraldatascience.io/5-eda/ttests.html

# Extend the continent mapping to include Asian countries and others
continent_map = {
    'Finland': 'Europe', 'Denmark': 'Europe', 'Norway': 'Europe', 'Iceland': 'Europe',
    'Netherlands': 'Europe', 'Switzerland': 'Europe', 'Sweden': 'Europe', 'New Zealand': 'Oceania',
    'Canada': 'North America', 'Australia': 'Oceania', 'United States': 'North America',
    'India': 'Asia', 'China': 'Asia', 'Japan': 'Asia', 'South Korea': 'Asia', 'Indonesia': 'Asia',
    'Saudi Arabia': 'Asia', 'Turkey': 'Asia', 'Israel': 'Asia', 'Singapore': 'Asia', 'Malaysia': 'Asia',
    'Vietnam': 'Asia', 'Thailand': 'Asia', 'Philippines': 'Asia',
    'Brazil': 'South America', 'Argentina': 'South America', 'Colombia': 'South America',
    'Mexico': 'North America', 'Chile': 'South America', 'Peru': 'South America',
    'South Africa': 'Africa', 'Nigeria': 'Africa', 'Egypt': 'Africa', 'Kenya': 'Africa'
}


# Map countries to continents again
data['Continent'] = data['Countries'].map(continent_map)

# Filter out countries without continent mapping
data_with_continents = data.dropna(subset=['Continent'])

# Calculate average happiness scores by continent
continent_happiness = data_with_continents.groupby('Continent')['Happiness_Score'].mean().sort_values()

# Plot the results again
plt.figure(figsize=(8, 5))
continent_happiness.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Average Happiness Scores by Continent", fontsize=16)
plt.ylabel("Average Happiness Score")
plt.xlabel("Continent")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.text(2, -3,'Figure 6: Bar Graph showing differences in happiness score across different continents', fontsize=10, ha='center')
plt.xticks(rotation=45)
plt.show()

#https://stackoverflow.com/questions/66557543/valueerror-mime-type-rendering-requires-nbformat-4-2-0-but-it-is-not-installed



### Test Methods Start Here ###
def test_continent_mapping_and_plot():
    continent_map = {
        'USA': 'North America', 'India': 'Asia', 'France': 'Europe',  # Extend as needed
    }
    data['Continent'] = data['Countries'].map(continent_map)
    data_with_continents = data.dropna(subset=['Continent'])
    assert 'Continent' in data.columns, "Continent column missing"
    assert not data_with_continents.empty, "Filtered dataset is empty"
    continent_happiness = data_with_continents.groupby('Continent')['Happiness_Score'].mean()
    plt.figure(figsize=(8, 5))
    bar = continent_happiness.plot(kind='bar', color='skyblue', edgecolor='black')
    assert bar is not None, "Bar plot not generated"
    plt.close()