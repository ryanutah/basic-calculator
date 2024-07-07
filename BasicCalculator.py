# Author:
# Agyeya Mishra
# Department of Civil Engineering
# Delhi Technological University (formerly, Delhi College of Engineering)
# New Delhi, India

import sys
from Functions import *
#Python program to create a simple calculator 

for line in sys.stdin:
    line = line.rstrip()
    if '+' in line:
        nums = line.split('+')
        print(add(int(nums[0]), int(nums[1])))
    elif '-' in line:
        nums = line.split('-')
        print(subtract(int(nums[0]), int(nums[1])))
    elif '*' in line:
        nums = line.split('*')
        print(multiply(int(nums[0]), int(nums[1])))
    elif '/' in line:
        nums = line.split('/')
        print(divide(int(nums[0]), int(nums[1])))
    elif '%' in line:
        nums = line.split('%')
        print(mod(int(nums[0]), int(nums[1])))
    elif '^' in line:
        nums = line.split('^')
        print(exponent(int(nums[0]), int(nums[1])))
    elif line == "quit" or line == "exit":
        exit()
    else:
        print("This mathematical expression is either wrong or not supported.")
    
  
