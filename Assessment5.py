#Fatima Munoz Ramirez
#CSCI128 Section J
#Assessment 5
#References: no one
#Time: 5 hours

x_0 = float(input("INPUT> "))
growth = float(input("INPUT> "))

x = x_0
list_of_values = []

while True:
    x_new = growth * x * (1-x)
    x_new = round(x_new, 6)
    if x_new == x:
        x = x_new
        print(f"OUTPUT {x_new}")
        break

    elif x_new in list_of_values:
        list_of_values.append(x_new)
        value = list_of_values.index(x_new)
        answer = list_of_values[value]
        x = x_new
        print(f"OUTPUT {answer}")

        cycle = list_of_values.index(x_new) + 1
        cycle2 = list_of_values[cycle:-1]
        output = str(cycle2)[1:-1]
        for x in cycle2:
            print(f"OUTPUT {x}")
        break
    
    list_of_values.append(x_new)
    x = x_new
