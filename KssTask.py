# Ques1) To print the sum of all numbers between m and n (both included), using for loops (m and n are user-defined inputs)
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the last number: "))
sum = 0

for i in range(num1, num2 + 1):
    sum = sum + i

print(f"Sum of numbers between {num1} and {num2} is {sum}")
'''
# Ques2) To take two numbers from the user and check if one number perfectly divides the other.
'''
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x % y == 0:
    print(f"{y} is perfectly divisible by {x}")
elif y % x == 0:
    print(f"{x} is perfectly divisible by {y}")
else:
    print("Neither {x} nor {y} is perfectly divisible by each other.")
'''
# Ques3) To print the area and perimeter of a circle if the diameter is given by the user.
'''
import math

diameter = float(input("Enter diameter of the circle: "))
radius = diameter / 2

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print(f"Area of the circle: {area}")
print(f"Perimeter of the circle: {perimeter}" )
'''
# Ques4) To print the factorial of a number given by the user.
'''
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
'''
# Ques5) To print the following pattern : 
# 1
# 12
# 123
# 1234
# 12345

x = int(input("Enter the number of lines for the pattern : "))

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
