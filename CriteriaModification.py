# This file sets the proper data types for the randomly generated added fields.

index = 1

while index <= 100:
    # print(index)
    str_read = "Pre-processed Files/food_" + str(index) + "pp.txt"
    with open(str_read, 'r') as file:
        lines = file.readlines()
    for i in range(2, 5):
        line = lines[i].strip().split()
        #  print(line)
        if i == 2:
            rating = float(line[1])
            lines[i] = f"{rating} \n"
        if i == 3:
            time = int(line[1])
            lines[i] = f"{time} \n"
        if i == 4:
            nationality = str(line[1])
            lines[i] = f"{nationality} \n"

    # print(lines)
    with open(str_read, 'w') as file:
        print()
        # file.writelines(lines), this is commented since the files are now changed

    index = index + 1
