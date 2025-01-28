import random  # For randomly selecting characters
import string  # For accessing sets of letters, digits, and special characters


def generate_password(min_lenght, numbers=True, special_characters=True):
    """
    Function to generate a random password.
    
    Parameters:
        min_lenght (int): The minimum length of the password.
        numbers (bool): Whether the password should include numbers.
        special_characters (bool): Whether the password should include special characters.
    
    Returns:
        str: The generated password.
    """
    letters = string.ascii_letters  # Includes all lowercase and uppercase letters
    digits = string.digits  # Includes all digits (0-9)
    special = string.punctuation  # Includes all special characters (!, @, #, etc.)

    # Start with letters as the base set of characters
    characters = letters
    if numbers:
        characters += digits  # Add digits if the user wants numbers in the password
    if special_characters:
        characters += special  # Add special characters if the user wants them

    pwd = ""  # Initialize the password as an empty string
    meets_criteria = False  # Track whether the password meets the criteria
    has_number = False  # Track if the password includes at least one number
    has_special = False  # Track if the password includes at least one special character

    # Continue generating characters until the password meets all criteria
    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)  # Select a random character from the pool
        pwd += new_char  # Add the character to the password

        # Check if the new character is a digit
        if new_char in digits:
            has_number = True
        # Check if the new character is a special character
        elif new_char in special:
            has_special = True

        # Check if the password meets all criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number  # Ensure it has at least one number if required
        if special_characters:
            meets_criteria = meets_criteria and has_special  # Ensure it has at least one special character if required

    return pwd  # Return the generated password


# Get user input for password generation criteria
min_lenght = int(input("Enter the minimum length: "))  # Minimum password length
has_number = input("Do you want to have numbers? (y/n): ").lower() == "y"  # Include numbers
has_special = input("Do you want to have special symbols? (y/n): ").lower() == "y"  # Include special characters

# Generate the password using the specified criteria
pwd = generate_password(min_lenght, has_number, has_special)
print(f"The generated password is: {pwd}")  # Output the generated password
