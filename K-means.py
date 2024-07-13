import json
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from Similarity.similarityFunctions import get_similarity, get_document

start = time.time()
legend_clusters = []
document_ids = list(range(1, 101))
similarities_matrix = np.zeros((100, 100))
with open('../Indexing/Vectors.json', 'r', encoding="utf8") as document:
    data = json.load(document)
for i in range(100):
    for j in range(i + 1, 100):
        similarity = get_similarity(document_ids[i], document_ids[j], data)
        similarities_matrix[i, j] = similarity
        similarities_matrix[j, i] = similarity

num_clusters = 10
kmeans = KMeans(n_clusters=num_clusters, init='k-means++')
clusters = kmeans.fit_predict(similarities_matrix)

plt.figure(figsize=(12, 8))
labels = ['o', 's', 'D', '^', 'p', 'v', '*', '>', 'H', '<']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for cluster_num in range(num_clusters):
    marker = labels[cluster_num % len(labels)]
    color = colors[cluster_num % len(colors)]
    counter = 0
    cluster_docs = np.where(clusters == cluster_num)[0]
    for doc_idx in cluster_docs:
        document = get_document(document_ids[doc_idx])
        plt.scatter(cluster_num + 1, doc_idx, marker=marker, color=color, label=f'Doc {document["ID"]}', s=100)
        if counter == 0:
            with open('K-means Clusters/cluster' + str(cluster_num+1) + '.json', 'w') as file:
                json.dump(document, file, indent=2)
            counter = counter + 1
        else:
            with open('K-means Clusters/cluster' + str(cluster_num+1) + '.json', 'a') as file:
                json.dump(document, file, indent=2)
    legend_clusters.append(plt.Line2D([0], [0], marker=marker, color='w', markerfacecolor=color, markersize=10))

plt.title('K-Means Clustering of Food Recipes/Blogs')
plt.xlabel('Cluster')
plt.ylabel('Document ID')
plt.legend(legend_clusters, [f'Cluster {i+1} Documents' for i in range(num_clusters)], loc="upper right")
plt.savefig('Plots/kmeans_clusters.png')
# plt.show()
end = time.time()
print("Execution speed using k-means clustering: ", round(end - start, 2), "seconds")
db_index = davies_bouldin_score(similarities_matrix, clusters)
print("Davies–Bouldin index =", round(db_index, 3))