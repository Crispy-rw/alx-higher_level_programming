#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1:]
if int(last_digit) > 5:
    print("Last digit of {:d} is {} and is greater than 5".format(number, last_digit))
elif int(last_digit) < 6 and int(last_digit) != 0:
    print("Last digit of {:d} is {} and is less than 6 and not 0".format(number, int(last_digit) * -1  if number < 0 else number ))
else:
    print("Last digit of {:d} is {} and is 0".format(number, last_digit))
  
