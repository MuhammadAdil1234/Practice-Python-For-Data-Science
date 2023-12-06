#!/usr/bin/env python
# coding: utf-8

# In[1]:


1


# In[2]:


3+4*7-3


# In[3]:


# It is all about data types in Pyhon


# In[4]:


# NUMBERS


# In[5]:


var = 5


# In[6]:


var


# In[7]:


var = var + 6


# In[8]:


var


# In[9]:


var = var + var


# In[12]:


var


# In[13]:


var_second = var * 2
var_second


# In[11]:


# strings


# In[14]:


str = "Muhammad Adil"


# In[15]:


print(str)


# In[18]:


# string formating 
name = "Muhammad Adil"
age = 23
detail = 'My name is {} and my age is {}'.format(name, age)


# In[17]:


print(detail)


# In[20]:


# string formating 
name = "Faisal"
age = 24
detail = 'My name is {name} and my age is {age}. And I am {prog}'.format(name=name, age=age, prog="programmer")
print(detail)


# In[21]:


# indexing of string
name = 'pythoncode'
name[0:]


# In[22]:


name[3:6]


# In[23]:


name[0:3]


# In[24]:


# list
mylist = ["apple", "banana", "cherry"]
print(mylist)


# In[32]:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]


# In[26]:


print(len(thislist))


# In[27]:


list1 = ["abc", 34, True, 40, "male"]
print(type(list1))


# In[28]:


print(type(thislist))


# In[31]:


#indexinf in list
print(thislist[-2])


# In[33]:


print(thislist[1:4])


# In[34]:


thislist[1]='Adil'


# In[35]:


print(thislist)


# In[36]:


thislist.insert(2, "watermelon")
print(thislist)


# In[37]:


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# In[38]:


thislist = ["apple", "banana", "cherry", ['adil', 'faisal', 'aqeel']]
print(thislist[3][0])


# In[39]:


# dictioneries 
dic = {'first': 'python', 'second':'programming', 'third': 'practice'}
dic.keys()


# In[40]:


dic.values()


# In[42]:


dic['second']


# In[45]:


# Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : [2000, 2001, 2003]
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["year"][2])


# In[51]:


# Tuples
x = ("apple", "banana", "cherry")

print(x)


# In[47]:


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# In[55]:


print(thistuple[1])


# In[49]:


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# In[52]:


# set
thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[53]:


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# In[56]:


thisset


# In[57]:


# if statements and conditions
if 1==1:
    print('I am Adil')


# In[58]:


if 3==2:
    print('python')
elif 4!=5:
    print('programming')


# In[59]:


if 3==2:
    print('python')
elif 4==5:
    print('programming')
else:
    print('OK!')


# In[60]:


#Nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# In[ ]:




