import random

dice = int(input("How many dice? "))

for i in range(dice):
    print("Die", i+1, "rolled a", random.randint(1, 6))
