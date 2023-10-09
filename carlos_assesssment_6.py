# Carlos Chavezz
# CSCI128 Section J
# Assessment 6
# Refrence: No one
# Time: 1 hour 30 min
import random

# Inputs
seed = input("SEED> ")
random.seed(seed)
months = int(input("MONTHS> "))
interest = float(input("INTEREST> "))
method = input("METHOD> ")
balance = 0

# Functions/Calculations

# Method for 1
for i in range(months):
    if method == "1":
        balance += 2000
        balance *= (1 + interest)
# Method for 2  
    elif method == "2":
        balance += 2000
        profit = random.random()
        if 0 < profit < 0.7:
            pass
        elif 0.7 <= profit < 0.9:
            balance *= 1.01
        elif 0.9 <= profit <= 1:
            balance *= 0.97
# Method for 3
    elif method == "3":
        if random.randint(0, 36) == 15:
            balance += 70000
        
        balance *= (1 + interest)
# OUTPUT
print(f"OUTPUT {balance:.2f}")
