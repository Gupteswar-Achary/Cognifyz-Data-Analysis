import pandas as pd

data = pd.read_csv('Dataset.csv')

cuisines = data['Cuisines']

top_3_Cuisines = cuisines.value_counts()[:3]
print("Top 3 Cuisines are:\n", top_3_Cuisines)

total_restaurants = cuisines.size

top_3_cuisine_percentages = (top_3_Cuisines / total_restaurants) * 100
print(top_3_cuisine_percentages)
