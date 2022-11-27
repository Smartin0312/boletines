""" Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400"""

year=int(input("dime un año"))
def is_leap_year(year):
    res = False
    if year%4==0 and (year%100!=0 or year%400==0):
        res=True
    return(res)

   
print(is_leap_year(year))