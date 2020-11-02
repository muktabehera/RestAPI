import requests
import json

base_url = 'https://petstore.swagger.io/v2'

def test_PetPost():
    pet_url = 'https://petstore.swagger.io/v2/pet'
    data1 = {'id':1, 'name': 'dog1'}
    r1 = requests.post(pet_url, json=data1)
    print(r1.text)

test_PetPost()

def test_PetPostbyId():
    pet_url = 'https://petstore.swagger.io/v2/pet'
    data2 = {'id': 1, 'name': 'dog2', 'status': 'available'}
    r2 = requests.post(pet_url, json=data2)
    print(r2.text)

test_PetPostbyId()

def test_PostStore():
    store_url = base_url + '/store/order'
    data3 = {"id": 0,"petId": 1, "shipDate": "2020-10-28T17:23:28.624Z", "status": "placed", "complete": True}
    r3 = requests.post(store_url, json = data3)
    print(r3.text)

test_PostStore()

# def test_PostMultipleUsers():
#     user_url = 'https://petstore.swagger.io/v2/user/createWithArray'
#     # data4 = [{"id": 1, "username": "one","firstName": "on", "lastName": "w1"}, {"id": 2, "username": "two", "firstName": "tw", "lastName": "w2"}]
#     data4 = {"id": 0, "username": "one","firstName": "on", "lastName": "w1","email": "test@test.com","password": "password123","phone": "453454321","userStatus": 0}
#     r4 = requests.post(user_url, json=data4)
#     print(r4.text)
#
# test_PostMultipleUsers()

# def test_PostUserList():
#     createlist_url = 'https://petstore.swagger.io/v2/user/createWithList'
#     data5 = [{'username': 'john', 'password' : 'password'}]
#     r5 = requests.post(createlist_url, json=data5)
#     print(r5.text)
#
# test_PostUserList()