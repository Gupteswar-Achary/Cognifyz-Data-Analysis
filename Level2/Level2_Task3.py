import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the data
data = pd.read_csv('Dataset.csv')

# Extract coordinates for clustering
coords = data[['Latitude', 'Longitude']]

# Determine the number of clusters (k)
k = 4  # You can choose a different number of clusters

# Apply K-Means clustering algorithm
kmeans = KMeans(n_clusters=k, random_state=0).fit(coords)
labels = kmeans.labels_

# Add cluster labels to the DataFrame
data['Cluster'] = labels

# Plot the clusters
plt.figure(figsize=(10, 6))
for cluster in range(k):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Longitude'], cluster_data['Latitude'], label=f'Cluster {cluster}', alpha=0.5)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Restaurant Clusters')
plt.legend()
plt.show()
