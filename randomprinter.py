import string
import random
import time
letters = string.ascii_letters
target = input("Enter Your Word :")
result = ""
for letter in target:
    while True:
        i = random.choice(letters)
        print(result + i)
        if i == letter:
            result += i
            break
        time.sleep(0.001)