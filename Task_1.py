import secrets         # secrets module : To generate strong random numbers
import string          # string module : A collection of string constants 

length = int(input("Enter password length: "))        # Take password length from user

# Characters to use
letters = string.ascii_letters      # a-z A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # !@#$%^&* etc.

all_chars = letters + digits + symbols       # Combine all characters

password = ""         # Generate password
for i in range(length):
    password += secrets.choice(all_chars)

print("Generated Strong Password:", password)      # Display result
