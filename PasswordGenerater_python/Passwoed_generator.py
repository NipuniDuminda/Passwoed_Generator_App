import random

# Define Character Sets
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_symbols = '!@#$%^&*()_-+=<>?/[]{}|'

# Create the Password Generator Function
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    characters = ''

    if use_lowercase:
        characters += lowercase_letters
    if use_uppercase:
        characters += uppercase_letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += special_symbols

    if not characters:
        return "No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get User Input
def get_user_input():
    length = int(input("Enter the password length: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include special symbols? (yes/no): ").lower() == 'yes'

    return length, use_lowercase, use_uppercase, use_numbers, use_symbols

# Main Program
if __name__ == "__main__":
    length, use_lowercase, use_uppercase, use_numbers, use_symbols = get_user_input()
    password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)

    if password != "No character set selected.":
        print("Generated Password:", password)
    else:
        print("Please select at least one character set.")
