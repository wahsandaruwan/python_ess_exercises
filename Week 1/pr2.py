# =========Assignment Statements Practices============

# 1) Given a template that pre-defines a variable miles, write an assignment statement that defines a variable feet whose value is the number of feet in miles miles.

miles = 13
feet = miles * 5280
print(feet)

# 2) Given a template that pre-defines three variables hours, minutes and seconds, write an assignment statement that updates the variable total_seconds to have a value corresponding to the total number of seconds for hours hours, minutes minutes and seconds seconds.

hours = 7
minutes = 21
seconds = 37
total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
print(total_seconds)

# 3) Given a template that pre-defines the variables width and height that are the lengths of the sides of a rectangle, write an assignment statement that defines a variable perimeter whose value is the perimeter of the rectangle in inches.

width = 4
height = 7
perimeter = (width * 2) + (height * 2)
print(perimeter)

# 4) Given a template that pre-defines the variables width and height that are the lengths of the sides of a rectangle, write an assignment statement that defines a variable area whose value is the area of the rectangle in square inches.

width = 4
height = 7
area = width * height
print(area)

# 5) Given a template that pre-defines the constant PI and the variable radius corresponding to the radius of a circle in inches, write an assignment statement that defines a variable circumference whose value is the circumference of a circle with radius radius in inches.

PI = 3.14
radius = 8
circumference = 2 * PI * radius
print(circumference)

# 6) Given a template that pre-defines the constant PI and the variable radius corresponding to the radius of a circle in inches, write an assignment statement that defines a variable area whose value is the area of a circle with radius radius in square inches.

PI = 3.14
radius = 8
area = PI * radius ** 2
print(area)

# 7) Given the pre-defined variables present_value, annual_rate and years, write an assignment statement that define a variable future_value whose value is present_value dollars invested at annual_rate percent interest, compounded annually for years years.

present_value = 1000
annual_rate = 7 / 100
years = 10
future_value = present_value * ((1 + annual_rate) ** years)
print(future_value)

# 8) Give the pre-defined variables first_name and last_name, write an assignment statement that defines the variable name_tag whose value is the string "My name is % %." where the percents should be replaced by first_name and last_name. Remember that, in Python, you can use the + operator on strings to concatenate (i.e. join) them together into a single string.

first_name = "Joe"
last_name = "Warren"
name_tag = f"My name is {first_name} {last_name}"
print(name_tag)

# 9) Challenge: Given the variables x_0, y_0, x_1, and y_1, write an assignment statement that defines a variable distance whose values is the distance between the points (x_0,y_0) and (x_1,y_1)

x_0 = 2
y_0 = 2
x_1 = 5
y_1 = 6
distance = (((x_0 - x_1) ** 2) + ((y_0 - y_1) ** 2)) ** 0.5
print(distance)

# 10) Challenge:Heron's formula states the area of a triangle is sqrt{s(s-a)(s-b)(s-c)} where a, b and c are the lengths of the sides of the triangle and s= 1/2 (a+b+c) is the semi-perimeter of the triangle. Given the variables x_0, y_0, x_1, y_1, x_2, y_2, write a Python program that computes a variable area whose value is the area of the triangle with vertices (x_0,y_0), (x_1,y_1) and (x_2,y_2). (Hint: our solution uses five assignment statements.)

x_0, y_0 = 0, 0
x_1, y_1 = 3, 4
x_2, y_2 = 1, 1

a = (((x_0 - x_1) ** 2) + ((y_0 - y_1) ** 2)) ** 0.5
b = (((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2)) ** 0.5
c = (((x_2 - x_0) ** 2) + ((y_2 - y_0) ** 2)) ** 0.5

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(area)