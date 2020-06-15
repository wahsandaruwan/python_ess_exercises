# =========Common Python Errors===========

# ---------Syntax Error------
# 'Syntax' refers to the rules that dictate how your Python program should be structured. For example, one rule states that you may not begin a variable name with a digit in Python. A SyntaxError will pop up if you violate any of Python's syntax rules. This could be forgetting to close a parenthesis or quote, mistakes in indentation, forgetting colons after function headers, etc.
# In python this is ok, but python 3 print is a function
print "To error is human, to forgive is divine" # Should include ()

# Missing quatations
print("To error is human, to forgive is divine)

# --------Indentation Error--------
# Python uses 'indentation' to group the statements that form the body of a function definition or the clauses of an if-elif-else statement. In particular, all of the statements in this body should have the same level of indentation. Python gives this error when it detects two statements that should be at the same level of indentation.
# Sometimes python doesn't recognize errors until the processing the next line
# In these cases check your previous line
print_quote = True
if print_quote:
    print("To error is human, to forgive is divine")
else:
    # Can't leave this empty, atleast type 'pass'
print_quote = False

# ---------Name Error----------
# A 'NameError' is triggered when Codeskulptor doesn't recognize the variable, function name, etc. that you're referring to. A NameError is Codeskulptor's way of saying "I've never heard of that before!" Common causes of this are misspellings or forgetting to declare variables entirely.
# Missing Spelling
pope_quote = "To error is human, to forgive is divine"
print(popequote) # Variable is not defined

# ----------Type Error---------
# This error can come up when you're trying to do perform an operation on something, but the operation and the thing just don't go together. One example is trying to multiply a dictionary and an integer - it just won't work. A helpful tool in debugging type errors is the Python \color{red}{\verb|type()|}type() function. Adding print statements like "\color{red}{\verb|print(type(my_variable))|}print(type(my_variable))" will help you figure out what's going wrong.
# Concatiating,converting
joe_ranking = 1
print("Joe is number " + joe_ranking + " coder.") 
# Pyhton does not know how to add a number and string
# str(joe_ranking)

# ----------Index Error----------
# An IndexError happens when you try to access an index that doesn't actually exist. It's like telling someone to take 13 eggs out of a 12-egg carton - it won't work, because there are only 12 spaces. Printing out your index values, along with \color{red}{\verb|len(the_list_in_question)|}len(the_list_in_question) will help you in debugging these errors. Important to note: negative indices *are* possible in Python! See the video lecture on lists for more information.

# ---------Token Error-------------
# Very simply, tokens are things that stand for other things - sort of like variables, except they're used at a more structural level. Some examples of tokens are EOF (End Of File) and EOL (End Of Line). These are the two most common ones you will come across in Python, but they are used everywhere in programming. The TokenErrors that you will see in this course are usually solved by remembering to close your brackets. See the example for a more in-depth explanation of why this is.

# ---------Value Error-------------
# A ValueError is raised when a function receives an argument that looks ok on the surface (e.g., it receives a character, and it was looking for a character), but the value of that argument is unexpected (e.g., the function was only built to handle digits, and it received a letter 'a'). This type of error can be solved by checking the documentation for whatever function you're trying to use and making sure that whatever you put inside the parentheses, the function was built to handle it.

# ----------Attribute Error-------------
# In object-oriented programming (OOP), objects have "attributes" - things that they're aware of, and/or know how to do. In terms of Python, attributes are an objects properties and the methods defined by its class. An AttributeError will be thrown when you ask an object to do something or access something that isn't in its class definition.

# -----------Miscellaneous section - these errors are either self-explanatory or not common in the level of programming done in this class------------------
# ZeroDivisionError - you guessed it - you're trying to divide by zero somewhere
# ImportError - caused by trying to import a module that doesn't exist. Check your spelling.
# HierarchyError - Internet Explorer is not supported by CodeSkulptor3. Use Chrome or Firefox.
# JavaScript section - these are not Python errors. They are related to your browser, not your code.