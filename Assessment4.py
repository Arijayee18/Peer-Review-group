#Fatima Munoz Ramirez
#CSCI128 Section J
#Assessment 4
#References: no one
#Time: 5 hours

#Inputs
point1 = (input("INPUT P1> "))
point2 = (input("INPUT P2> "))
point3 = (input("INPUT P3> "))

#Splitting input and floating 
splitting_input1 = point1.split(" ")
splitting_input2 = point2.split(" ")
splitting_input3 = point3.split(" ")

x1 = float(splitting_input1[0])
y1 = float(splitting_input1[1])
x2 = float(splitting_input2[0])
y2 = float(splitting_input2[1])
x3 = float(splitting_input3[0])
y3 = float(splitting_input3[1])

#Find the distanc of the 3 sides
side1 = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)
side2 = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5, 4)
side3 = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5, 4)
sides_list = [side1, side2, side3]
sides_list.sort()

#Print length of sides
print("OUTPUT", sides_list)

if point1 == point2 or point2 == point3 or point3 == point1:
   print("OUTPUT Duplicate Point")
elif sides_list[0] + sides_list[1] == sides_list[2]:
   print("OUTPUT Collinear")
elif side1 == side2 and side2 == side3:
   print("OUTPUT Acute Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
      if (sides_list[0] ** 2) + (sides_list[1] ** 2) == sides_list[2] ** 2:
         print("OUTPUT Right Isosceles Triangle")
      elif (sides_list[0] ** 2) + (sides_list[1] ** 2) < sides_list[2] ** 2:
         print("OUTPUT Obtuse Isosceles Triangle")
      else:
         print("OUTPUT Acute Isosceles Triangle")
elif not side1 == side2 or not side2 == side3 or not side3 == side1:
      if (sides_list[0] ** 2) + (sides_list[1] ** 2) == sides_list[2] ** 2:
         print("OUTPUT Right Scalene Triangle")
      elif (sides_list[0] ** 2) + (sides_list[1] ** 2) < sides_list[2] ** 2:
         print("OUTPUT Obtuse Scalene Triangle")
      else:
         print("OUTPUT Acute Scalene Triangle")
else:
    print("")


