import random

tails = 0
heads = 0

for i in range(1000):

    result = random.choice([tails, heads])

    if result == tails:
        tails += 1
    else:
        heads += 1

print("Heads Probability:", heads/(1000))
print("Tails Probability:", tails/(1000))
