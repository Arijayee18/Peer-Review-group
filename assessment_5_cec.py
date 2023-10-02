# Carlos Chavez
# CSCI128 Section J
# Assessment 5
# Refeernce: No one
# Time: 1 hour 

# Read input values
x0 = float(input())  # Starting population
lambda_val = float(input())  # Lambda value

# Initialize a list to store the sequence
sequence = [x0]

# Define a function to calculate population growtH
def population_growth(x, lmbda):
    return lmbda * x * (1 - x)  

# Generate the sequence
while True:
    next_x = population_growth(sequence[-1], lambda_val)
    
    # Check if the next value is already in the sequence (indicating a cycle)
    if round(next_x, 6) in [round(val, 6) for val in sequence]:
        cycle_start_index = sequence.index(round(next_x, 6))
        cycle = [round(val, 6) for val in sequence[cycle_start_index:]]
        break
    
    sequence.append(round(next_x, 6))

# Check if the result is a single value or a cycle
if len(cycle) == 0:
    # Converges to a single value
    print("OUTPUT", round(sequence[-1], 6))
else:
    # Converges to a cycle
    for val in cycle:
        print("OUTPUT", val)
