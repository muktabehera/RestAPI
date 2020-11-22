#Note: https://docs.python.org/3/library/ ( you will find all the standard libraries/module)

def midnum(x):
    l = len(x)
    mid = int((l-1)/2)
    midvalue = x[mid]
    print("value of midnumber is %s" %midvalue)
    return midvalue

def firstnvalue(x,n):
    l = len(x)
    nvalues = x[:n]
    print("the first %s values are %s" %(n,nvalues))
    return nvalues

def listsort(x):
    x.sort()
    print("the sorted list is %r" %x)
    return x

def reverse(x):
    x.reverse()
    print("reversed list is %s" %x)
    return x

def append(x):
    x.append(7)
    print("appneded new list is %s" %x)
    return x

def insert(x,index,value):
    x.insert(index,value)
    print("the list after insert is %s" %x)
    return(x)



if __name__ == '__main__':
    mylist = [3,4,5,6,7,8,9,2,1,0]
    midnum(mylist)
    num = 5
    firstnvalue(mylist,num)
    listsort(mylist)
    reverse(mylist)
    append(mylist)
    myindex = 2
    myvalue = 8
    insert(mylist, myindex, myvalue)

# a = ['a','b','c','v','a','b']
# b = a.copy()
# print(b)

# Find the first non-recurring character in string
# def firstUniqChar(string) -> int:
#     seems = dict()
#     index = len(string)
#     c = ''
#     for i, char in string:
#         if char not in seems:
#             seems.setdefault(char, (i,1))
#         else:
#             seems[char] = (seems[char][0], seems[char][1] + 1)
#
#     for k, value in seems.items():
#         if value[1] == 1 and value[0] < index:
#             index = value[0]
#             c = k
#     return  index if c else -1


# import requests
# import json
# url = "https://hacker-news.firebaseio.com/v0/updates.json"
# response = requests.get(url)
# response.status_code
# response.text
# a = response.text
# res = json.loads(a)
# type(res) *dict
# res['items']

##LIST
# len() length of the list
    #len(list)
# append()	Adds an element at the end of the list
    #list.append('s')
# extend()	Add the elements of a list (or any iterable), to the end of the current list
    # f = ['d','f']
    # f.extend(['e', 'k'])
# insert()	Adds an element at the specified position (index,value)
   # thislist.insert(2, 'test')
# clear()	Removes all the elements from the list
    #list.clear()
# copy()	Returns a copy of the list or dictionary
    # thislist = ["apple", "banana", "cherry"]
    # mylist = thislist.copy()
    #OR
    # mylist = list(thislist) i.e. list()
# count()	Returns the number of elements with the specified value
   #thislist.count('s')
# index()	Returns the index of the first element with the specified value
   # thislist.index('a')
# pop()	    Pop's out the element at the specified position/index
    #f.pop(0)
# remove()	Removes the item with the specified value from list
    #f.remove('a')
    #print(f)
# reverse()	Reverses the order of the list
    #f.reverse()
# sort()	Sorts the list in Ascending order
    #f.sort()
# del() deletes the list
    #del(list)
# slicing works for both *string and *list
    # a = [1,2,3,4,5,6]
    #a[1:3] i.e. (1 is index, 3 is 3rd place) = [2,3] will be result
    #a[:3] = [1,2,3]

#list to string: ''.join(list)
    #list = ['a','b']
    #string = ''.join(list)
# string to list with split words: string.split(" ")
    #s = "sun is bright"
    #k = s.split(" ") or s.split()
# string to list with split char:   list(str)
    #str = "mom"
    #list(str) will give result ["m","o","m"]
# int to list:
    # x = 123
    # y = str(x)
    # z = list(y)
# string to int:
    # s = '123'
    # ints = int(s)


# if (string.find(sub_str) == -1): *string.find(sub_str, start, end)
#         print("NO")
#     else:
#         print("YES")
#dictionary: sorted(dict)

#Exception handling:::
# def exceptionhandling():
#   try:
        #car = {"make":"bmw", "year": 2000, "model" : "550i"}
        #print(car["color"])
#   except:
        #print("Key not found")
#   finally:
        #print("please try again with different key")



#A simple class:
# class myname():
    # def name(self):
        # print("myname is" + "tony")
# m = myname()
# m.name()

# convert a value to a boolean value(contains two values true and false) :
# a = "dfsfsf"
# b = bool(a)

##String##
## Replace , str.replace(old, new[, max])
    # s1 = "hello"
    # s1.replace('h','d')
    # s1.replace('ll','just')
## find , str.find(substring, start, end)
    # s2 = 'hello world now'
    # s1.find('world',2,-2) will search string within 'llo world n', note:index starts with 0. If substring exists returns index else returns -1
    # s1.find('hell',0,10)
## lower() / upper() , converts string to lower/upper
    # str = 'XYZ'
    # print(str.lower())
    # print(str.upper())
## string reverse using slicing
    #str = "ajklmnop"
    #rev = str[: : -1]
## string have also index starting from 0
    # str = "hello"
    #str[4] , result will be 'o'
## strings can be multiplied / Lists can be multiplied
    # s = "hello"
    # print(s*2) , will be hellohello
    # l = [1,2,3]
    # print(l*2) , will be [1, 2, 3, 1, 2, 3]
## concating string / concating list
    # s1 = "hello"
    # s2 = " world"
    # print(s1+s2), will be hello world
    # l1 = ['a','b']
    # l2 = ['c','d']
    # print(l1+l2), will be ['a', 'b', 'c', 'd']


##Dictionary
# Append to a dictionary:
    #dict = {}
    #dict["color"]="blue"
    # print(dict)
# find keys from dictionary:
    #dict = {'a':2,'b':3}
    #for x in dict:
        #print(x)
        #OR
     #dict.keys(), will return dict_keys(['a', 'b'])
# find values from dictionary:
    # dict = {'a':2,'b':3}
    # dict.values() , will return all values i.e. dict_values([2, 3])
    #OR
    #dict['a'] , will return value for key 'a'
# finding key for a particular value in dictionary:
    # my_dict ={"java":100, "python":112, "c":11}
    # key_list = list(my_dict.keys())
    # val_list = list(my_dict.values())
    # print(key_list[val_list.index(100)])
    # print(key_list[val_list.index(112)])


