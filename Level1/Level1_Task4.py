import pandas as pd


data = pd.read_csv('Dataset.csv')

total_restaurant = len(data['Restaurant ID'])

has_online = len(data[data['Has Online delivery'] == 'Yes'])

per = (has_online / total_restaurant) * 100
print(f'\nPercentage of restaurants that offer online delivery: {per:.2f}%')

average_rating = data.groupby('Has Online delivery')['Aggregate rating'].mean()
print('\nAverage ratings of restaurants with and without online delivery\n', average_rating)
