#!/usr/bin/env python
# coding: utf-8


# for loop
list = [1,2,3,4,5]
for num in list:
    print(num)


# we can also use range in loops
for num in range(6):
    print(num)



#list comprehensive 
#simple list conversion
firstlist = [2, 4, 6, 8]
firstlist[1]=firstlist[1]*2
secondlist = []
for i in firstlist:
    secondlist.append(i*2)
print(secondlist)

#complex list comprehensive
first = [2, 4, 6, 8]
second = [i*2 for i in first]
print(second)

# while loops
num = 6
while num < 12:
    print(num)
    num +=1

