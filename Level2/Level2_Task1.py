import pandas as pd

data = pd.read_csv('Dataset.csv')

rating = data['Aggregate rating']
bins_values = [1, 2, 3, 4, 5]
bins_labels = ['<2', '2-3', '3-4', '4-5']

rating_distribution = pd.cut(rating, bins=bins_values, labels=bins_labels).value_counts()
print(rating_distribution)
print(f"\nThe most common rating range: {rating_distribution.index[0]}")

votes = data['Votes']
avg_votes = votes.mean()
print(f"The average number of votes received by restaurants: {avg_votes}")
