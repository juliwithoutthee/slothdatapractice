import pandas as pd


# data frame 
df = pd.read_csv('sloth_data.csv')

# prints out first five lines
print(df.head())

specie = df['specie'] 
print(specie)

critically_endangered = df["critically_endangered"]