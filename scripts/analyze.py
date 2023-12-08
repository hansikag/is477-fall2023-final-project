from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
df = pd.read_csv('./data/wine.data')
df.columns = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
print(df)
# Compute summary statistics
summary = df.describe()
print(summary)

# Perform a simple classification task
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(df)

# Create a simple visualization
plt.scatter(df['Alcohol'], df['Proline'], c=df['Cluster'])
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.title('K-Means Clustering')
plt.show()

# Save the summary statistics and the DataFrame with cluster assignments to the results directory
summary.to_csv('./results/summary.csv')
df.to_csv('./results/clustering_results.csv')
