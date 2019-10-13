#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
#def solve(meal_cost, tip_percent, tax_percent):
    


meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())
    
tip=meal_cost *(tip_percent/100)
#print(meal_cost)
tax=meal_cost *(tax_percent/100)
#print(tax)
total_cost=(meal_cost+tip+tax)
print(int(total_cost))


    #solve(meal_cost, tip_percent, tax_percent)
