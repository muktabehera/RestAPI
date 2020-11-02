import requests
import json
from datetime import datetime as dt


version = 2
base_url = 'https://petstore.swagger.io/v' + str(version)


petId = 1
pet_url = '/pet/' + str(petId)

pet_response = requests.get(base_url+pet_url)
# response = response.json()
# response.text
print(pet_response.text)
print(pet_response.status_code)

status1 = 'available'
status1_url = '/pet/findByStatus?status=' + status1

status1_response = requests.get(base_url+status1_url)
print(status1_response.text)
print(status1_response.status_code)

status2 = 'pending'
status2_url = '/pet/findByStatus?status=' + status2

status2_response = requests.get(base_url+status2_url)
print(status2_response.text)
print(status2_response.status_code)

status3 = 'sold'
status3_url = '/pet/findByStatus?status=' + status3

status3_response = requests.get(base_url+status3_url)
print(status3_response.text)
print(status3_response.status_code)

username = 'test'
user_url = '/user/' + username

user_response = requests.get(base_url+user_url)
print(user_response.text)
print(user_response.status_code)


storeorderId = 9
storeorder_url = '/store/order/' + str(storeorderId)

storeorderId_response = requests.get(base_url+storeorder_url)
print(storeorderId_response.text)
print(storeorderId_response.status_code)

# Post store order
#currentdate = dt.
#poststoreorder_url = base_url + '/store/order'
data1 = {'id': 1, 'petId': 1,  'quantity': 13,
  'shipDate': "2020-10-27T20:56:29.037Z",
  'status': 'placed',
  'complete': 'true'}

r1 = requests.post('https://petstore.swagger.io/v2/store/order', json=data1)
print(r1.text)

# Post pet
data2 = {"id": "200", "name": "doggie200"}
r2 = requests.post('https://petstore.swagger.io/v2/pet', json = data2)
print(r2.text)

# Put i.e. update Pet
data3 = {"id": "200", "name": "doggieNew200"}
r3 = requests.put('https://petstore.swagger.io/v2/pet', json = data3)
print(r3.text)