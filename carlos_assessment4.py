# Carlos Chavez
# CSCI 128 Section J

distance_one = input("P1> ").split()
distance_two = input("P2> ").split()
distance_three = input("P3> ").split()

distance_one = [float(distance_one[0]), float(distance_one[1])]
distance_two = [float(distance_two[0]), float(distance_two[1])]
distance_three = [float(distance_three[0]), float(distance_three[1])]

length_a = round(((distance_two[0] - distance_one[0]) ** 2 + (distance_two[1] - distance_one[1]) ** 2) ** 0.5, 4)
length_b = round(((distance_three[0] - distance_two[0]) ** 2 + (distance_three[1] - distance_two[1]) ** 2) ** 0.5, 4)
length_c = round(((distance_one[0] - distance_three[0]) ** 2 + (distance_one[1] - distance_three[1]) ** 2) ** 0.5, 4)

side_list = [length_a, length_b, length_c] 
side_list.sort()

a, b, c, = sorted([length_a, length_b, length_c])
if a ** 2 + b ** 2 == c ** 2:
    angle = "Right"
elif a ** 2 + b ** 2 > c ** 2:
    angle = "Acute"
else: 
    angle = "Obtuse"

if length_a == length_b == length_c:
    side_length = "Equilateral"
elif length_a == length_b or length_b == length_c or length_a == length_c:
    side_length = "Isosceles"
else:
    side_length = "Scalene"

print("OUTPUT", side_list)

if distance_one == distance_two or distance_two == distance_three or distance_one == distance_three:
    print("OUPUT Duplicate Point")
    angle = ""
elif length_a + length_b == length_c or length_a + length_c == length_b or length_b + length_c == length_a: 
    print("OUTPUT Collinear")
else:
    print("OUTPUT", angle, side_length, "Triangle")
