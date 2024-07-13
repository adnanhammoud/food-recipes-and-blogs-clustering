# This contains a function to compute similarity, and another for the clustering algorithm
# to return the document as is and not pre-processed
import json
from sklearn.metrics.pairwise import cosine_similarity

# Inputs to this function are already vectorized documents based on tf-idf weights and their corpus
# This function is specific for json documents having the necessary format
def get_similarity(docID1, docID2, vectors):
    data = vectors

    for document in data:
        if document["ID"] == docID1:
            doc1 = document

        if document["ID"] == docID2:
            doc2 = document

    title_similarity = cosine_similarity([doc1["title"]], [doc2["title"]])[0][0]
    description_similarity = cosine_similarity([doc1["description"]], [doc2["description"]])[0][0]
    rating_similarity = cosine_similarity([doc1["rating"]], [doc2["rating"]])[0][0]
    time_similarity = cosine_similarity([doc1["time"]], [doc2["time"]])[0][0]
    nationality_similarity = cosine_similarity([doc1["nationality"]], [doc2["nationality"]])[0][0]

    similarity = (0.7*title_similarity + 0.9*description_similarity + 0.3*rating_similarity +
                  0.1*time_similarity + 0.4*nationality_similarity)

    return similarity

# This function modifies the description to be de-pre-processed to be user-readable
def get_document(docID):
    with open('../Files/Raw Files/food_' + str(docID) + '.txt', 'r', encoding='utf8') as file:
        document = file.read()

    with open('../Pre-processing/Pre-processed JSON Files/food' + str(docID) +".json") as file:
        data = json.load(file)

    data["description"] = document.strip()
    return data

# Testing
#print(get_document(1))
# s = "y"
# while s == "y":
#     i = eval(input("i = "))
#     j = eval(input("j = "))
#     sim = get_similarity(i, j, '../Indexing/Vectors.json')
#     print(sim)
#     s = input("Again? ")

# with open('../Indexing/Vectors.json', 'r', encoding="utf8") as document:
    # data = json.load(document)
# print(get_similarity(100,94, data))