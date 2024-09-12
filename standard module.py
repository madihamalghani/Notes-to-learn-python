# Built in functions in python:
# https://docs.python.org/3/library/functions.html
x=-9.6
print(f'Number x={x} and its absolute is = ',abs(x))

# We can import a function:
from math import sqrt
print('Enter the number for which square root is required: ')
number=int(input())
print(f'Square root of given number is {sqrt(number)}')

# Import using Aliases:
import math as Mymath
print('Enter number for which square root is required')
number=int(input())
print(f'Square root of given number is= {Mymath.sqrt(number)}')

# import a module:
import math
sRoot=math.sqrt(81)
print(sRoot)
# importing os library(contains function related to operating system)
import os
pathCurrent=os.getcwd
print(pathCurrent)
# date time library:
import datetime
current_date=datetime.date.today()
print('current date: ',current_date)
# getting day and time both for now:
current_date_time=datetime.datetime.now()
print('Current date and time: ',current_date_time)


