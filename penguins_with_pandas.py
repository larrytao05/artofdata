import pandas

peng = pandas.read_csv("Datasets/penguins.csv")

gentoo = peng[peng["species"] == "Gentoo"]
print(gentoo["bill_length_mm"].max())