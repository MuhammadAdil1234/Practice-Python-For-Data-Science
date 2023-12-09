#!/usr/bin/env python
# coding: utf-8

# In[26]:


f = open('file.txt', 'a')


# In[21]:


# print(f.read())
# for x in f:
#   print(x)
print(f.readline()) # line by line reading
print(f.readline())


# In[30]:


# write something in file
f = open('file.txt', 'a')
f.write("Now the file has more content!")
f.close()
#read the file after the appending:
f = open("file.txt", "r")
print(f.read())


# In[32]:


# create a file
f = open("newfile.txt", "w")


# In[33]:


# create another file
f = open("anotherfile.txt", "w")


# In[34]:


# delete the file
import os
if os.path.exists("newfile.txt"):
  os.remove("newfile.txt")
else:
  print("The file does not exist")


# In[ ]:




