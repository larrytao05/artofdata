import requests
import csv
import codecs

# define base url and endpoint for the API request
BASE_URL = "https://hm-cs.herokuapp.com"
ENDPOINT = "/socks"
start_index = 0

# open the writer
writer = csv.writer(open("Datasets/animal_crossing.csv"))

# continue sending requests as long as there are indices to discover
while (True):

    # info to send to server
    payload = {'key':'ArtOfDataKEY123', 'idx':start_index}

    # send the request
    response = requests.get(BASE_URL + ENDPOINT, params=payload)


    # checking if the response is ok
    if response.ok:
        info = response.text.strip().encode()
        print(codecs.decode(info, encoding="utf-8-sig"))
        start_index += 1
    else:
        break

