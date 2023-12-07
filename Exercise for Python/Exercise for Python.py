#!/usr/bin/env python
# coding: utf-8


"** What is 7 to the power of 4?**"
7**4


"""** Split this string:**

s = "Hi there Sam!"
**into a list. **"""

s = 'Hi there Sam'
s.split()



"""** Given the variables:**

planet = "Earth"
diameter = 12742
** Use .format() to print the following string: **

The diameter of Earth is 12742 kilometers."""

planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet,diameter))



"** Given this nested list, use indexing to grab the word hello **"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]



"""** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]




"""** Create a function that grabs the email website domain from a string in the form: **

user@domain.com
So for example, passing "user@domain.com" would return: domain.com"""

def get_email_domain(email):
    # Split the email address at the '@' symbol
    parts = email.split('@')
    print(parts[0])

    # Check if the email has the expected format
    if len(parts) == 2:
        print(len(parts))
        # Return the second part (domain)
        return parts[1]
    else:
        # Handle invalid email format
        return "Invalid email format"

# Example usage:
email_address = "user@domain.com"
result = get_email_domain(email_address)
print(result)




"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
"""
def find_dog(str):
    count=0
    lis = str.split()
    return 'dog' in lis # this is amazing and unique to find dog in the list

#     for i in range(0, len(lis)):
#         if lis[i]=='dog':
#             count+=1
#     print(count)
str = 'is there any dog here dog dog dog ?'
find_dog(str)




"""** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**"""
seq = ['soup','dog','salad','cat','great']

list(filter(lambda x: not x.startswith('s'), seq))




"""Final Problem
**You are driving a little too fast, and a police officer stops you.
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function)
-- on your birthday, your speed can be 5 higher in all cases. **"""

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <=60:
        return 'No ticket'
    elif speed >=61 and speed <=80:
        return 'Small ticket'
    elif speed>=80:
        return 'Big ticket'
caught_speeding(81,True)





