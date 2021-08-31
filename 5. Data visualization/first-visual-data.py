import pandas as pd


wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head())