import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# data frame 
df = pd.read_csv('sloth_data.csv')

pd.set_option("display.max.columns", None)

# prints out first five lines
print(df.head())

specie = df['specie'] 
# print(specie)

specie_three_toed = df[(df["specie"] == "three_toed")]
print(len(specie_three_toed))

specie_two_toed = df[(df["specie"] == "two_toed")]
print(len(specie_two_toed))

critically_endangered = df[(df["endangered"] == "critically_endangered")] 
print(len(critically_endangered))

vulnerable = df[(df["endangered"] == "vulnerable")]

least_concern = df[(df["endangered"] == "least_concern")]

# Filters and creates a new csv file 
specie_three_toed.to_csv("specie-three-toed.csv")

specie_two_toed.to_csv("specie-two-toed.csv")


# Sort sub species 

sub_specie = df[["sub_specie"]]
print(sub_specie)

hoffman = df[(df["sub_specie"]== "Hoffman’s two-toed sloth")]
print(len(hoffman))

linnaeus = df[(df["sub_specie"] == "Linnaeus’s two-toed sloth")]
print(len(linnaeus))

brown_throat = df[(df["sub_specie"] == "Brown-throated sloth")] 

pygmy = df[(df["sub_specie"] == "Pygmy three-toed sloth")] 

pale_throat = df[(df["sub_specie"] == "Pale-throated sloth")] 

maned = df[(df["sub_specie"] == "Maned three-toed sloth")]
