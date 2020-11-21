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

