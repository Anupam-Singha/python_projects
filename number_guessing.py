#python project to guess the number

import random
import math

lower = int(input("Enter the lower digit:"))
upper = int(input("Enter the upper digit:"))

x = random.randint(lower, upper)

# number of guess available

guess = round(math.log(upper - lower + 1, 2))
print("you have got only", round(math.log(upper - lower + 1, 2)) , "guess")

count = 1

for i in range(count, guess+1):
    num1 = int(input("Enter the number"))
    if num1 == x:
        print("You have guessed the correct number which is", x)
        break
    elif num1 > x:
        print("You are too high")
    elif num1 < x:
        print("You are too low")
        count = count + 1
    

