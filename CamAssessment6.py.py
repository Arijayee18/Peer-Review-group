# import the Python random module
import random

# get the seed value to be used
seed = input("SEED> ")
# set the random seed
random.seed(seed)

# get the number of months to simulate
months = int(input("MONTHS> "))

# get the interest rate
interest = float(input("INTEREST> "))

# ask for the desired invest method
method = input("METHOD> ")

Y = 0

if method == "1":
    # savings account
    for i in range(months):
        Y = Y + 2000
        Y = (1 + interest) * Y
    print(f'OUTPUT {Y:.2f}')

elif method == "2":
    # index fund
    for i in range(months):
        Y = Y + 2000
        probability = random.random()
        if probability >= 0 and probability <= 0.7:
            Y = Y
        elif probability > 0.7 and probability <= 0.9:
            Y = Y * 1.01
        elif probability > 0.9:
            Y = Y * 0.97
    print(f'OUTPUT {Y:.2f}')

elif method == "3":
    # roulette
    for i in range(months):
        probability = random.randint(0, 36)
        if probability == 15:
            Y = Y + 70000
        Y = (1 + interest) * Y
    print(f'OUTPUT {Y:.2f}')
