from random import choice
from string import ascii_letters, digits, punctuation

while True:
  try:
    length = int(input("Length: "))
    if length < 7:
      print("Error: Password must be at least 7 characters long. Try again.")
    else:
      break
  except ValueError:
    print("Error: Please enter a valid number for the password length.")

while True:
  try:
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    break
  except ValueError:
    print("Error: Please enter 'y' or 'n' for each character type.")

characters = ''
if use_lowercase:
  characters += ascii_letters.lower()
if use_uppercase:
  characters += ascii_letters.upper()
if use_digits:
  characters += digits
if use_symbols:
  characters += punctuation

password = ""
if characters:
  for _ in range(length):
    character = choice(characters)
    password = password + character
else:
  print("Error: Invalid Character type. dummy")

print(f"Your password is: {password}")
