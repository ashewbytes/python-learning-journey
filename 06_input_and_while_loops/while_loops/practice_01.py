"""
Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

prompt = "Enter a topping you want to add to your pizza."
prompt += "\nEnter 'quit' to exit. "

message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(f"Your {message.capitalize()} is added to your pizza.")