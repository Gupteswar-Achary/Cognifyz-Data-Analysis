import pandas as pd

data = pd.read_csv('Dataset.csv')

data["Cuisine_combination"] = data['Cuisines']
top_10_cuisine_comb = data['Cuisine_combination'].value_counts().head(10)
print(f"Top 10 most common combination of the cuisines are {top_10_cuisine_comb}")

top_10_cuisine_data = data[data['Cuisine_combination'].isin(top_10_cuisine_comb.index)]
average_rating = top_10_cuisine_data.groupby('Cuisine_combination')['Aggregate rating'].mean().sort_values(ascending=False)
print(average_rating)
