# 1) Write a Python function is_even that takes as input the parameter number (an integer) and returns True if number is even and False if number is odd. Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.

def is_even(number):
    if number % 2 == 0:
        return "even"
    elif number % 2 == 1:
        return "odd"
    else:
        return None

print(is_even(22))


# 2) Write a Python function is_cool that takes as input the string name and returns True if name is either "Joe", "John" or "Stephen" and returns False otherwise.

def is_cool(name):
    if name == "Joe" or name == "John" or name == "Stephen":
        return True
    else:
        return False
    
print(is_cool("sdv"))


# 3) Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the range [1, 12]) and is_am (a Boolean “flag” that represents whether the hour is before noon). The function should return True when the input corresponds to 11am or 12pm (noon) and False otherwise. If the problem specification is unclear, look at the test cases in the provided template. Our solution does not use conditional statements.

def is_lunchtime(hour, is_am):
    if (hour == 11 and is_am) or (hour == 12 and is_am):
        return True
    else:
        return False

print(is_lunchtime(2, True))


# 4) Write a Python function is_leap_year that take as input the parameter year and returns True if year (an integer) is a leap year according to the Gregorian calendar and False otherwise. The Wikipedia entry for leap years contains a simple algorithmic rule for determining whether a year is a leap year. Your main task will be to translate this rule into Python.

#   If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year.
#   If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
#   If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Common Year"
        else:
            return "Leap Year"
    else:
        return "Common Year"

print(is_leap_year(2000))


# 5) Write a Python function interval_intersect that takes parameters a, b, c, and d and returns True if the intervals [a, b] and [c ,d] intersect and False otherwise. While this test may seem tricky, the solution is actually very simple and consists of one line of Python code. (You may assume that a <= b and c <= d.)

def interval_intersect(b, a, d, c):
    """
    Returns whether the intervals [int1_lower, int1_upper] and 
    [int2_lower, int2_upper] intersect.
    """
    return (d <= a) and (b <= c) # int2 lower <= int1 upper AND int1 lower <= int2 upper

print(interval_intersect(0, 1, 2, 3))

# 6) Write a Python function name_and_age that take as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. The function should include an error check for the case when age is less than zero. In this case, the function should return the string "Error: Invalid age".

def name_and_age(name, age):
    if age <= 0:
        return "Error: Invalid age"
    else:
        return f"{name} is {age} years onld."

print(name_and_age("Himal", 0))


# 7) Write a Python function print_digits that takes an integer number in the range [0,100) and prints the message "The tens digit is %, and the ones digit is %." where the percents should be replaced with the appropriate values. The function should include an error check for the case when number is negative or greater than or equal to 100. In those cases, the function should instead print "Error: Input is not a two-digit number.". 

def print_digits(number):
    if (number >= 0) and (number < 100):
        return f"The tens digit is {number//10}, and the ones digit is {number%10}."
    else:
        return "Invalid Number"
    
print(print_digits(23))


# 8) Write a Python function name_lookup that takes a string first_name that corresponds to one of ("Joe", "Scott", "John" or "Stephen") and then returns their corresponding last name ("Warren", "Rixner", "Greiner" or "Wong"). If first_name doesn't match any of those strings, return the string "Error: Not an instructor".

def name_lookup(first_name):
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"
    
print(name_lookup("Nama"))


# 9) Pig Latin is a language game that involves altering words via a simple set of rules. Write a Python function pig_latin that takes a string word and applies the following rules to generate a new word in Pig Latin. If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word. For example, pig_latin("pig") would return "igpay". If the first letter in word is a vowel, append "way" to the end of the word. For example, pig_latin("owl") returns "owlway". You can assume that word is in lower case. The provided template includes code to extract the first letter and the rest of word in Python. Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. However, we don't know enough Python to implement full Pig Latin just yet.

def pig_latin(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" :
        return word + "way"
    else:
        return word[1 : ] + word[0] + "ay"

print(pig_latin("owl"))


# 10) Challenge: Given numbers a, b, and c, the quadratic equation a(x)^2 + bx + c = 0 can have zero, one or two real solutions (i.e; values for x that satisfy the equation). The quadratic formula x = (-b +/- (b^2 - 4ac) ^ 0.5) / 2a can be used to compute these solutions. The expression b^2 - 4ac is the discriminant associated with the equation. If the discriminant is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions. Write a Python function smaller_root that takes an input the numbers a, b and c and returns the smaller solution to this equation if one exists. If the equation has no real solution, print the message "Error: No real solutions" and simply return. Note that, in this case, the function will actually return the special Python value None.
import math
def smaller_root(a, b, c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    dis = (b **2) - (4 * a * c)

    if dis < 0:
        return "Error: No real solutions"
    else:
        s = (-b - (dis ** 0.5)) / (2 * a)
        return s
    

print(smaller_root(6, -3, 5))