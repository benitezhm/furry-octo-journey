import random
from datetime import datetime

first_number = random.random()
print(first_number)

second_number = random.randint(1, 10)
print(second_number)

random.seed(datetime.now().microsecond)
third_number = random.random()
print(third_number)