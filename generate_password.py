import random
import string

def generate_password(length, uppercase, lowercase, digits, symbols, disallowed):
    """Generates a random password based on user-specified requirements"""
    # Define the character sets for each category
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    digits_set = set(string.digits)
    symbols_set = set(string.punctuation)

    # Define the pool of characters based on user's requirements
    pool = set()
    if uppercase:
        pool.update(uppercase_set)
    if lowercase:
        pool.update(lowercase_set)
    if digits:
        pool.update(digits_set)
    if symbols:
        pool.update(symbols_set)
    
    # Remove disallowed characters from the pool
    pool.difference_update(disallowed)

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.sample(list(pool), length))

    return password

# Get user's requirements for password generation
length = int(input("Enter password length: "))
uppercase = input("Require uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Require lowercase letters? (y/n): ").lower() == 'y'
digits = input("Require digits? (y/n): ").lower() == 'y'
symbols = input("Require symbols? (y/n): ").lower() == 'y'
disallowed = set(input("Enter disallowed characters: "))

# Generate a random password that meets the user's requirements
password = generate_password(length, uppercase, lowercase, digits, symbols, disallowed)

# Display the generated password
print("Generated password:", password)
