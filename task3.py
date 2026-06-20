# Password Generator Tool

import random
import string

# Ask user for password length
length = int(input("Enter the password length: "))

# Characters to use in password
characters = string.ascii_letters + string.digits

# Generate random password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display generated password
print("Generated Password:", password)