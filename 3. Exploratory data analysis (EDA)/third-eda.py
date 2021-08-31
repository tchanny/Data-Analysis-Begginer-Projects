import numpy as np
from itertools import repeat
import pandas as pd
import matplotlib.pyplot as plt

data = {'Nuts': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Chocolate': [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
        'Preference': [10.5, 9.84, 25.64, 8.6, 7.98, 7.32, 6.7, 6.23, 5.51, 5.0, 4.73, 0.5, 0.45, 0, 0, 0, 1]}

df = pd.DataFrame(data)


people = df['Preference'] * 100
nuts_preference = []

for i in range(len(people)):
    nuts_preference.extend(repeat(df['Nuts'][i], int(people[i])))

plt.hist(nuts_preference, bins=np.arange(0, 100, 5), rwidth=0.9, alpha=0.5, density=True)
plt.xlabel('Nuts Proportion')
plt.grid()