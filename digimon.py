import csv

'''
Author: Larry Tao
Date: 10/18/21
Name: Analyzing digimon.csv file for art of data lab
'''

with open("datasets/digimon.csv", "r") as f:
    counter = 1
    hps = [None, None, None]
    hp_species = [None, None, None]
    data = list(csv.DictReader(f))
    dict = {"total_spd":0.0, "num":0.0}
    for digimon in data:
        digi = digimon["Digimon"]
        hp = float(digimon["HP"])
        spd = float(digimon["Spd"])
        memory = float(digimon["Memory"])
        atk = float(digimon["Atk"])
        if atk > 100 and memory <= 5 and counter <= 3:
            counter += 1
            print(digi)
            print(atk)
            print(memory)
        dict["total_spd"] += spd
        dict["num"] += 1
        dict[digi] = {"hp":hp, "spd":spd, "memory":memory, "atk":atk}
        for i in range(len(hps)):
            if hps[i] == None:
                hps[i] = dict[digi]["hp"]
                hp_species[i] = digi
                break
            elif dict[digi]["hp"] > hps[i]:
                hps[i] = dict[digi]["hp"]
                hp_species[i] = digi
                break



avg_spd = dict["total_spd"] / dict["num"]
print(avg_spd)    



    

print(hps)
print(hp_species)

