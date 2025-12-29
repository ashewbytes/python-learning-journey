# Average of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("The average of these two number is", (a+b)/2)

# Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
total = a + b 

print(f"The sum of these two numbers is {total}")


# product of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a * b

print(f"Product of these two number is {c}")

# square of a number]
a = int(input("Enter a number: "))
square = a ** 2
print("Square of a number is", square)

# cube of a number
a = int(input("Enter a number: "))
cube = a ** 3
print("Cube of a number is", cube)

# finding speed
distance = int(input("Enter your distance: "))
time = int(input("Enter time: "))
speed = distance / time
print(speed)

# percentage calculation
total_marks = int(input("Enter total marks: "))
marks_obtained = int(input("Enter your marks: "))
percentage = marks_obtained * 100 / total_marks
print("Your percentage is :", percentage,"%")

# even or odd 
number = int(input("Enter a number"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

num = int(input("Enter a number: "))
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")

# fail and pass
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("pass")
else:
    print("fail")

# age eligible to vote or not

age = int(input("Enter your age: "))
if age < 18:
    print("You are not allowed to vote!")
else:
    print("You can cast your vote.")

# number divisible by 3 and 5
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("This number is divisible by 5 and 3")
else:
    print("It is not divisible by 5 and 3")

# two number difference

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
difference = first_number - second_number

print(f"The difference between first and second number: {difference}")

# two number quotient
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
quotient = first_number / second_number

print(f"The quotient of these two numbers are: {quotient}")

# area of circle
radius = float(input("Enter radius: "))
area = 3.14 * radius ** 2

print(f"Area of circle is: {area}")

# circumference of circle

import math
radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius

print(f"Circumference of a circle is {circumference:.2f}")

# radius using diameter
diameter = 10
radius = diameter / 2

print(f"Radius of circle is {radius}")

area = math.pi * radius ** 2
print(f"Area of circle is {area:.2f}m^2")


# if area of circle is 154cm^2

area = 154
radius = math.sqrt(area / math.pi)

print(f"Radius of circle is {radius}")

# Area of rectangle
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
print(f"Area of a rectangle is {area}")

# perimeter of rectangle
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
perimeter = 2  * (length + breadth)

print(f"Perimeter of rectangle is {perimeter}")

# simple interest

principal = float(input("Enter Principle: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))
simple_interest = (principal * rate * time) / 100

print(f"Simple interest is {simple_interest:.2f}")

