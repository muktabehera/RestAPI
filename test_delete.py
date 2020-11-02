import requests
import json

base_url = 'https://petstore.swagger.io/v2'

def test_PetPost():
    pet_url = 'https://petstore.swagger.io/v2/pet'
    data1 = {'id':1, 'name': 'dog1'}
    r1 = requests.post(pet_url, json=data1)
    print(r1.text)

test_PetPost()

def test_PetDelete():
    pet_url = 'https://petstore.swagger.io/v2/pet/1'
    #data2 = {'id': 1}
    r2 = requests.delete(pet_url)
    # print(r2.status_code)

    print(f"response status = {r2.status_code} \n response text = {r2.text}")

test_PetDelete()

#

