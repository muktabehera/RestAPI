import requests
import json


version = 2
base_url = 'https://petstore.swagger.io/v' + str(version)


petId = 1
#print(type(petId))
pet_url = '/pet/' + str(petId)

username = 'test'
user_url = '/user/' + username


pet_response = requests.get(base_url+pet_url)
# response = response.json()
# response.text
print(pet_response.text)
print(pet_response.status_code)
# print(response)

user_response = requests.get(base_url+user_url)
print(user_response.text)
print(user_response.status_code)


