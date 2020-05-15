import random

def num(list):
    return random.randint(0, len(list)-1)

for i in range(10):
	print(num([1,2,3,4]))