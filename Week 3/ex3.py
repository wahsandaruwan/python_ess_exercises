# ============Conditionals==========

# ---------------If Statements------------
def greet(friend, money):
    """Greet people. Say hi if they are your firend and give them $20 if you have enough money
    """    
    # It acts like a condition | Bellow 2 if statements are independent
    if friend:
        print("Hi!")
    if money > 20:
        money = money - 20
    return money # Doesn't matter if statements whether true or false

money = 100

money = greet(False, money)
print("Money  : ",money)
print("")

money = greet(True, money)
print("Money  : ",money)
print("")

money = greet(True, money)
print("Money  : ",money)
print("")

# -----------------else and elif--------------

def greet(friend, money):
    """Greet people. Say hi they are your friend. Give them $20 if they are your friend and you have enough money. Steal $10 from them if they are not your friend.
    """    
    if friend and (money > 20):
        print("Hi")
        money = money - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        money = money + 10
    return money

money = 35

money = greet(True, money)
print("Money : ",money)
print("")

money = greet(False, money)
print("Money : ",money)
print("")

money = greet(True, money)
print("Money : ",money)
print("")


# -----------------Collatz conjecture-----------------
# That takes an integer n and divides it by two if n is even and multiplies n by 3 and then adds one to the result if n is odd.

def f(x):
    if x % 2 == 0:
        return x // 2
    elif x % 2 == 1:
        return x * 3 + 1
    else:
        print('Something went worng')
        return None
    
print("Sequence")
number = 674
print(number)
count = 0
while(number != 1):
    count += 1
    number = f(number)
    print(number)
print(number)
print("============")
print(count)