# even or odd
number = int(input("Enter a number: "))


if number % 2 != 0:
    print("Odd")
else: 
    print("Even")

# positive / negetive / zero
number = int(input("Enter a number: "))

if number < 0 :
    print("Negetive")

elif number == 0:
    print("Zero")

else:
    print("Positive")

# greatest of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greatest")
elif num2 > num1:
    print(f"{num2} is greatest")
else:
    print("Both are equal")

# greatest of three number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 or num3:
    print(f"{num1} is greatest")
elif num2 > num1 or num3:
    print(f"{num2} is greatest")
elif num3 > num2 or num1:
    print(f"{num3} is greatest")
else:
    print("All are equal")

# pass or fail 
marks = int(input("Enter your marks: "))

if marks < 33:
    print(f"You got {marks}!, You are fail")
else :
    print(f"You got {marks}, You are pass")

# age eligible for vote or not
age = int(input("Enter your age: "))

if age < 18:
    print(f"You are not allowed to vote.")
else:
    print(f"You can cast your vote.")

# number divisible by 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"It is divisible by 3 and 5.")
else:
    print("It is not divisible by 3 and 5.")

# leap year check
year = int(input("Enter your year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year.")


# even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

# positive / negetive / zero
number = int(input("Enter a number: "))
if number > 0:
    print("negetive")
elif number == 0:
    print("zero")
else:
    print("positive")

# greatest of two numbers
num1 = int(input("Enter number A: "))
num2 = int(input("Enter number B: "))

if num1 > num2:
    print("A is bigger than b")
else:
    print("B is bigger than a")

# greatest of three numbers
num1 = int(input("Enter number A: "))
num2 = int(input("Enter number B: "))
num3 - int(input("Enter number C: "))

if num1 > num2 and num1 > num3:
    print("A is greatest")
elif num2 > num3 and num2 > num1:
    print("B is greatest")
else:
    print("C is greatest")

# pass or fail
marks = int(input("Enter your marks: "))

if marks < 40:
    print("Fail")
else:
    print("Pass")

# eligible for vote or not
age = int(input("Enter your age: "))

if age < 18:
    print("You're not allowed to vote.")
else:
    print("You can vote.")

# number divisible by 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by 3 and 5.")
else:
    print("Number is not divisible by 3 and 5.")

# leap year check
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Its a leap year.")
else:
    print("It's not a leap year.")


n = 12
i = 1

while i <= n:
    print(i)
    i += 1

# sum of first n numbers
n = int(input("Enter a number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1
print(total)
