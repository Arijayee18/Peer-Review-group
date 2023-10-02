'''
Ari'Jaye Derritt
CSCI 128 - Section J
Assessment 5
References: TA Alyssa 
Time: 3hours 
'''


x0 = float(input())
y = float(input())
x = x0
x = round(x,6)
y = round(y,6)
cycle = []
notconverged = True
while notconverged == True:
    xnew = round(y * x * (1-x),6)
    cycle.append(x)
    if xnew ==cycle[-1]:
        print('OUTPUT', xnew)
        notconverged = False
        break
    elif xnew in cycle:
        b = cycle.index(xnew)
        for i in cycle[b:]:
            print('OUTPUT', i)
        notconverged = False
        break
    x=xnew
    