'''
Ari'Jaye Derritt
Section J
Assessment 6 
References: TA Alyssa
Time: 3 hours
'''
# import the Python random module
import random

# get the seed value to be used
seed = input("SEED> ")
# set the random seed
random.seed(seed)
# get the number of months to simulate
months = int(input("MONTHS> "))
#intial investment
invest = 0
# get the interest rate
interest = float(input("INTEREST> "))
# ask for the desired invest method
method = input("METHOD> ")
savings = 0
invest = 0
winnings = 0
if method == "1":
    for save in range(months):
        invest += 2000
        invest *= (interest + 1) 
    print(f'OUTPUT {invest:.2f}')
elif method == "2":
    for i in range(months):
        randomProbability = random.random()
        invest += 2000
        if randomProbability > 0 and randomProbability < 0.7:
            invest = invest
        elif randomProbability > 0.7 and randomProbability < 0.9:
            invest = invest * 1.01
        elif randomProbability > 0.9 and randomProbability < 1:
            invest = invest * 0.97
    print(f'OUTPUT {invest:.2f}')
elif method == "3":
    invest +=2000
    for bet in range(months):
        ranNum = random.randint(0,36)
        if ranNum == 15:
            winnings = winnings + 2000 * 35
        winnings = (interest + 1) * winnings 
    print(f'OUTPUT {winnings:.2f}')
            
        
