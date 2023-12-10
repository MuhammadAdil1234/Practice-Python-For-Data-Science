#!/usr/bin/env python
# coding: utf-8


#classes in python
class first_class:
    x=5
#create an object to access class
obj = first_class()
print(obj.x)


# init function for class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)
"""Note: The __init__() function is called automatically every time the class is being used to create a new object.

"""



# we can also make own function in a class and acess these function with objects
class Person2:
  def __init__(self, name, age):
    """Note: The self parameter is a reference to the current instance of the class, 
       and is used to access variables that belong to the class."""
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc()


# Inheritance in classes 
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass  # Placeholder for the area calculation

    def display_info(self):
        print(f"This is a {self.color} shape.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def display_info(self):
        super().display_info()
        print(f"It's a circle with radius {self.radius}.")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_info(self):
        super().display_info()
        print(f"It's a rectangle with length {self.length} and width {self.width}.")

# Example Usage:
circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)

circle.display_info()
print("Area:", circle.area())

print("\n")

rectangle.display_info()
print("Area:", rectangle.area())



