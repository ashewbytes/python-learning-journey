"""
Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

age = input("Enter your age to get ticket price: ")

while True:
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("You have to pay $10 for your ticket.")
    else:
        print("You have to pay $15 for your ticket.")
    
    age = input("Enter your age to get ticket price: ")





