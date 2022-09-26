import pandas as pd



# data frame 
df = pd.read_csv('sloth_data.csv')

# prints out first five lines
print(df.head())

specie = df['specie'] 
# print(specie)

specie_three_toed = df[(df["specie"] == "three_toed")]
print(len(specie_three_toed))

specie_two_toed = df[(df["specie"] == "two_toed")]
print(len(specie_two_toed))

# critically_endangered = df["critically_endangered"]  # Fix later


# Filters and creates a new csv file 
specie_three_toed.to_csv("specie-three-toed.csv")

specie_two_toed.to_csv("specie-two-toed.csv")