import os
import pandas as pd

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

print(data.info())



def test_renaming():

    expected_columns = [
        'Overall rank',       
        'Countries',          
        'Happiness_Score',    
        'GDP_per_Capita',     
        'Social_Support',     
        'Life_Expectancy',    
        'Freedom',            
        'Generosity',         
        'Corruption'          
    ]

    # Assert that the actual columns match the expected columns
    assert list(data.columns) == expected_columns, (
        f"Column names do not match expected columns. Got {list(data.columns)}, expected {expected_columns}."
    )

    

