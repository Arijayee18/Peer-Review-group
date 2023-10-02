# Cameron Alcorn
# CSCI 128 - Section J
# Assessment 5
# References: None
# Time: 1 Hour
x = float(input("X0>"))
x_new = x
previous_values_list = [x]
lambda_1 = float(input("LAMBDA>"))
while True:
    x_new = lambda_1 * x_new * (1 - x_new)
    x_new = round(x_new, 6)
    if x_new in previous_values_list:
        n = previous_values_list.index(x_new)
        k = n
        for x in range(len(previous_values_list[n:])):
            print(f'OUTPUT {previous_values_list[k]}')
            k += 1
        break
    previous_values_list.append(x_new)
