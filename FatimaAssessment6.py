#Fatima Munoz Ramirez
#CSCI128 Section J
#Assessment 6
#References: TA Tyler
#Time:  4 hours

import random

seed = input("INPUT> ")
months = int(input("INPUT> "))
interest = float(input("INPUT> "))
method = input("INPUT> ")

random.seed(seed)

fluid_cash = 2000
networth = 0


if method == "1":
    for value in range(months):
        ending_balance = (interest + 1) * fluid_cash
        fluid_cash = ending_balance
        networth += ending_balance 
    print(f"OUTPUT {networth:.2f}")

elif method == "2":
    for value in range(months):
            probability = random.random()
            if probability <= 0.7:
                networth = networth + fluid_cash
            elif probability <= 0.9:
                networth = (networth + fluid_cash) * 1.01
            else:
                networth = (networth + fluid_cash) * 0.97
    print(f"OUTPUT {networth:.2f}")

elif method == "3":
    for value  in range(months):
        number = random.randint(0,36)
        if number == 15:
            earning = 2000 * 35 
            networth = networth + earning
            networth = (interest + 1) * networth     
    print(f"OUTPUT {networth:.2f}")
   
