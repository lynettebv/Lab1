#!/usr/bin/env python3
import math

name = "Lynette Vandiepen"
age = 25
height = 5 + (5/12)
favorite_color = "Red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello: {name}, my age is {age}, my favorite color is {favorite_color}!")

print(f"Hello: {name}, my age is {age:05d}, my height is {height:.2f}, my favorite color is {favorite_color}!")

name = 'Lynette\'s Vandiepen' # example
name = "Lynette's Car" # example
name = """ Lynette's 
multi-line
string""" # example
name = "Lynette Vandiepen"

print(f"Hello: {name}, my age is {age}, my favorite color is {favorite_color}!")
print(f"Hello: {name}, my age is {age:05d}, my height is {height:.2f}, my favorite color is {favorite_color}!")

print(f"""name: {name}
age: {age}
height: {height:.2f}
favorite color: {favorite_color}
""")

# r = int(input("Enter a circle radius: "))
r = 5
circle_area = math.pi * math.pow(r, 2)
print(f"Circle Area with radius {r} is {circle_area:.1f}")

print(f"Square Root of my age is: {math.sqrt(age)}")

print(f"sin of height: {math.sin(height)}, cos of height: {math.cos(height)}")

print(f"Sum of age and 5: {age + 5}")
print(f"The difference between my height and 4 is {height - 4}")
print(f"The product of age and height is: {age * height}")
print(f"Quotient of height and 2 is: {height / 2}")
print(f"The remainder of age divided by 3 is: {age % 3}")
print(f"My age raised to the power of 2 is: {age ** 2}")
# age_raised_to_2 = age**2 -another way
# print(f"Age raised to the power of 2 {age_raised_to_2}") -another way to do it

temp_farenheit = float(input(f"{name} enter temperature in Farenheit: "))
celsius = (temp_farenheit - 32) * (5/9)
print(f"Temp Farenheit {temp_farenheit}°F in Celsius is {celsius}°C")