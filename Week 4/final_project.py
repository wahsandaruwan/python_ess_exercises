"""
Collections of custom functions that related to datetime library/module
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    #Chek month
    if 0 < month < 12:
        #Get number of days
        return (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days
    elif month == 12:
        #Get number of days
        return (datetime.date(year+1, month-11, 1) - datetime.date(year, month, 1)).days
    else:
        return 0


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    #Check year and month
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and 0 < month <= 12:
        #Check the day        
        if 0 < day <= days_in_month(year, month):
            return True
        else:
            return False
    else:
        return False
        

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    #Check dates are valid
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        #Check second date is greater than first date
        if datetime.date(year1, month1, day1) < datetime.date(year2, month2, day2):
            #Get the date difference
            return (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days
        else:
            return 0
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    #Check date is valid
    if is_valid_date(year, month, day):
        #Check birthday is valid
        if datetime.date(year, month, day) < datetime.date.today():
            year2 = datetime.date.today().year
            month2 = datetime.date.today().month
            day2 = datetime.date.today().day
            #Get the date difference
            return days_between(year, month, day, year2, month2, day2)
        else:
            return 0
    else:
        return 0


#Calling all functions    
print(days_in_month(2020, 6))

print(is_valid_date(1, 4, 31))

print(days_between(2020, 7, 4, 2020, 8, 6))

print(age_in_days(1995, 2, 13))