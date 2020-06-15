# 1) Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in  miles.

def miles_to_feet(miles):
    return miles * 5280

print(miles_to_feet(25))

# 2) Write a Python function total_seconds that takes three parameters hours, minutes and seconds and returns the total number of seconds for hours hours, minutes minutes and seconds seconds.

def total_seconds(hours,minutes,seconds):
    return((hours * 60 * 60) * (minutes * 60) * seconds)

print(total_seconds(7, 21, 37))

# 3) Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.

def rectangle_parimeter(width, height):
    return width * 2 + height * 2

print(rectangle_parimeter(4, 7))

# 4) Write a Python function rectangle_area that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the area of the rectangle in square inches.

def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 7))

# 5) Write a Python function circle_circumference that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the circumference of a circle with radius radius in inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π

import math
def circle_circumference(radius):
    return 2 * math.pi * radius

print(circle_circumference(8))

# 6) Write a Python function circle_area that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the area of a circle with radius radius in square inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(8))

# 7) Write a Python function future_value that takes three parameters present_value, annual_rate and years and returns the future value of present_value dollars invested at annual_rate percent interest, compounded annually for years years.

def future_value(present_value, annual_rate, years):
    return present_value * (1 + 0.01 * annual_rate) ** years

print(future_value(1000, 7, 10))

# 8) Write a Python function name_tag that takes as input the parameters first_name and last_name (strings) and returns a string of the form "My name is % %." where the percents are the strings first_name and last_name. Reference the test cases in the provided template for an exact description of the format of the returned string.

def name_tag(first_name, last_name):
    return f"My name is {first_name} {last_name}"

print(name_tag("Himal", "Sandaruwan"))

# 9) Write a Python function name_and_age that takes as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. Reference the test cases in the provided template for an exact description of the format of the returned string. 

def name_and_age(name, age):
    return f"{name} is {age} years old."

print(name_and_age("Himal", 25))

# 10) Write a Python function point_distance that takes as input the parameters x_0, y_0, x_1 and y_1, and returns the distance between the points (x_0,y_0) and (x_1,y_1)

def point_distance(x_0, y_0, x_1, y_1):
    return((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5

print(point_distance(2, 2, 5, 6))

# 11) Challenge: Write a Python function triangle_area that takes the parameters x_0, y_0, x_1, y_1, x_2, and y_2 (all numbers), and returns the area of the triangle with vertices (x_0,y_0), (x_1,y_1) and (x_2,y_2). (Hint: use the function point_distance as a helper function and apply Heron's formula.)

def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    a = point_distance(x_0, y_0, x_1, y_1)
    b = point_distance(x_0, y_0, x_2, y_2)
    c = point_distance(x_1, y_1, x_2, y_2)

    s = (a + b + c) / 2

    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(triangle_area(0, 0, 3, 4, 1, 1))

# 12)Challenge: Write a Python function print_digits that takes an integer number in the range (0,100), (i.e., at least 0, but less than 100) and prints the message "The tens digit is %, and the ones digit is %.", where the percent signs should be replaced with the appropriate values. (Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits. Note that this function should print the desired message, rather than returning it as a string.

def print_digits(number):
    """Prints tens digit number and ones digit number
    """    
    print(f"The tens digit is {number // 10} and the ones digit is {number % 10}")

print_digits(42)

# 13) Challenge:Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket with a specific number combination and, if the number on the ticket matches the numbers generated in a random drawing, the player wins a massive jackpot. Write a Python function powerball that takes no arguments and prints the message "Today’s numbers are %, %, %, %, and %. The Powerball number is %.". The first five numbers should be random integers in the range (1, 60) i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates. The Powerball number is a random integer in the range [1,36), i.e., at least 1 but less than 36. Note that this function should print the desired message, rather than returning it as a string.
import random
def powerball():
    print(f"Today’s numbers are {random.randrange(1, 60)}, {random.randrange(1, 60)}, {random.randrange(1, 60)}, {random.randrange(1, 60)}, and {random.randrange(1, 60)}. The Powerball number is {random.randrange(1, 36)}.")

powerball()