## Write a program to display the Fibonacci sequence in Python?
# 0,1,2,3,5,8,13 etc
#class practice():
    # def fibonacci(self,n):
    #     #n = 10
    #     n0 = 0
    #     n1 = 1
    #     l = list()
    #     if n <= 0:
    #         print("Enter positive integer")
    #     elif n == 1:
    #         print("Numbers in Fibonacci sequence upto", n, ":")
    #         print(n0)
    #     else:
    #         for x in range(0,n):
    #             l.append(n0)
    #             nth = n0 + n1
    #             n0 = n1
    #             n1 = nth
    #
    #     print(f"The fibonacci sequence upto {n} is {l}")

#a = practice()
#a.fibonacci(10)

##Given number is prime number or not. [ note - 2 is divisible by 2 and is still prime]
# Note: A number divisible by 1 and itself only is prime. So if it is divisible by any other number its not prime.
# def primetest(n):
#     # check if n is greater than 2:
#     # if greater than 2 test n%i in range 2,n
#
#     if n > 2:
#         result = 1
#         for i in range(2, n):
#             if n % i == 0:
#                 result = 0
#
#         if result == 0:
#             print("Not Prime")
#
#         elif result == 1:
#             print("Prime")
#
#
# n = 99
# primetest(n)

##Write Python code to check the given sequence is a palindrome or not?
#mom

# class test():
#     def palindrome(self):
#         s = "MOM"
#         #convert string to list
#         l = list(s)
#         # reverse the list
#         l.reverse()
#         # convert it to string
#         s2 = ''.join(l)
#         # compare two strings
#         if s == s2:
#             print(f"yes {s} is a palindrome")
#         else:
#             print(f"No {s} is not a palindrome")
#
# a = test()
# a.palindrome()
##OR
# def checkpalindrome(s):

#     # assuning the input is string
#     rev_s = s[ : : -1]
#     print(rev_s)
#     if s == rev_s:
#         print("Palindrome")
#     else:
#         print("No not a palindrome")


# s = "mom"
# checkpalindrome(s)

##Write Python code to sort a numerical dataset?

# class test():
#     def sort(self,l):
#         #l = [1,2,3,4,5,8,1,2,3,4,5]
#         l.sort()
#         print(f"the sorted list is {l}")
#
# a = test()
# l = [1,2,3,4,5,8,1,2,3,4,5]
# a.sort(l)

### Write Python code to sort a numerical dataset without using sort function.
#
# def sortinglist(l):
#     # assuming its list and we are doing ascending sort
#     finallist = []
#
#     while len(l) >= 1:
#         m = min(l)
#         finallist.append(m)
#         l.remove(m)
#
#     return (finallist)
#
#
# l = [3, 4, 2, 1]
# print(sortinglist(l))


## converting list into nested list:
# x = [ "abc","def"]
# print(list(map(list,x))) # result is [['a', 'b', 'c'], ['d', 'e', 'f']]

## Python class with a constructor
# class test:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#     def print(self):
#         print(f"hello my name is {self.name}, addess is {self.address}")
#
# a = test("rosy","111 e lane")
# a.print()

## Print a string N times.
# class test():
#
#     def funNtimes(self, s, n):
#         # m = s*n
#         # print(m)
#         for i in range(0, n):
#             print(s)
#
#
# s = "hello"
# n = 10
# a = test()
# a.funNtimes(s, n)

##Check the memory usage of  an object
# import sys
#
# def size():
#     d = "ghitm"
#     print(sys.getsizeof(d))
# size()

## Find the most frequent/recurring value in a list
# class test():
#     def frequestValue(self):
#         l = ['a','b','c','d','a','a','b','c','e','f']
#         dict = {}
#         for x in l:
#             c = l.count(x)
#             #append key value pair to dict
#             dict[x]=c
#         print(dict) # {'a': 3, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1}
#
#         # make list of keys from dict , i.e.['a', 'b', 'c', 'd', 'e', 'f']
#         keys = list(dict.keys())
#         print(keys)
#
#         #make list of values from dict, i.e. [3, 2, 2, 1, 1, 1]
#         values = list(dict.values())
#         print(values)
#
#         # store it in another list
#         valueoriginal = list()
#         for x in values:
#             valueoriginal.append(x)
#         print(valueoriginal)
#
#         # find the max numbers it occurred
#         values.sort()
#         print(values)
#         maxvalue = values[len(values)-1]
#         print(maxvalue)
#
#         #find index for max value from 'original values list
#         myindex = valueoriginal.index(maxvalue)
#         print(myindex)
#
#         #find the key having myindex from list 'keys'
#         answer = keys[myindex]
#         print(f"the max occurring value is '{answer}'")
#
# a = test()
# a.frequestValue()


## Checking whether the two words are anagrams or not[A word can be formed by rearranging the letters of another]
# ex- cinema, iceman

# class test():
#     def anagram(self):
#         s1 = "cinema"
#         s2 = "iceman"
#         # convert s1 to list
#         lists1 = list(s1)
#         print(lists1)
#
#         #convert s2 to list
#         lists2 = list(s2)
#         print(lists2)
#
#         #compare if all values in lists1 is in lists2
#         if len(lists1)== len(lists2):
#             for x in lists1:
#                 if x in lists2:
#                     pass
#             print(f"string: {s1}")
#             print(f"string: {s2}")
#             print(f"Yes both the strings are anagram")
#
#         else:
#             print("Both strings can not be a anagram")
#
# a = test()
# a.anagram()

#OR
# class test():
#     def anagram(self):
#         s1 = "cinema"
#         s2 = "iceman"
#         if len(s1)==len(s2):
#             for x in s1:
#                 if x in s2:
#                     pass
#             print("yes it is anagram")
#
# a = test()
# a.anagram()


##Print the file path of imported modules
# import os
# import socket
# print(os)
# print(socket)

##What is the difference between tuples and lists in Python?
    # tuple = ('a','b','c',1,2)
    # list = ['a','b','c',1,2]
    # tuple can not be updated, can say it's read only.
    # 1. Tuple has indexes like list, values can be found using index tuple[2]
    # 2. Tuple can be sliced, tuple[1:3]
    # 3. print(tuple * 2)

## import random
# d = random.randrange(0,100)  # random Integer from 0 to 99 inclusive
# d2 = random.randrange(10)    # Integer from 0 to 9 inclusive
# e = random.random()          # Random float:  0.0 <= x < 1.0
# f = random.uniform(2.0,9.0)  # Random float:  2.0 <= x < 9.0
# print(d, d2, e, f)

# ## Shuffle a List:
# import random
# l = ["d","e",1,2,3]
# random.shuffle(l)
# print(l)

## Ask user to enter a number, and then prints that number, tripled
# a = input("enter a number:")
# print(type(a))
# n = int(a)
# print(f"Tripled number is {n*3}")

## Create a linked list
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print (printval.dataval)
#             printval = printval.nextval
#
# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # Link first Node to second node
# list.headval.nextval = e2
#
# # Link second Node to third node
# e2.nextval = e3
#
# list.listprint()

### How Many Numbers Are Smaller Than the Current Number in a list
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

# def smaller(l):
#     a = []
#     for x in l:
#         count = 0
#         for y in l:
#             if y < x:
#                 count = count + 1
#         a.append(count)
#
#     print(a)
#
#
# l = [5, 6, 7, 8, 4, 3]
# smaller(l)

#
###Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Input: s = "leetcode"
# Output: 2

# def power(s):
#     #  check string is not empty
#     # now test
#     prev = s[0]
#     count = 1
#     maxcount = 1
#     n = len(s)
#     for i in range(1, n):
#         if s[i] == prev:
#             count = count + 1
#             maxcount = max(count, maxcount)
#         else:
#             count = 1
#             prev = s[i]
#     print(maxcount)
#
#
# s = "leetcode"
# power(s)

### Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.

# def lengthofLastword(s):
#     # string input
#     # check if it has any last word with space separated
#     # create list
#     # check the length of the list
#     # check the value in the last index and print
#     l = s.split(' ')
#     if len(l) == 1 :
#         print(f"It does not have last word separated by space")
#         print(0)
#     else:
#         n = len(l)
#         print(l[n-1])

# s = "hi you"
# lengthofLastword(s)

### You are given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# def segment(s):
#     # convert to list
#     # with index try finding count?
#
#     l2 = []
#     l = s.split(' ')
#     n = len(l)
#     for i in range(0, n):
#         sub = l[i]
#         n1 = len(sub)
#
#         l2.append(n1)
#     print(l2)
#
#     # find max count
#     listsort = sorted(l2)
#     print(listsort[len(listsort) - 1])

# s = "Hello, my name is John"
# segment(s)

####### example of testcases using pytest:
# import pytest

# class Testnow():

#     @pytest.mark.smoke
#     def test_upper(self):
#         assert 'foo'.upper() == 'FOO'

#     def test_isupper(self):
#         assert 'FOO'.isupper()
#         assert not 'Foo'.isupper()


#     def test_split(self):
#         s = 'hello world'
#         assert s.split(2) == ['hello', 'world']
#         # s.split should throw when the separator is not a string
#         with pytest.raises(TypeError):
#             pass

# a = Testnow()
# a.test_isupper
# a.test_split
# a.test_upper

# pytest.main()
# #pytest.main(['-k','test_isupper'])  # running specific test case
# #pytest.main(['-k','smoke'])  # running specific marked testcase

### read the data from the URL and print it [note- skip this, follow the requests & BeautifulSoup > html.parser]
# import urllib.request
# # open a connection to a URL using urllib
# webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

# #get the result code and print it
# code = webUrl.getcode()
# print (f"The response code is {code}")

# # read the data from the URL and print it
# data = webUrl.read()
# print (data)
#----------------------------------------------

### find the number of articles in Hacker news home page[parsing html page]

# import requests
# from bs4 import BeautifulSoup as bs

# response = requests.get("https://news.ycombinator.com/")
# print(response.text)
# print(response.content)
# print(response.status_code)

# soup = bs(response.text, 'html.parser')     # or response.content [ **creates object for bs]
# print(soup.title.string)
# ranks = soup.findAll('span', {'class':'rank'})   #soup.findAll
# #print(ranks)
# l =[]
# for i in ranks:
#     #print(i.text)
#     s = i.text
#     l.append(int(s.split('.')[0]))
# print(l)
# print(max(l))


## Rest API, Pytest : Verify that a given address is from 'CA'
# import requests
# import json
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     baseurl = "https://us-street.api.smartystreets.com/street-address?"
#     authid = "0f4db2c2-e936-20ea-1b84-1d6807d35f07"
#     authtoken = "3YTaJHzy3ON7GNBC3I7G"
#
#     url = baseurl + 'auth-id=' + authid + '&auth-token=' + authtoken + '&street=1600+amphitheatre+pkwy&city=mountain+view&state=CA&candidates=10'
#
#     # request_payload  = {}
#     headers = {'Content-Type': 'application/json',
#                'Host': 'us-street.api.smartystreets.com'
#                }
#
#     # address_response = requests.get(url=url,headers=headers).json()
#
#     address_response = requests.get(url=url, headers=headers)
#
#     r = json.loads(address_response.text)
#
#     ans = r[0]['components']['state_abbreviation']
#
#     return {
#         'ans': ans,
#     }
#
#
# def test_address(setup):
#     # result = setup()
#
#     assert setup['ans'] == 'CA'
#
# pytest.main()

#### 31: 1 Qrt (25), 1 nickle (5), 1 pennie (1) [dime 10]
# num_coins(cents) ==> 3

# def coin(cents):
#     count = 0
#
#     if cents > 25:
#         q1cents = cents // 25
#         count = count + q1cents
#         r1cents = cents % 25
#         if r1cents > 10:
#             q1r1cents = r1cents // 10
#             count = count + q1r1cents
#             r1r1cents = r1cents % 10
#             if r1r1cents > 5:
#                 q1r1r1cents = r1r1cents // 5
#                 count = count + q1r1r1cents
#                 r1r1r1cents = r1r1cents % 5
#                 if r1r1r1cents > 1:
#                     q1r1r1r1cents = r1r1r1cents // 1
#                     count = count + q1r1r1r1cents
#             elif r1r1cents > 1:
#                 q2r1r1cents = r1r1cents // 1
#                 count = count + q2r1r1cents
#         elif r1cents > 5:
#             q3r1cents = r1cents // 5
#             count = count + q3r1cents
#             r3r1cents = r1cents % 5
#             if r3r1cents > 1:
#                 q4r3r1cents = r3r1cents // 1
#                 count = count + q4r3r1cents
#         elif r1cents > 1:
#             q5r1cents = r1cents // 1
#             count = count + q5r1cents
#
#     elif cents > 10:
#         q2cents = cents // 10
#         count = count + q2cents
#         r2cents = cents % 10
#         if r2cents > 5:
#             q6r2cents = r2cents // 5
#             count = count + q6r2cents
#             r6r2cents = r2cents % 5
#             if r6r2cents > 1:
#                 q7r6r2cents = r6r2cents // 1
#                 count = count + q7r6r2cents
#
#         elif r2cents > 1:
#             q7r2cents = r2cents // 1
#             count = count + q7r2cents
#     elif cents > 5:
#         q3cents = cents // 5
#         count = count + q3cents
#         r3cents = cents % 5
#         if r3cents > 1:
#             q8r3cents = r3cents // 1
#             count = count + q8r3cents
#     elif cents > 1:
#         q4cents = cents // 1
#         count = count + q4cents
#
#     print(count)
#
#
# cents = 153
# coin(cents)

### urlencode before making get request
# requests.utils.quote("615 e poplar")

### generate uuid
# import uuid
# print(uuid.uuid4())  # 6b8571a1-61d9-4700-8cb1-594b91127505
# print(uuid.uuid4().hex) # 886158d9336949c69a1b3d144b4f5305

### from a list find how many times a number is iterated(collections):
    # l = [2,2,3,4,4,4]
    # import collections
    # a = collections.Counter(l)
    # print(a)        # Counter({4: 3, 2: 2, 3: 1})
    # print(a.most_common(2)) # returns n numbers of the key-value pairs where the value is the most recurring. i.e. [(4, 3), (2, 2)]
    # mydict = dict(a)
    # print(mydict) # result will be {2: 2, 3: 1, 4: 3}
    ### import collections
    ### a=collections.Counter([2,2,3,3,3,4])
    ### b=collections.Counter([2,2,3,4,4])
    ### a|b  # result is "Counter({3: 3, 2: 2, 4: 2})", returns the pair of keys and the highest recurring value
    ### a&b # result is "Counter({3: 1, 4: 1, 5: 1})", returns the pair of keys and the lowest recurring value.

### Sorting in ascesnding order "Selection sort"

# def ascsort(l):
#     # find min value in l, append it to sorted list:
#     # remove min value from l
#     # Repeat
#     a = []
#     while len(l) >= 1:
#         m = min(l)
#         a.append(m)
#         # print(a)
#         l.remove(m)
#         # print(l)
#
#     print(a)
#
#
# l = [2, 1, 6, 3]
# ascsort(l)

#### Target ==>
### [14,13, 6, 4, 1,2] with target 3 print 1 and 3 in a list

# def target(l, t):
#     l2 = l.copy()
#     targetlist = []
#     not_solved = True
#     # print(l2)
#
#     for x in l:
#         for y in l2:
#             if x != y:
#                 if x + y == t:
#                     targetlist.extend([x, y])
#                     not_solved = False
#
#         if not_solved == False:
#             break
#     return targetlist
#
#
# l = [1, 5, 6, 2, 4]
# t = 11
# print(target(l, t))

# ####Q==> Create a new dictionary by extracting the following keys from a given dictionary
## keys to extract ["name", "salary"]
## sampleDict = {
##   "name": "Kelly",
##   "age":25,
##   "salary": 8000,
##   "city": "New york"
## }
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# new = {}
#
# keys = ["name","salary"]
#
# for x in keys:
#     new[x] = sampleDict[x]
# print(new)
