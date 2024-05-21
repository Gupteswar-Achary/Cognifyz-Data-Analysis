import pandas as pd

# Load the dataset
data = pd.read_csv('Dataset.csv')

# Identify restaurant chains
name_counts = data['Restaurant Name'].value_counts()
chains = name_counts[name_counts > 1]
print("Restaurant chains : ")
print(chains)

# Filter data for chains
chain_data = data[data['Restaurant Name'].isin(chains.index)]

# Analyze ratings
average_ratings = chain_data.groupby('Restaurant Name')['Aggregate rating'].mean()

# Analyze popularity
popularity = chain_data['Restaurant Name'].value_counts()

# Combine ratings and popularity into a single DataFrame
analysis = pd.DataFrame({
    'Average Rating': average_ratings,
    'Number of Reviews': popularity
})

# Print the analysis
print(analysis)
