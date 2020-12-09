# from collections import deque
#
# # Create linked lists
# linkb = deque('abc') # its same as deque(['a', 'b', 'c'])
# linkc = deque(['a','b','c'])
# linkd = deque([{'data': 'a'}, {'data': 'b'}])
#
# # append to linkedlist
# linkb.append('d')
# print(linkb)
#
# # delete right most last element from list
# linkb.pop()
# print(linkb)
#
# # add or remove elements from the left side, or head, of the list:
# linkb.popleft()
# print(linkb)
#
# # creating queue:[note - Queue is FIFO, first element getting in will get out]
# testqueue = deque()
# testqueue.append('red')
# testqueue.append('blue')
# testqueue.append('green')
# print(testqueue)
#
# # creating Stack:[note - Stack is LIFO, last in first out. Head is the last element on left ]
# teststack = deque()
# teststack.appendleft('first')
# teststack.appendleft('second')
# teststack.appendleft('third')
# print(teststack)
#
# # For removing items from a stack, use popleft() or pop()
# teststack.popleft()
#
# # traversing a linked list:
# for x in linkc:
#     print(x)

#Note  - All most all functions that an be done using list can be done on deque
# Deque : It is a linked list. double-ended queue