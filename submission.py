'''
Ari'Jaye Derritt
CSCI 128 - Section J
Assessment 4
References: no one
time: 1 hour 
'''
p1 = input("P1> ")
p2 = input("P2> ")
p3 = input("P3> ")

#spliiting the string to get x and y coordinates
p1 = p1.split()
p2 = p2.split()
p3 = p3.split()

#x and y coordinates 
p1x = float(p1[0])
p1y = float(p1[1])
p2x = float(p2[0])
p2y = float(p2[1])
p3x = float(p3[0])
p3y = float(p3[1])

# Step 1: Find the side lengths 
side1 = round((((p2x-p1x)**2)+(p2y-p1y)**2)**0.5, 4)
side2 = round((((p3x-p2x)**2)+(p3y-p2y)**2)**0.5, 4)
side3 = round((((p3x-p1x)**2)+(p3y-p1y)**2)**0.5, 4)
sideList = [side1, side2, side3]
sideList.sort()
print(f'OUTPUT {sideList}')

#Step 2: determine whether the points are duplicate or collinear, then the type of triangle

if p1 == p2 or p1 == p3 or p2==p3:
    print('OUTPUT Duplicate Point')
elif sideList[0] + sideList[1] == sideList[2]:
    print('OUTPUT Collinear')
elif sideList[0]**2 + sideList[1]**2 < sideList[2]**2: #obstuse triangle
    if sideList[0]==sideList[1] or sideList[1]==sideList[2] or sideList[0]==sideList[2]:
        print('OUTPUT Obtuse Isosceles Triangle')
    elif sideList[0] != sideList[1] and sideList[1]!=sideList[2] and sideList[0]!=sideList[2]:
        print('OUTPUT Obtuse Scalene Triangle')
    else:
        print('OUTPUT Oblique Triangle')
elif sideList[0]**2 + sideList[1]**2 == sideList[2]**2: #right triangle
    if sideList[0] != sideList[1] and sideList[1] != sideList[2] and sideList[0] != sideList[2]:
        print('OUTPUT Right Scalene Triangle')
    if sideList[0]==sideList[1]or sideList[1]==sideList[2] or sideList[0]==sideList[2]:
        print('OUTPUT Isosceles Triangle')
elif sideList[0]**2 + sideList[1]**2 > sideList[2]**2: #acute triangle
    if side1 == side2 == side3:
        print('OUTPUT Acute Equilateral Triangle')
    elif sideList[0] == sideList[1] or sideList[1] == sideList[2] or sideList[0] == sideList[2]:
        print('OUTPUT Acute Isosceles Triangle')
    elif sideList[0] != sideList[1] and sideList[1] != sideList[2] and sideList[0] != sideList[2]:
        print('OUTPUT Acute Scalene Triangle')
    else:
        print('OUTPUT Oblique Triangle')
        






