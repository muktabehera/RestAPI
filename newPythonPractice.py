## Write a program to display the Fibonacci sequence in Python?
# 0,1,1,2,3,5,8,13 etc
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
# def testPrime(n):
#     # check if n is greater than 2:
#     # if greater than 2 test n%i in range 2,n

#     if n == 2:
#         print(f"{n} is a prime number")

#     elif n < 2:
#         print("Please enter a number greater than 2")

#     elif n > 2:
#         for i in range(2, n):
#             if n % i == 0:
#                 result = "not prime"
#                 break
#             else:
#                 result = "prime"
#
#     if result == "not prime":
#         print(f"{n} is not a prime number")
#
#     if result == "prime":
#         print(f"{n} is a prime number")
# n = 99
# fun1(n)

##Write Python code to check the given sequence is a palindrome or not?
#mom, madam, nurses run

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
## OR:
# def checkpalindrome(s):
#     fs = s.replace(" ", "")
#     rev_fs = fs[:: -1]
#     if fs == rev_fs:
#         print("Palindrome")
#     else:
#         print("Not Plaindrome")
# s = "nurses run"
# checkpalindrome(s)


##Write Python code to sort a numerical dataset?
# class data():
#     def fun1(self,l):
#         dl = sorted(l, reverse = True)
#         print(f"descending order of the set is {dl}")
#         al = sorted(l)
#         print(f"Ascending order of the set is {al}")
# l = [2,4,5,3,1]
# a = data()
# a.fun1(l)

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
# def fun1(l):
#     d = {}
#     for x in l:
#         d[x] = l.count(x)
#     valuelist = list(d.values())
#     keylist = list(d.keys())
#     m = max(valuelist)
#     i = valuelist.index(m)
#     print(keylist[i])
#
# l = [3,4,5,3,4,5,3,5,5]
# fun1(l)


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
# def fun1(s1, s2):
#     result = 0
#     for x in s1:
#         if x in s2:
#             pass
#             if len(s1) == len(s2):
#                 result = 1
#     else:
#         result = 0
#
#     if result == 1:
#         print("Yes anagrams")
#     if result == 0:
#         print("No not anagrams")
# s1 = "cinema"
# s2 = "icemann"
# fun1(s1, s2)


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
# OR
# def fun1(s):
#     l = s.split(' ')
#     if len(l) <= 1:
#         return 0
#     elif len(l) > 1:
#         n = l.pop()
#         return len(n)
# s = "how are you"
# print(fun1(s))

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
#     OR
#     r = json.dumps(address_response.text) ## if address_response.text is string
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

# #### cents = 31  , output : num_coins(cents) ==> 3
# hint: : 1 Qrt (25), 1 nickle (5),1 dime (10) 1 pennie (1)

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

# OR Given two lists, find the pair of keys and the highest/lowest recurring value
# l1 = [2,2,3,3,3,4]
# l2 = [2,2,3,4,4]
# d1 = {}
# d2 = {}
# for x in l1:
#     d1[x] = l1.count(x)
# for y in l2:
#     d2[y] = l2.count(y)
# d3 = {}
# for x in d1:
#     if x in d2:
#         m = max(d1[x],d2[x]) # min in case lowest occurring
#         d3[x] = m
# print(d3)  , result {2: 2, 3: 3, 4: 2} or {2: 2, 3: 1, 4: 1}



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
### [14,13, 6, 4, 1,2] with target 3 print 1 and 2 in a list

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
# OR
# def fun1(l,t):
#     for x in l:
#         a = []
#         for y in l:
#             if x != y:
#                 if x + y == t:
#                     a.extend([x,y])
#     print(a)
# l = [14,13, 6, 4, 1,2]
# t = 8
# fun1(l,t)

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

#### Given a string ‘str’ of digits and an integer ‘n’, build the lowest possible number by removing ‘n’ digits from the string and not changing the order of input digits.
#
# def findingsmallest(str, n):
#     i = 0
#     l = list(str)
#
#     while i < n:
#         m = max(l)
#         l.remove(m)
#         i = i + 1
#     print(l)
#     print(''.join(l))
#
#
# str = "18329"
# n = 3
# findingsmallest(str, n)

### You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index. For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24]. You cannot use division in this problem.

# def prod(l):
#     a = []
#
#     for i in range(0, len(l)):
#         s = 1
#         smax = 1
#         for j in range(0, len(l)):
#
#             if j != i:
#                 s = l[j] * s
#         smax = max(s, smax)
#         a.append(smax)
#
#     print(a)
# l = [1, 2, 3, 4, 5]
# prod(l)
## OR
# def product(l):
#     a = []
#     for x in l:
#         m = 1
#         for y in l:
#             if l.index(x) != l.index(y):
#                 m = m * y
#         a.append(m)
#
#     print(a)
# l = [1, 2, 3, 4, 5]
# product(l)


#### Given an array consisting many inner arrays, flatten the array into one: example: input: [[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]] output: [6,4,7,9,5,4,2,4,8,2,2,7,9,0,7,9,3,1,8,5]

#
# def fun1(l1):
#     a = []
#
#     for i in range(0, len(l1)):
#         if type(l1[i]) == type([]):
#             for x in l1[i]:
#                 if type(x) == type([]):
#                     for y in x:
#                         if type(y) == type([]):
#                             pass
#                         elif type(y) != type([]):
#                             a.append(y)
#                 elif type(x) != type([]):
#                     a.append(x)
#         elif type(l1[i]) != type([]):
#             a.append(l1[i])
#
#     print(a)
#
#
# l1 = [[6, 4, 7, [9, 5, 4, [2, 4, 8]]], [2, 2, 7], [9, 0, 7, [9, 3, 1, 8, 5]]]
# fun1(l1)
# OR
# def fun1(l):
#     a = []
#     for x in l:
#         if type(x) != type(list()):
#             a.append(x)
#         elif type(x) == type(list()):
#             for x1 in x:
#                 if type(x1) != type(list()):
#                     a.append(x1)
#                 elif type(x1) == type(list()):
#                     for x2 in x1:
#                         if type(x2) != type(list()):
#                             a.append(x2)
#                         elif type(x2) == type(list()):
#                             for x3 in x2:
#                                 if type(x3) != type(list()):
#                                     a.append(x3)
#     print(a)
# l = [[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]]
# fun1(l)

### Given a list and a integers N. At every nth reverse the list
# n = 3, input: [1,2,3,4,5,6,7,8], output = [3,2,1,6,5,4,8,7]

# def fun1(l, n):
#     ln = len(l)
#     f = []
#     while ln >= n:
#         a = []
#         for i in range(0, n):
#             a.append(l[i])
#         a.reverse()
#         del l[0:n]
#         ln = ln - n
#         f.extend(a)
#
#     if ln <= n:
#         l.reverse()
#         f.extend(l)
#
#     print(f)
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 3
# fun1(l, n)
# OR
# def fun1(l, n):
#     a = []
#     while len(l) >= n:
#         x = l[0:n]
#         x.reverse()
#         a.extend(x)
#         del l[0:n]
#     else:
#         l.reverse()
#         a.extend(l)
#
#     print(a)
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 3
# fun1(l, n)

### Find if Given number is power of 2 or not. More specifically, find if given number can be expressed as 2^k where k >= 1.
#
# def fun1(num):
#     for i in range(0, 100):
#
#         if 2 ** i == num:
#             print(f"The given number is {i} power of 2")
#
#
# num = 32
# fun1(num)

### Write a Python script to sort (ascending and descending) a dictionary by value

# def flipdict(d):
#     f = {}
#     for x, y in d.items():
#         f[y] = x
#
#     return f
#
#
# def fun1(d):
#     mydict = {}
#     fd = flipdict(d)
#     fdkeys = list(fd.keys())
#     sortfdkeys = sorted(fdkeys, reverse=True)  # for ascending delete reverse = True
#     for x in sortfdkeys:
#         mydict[x] = fd[x]
#
#     return flipdict(mydict)
#
#
# d = {'a': 4, 'h': 3, 'k': 1, 'l': 2}
# print(fun1(d))

### Write a Python script to add a key to a dictionary.

# def addkeyvalue(key, value, d):
#     d[key] = value
#
#     return d
#
#
# d = {0: 10, 1: 20}
# key = 2
# value = 30
# print(addkeyvalue(key, value, d))

### Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def con(d1, d2, d3):
#     newd = {}
#     for key in d1:
#         newd[key] = d1[key]
#
#     for key in d2:
#         newd[key] = d2[key]
#
#     for key in d3:
#         newd[key] = d3[key]
#
#     return newd
#
#
# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
# print(con(d1, d2, d3))

### Write a Python script to check whether a given key already exists in a dictionary

# def check(dkey, d):
#     result = 0
#     for key in d:
#         if key == dkey:
#             print("Yes")
#             result = 1
#
#     if result == 0:
#         print("No key does not exists in the dictionary")
#
#
# d = {'a': 1, 'b': 2}
# dkey = 'b'
# check(dkey, d)

### Write a Python program to iterate over dictionaries using for loops

# def fun1(d):
#     for key, value in d.items():
#         print(key, value, end='  ')
#
#
# d = {'a': 1, 'b': 2}
# fun1(d)

###Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# def dicttest(n):
#     f = {}
#     for i in range(1, n + 1):
#         f[i] = i * i
#
#     print(f)
#
# n = 5
# dicttest(n)

###Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# def dictsquare(n1, n2):
#     f = {}
#     for i in range(n1, n2 + 1):
#         f[i] = i ** 2
#
#     print(f)
#
# n1 = 1
# n2 = 15
# dictsquare(n1, n2)

###Write a Python script to merge two Python dictionaries.
# def mergedict(d1, d2):
#     newdict = {}
#     for x in d1:
#         newdict[x] = d1[x]
#     for y in d2:
#         newdict[y] = d2[y]
#
#     return newdict
#
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# print(mergedict(d1, d2))

###Write a Python program to sum all the values/keys/items in a dictionary
# def summing(d):
#     sumkey = 0
#     sumvalue = 0
#
#     for x in d:
#         sumkey = sumkey + x
#     print(f"sum of keys in the dict is {sumkey}")
#
#     for key in d:
#         sumvalue = sumvalue + d[key]
#     print(f"sum of keys in the dict is {sumvalue}")
#
#     sumitems = sumkey + sumvalue
#     print(f"sum of keys in the dict is {sumitems}")
#       OR
#     sumitems = 0
#     for x,y in d.items():
#       sumitems = sumitems + x + y
#     print( f"sum of keys in the dict is {sumitems}"
#
# d = {1: 2, 3: 4, 5: 6, 7: 8}
# summing(d)

###Write a Python program to multiply all the keys/values/items in a dictionary
# def multi(d):
#     multikeys = 1
#     multivalues = 1
#     multiitems = 1
#     for key in d:
#         multikeys = multikeys * key
#
#     for key in d:
#         multivalues = multivalues * d[key]
#
#     for key, value in d.items():
#         multiitems = multiitems * key * value
#
#     print(multikeys)
#     print(multivalues)
#     print(multiitems)
#
#
# d = {1: 2, 2: 3, 3: 4}
# multi(d)

###Write a Python program to remove a key from a dictionary.
# def fun1(key, d):
#     # del d[key]
#     d.pop(key)
#
#     # print(d)
#     print(d)
#
# key = 'a'
# d = {'b': 2, 'a': 3}
# fun1(key, d)

###Write a Python program to map two lists into a dictionary.
# def dictfromlist(l1,l2):
#     newdict = dict(zip(l1,l2))
#     print(newdict)
#
# l1 = [1,2]
# l2 = [3,4]
# dictfromlist(l1,l2)

###Write a Python program to sort a dictionary by key.
# def fun1(d):
#     newd = {}
#     # find keys list
#     # sort keys list
#     # make new dict
#     listkeys = list(d.keys())
#     sortlistkeys = sorted(listkeys)
#
#     for x in sortlistkeys:
#         newd[x] = d[x]
#
#     print(newd)
#
# d = {1: 'a', 3: 'c', 2: 'd'}
# fun1(d)

###Write a Python program to get the maximum and minimum value in a dictionary.
# def dictmaxminvalue(d):
#     listvalues = list(d.values())
#     maxvalue = max(listvalues)
#     minvalue = min(listvalues)
#
#     print(f"The max value is dictionary is {maxvalue}")
#     print(f"The min value is dictionary is {minvalue}")
#
#
# d = {1: 3, 2: 4, 4: 5, 3: 1}
# dictmaxminvalue(d)

###Write a Python program to remove duplicates from Dictionary.[key in a dictionary should be unique,If a key needs to store multiple values, then the value associated with the key should be a list or another dictionary.]
# def fun1(d):
#     f = {}
#     for x in d:
#         if x not in f:
#             f[x] = d[x]
#
#     print(f)
#
#
# d = {1: 2, 2: 3, 2: 3, 4: 5, 1: 2, 1: 4}
# fun1(d)

###Write a Python program to check a dictionary is empty or not.
# def check(d):
#     d2 = {}
#
#     if d == d2:
#         print("Yes it is an empty dictionary")
#
#     elif d != d2:
#         print("No it is not an empty dictionary")
#
#
# d = {1: 2}
# check(d)

###Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# def dictnew(d1, d2):
#     new = {}
#     for x in d1:
#         if x in d2:
#             v = d1[x] + d2[x]
#             new[x] = v
#         elif x not in d2:
#             new[x] = d1[x]
#     for y in d2:
#         if y not in new:
#             new[y] = d2[y]
#
#     print(new)
#
#
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# dictnew(d1, d2)

###Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
#
# def test(d):
#     a = []
#     for x in d:
#         for key in x:
#             a.append(x[key])
#
#     uniq = []
#
#     for x in a:
#         if x not in uniq:
#             uniq.append(x)
#
#     print(uniq)
#
#
# d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# test(d)
# OR:
# def fun1(l):
#     a = []
#     for x in l:
#         for key in x:
#             if x[key] not in a:
#                 a.append(x[key])
#     print(a)
# l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# fun1(l)


### Write a Python program to find the highest 3 values in a dictionary.
# def fun1(d):
#     listvalues = list(d.values())
#     newlist = sorted(listvalues, reverse=True)
#     print(newlist[0:3])
#
#
# d = {1: 2, 3: 4, 5: 6, 2: 3, 6: 9}
# fun1(d)

### Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# def fun1(d):
#     fd = {}
#     for i in range(0, len(d)):
#         if d[i]['item'] in fd:
#             v = d[i]['amount'] + fd[d[i]['item']]
#             fd[d[i]['item']] = v
#         elif d[i]['item'] not in fd:
#             fd[d[i]['item']] = d[i]['amount']
#
#     print(fd)
#
#
# d = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750}
# ]
#
# fun1(d)
# OR
# def fun1(d):
#     fd = {}
#     for i in range(0,len(d)):
#         k = d[i]['item']
#         v = d[i]['amount']
#         if k not in fd:
#             fd[k] = v
#         elif k in fd:
#             v2 = fd[k] + v
#             fd[k] = v2
#
#     print(fd)
# d = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# fun1(d)


### Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# def fun1(s):
#     d = {}
#
#     for x in s:
#         d[x] = s.count(x)
#
#     print(d)
#
#
# s = 'w3resource'
# fun1(s)

###Write a Python program to count the values associated with key in a dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True
#
# def fun1(d, key, value):
#     c = 0
#
#     for x in d:
#         if x[key] == value:
#             c = c + 1
#     print(f"Count of '{value}' associated with key '{key}' is {c}")
#
#
# d = [
#     {'id': 1, 'success': True, 'name': 'Lary'},
#     {'id': 2, 'success': False, 'name': 'Rabi'},
#     {'id': 3, 'success': True, 'name': 'Alex'},
#     {'id': 4, 'success': True, 'name': 'Alexy'}
# ]
# key = 'success'
# value = True
# fun1(d, key, value)

###Write a Python program to sort a list alphabetically in a dictionary.
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# output = {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
# def fun1(d):
#     fd = {}
#     for x in d:
#         item = d[x]
#         item.sort()
#         fd[x] = item
#
#     print(fd)
#
#
# d = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# fun1(d)

###Write a Python program to remove spaces from dictionary keys.
# d = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# output = {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
# def fun1(d):
#     fd = {}
#     for x in d:
#         x1 = x.replace(" ", "")
#         fd[x1] = d[x]
#
#     print(fd)
#
#
# d = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# fun1(d)

###Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# def flip(d):
#     fd = {}
#     for x, y in d.items():
#         fd[y] = x
#
#     return fd
#
#
# def fun1(d, n):
#     myfd = flip(d)
#     myfdkey = list(myfd.keys())
#     myfdkeysorted = sorted(myfdkey, reverse=True)
#     myfdfinal = {}
#     for x in myfdkeysorted:
#         myfdfinal[x] = myfd[x]
#     final = flip(myfdfinal)
#     print(final)
#
#     count = 0
#     for x, y in final.items():
#         if count < n:
#             print(x, y)
#             count = count + 1
#
#
# d = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
# n = 3
# fun1(d, n)

### Write a Python program to count number of items in a dictionary value that is a list.
# def fun1(d):
#     listvalues = list(d.values())
#
#     c = 0
#     for x in listvalues:
#         for item in x:
#             c = c + 1
#
#     print(c)
#
#
# d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# fun1(d)

### Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

# def flipdict(d):
#     fd = {}
#     for x, y in d.items():
#         fd[y] = x
#
#     return fd
#
#
# def counterdict(d):
#     myfd = flipdict(d)
#     result = {}
#     keylist = list(myfd.keys())
#     sortedkeylist = sorted(keylist, reverse=True)
#     for x in sortedkeylist:
#         result[x] = myfd[x]
#
#     finalresult = flipdict(result)
#     print(finalresult)
#
#     l = []
#     for x, y in finalresult.items():
#         t = (x, y)
#         l.append(t)
#     print(l)
#
#
# d = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
# counterdict(d)

### Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
#
# def fun1(l1, l2):
#     k = dict(zip(l1, l2))
#     print(k)
#
# l1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# l2 = [1, 2, 2, 3]
# fun1(l1, l2)
# OR:
# def fun1(l1, l2):
#     f = {}
#     for i in range(0, len(l1)):
#         if l1[i] not in f:
#             f[l1[i]] = l2[i]
#         elif l1[i] in f:
#             v = [f[l1[i]], l2[i]]
#             f[l1[i]] = v
#
#     print(f)
# l1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-V']
# l2 = [1, 2, 2, 3, 1]
# fun1(l1, l2)

###  Write a Python program to replace dictionary values with their average.
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# def fun1(d):
#     newlist = []
#     for i in range(0, len(d)):
#         new = {}
#         v1 = d[i]['V']
#         v2 = d[i]['VI']
#         v = (v1 + v2) / 2
#         new['id'] = d[i]['id']
#         new['subject'] = d[i]['subject']
#         new['V+VI'] = v
#         newlist.append(new)
#
#     print(newlist)
#
# d = [
#     {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
#     {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
#     {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
# ]
# fun1(d)

###  Write a Python program to match key values in two dictionaries.
# Sample dictionary: d1 = {'key1': 1, 'key2': 3, 'key3': 2},d2 = {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both d1 and d2

# def fun1(d1, d2):
#     for x in d1:
#         if x in d2:
#             if d2[x] == d1[x]:
#                 print(f"{x} : {d1[x]} is present in both d1 and d2")
#
#
# d1 = {'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# fun1(d1, d2)

### Write a Python program to store a given dictionary in a json file.
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

# import json
#
#
# def fun1(d):
#     j = json.dumps(d)
#     # print(type(j))
#     f = json.loads(j)
#
#     print(f)
#
#
# d = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'},
#                   {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
#      'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# fun1(d)

### Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
#Output:
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

# d = {}
# l1 = []
# l2 = []
# l3 = []
# for x in range(11,20):
#     l1.append(x)
# for y in range(21,30):
#     l2.append(y)
# for z in range(31,40):
#     l3.append(z)
# d['x'] = l1
# d['y'] = l2
# d['z'] = l3
# # Now access the fifth value of each key from the dictionary.
# print(d['x'][4])
# print(d['y'][4])
# print(d['z'][4])
# print(f"x has value {d['x']}")
# print(f"y has value {d['y']}")
# print(f"z has value {d['z']}")

### Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
# def fun1(d):
#     a = []
#     for x in d:
#         if d[x] == None:
#             a.append(x)
#
#     for x in a:
#         del d[x]
#
#     print(d)
#
# d = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': None}
# fun1(d)

### Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
# def fun1(d):
#     fd = {}
#     for x in d:
#         if d[x] > 170:
#             fd[x] = d[x]
#
#     print(fd)
#
# d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# fun1(d)

### Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
# def fun1(l1, l2, l3):
#     l = []
#     for i in range(0, len(l1)):
#         d = {}
#         d1 = {}
#         d1[l2[i]] = l3[i]
#         d[l1[i]] = d1
#         l.append(d)
#
#     print(l)
#
# l1 = ['S001', 'S002', 'S003', 'S004']
# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3 = [85, 98, 89, 92]
# fun1(l1, l2, l3)

### Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
# def fun1(d,h,w):
#     a = {}
#     for x in d:
#         if d[x][0] >= 6.0 and d[x][1] >= 70:
#             a[x] = d[x]
#             print(a)
#
# d = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# h = 6
# w = 70
# fun1(d,h,w)

### Write a Python program to check all values are same in a dictionary.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
# def checkvalue(d, v):
#     n = len(d)
#     c = 0
#     for x in d:
#         if d[x] == v:
#             c = c + 1
#
#     if c == n:
#         return True
#     elif c != n:
#         return False
#
#
# d = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# v = 12
# print(checkvalue(d, v))

### Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w'
# Expected Result : Empty String

# def fun1(s):
#     n = len(s)
#     if n > 2:
#         slice1 = s[0:2]
#         slice2 = s[n-2:n]
#         fs = slice1 + slice2
#
#         result = fs
#     elif n < 2:
#         result = "Empty String"
#     return result
#
# s = 'w3resource'
# print(fun1(s))

### Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
# def fun1(s):
#     l = list(s)
#     l1 = l[0]
#     for i in range(1, len(l)):
#         if l[i] == l1:
#             l[i] = '$'
#
#     print(l)
#     print(''.join(l))
#
#
# s = 'restart'
# fun1(s)

### Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# def fun1(s1,s2):
#     l1 = list(s1)
#     l2 = list(s2)
#     x = l1[0:2]
#     y = l2[0:2]
#     l1[0:2] = y
#     l2[0:2] = x
#     fs1 = ''.join(l1)
#     fs2 = ''.join(l2)
#     fs = fs1 + ' ' + fs2
#     print(fs)
# s1 = 'abc'
# s2 = 'xyz'
# fun1(s1,s2)

### Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
# def fun1(s):
#     # add 'ing' at the end of a given strin, if len is > 3
#     # If the given string already ends with 'ing' then add 'ly' instead
#     # If the string length of the given string is less than 3, leave it unchanged
#     n = len(s)
#     if n >= 3:
#         if s[n - 3: n] == 'ing':
#             print(s + 'ly')
#         elif s[n - 3: n] != 'ing':
#             print(s + 'ing')
#
#     elif n < 3:
#         print(s)
#
#
# s = 'string'
# fun1(s)

### Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
# def fun1(s):
#     s1 = s.find('not')
#     # d1 = s.index('not')
#     s2 = s.find('poor')
#     if s1 < s2:
#         s3 = s.replace(s[s1:s2+4], 'good')
#     if s1 == -1:
#         return s
#     return s3
#
# s = 'The lyrics is not that poor!'
# print(fun1(s))

###  Write a Python function that takes a list of words and returns the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
# def fun1(l):
#     longword = []
#     for x in l:
#         n = len(x)
#         longword.append(n)
#     m = max(longword)
#     i = longword.index(m)
#     print(f"Longest word: {l[i]}")
#     print(f"Length of the longest word: {m}")
#
# l = ["PHP", "Exercises", "Backend"]
# fun1(l)
# OR
# def longest(s):
#     maxl = 0
#     for item in s:
#         l = len(item)
#         maxl = max(l,maxl)
#     print(maxl)
# s = ['string','longinging','longest']
# longest(s)

###  Write a Python program to remove the nth index character from a nonempty string.
# def fun1(s,n):
#     l = list(s)
#     l.pop(n)
#     f = ''.join(l)
#
#     return f
# s = "hello"
# n = 3
# print(fun1(s,n))

###  Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# def fun1(s):
#     l = list(s)
#     x = l[0]
#     y = l[len(l) - 1]
#
#     l[0] = y
#     l[len(l) - 1] = x
#     print(''.join(l))
# s = "everyday"
# fun1(s)

###  Write a Python program to remove the characters which have odd index values of a given string.
# def fun1(s):
#     l = list(s)
#     a = []
#     for i in range(0, len(l)):
#         if i % 2 != 0:
#             a.append(l[i])
#
#     for x in l:
#         if x in a:
#             l.remove(x)
#     print(''.join(l))
#
# s = "allaboard"
# fun1(s)

###  Write a Python program to count the occurrences of each word in a given sentence.
# def fun1(s):
#     l = s.split()
#     d = {}
#     for x in l:
#         y = l.count(x)
#         d[x] = y
#
#     print(d)
#
#
# s = "hello how are you how"
# fun1(s)

### Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# def fun1():
#     s = input("please enter a string : ")
#     print(f"Upper case for the input string is {s.upper()}")
#     print(f"Lower case for the input string is {s.lower()}")
# fun1()

### Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, black, pink, green
# Expected Result : black, green, pink, red
# def fun1():
#     d = input("Please input comma separated words:")
#     l = d.split(',')
#     l.sort()
#     fd = ','.join(l)
#     return fd
# print(fun1())

### Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# # insert_end('Exercises') -> eseseses
# def fun1(s):
#     if len(s) >= 2:
#         l = len(s)
#         last = s[l-2: l]
#         print(last*4)
#     else:
#         print(s)
# s = "hello"
# fun1(s)

### Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
# def fun1(s):
#     if len(s) < 3:
#         return s
#     elif len(s) >= 3:
#             fs = s[0:3]
#             return fs
# print(fun1('py'))

### Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
# s = 'https://www.w3resource.com/python-exercises/string'
# l = s.rsplit('/',1)
# a = s.rsplit('-',1)
# print(l[0])
# print(a[0])

### Write a Python function to reverses a string if it's length is a multiple of 4.
# def fun1(s):
#     if len(s) % 4 == 0:
#         print(s[:: -1])
# s = "hellollo"
# fun1(s)
#OR
# def fun1(s):
#     if len(s)%4 == 0:
#         l = list(s)
#         l.reverse()
#         print(''.join(l))
#     elif len(s)%4 != 0:
#         print(s)
# s = "rtghtyu"
# fun1(s)

# ### Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
# def fun1(s):
#     s1 = s[0:4]
#     c = 0
#     for x in s1:
#         if x.isupper() == True:
#             c = c + 1
#     if c >= 2:
#         fs = s.upper()
#         print(fs)
#     elif c < 2:
#         print("Not valid for conversion")
# s = "hELlomy"
# fun1(s)

### Write a Python program to remove a newline in Python.
# s = 'Python Exercises\n'
# print(s)
# print(s.rstrip())

### Write a Python program to check whether a string starts with specified characters.
# def fun1(s,c):
#     if s[0] == c:
#         print(f"The string starts with {c}")
#     elif s[0] != c:
#         print(f"The string does not start with {c}")
# s = "hello"
# c = 'e'
# fun1(s,c)

### Write a Python program to remove existing indentation from all of the lines in a given text.
# s = "hello:hi:how:are:you"
# s2 = s.replace(':',' ')
# print(s2)

### Write a Python program to sum all the items in a list.
# def fun1(l):
# #     s = sum(l)
# #     return s
# # l = [1,4,5]
# # print(fun1(l))

### Write a Python program to multiplies all the items in a list.
# def fun1(l):
#     m = 1
#     for x in l:
#         m = x*m
#     print(m)
# l = [4,5]
# fun1(l)

### Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# def fun1(l):
#     a = []
#     for x in l:
#         if len(x) >= 2:
#             a.append(x)
#     c = 0
#     for x in a:
#         if x[0] == x[len(x)-1]:
#             c = c + 1
#     print(c)
# l = ['abc', 'xyz', 'aba', '1221']
# fun1(l)

###  Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def flip(l):
#     fl = []
#     for x in l:
#         lx = list(x)
#         a = lx[0]
#         b = lx[1]
#         lx[0] = b
#         lx[1] = a
#         t = tuple(lx)
#         fl.append(t)
#     return fl
# l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # flip(l)
# def sortlist(l):
#     mylist = flip(l)
#     mylist.sort()
#     finallist = flip(mylist)
#     print(finallist)
# sortlist(l)

### Write a Python program to remove duplicates from a list.
# l = [1,2,3,12,3,2,2]
# a = []
# for x in l:
#     if l.count(x) == 1:
#         a.append(x)
#     elif l.count(x) > 1:
#         if x not in a:
#             a.append(x)
# print(a)
##OR
# def fun1(l):
#     for item in l:
#         if l.count(item) > 1:
#             l.remove(item)
#     print(l)
# l = [1, 2, 3, 12, 3, 2, 2]
# fun1(l)

# Write a Python program to find the list of words that are longer than n from a given list of words.
# def fun1(l):
#     a = []
#     for x in l:
#         if len(x) >= n:
#             a.append(x)
#     print(a)
# l = ["orange","red","lemoned"]
# n = 6
# fun1(l)

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# def fun1(l):
#     x = []
#     a = l[0]
#     b = l[4]
#     c = l[5]
#     x.extend([a,b,c])
#     print(x)
#     for item in x:
#         l.remove(item)
#     print(l)
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# fun1(l)
# OR:
# def fun1(l):
#     a = []
#     for i in range(0, len(l)):
#         if i in (0, 4, 5):
#             a.append(l[i])
#     for item in a:
#         l.remove(item)
#     print(l)
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'orange']
# fun1(l)

# l = [3,5,4,1], find misiing i.e. 2
# l = [3,5,4,1,0]
# for i in range(0,6):
#     if i not in l:
#         print(i)

#### l = ['flowing', 'flower', 'flight'], find common prefix
# def fun1(l):
#     a = []
#     # break words into groups using `zip` and `*`
#     # ["flower","flow","flight"] becomes:
#     # (('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g'))
#     for item in zip(*l):
#         a.append(item)
#     prefix = []
#     for item in a:
#         if len(item) == item.count(item[0]):
#             prefix.append(item[0])
#     print(prefix)
#
#
# l = ['flowing', 'flower', 'flight']
# fun1(l)

### Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# def fun1(l):
#     for item in l:
#         if item == 0:
#             l.remove(0)
#             l.append(0)
#     print(l)
# l = [0,1,0,3,12]
# fun1(l)
## OR
# def nonzero(l):
#     a = []
#     # append all non zero
#     for item in l:
#         if item != 0:
#             a.append(item)
#
#     # then append all zero
#     for item in l:
#         if item == 0:
#             a.append(item)
#
#     print(a)
# l = [0, 1, 0, 3, 12]
# nonzero(l)

###Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# def fun1(l):
#     a = []
#     for item in l:
#         if item%2 == 0:
#             a.append(item)
#     for item in l:
#         if item%2 != 0:
#             a.append(item)
#     print(a)
# l = [3,1,2,4]
# fun1(l)

###Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array.
# Input: [4,3,2,7,8,2,3,1]
# Output: [5,6]
# def fun1(l):
#     a = []
#     for i in range(1,len(l)+1):
#         if i not in l:
#             a.append(i)
#     print(a)
# l = [4,3,2,7,8,2,3,1]
# fun1(l)

###Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. Return the number of negative numbers in grid.
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# def fun1(l):
#     a = []
#     for item in l:
#         for x in item:
#             if x < 1:
#                 a.append(x)
#     print(len(a))
# l = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# fun1(l)

###Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even. Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# def fun1(l):
#     even = []
#     odd = []
#     for item in l:
#         if item%2 == 0:
#             even.append(item)
#     for item in l:
#         if item%2 != 0:
#             odd.append(item)
#     i = 0
#     for item in even:
#         odd.insert(i,item)
#         i = i + 2
#     print(odd)
# l = [4,2,5,7]
# fun1(l)

###Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create. You can return the output in any order.
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# def fun1(s):
#     upper_s = []
#     lower_s = []
#
#     for i in range(0, len(s)):
#         upper_s.append(s[i].upper())
#         lower_s.append(s[i].lower())
#
#     print(''.join(upper_s), ''.join(lower_s), end=" ")
#
#     half = []
#     for i in range(len(s) // 2, len(s)):
#         half.append(s[i].upper())
#     strhalf = ''.join(half)
#     full1 = s[0:len(s) // 2] + strhalf
#
#     otherhalf = []
#     for i in range(0, len(s) // 2):
#         otherhalf.append(s[i].upper())
#     strotherhalf = ''.join(otherhalf)
#     full2 = strotherhalf + s[len(s) // 2:len(s)]
#
#     print(full1, full2)
# s = "a1b2"
# fun1(s)
# ## OR
# def transform(s):
#     # all letter lowercase
#     lower = s.lower()
#     print(lower)
#
#     # all letter uppercase
#     upper = s.upper()
#     print(upper)
#
#     # left half uppercase + right half lowercase
#     m = len(s) // 2
#     # print(m)
#     left = s[0:m]
#     right = s[m:len(s)]
#     upperlower = left.upper() + right.lower()
#     print(upperlower)
#
#     # right half uppercase + lft half uppercase
#     lowerupper = left.lower() + right.upper()
#     print(lowerupper)
#
#     l = []
#     l.append(lower)
#     l.append(upper)
#     l.append(upperlower)
#     l.append(lowerupper)
#     print(l)
# s = "a1b2"
# transform(s)

###Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# def fun1(s):
#     a = []
#     b = []
#     c = []
#     for i in range(0, len(s)):
#
#         if s.count(s[i]) == 2:
#             a.append(s[i])
#     elif s.count(s[i]) < 2:
#     b.append(s[i])
#
# elif s.count(s[i]) > 2:
# c.append(s[i])
# print(a, b, c)
#
# l = []
# l.extend(a)
# l.insert(1, c)
# print(l)
# l1 = []
# for item in l:
#
#     if type(item) == type([]):
#         l1.extend(item)
#     elif type(item) != type([]):
#         l1.append(item)
#
# mid = len(l1) // 2
# l1.insert(mid, b[0])
# print(''.join(l1))
# print(len(l1))
# s = "abccccdd"
# fun1(s)
## OR
# def funpalindrome(s):
#     l = list(s)
#     print(l)
#     # find letters that have count 2
#     count2 = []
#     for item in l:
#         if l.count(item) >= 2:
#             if item not in count2:
#                 count2.append(item)
#     print(count2)
#
#     # find letters that are unique, i.e. count is 1
#     unique = []
#     for item in l:
#         if l.count(item) < 2:
#             if item not in unique:
#                 unique.append(item)
#
#     print(unique)
#
#     # Now create a longest palindrome and check length
#     palindrome = []
#     for item in count2:
#         palindrome.append(item)
#
#     count2.reverse()
#     for item in count2:
#         palindrome.append(item)
#     print(palindrome)
#
#     mid = len(palindrome) // 2
#     palindrome.insert(mid, unique[0])
#     print(palindrome)
#     print(len(palindrome))
# s = "ababDefe"
# funpalindrome(s)

### Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can. Return the final string after all such duplicate removals have been made.
# It is guaranteed the answer is unique.
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         # find the item having count more than 2
#         # if adjacent delete
#         l = list(S)
#         a = []
#         for item in l:
#             if item not in a:
#                 if l.count(item) >= 2:
#                     a.append(item)
#         # print(a)
#         for item in a:
#             i = l.index(item)
#             if l[i + 1] == item:
#                 # print(l[i],l[i+1])
#                 l.pop(i)
#                 l.pop(i)
#                 a.remove(item)
#                 if len(a) > 0:
#                     for item in a:
#                         i = l.index(item)
#                         if l[i + 1] == item:
#                             # print(l[i],l[i+1])
#                             l.pop(i)
#                             l.pop(i)
#                             a.remove(item)
#                 elif len(a) == 0:
#                     break
#
#         return ''.join(l)
# OR
# def fun1(s):
#     l = list(s)
#     print(l)
#
#     # find the letters that hv count more than 1
#     dup = []
#     for item in l:
#         if item not in dup:
#             if l.count(item) > 1:
#                 dup.append(item)
#     print(dup)
#     # find the adjacent and equal letter and remove
#     for item in dup:
#         i = l.index(item)
#         if l[i] == l[i + 1]:
#             del l[i]
#             del l[i]
#     print(l)
#
#     for item in dup:
#         if item in l:
#             i = l.index(item)
#             if l[i] == l[i + 1]:
#                 del l[i]
#                 del l[i]
#     print(l)
# s = "baabcdee"
# fun1(s)

