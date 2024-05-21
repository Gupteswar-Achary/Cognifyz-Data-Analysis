import pandas as pd

data = pd.read_csv('Dataset.csv')

city = data['City']

count_city = city.value_counts()
top_city = count_city.sort_values(ascending=False).index[0]
print('\nThe city with the highest number of restaurants in the dataset is: ', top_city)

city_rating = data.groupby('City')['Aggregate rating'].mean()
print("\nAverage rating of each city: ", city_rating)

top_rating = city_rating.sort_values(ascending=False).index[0]
print('\nThe city with the highest rating in the dataset is: ', top_rating)
