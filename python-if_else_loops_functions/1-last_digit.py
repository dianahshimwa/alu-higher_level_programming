#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 0 and number < 0:
    last_digit -= 10
output_string = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    output_string += " and is greater than 5"
elif last_digit == 0:
    output_string += " and is 0"
else:
    output_string += " and is less than 6 and not 0"

print(output_string)
