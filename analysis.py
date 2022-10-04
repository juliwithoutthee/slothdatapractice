import pandas as pd

df = pd.read_csv('sloth_data.csv')

# Gives descriptive statistics 
print(df.describe())