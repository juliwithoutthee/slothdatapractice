import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


df = pd.read_csv('sloth_data.csv')

# Gives descriptive statistics 
print(df.describe())

plt.plot([1,2,3], [2,4,6])