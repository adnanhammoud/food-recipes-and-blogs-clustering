import json

for i in range(1, 101):
    with open('Pre-processed Files/food_' + str(i) + "pp.txt", 'r') as file:
        lines = file.readlines()
    print(i)
    data = {
        "ID": i,
        "title": lines[0].strip(),
        "description": lines[1].strip(),
        "rating": lines[2].strip(),
        "time": lines[3].strip(),
        "nationality": lines[4].strip()
    }

    with open("Pre-processed JSON Files/food" + str(i) + ".json", "w") as json_file:
        json.dump(data, json_file, indent=2)
