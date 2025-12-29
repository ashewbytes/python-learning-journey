# 1 to n number
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i +=1


# sum of first n numbers
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
print(total)


# sum of 1 to 5
n = 5
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
print(total)

# table of a number
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    result = i * number
    print(f"{number} x {i} = {result}")
    i += 1


n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
print(total)

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    result = n * i
    print(result)
    i += 1

# factorial of a number
n = int(input("Enter a number: "))
factorial = 1
while n > 0:
    factorial = factorial * n
    n -= 1
print(factorial)


n = int(input("Enter a number: "))
while n > 0:
    print(n)
    n -= 1