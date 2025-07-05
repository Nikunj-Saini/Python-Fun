import random
answer = random.randint(0,50)
i = int(input("Choose a number between 1 and 50: "))
while i < 1 or i > 50:
    print("Please enter a valid input between 1 and 50.")
    i = int(input("Choose a number between 1 and 50: "))
while i != answer:
    if i > answer:
        print("high")
    else:
        print("low")
    i = int(input("Enter a number between 1 and 50: "))
    while i < 1 or i > 50:
        print("Please enter a valid input between 1 and 50.")
        i = int(input("Enter a number between 1 and 50: "))
print("congratulation mitr")
