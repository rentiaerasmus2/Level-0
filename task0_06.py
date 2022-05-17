def max_of_three(num1, num2, num3):
    if num1 > num2:
       return num1
    return num2
    return max_of_three(num1, max_of_three( num2, num3))

print(max_of_three(3, 6, 2))
