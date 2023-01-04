#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    num_type = "negative"
elif number > 0:
    num_type = "positive"
else:
    num_type = "zero"
print(f"{number} is {num_type}")
