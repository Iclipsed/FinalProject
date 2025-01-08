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