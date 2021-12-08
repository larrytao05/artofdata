import requests
import csv

class Pokemon:
    """Pokemon is used to store certain information about a pokemon species"""

    def __init__(self, name, height, type1, type2, id, weight) -> None:
        """Parameters: id, name, height, weight, and types"""

        self.name = name
        self.height = height
        self.type1 = type1
        self.type2 = type2
        self.id = id
        self.weight = weight
    
    def __str__(self) -> str:
        """Returns a string representation of the pokemon's information"""

        return str(self.id) + ", " + self.name + ", " + str(self.height) + ", " + str(self.weight) + ", " + self.type1 + ", " + self.type2

# preset url info
BASE_URL = "https://pokeapi.co/"
ENDPOINT = "api/v2/pokemon/"

# opening the csv
with open("Datasets/pokemon_mess.csv") as f:

    # creating a csv reader that can iterate through the information
    data = csv.DictReader(f)

    # creates the first row of the csv
    fieldnames = ["id", "name", "height", "weight", "type1", "type2"]
    print(fieldnames[0] + "," + fieldnames[1] + "," + fieldnames[2] + "," + fieldnames[3] + "," + fieldnames[4] + "," + fieldnames[5])

    # iterating through the csv
    for pokemon in data:

        # creating a pokemon object with all of the data we want to change
        poke = Pokemon(pokemon["name"].lower(), pokemon["height"], pokemon["type1"], pokemon["type2"], pokemon["id"], pokemon["weight"])

        # getting the correct info from the API
        response = requests.get(BASE_URL + ENDPOINT + poke.name, params=None)

        # checking if the response is ok
        if response.ok:
            info = response.json()
        else:
            print(response.status_code, response.text)

        # storing the information
        poke.height = info["height"]
        poke.id = info["id"]
        if len(info["types"]) == 2:
            poke.type2 = info["types"][1]["type"]["name"]
        else:
            poke.type1 = info["types"][0]["type"]["name"]
        poke.weight = info["weight"]

        # printing out all of the information to the csv
        print(poke)
    

        
        


