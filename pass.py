import random
import string
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

length = int(input("Enter the desired password length: "))
password = generate_password(length)
if password:
    print("Generated Password:", password)
length2 = int(input("Enter the desired password length: "))
generate_password(length2)


