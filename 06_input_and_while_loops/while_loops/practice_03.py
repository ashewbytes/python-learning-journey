# Ask the user for their age repeatedly and print their age category until they enter a negative number.
prompt = "Enter your age."
prompt += "\nEnter negetive number to exit. "
age = int(input(prompt))
while age >= 0:
    
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a Teen.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are senior.")
    
    age = int(input(prompt))

