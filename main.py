import random
import string

def generate_password(length):

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = (
        uppercase_letters +
        lowercase_letters +
        digits +
        special_characters
    )

    # Ensure password contains at least one character from each category
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill remaining length randomly
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle password for randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)


# Main Program
print("=" * 50)
print("            PASSWORD GENERATOR")
print("=" * 50)

try:
    
    password_length = int(input("Enter desired password length (minimum 4): "))

    if password_length < 4:
        print("\nPassword length should be at least 4.")

    else:
        secure_password = generate_password(password_length)

        print("\nGenerated Secure Password:")
        print(secure_password)

        print("\nPassword generated successfully!")

except ValueError:
    print("\nInvalid Input! Please enter a numeric value.")