# Intro to APIs
## Background
![Several clients connect to a server via HTTP](img/server_clients.png)
1. What does **HTTP** stand for, and what does it mean in the context of the _internet_?

Hyper-Text Transfer Protocol

2. What is the relationship between a **server** and **clients**?

the server is the computer that the clients connect to

3. In the context of this diagram and APIs, what is a **URL**?

It is an address to a specific server

4. In the context of this diagram and APIs, what is an **endpoint**?

a specific location on a server

## Server-Client Communication
Let's examine an interaction between a server and a client.
![A client sends a GET request to a server, who provides the item after authenticating the client](img/server_client.png)
1. How does the server know who the client is?

a client key

2. Why does the server need a `KEY` before sending `X`?

in order to ensure the identity of the client

3. The server and client are communicating via HTTP (Hyper _Text_ Transfer Protocol). What format will the requested `X` be sent as?

HTML

## Data Transfer
### Review
Examine the following Python dictionary.
```py
pokemon = {
    'name': "Scolipede",
    'height': 25,
    'types': [
        {
            'slot': 1,
            'type': "bug"
        },
        {
            'slot': 2,
            'type': "poison
        }
    ]
}
```
1. What does `pokemon['name']` evaluate to?

Scolipede

2. What does `pokemon['types'][0]` evaluate to?

1, bug

3. Write Python code that accesses the `height`.

`pokemon['height']`

4. Write Python code that accesses the `type` in slot 2.

`pokemon[types][1][type]`


### JSON
1. What does **JSON** stand for? Why is it useful for **REST** APIs?

Javascript Object Notation

It makes it easier to transfer data because of the format that it provides

It allows the server to recieve and send data in a format that is more easily accessible

Examine the following **Javascript object**.
```js
pokemon = {
    'name': "Scolipede",
    'height': 25,
    'types': [
        {
            'slot': 1,
            'type': "bug"
        },
        {
            'slot': 2,
            'type': "poison"
        }
    ]
}
```

2. What does `pokemon['name']` evaluate to?
3. How would you access the `type` in slot 2?
4. How is a Javascript object different than a Python dictionary?

kinda the same

## Consuming APIs With Python
Let's return to this diagram:  
![A client sends a GET request to a server, who provides the item after authenticating the client](img/server_client.png)  
and accompany it with some Python code:
```python
import requests````
BASE_URL = "http://www.server.com/"
ENDPOINT = "endpoint"
API_KEY = "abcd1234"

payload = {'key': API_KEY, 'q': "X"}

response = requests.get(BASE_URL+ENDPOINT, params=payload)
if response.ok:
    data = response.json()
else:
    print(reponse.status_code, response.text)
```

1. What is the **requests** module used for?

sending a request to a server

2. What parameters does the `get` method take?

full url, and parameters

3. What is a **payload** in the context of APIs?

data that the API looks at

4. We can now treat `data` as a Python dictionary. Why is that allowed?

they have the same format

5. How do we check if the response is OK?

if response.ok

6. What do we do if the response is not OK?

print the response status

7. What is an HTTP **status code**?

like Error 404 or something
A code that represents a certain type of error
