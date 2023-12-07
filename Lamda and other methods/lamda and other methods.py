#!/usr/bin/env python
# coding: utf-8

# Map function 
"""applies on function for each item in the iterable like list, tuples"""

def add_two(num):
    return num + 2

first = [1, 2, 3, 4, 5]
# Using a different name for the function, e.g., 'add_two', to avoid conflicts
result = list(map(add_two, first))

print(result)


# lamda function / Anonymous function
f = lambda x : x*5
print(f(5))


ft = [1, 2, 3, 4, 5]
# Using a different name for the function, e.g., 'add_two', to avoid conflicts
result = list(map(lambda x : x+2, ft))

print(result)


ft = [1, 2, 3, 4, 5]
# Using a different name for the function, e.g., 'add_two', to avoid conflicts
result = list(filter(lambda x : x%2==0, ft))

print(result)


list = [1, 3, 5,7, 2, 9]
list.clear()



list2 = [1, 3, 5,7, 2, 9]
list2.append(6)


str = 'I am Muhammad Adil'
str.split()





