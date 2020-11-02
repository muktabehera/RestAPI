import requests
import json

base_url = 'https://petstore.swagger.io/v2'

def test_updatePet():
    pet_url = base_url + '/pet'
    data1 = {'id': 1 , 'name' : "doggie123"}
    r1 = requests.put(pet_url, json = data1)
    print(r1.text)

test_updatePet()

