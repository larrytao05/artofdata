import csv
with open("datasets/favorite_colors.csv", "r") as f:
    dict = {}
    found = []
    data = list(csv.DictReader(f))
    for row in data:
        grade = row["grade"]
        color = row["favorite_color"]
        if grade not in dict:
            dict[grade] = {}
        if color not in dict[grade]:
            dict[grade][color] = 0
        dict[grade][color] += 1


total = sum([grade["yellow"] for grade in dict.values()])
print(total)
