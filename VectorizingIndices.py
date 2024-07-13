# This file computes the vector of each field of each document and stores them in a json document
from sklearn.feature_extraction.text import TfidfVectorizer
import json

title_vectorizer = TfidfVectorizer()
description_vectorizer = TfidfVectorizer()
rating_vectorizer = TfidfVectorizer()
time_vectorizer = TfidfVectorizer()
nationality_vectorizer = TfidfVectorizer()

openTimes = open("times.txt", 'r', errors="ignore")
X4 = time_vectorizer.fit(openTimes)

openNationalities = open("nationalities.txt", 'r', errors="ignore")
X5 = nationality_vectorizer.fit(openNationalities)

openDescriptions = open("descriptions.txt", 'r', errors="ignore")
X2 = description_vectorizer.fit(openDescriptions)

openRatings = open("ratings.txt", 'r', errors="ignore")
X3 = rating_vectorizer.fit(openRatings)

openTitles = open("titles.txt", 'r', errors="ignore")
X1 = title_vectorizer.fit(openTitles)

json_entries = []
criteria = ["title", "description", "rating", "time", "nationality"]
index = 1

while index <= 100:
    json_entry = {"ID": index}
    str_read = "../Pre-processing/Pre-processed Files/food_" + str(index) + "pp.txt"
    open_food = open(str_read, 'r')
    read_lines = open_food.readlines()
    i = 0
    for line in read_lines:
        if i == 0:
            X_array = title_vectorizer.transform([line]).toarray()[0]
        if i == 1:
            X_array = description_vectorizer.transform([line]).toarray()[0]
        if i == 2:
            X_array = rating_vectorizer.transform([line]).toarray()[0]
        if i == 3:
            X_array = time_vectorizer.transform([line]).toarray()[0]
        if i == 4:
            X_array = nationality_vectorizer.transform([line]).toarray()[0]
        line_vector = X_array.tolist()
        json_entry[criteria[i]] = line_vector
        i = i + 1
    i = 0
    json_entries.append(json_entry)
    with open("Vectors.json", 'w') as json_file:
        json.dump(json_entries, json_file, indent=2)
    index = index + 1

# with open("Vectors.json", "r") as json_file:
    # vectors_data = json.load(json_file)

# print(vectors_data)