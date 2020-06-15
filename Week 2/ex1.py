# =========Functions==========

# ------Call a function-------
def sample(inp1, inp2, inp3):
    # Docstrings that describes what the function does
    """This function takes 3 arguments and always returns 3
    """      
    return 3
# Calling the function
# Way 1
sample(4, 5, 6)

# Way 2
print(sample(1, 2, 3))

# Way 3
result = sample(6, 8, 9)
print(result)

# Note : We should pass the right number of arguments


# ---------Defining Function---------
def sayHello():
    """Prints 'Hello'
    """    
    print("Hello")

# Call the function (We can call a function multiple times if we want)
sayHello()
sayHello()

# --------------
def doubleVal(input):
    """Return twice the input vallue
    """    
    return input * 2

result = 32 + doubleVal(15)
print(result)

# ---------------
def product(val1, val2, val3):
    """Returns the product of the three input values
    """    
    product = val1 * val2 * val3
    return product

result = product(7, 13.3, -1.2) * 54.3
print(result) 
# Note : print is a function and it is a built in function. And it is different because
# we can pass more than one argument to it.
print(result, result, result)


# =============Parameters and Varibales within Functions===========

def fahrenhite_to_celsius(fahrenhite):
    """Returns celsius temperatur that corresponds to fahrenhite temperature input
    """    
    offset = 32
    multiplier = 5 / 9
    celsius = (fahrenhite - offset) * multiplier
    print("Inside Function : ", fahrenhite, offset, multiplier, celsius)
    return celsius

temperature = 95
converted = fahrenhite_to_celsius(temperature)
print("Fahrenhite Temperature : ", temperature)
print("Celsius Temperature : ", celsius) # <==== we can't use celsius here

# Note : Varibales defined inside a function are local to that function

# ----------------------------

fahrenhite = 27
offset = 2
multiplier = 19
celsius = 77

print("Before : ", fahrenhite, offset, multiplier, celsius)
newtemp = fahrenhite_to_celsius(32)
print("After : ", fahrenhite, offset, multiplier, celsius) # Print same value like  before
print("result : ", newtemp) # Got expected result

# -----------------------------

def sum_of_squares(num1, num2):
    """Return the sum of the squares of the two inputs
    """    
    sq1 = num1 * num2
    sq2 = num1 * num2
    sumsq = sq1 + sq2
    return sumsq

print(sum_of_squares(20,33.4))

# --------------------------------

# Distnace between 2 points
def distance(x_0, y_0, x_1, y_1):
    """Return distance between 2 points (x_0, y_0) and (x_1, y_1)
    """    
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1

    return(x_dist ** 2 + y_dist ** 2) ** 0.5

# Compute the distance between (2, 2) and (5, 6)
x_0, y_0 = 2, 2
x_1, y_1 = 5, 6

print(distance(x_0, y_0, x_1, y_1))


# ==========Comparing return vs print===========
# Print statements can be appear in anywhere but return statements appear inside functions

# Calling the function iside print statement
def welcome(location):
    """Given a string location, return a string of the form 'Welcome to location'
    """    
    answer = "Welcome to " + location
    return answer
    print("Hello...") # We never gonna execute this print function, because 'return' terminates the function execution

print(welcome("the Matrix"))

# -------------------------

# Just calling the function
def welcome(location):
    """Given a string location, return a string of the form 'Welcome to location'
    """    
    answer = "Welcome to " + location
    print(answer) # Now it will print

welcome("the World")

# --------------------------

# Calling the function inside the print statement
def welcome(location):
    """Given a string location, return a string of the form 'Welcome to location'
    """    
    answer = "Welcome to " + location
    print(answer) # This will print without any issue But,
    # In this case we are trying to terminate the execution of a function without 'return' statement, then it will give us 'None', it is the default return value in cases like these.
    
print(welcome("the Python Programming")) # <==== 'None'





