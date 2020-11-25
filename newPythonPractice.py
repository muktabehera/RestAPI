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

##Given number is prime number or not.
# class test():
#     def findprime(self):
#         num = 100
#         for x in range(2,num):
#             if x%2 == 0:
#                 print(f"The number {x} is not prime")
#             else:
#                 print(f"{x} is a prime number")
#
# t = test()
# t.findprime()

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
#     def printNtimes(self,str,n):
#         # str = "testing"
#         # n = 10
#         x=0
#         while x < n:
#             print(str)
#             x= x+1
#
#         print(str*n)
#
# a = test()
# str1= "hello every one"
# n1 = 3
# a.printNtimes(str1,n1)

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

# def smallernumbers(l):
#     r = []
#
#     for i in l:
#         s = 0
#         for j in l:
#             if i != j and j < i:
#                 s = s + 1
#         r.append(s)
#
#     print(r)
#
#
# l = [8, 1, 5, 6, 7]
# smallernumbers(l)

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