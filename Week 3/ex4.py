# ==========Coding Standards===========

# --------Documentation (Docstrings)-----------

# Docstrings are an integral part of the Python language. They need to be in the following places
#   At the top of each file describing the purpose of the program or module
#   Bellow each function definfiton describing the purpose of the function

# Docstrings describes what is being done in a program or function, not how it is being done.

"""An example program that illustrates the use of docstrings
"""
def welcome(location):
    """Takes the input string welcome and returns a string of the form
    'Welcome to the location'
    """    
    return "Welcome to the " + location

# --------------Comments----------------

# Comments should describes how a section of code is accomplishing something. You should not comment obvious code. Instead, you should document complex code and/or design decisions. You should not comment your code by putting a multi line string in the middle of your program.

# ----------------Global Variables---------------

# Global variables should never be used in this specialization. Avoiding their use is good programming practice in any language. While programmers will sometimes break this rule, you should not break this rule in this specialization.
# But you can use global variables with names that are in all capital letters for constants. And you should never change it.

# ----------------Names-----------------

# All variable and function names must be at least 3 characters. The first character of a name should follow these coventions.
#   Variable names should always starts with a lower case letter (Execept constants)
#   Function names should always start with a lower case letter

# You can seperate words with underscore


# -----------Indentation------------

# Each indentation level should be indented by 4 spaces. It is important not to mix tabs and spaces


# ---------Scope--------------------

# You should not use names that knowingly duplicate other names in an outer scope. This would make the name in the outer scope impossible to access. In particular, you should never use names that are the same as existing Python built-in functions.


# ----------------Arguments and local variables------------

# While there is not necessarily a maximum number of arguments a function can take or a maximum number of local variables you can have, too many arguments or variables lead to unnecessarily complex and unreadable programs. Pylint will enforce maximum numbers of arguments and variables, etc.