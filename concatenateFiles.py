titles = "../Indexing/titles.txt"
descriptions = "../Indexing/descriptions.txt"
ratings = "../Indexing/ratings.txt"
times = "../Indexing/times.txt"
nationalities = "../Indexing/nationalities.txt"

index = 2
lines = []
while index <= 100:
    str_read = "Pre-processed Files/food_" + str(index) + "pp.txt"
    open_food = open(str_read, 'r')
    read_food = open_food.readlines()
    for line in read_food:
        lines.append(line)
    title = lines[0]
    description = lines[1]
    rating = lines[2]
    time = lines[3]
    nationality = lines[4]
    lines = []
    if index == 1:
        with open(titles, "w") as file:
            file.write(title)

        with open(descriptions, "w") as file:
            file.write(description)

        with open(ratings, "w") as file:
            file.write(rating)

        with open(times, "w") as file:
            file.write(time)

        with open(nationalities, "w") as file:
            file.write(nationality)
    else:
        with open(titles, "a") as file:
            file.write(title)

        with open(descriptions, "a") as file:
            file.write(description)

        with open(ratings, "a") as file:
            file.write(rating)

        with open(times, "a") as file:
            file.write(time)

        with open(nationalities, "a") as file:
            file.write(nationality)

    index = index + 1
