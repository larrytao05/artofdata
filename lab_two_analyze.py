import csv

# open file
with open("Datasets/animal_crossing.csv", "r") as f:

    # clean the data
    data = csv.DictReader((line.replace('\0','') for line in f), delimiter=',')

    # dictionaries to store info
    Dict = {}
    colors = {}

    # loop through data and get all the information we need
    for clothing in data:
        if clothing["Color 1"] in colors.keys():
            colors[clothing["Color 1"]] += 1
        else:
            colors[clothing["Color 1"]] = 1
        if clothing["Color 2"] != clothing["Color 1"]:
            if clothing["Color 2"] in colors.keys():
                colors[clothing["Color 2"]] += 1
            else:
                colors[clothing["Color 2"]] = 1
        if clothing["ÿþName"] in Dict.keys():
            Dict[clothing["ÿþName"]] += 1
        else:
            Dict[clothing["ÿþName"]] = 1

# get the max value of variations
max = 0, "bob"
for clothingType in Dict:
    if Dict[clothingType] > max[0]:
        max = Dict[clothingType], clothingType

# if a sock has the same number of variations as the max, print it
for clothingType in Dict:
    if Dict[clothingType] == max[0]:
        print(Dict[clothingType], clothingType)

# find how many socks of each color there are
for color in colors.keys():
    print(color, colors[color])