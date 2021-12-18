import csv
import pandas

# Author: Larry Tao
# Date: 10/13/21
# 1. Which species of penguins has the longest bills (on average)?
# 2. Which species of penguins is the most massive (on average)?
# 3. How many Chinstrap penguins are on Dream island?

# create a table with information from penguins.csv
with open("datasets/penguins.csv", "r") as f:
    dict = {}
    data = list(csv.DictReader(f))

    # for every penguin in the data:
    for penguin in data:

        # putting info that we want into variables
        species = penguin["species"]
        mass = penguin["body_mass_g"]
        bill_length = penguin["bill_length_mm"]
        location = penguin["island"]

        # if statements for the first time we see each variable
        if species not in dict:
            dict[species] = {}
            dict[species]["entries"] = 0
        if "mass" not in dict[species]:
            dict[species]["mass"] = []
        if "bill_length" not in dict[species]:
            dict[species]["bill_length"] = []
        if location not in dict[species]:
            dict[species][location] = 0

        # adding info to preexisting lists / values
        dict[species]["entries"] += 1
        dict[species][location] += 1
        dict[species]["mass"].append(float(mass))
        dict[species]["bill_length"].append(float(bill_length))

# finding largest average mass
largest = ["bob", 0]
for species in dict:
    counter = 0
    total = 0.0
    for mass in dict[species]["mass"]:
        counter += 1
        total += mass
    if (total / counter) > largest[1]:
        largest = species, total / counter

print(largest)

# finding largest average bill length
longest = ["bob", 0]
for species in dict:
    counter = 0
    total = 0.0
    for length in dict[species]["bill_length"]:
        counter += 1
        total += length
    if (total / counter) > longest[1]:
        longest = species, total / counter


print(longest)

# finding how many chinstraps are on Dream Island
print(dict["Chinstrap"]["Dream"])

