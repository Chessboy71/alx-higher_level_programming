#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = 1
if number < 0:
    number = - number
    neg = -1


if number % 10 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(
        number*neg, number % 10 * neg))
elif number % 10 * neg > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number*neg, number % 10 * neg))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
        number*neg, number % 10 * neg))
