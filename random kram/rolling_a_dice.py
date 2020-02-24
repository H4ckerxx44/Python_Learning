import random
import numpy as np
dice1 = random.randrange(6) + 1
dice2 = random.randrange(6) + 1
dice3 = random.randrange(6) + 1
dice4 = random.randrange(6) + 1
dice5 = random.randrange(6) + 1
dice6 = random.randrange(6) + 1


total = dice1 + dice2 + dice3 + dice4 + dice5 + dice6
median = np.median(total / 6)

print("dice 1 ==", dice1)
print("dice 2 ==", dice2)
print("dice 3 ==", dice3)
print("dice 4 ==", dice4)
print("dice 5 ==", dice5)
print("dice 6 ==", dice6)
print("the total amount is = ", total)
print("median == ", median)

