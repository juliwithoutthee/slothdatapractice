import pandas as pd
from pexpect import split_command_line


# data frame 
df = pd.read_csv('sloth_data.csv')

# prints out first five lines
print(df.head())

specie = df['specie'] 
# print(specie)

specie_three_toed = df[(df["specie"] == "three_toed")]
print(len(specie_three_toed))

# critically_endangered = df["critically_endangered"]