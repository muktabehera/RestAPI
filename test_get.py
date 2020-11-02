import requests
import json

base_url = 'https://petstore.swagger.io/v2'
petid = '1'
orderid = '1'
username = 'user1'
status1 = 'available'
status2 = 'pending'
status3 = 'sold'

def test_getPetbyID():
  r1 = requests.get(base_url + '/pet/' + petid)
  print(r1.text)

test_getPetbyID()

def test_getPetbyStatus1():
    r4 = requests.get(base_url + '/pet/findByStatus?status=' + status1)
    print(r4.text)

test_getPetbyStatus1()

def test_getPetbyStatus2():
    r5 = requests.get(base_url + '/pet/findByStatus?status=' + status2)
    print(r5.text)

test_getPetbyStatus2()

def test_getPetbyStatus3():
    r6 = requests.get(base_url + '/pet/findByStatus?status=' + status3)
    print(r6.text)

test_getPetbyStatus3()

def test_getStoreOrderById():
    r2 = requests.get(base_url + '/store/order/' + orderid)
    print(r2.text)

test_getStoreOrderById()

def test_getUserByUsername():
    r3 = requests.get(base_url + '/user/' + username)
    print(r3.text)

test_getUserByUsername()