# Cameron Alcorn
# CSCI 128 Section J
# Assessment 4
# References: None
# Time: 90 mins
coord1 = input("COORD1>").split()
coord1[0] = float(coord1[0])
coord1[1] = float(coord1[1])

coord2 = input("COORD2>").split()
coord2[0] = float(coord2[0])
coord2[1] = float(coord2[1])

coord3 = input("COORD3>").split()
coord3[0] = float(coord3[0])
coord3[1] = float(coord3[1])

dist12 = round((((coord1[0] - coord2[0]) ** 2) + ((coord1[1] - coord2[1]) ** 2)) ** 0.5, 4)
dist13 = round((((coord1[0] - coord3[0]) ** 2) + ((coord1[1] - coord3[1]) ** 2)) ** 0.5, 4)
dist23 = round((((coord2[0] - coord3[0]) ** 2) + ((coord2[1] - coord3[1]) ** 2)) ** 0.5, 4)

dist_list = [dist12, dist13, dist23]
dist_list.sort()
print(f'OUTPUT {dist_list}')

if dist12 == 0 or dist13 == 0 or dist23 == 0:
    print("OUTPUT Duplicate Point")
elif dist_list[0] + dist_list[1] == dist_list[2]:
    print("OUTPUT Collinear")

angle_class = (dist_list[0]) ** 2 + (dist_list[1]) ** 2
if angle_class < (dist_list[2]) ** 2:
    angle = "Obtuse"
elif angle_class == (dist_list[2]) ** 2:
    angle = "Right"
else:
    angle = "Acute"

if dist12 == dist13 and dist12 == dist23:
    length = "Equilateral"
elif dist12 == dist13 or dist12 == dist23 or dist13 == dist23:
    length = "Isosceles"
else:
    length = "Scalene"

if dist12 != 0 and dist13 != 0 and dist23 != 0 and dist_list[0] + dist_list[1] != dist_list[2]:    
    print("OUTPUT", angle, length, "Triangle")