#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p = 1 if number > 0 else -1
number = number * p
if (number % 10 > 5):
    print(f"Last digit of {p * number} is {number % 10 * p} and is greater than 5")
elif (number % 10 == 0):
    print(f"Last digit of {p * number} is {number % 10 * p} and is 0")
else:
    print(f"Last digit of {p * number} is {number % 10 * p} and is less than 6 and not 0")
