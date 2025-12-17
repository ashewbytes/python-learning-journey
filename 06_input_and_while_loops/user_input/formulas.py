# two number sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2

print(f"The sum of these two numbers is {total}")

# two numbers difference
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
difference = num1 - num2

print(f"The difference of these two numbers is {difference}")

# two numbers quotient
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 / num2

print(f"The quotient of these two numbers is {quotient}")

# square of a number
number = int(input("Enter a number: "))
square = number ** 2

print(F"Square of a number is {square}")

# cube of a number
number = int(input("Enter a number: "))
cube = number ** 3

print(f"Cube of a number is {cube}")

# area of a rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth

print(f"Area of a rectangle is {area}")

# perimeter of a rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
perimeter = 2 * (length + breadth)

print(f"Perimeter of a rectangle is {perimeter:.2f}")

# area of circle
import math
radius = float(input("Enter radius: "))
area =  math.pi * radius ** 2

print(f"Area of circle is {area:.2f}")

# simple interest
principal = int(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time : "))
simple_interest = (principal * rate * time) / 100

print(f"Simple interest is {simple_interest:.2f}")

# average of 3 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3

print(f"The average of three numbers is {average:.2f}")

# percentage calculation
student_marks = int(input("Enter your marks: "))
total_marks = int(input("Enter total marks: "))
percentage = (student_marks * 100 ) / total_marks

print(f"Your percentage is {percentage:.2f}")

# celsius to fahrenheit
celsius = float(input("Enter celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"Fahrenheit is {fahrenheit:.2f}")

# fahrenheit to celsius
fahrenheit = float(input("Enter fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9

print(f"Celsius is {celsius:.2f}")

# total salary
basic = int(input("Enter your salary: "))
allowance = int(input("Enter allowance: "))
tax = int(input("Enter tax amount: "))
total_salary = basic + allowance - tax

print(f"Your total salary is {total_salary:.2f}")

# find speed
distance = int(input("Enter distance: "))
time = float(input("Enter time: "))
speed = distance / time

print(f"Your speed was {speed:.2f}")

# total price with gst
price = float(input("Enter price: "))
gst = float(input("Enter gst%: "))

gst_amount = (price * gst) / 100
total_price = gst_amount + price

print(f"Your GST price is {gst_amount:.2f}")
print(f"Your total price is {total_price:.2f}")


