def area_triangle(num1, num2, num3):
    perimeter = num1 + num2 + num3
    s = perimeter / 2
    area = (s*(s-num1)*(s-num2)*(s-num3))**0.5
    return area

num1 = int(3)
num2 = int(4)
num3 = int(5)

area = area_triangle(num1,num2,num3)

print ("the area of the triangle is:" + str(area))
