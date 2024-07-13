import json
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from Similarity.similarityFunctions import get_similarity

start = time.time()
with open('../Indexing/Vectors.json', 'r', encoding="utf8") as document:
    data = json.load(document)

similarities_matrix = np.zeros((100, 100))
document_ids = list(range(1, 101))

for i in range(100):
    for j in range(i + 1, 100):
        similarity = get_similarity(document_ids[i], document_ids[j], data)
        similarities_matrix[i, j] = similarity
        similarities_matrix[j, i] = similarity

linked = linkage(similarities_matrix, method='complete')

plt.figure(figsize=(12, 8))
dendrogram(linked, orientation='top', labels=document_ids, distance_sort=True, show_leaf_counts=True)
plt.title('Hierarchical Clustering of Food Recipes/Blogs')
plt.xlabel('Document ID')
plt.ylabel('Distance')
plt.savefig('Plots/hierarchical_clusters.png')
plt.show()
end = time.time()
print("Execution speed using hierarchical clustering:", round(end - start, 2), 'seconds')