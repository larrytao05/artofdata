import csv

'''
Author: Larry Tao
Date: 10/18/21
Name: Analyzing digimon.csv file for art of data lab
'''

# opening the csv
with open("datasets/digimon.csv", "r") as f:

    # defining variables that we need, along with a DictReader for our data
    counter = 1
    data = list(csv.DictReader(f))
    d = {"total_spd":0.0, "num":0.0, "hps":{}}
    dict = {}

    # iterating through every line in the csv
    for digimon in data:

        # putting data into variables
        typ = digimon["Type"]
        digi = digimon["Digimon"]
        hp = float(digimon["HP"])
        spd = float(digimon["Spd"])
        memory = float(digimon["Memory"])
        atk = float(digimon["Atk"])

        # easy solution (but not necessarily most efficient) for >300 atk question
        if atk > 100 and memory <= 5 and counter <= 3:
            counter += 1
            print(digi)
            print(atk)
            print(memory)

        # putting the data we've collected into the dictionary
        d["total_spd"] += spd
        d["num"] += 1
        dict[digi] = {"hp":hp, "spd":spd, "memory":memory, "atk":atk, "Type":typ}
        d["hps"][digi] = hp

# finding average speed
avg_spd = d["total_spd"] / d["num"]
print(avg_spd)    

# finding max hp
hps_sorted = sorted(d["hps"].keys(), key=d["hps"].get)
for i in range(-1, -4, -1):
    hp = hps_sorted[i]
    print(hp)
    print(d["hps"][hp])
                    

# find how many digimon have a value of "value" for the given attribute
def count_digimon(att, value):
   # iterate through all of the digimon
   total = 0
   for digi in dict:
       if dict[digi][att] == value:
           total += 1
   return total

# testing count_digimon
print(count_digimon("Type", "Vaccine"))