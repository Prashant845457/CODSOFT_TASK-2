import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters

    if include_digits:
        chars += string.digits

    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage
password_length = int(input("Enter the length of the password: "))
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

generated_password = generate_password(password_length, include_digits, include_special_chars)
print(f"Generated Password: {generated_password}")