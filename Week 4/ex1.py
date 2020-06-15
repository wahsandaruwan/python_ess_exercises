# ===========Importing Modules=================

# --------Import math module-----------
import math

# Import example module
# import example_module as example

# Constants
print("Math Constants")
print("==================")
print(math.pi)
print(math.e)
print("")

# Functions
print("Math Functions")
print("===============")
print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))
print("")

# Dir
print("Dir")
print("===============")
print(dir(math)) # Directory
print("")


# --------Import datetime module-----------

# Create some dates
import datetime
print("Creating Dates")
print("==================")

date1 = datetime.date(1999, 12, 31)
date2 = datetime.date(2000, 1, 1)
date3 = datetime.date(2012, 4, 5)
# date4 = datetime.date(2020, 12, 34) # Passing invalid day 34

print(date1)
print(date2)

# Today's Date
today = datetime.date.today()
print(today)
print("")

# Compare Dates
print("Comparing Dates")
print("==================")

print(date1 < date2)
print(date3 <= date1)
print(date2 == date3)

print("")

# Substracting Dates
print("Substrating Dates")
print("================")

diff1 = date2 - date1
print(diff1)
print(diff1.days)

diff2 = date3 - date2
print(diff2)
print(diff2.days)

# Year,Month,Day
print("Year, Month, Day")
print("================") 
dt1 = datetime.date(2016, 1, 7)

print(dt1)
print(dt1.year)
print(dt1.month)
print(dt1.day)
