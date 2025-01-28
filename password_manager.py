# from cryptography.fernet import Fernet

# '''
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)'''


# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key


# key = load_key()
# fer = Fernet(key)


# def view():
#     with open('passwords.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print("User:", user, "| Password:",
#                   fer.decrypt(passw.encode()).decode())


# def add():
#     name = input('Account Name: ')
#     pwd = input("Password: ")

#     with open('passwords.txt', 'a') as f:
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# while True:
#     mode = input(
#         "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
#     if mode == "q":
#         break

#     if mode == "view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("Invalid mode.")
#         continue


from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Function to derive a valid Fernet key from a password and salt
def derive_key(master_pwd: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))

# Generate and save a salt (if it doesn't exist already)
def write_salt():
    if not os.path.exists("salt.key"):
        salt = os.urandom(16)  # Generate a new 16-byte random salt
        with open("salt.key", "wb") as salt_file:
            salt_file.write(salt)

# Load the salt from the file
def load_salt() -> bytes:
    with open("salt.key", "rb") as salt_file:
        return salt_file.read()

# Ensure the salt file exists
write_salt()
salt = load_salt()

# Prompt user for the master password and derive the encryption key
master_pwd = input("What is the master password? ")
key = derive_key(master_pwd, salt)
fer = Fernet(key)

# View stored passwords
def view():
    if not os.path.exists("password.txt"):
        print("No passwords stored yet. Add some first.")
        return
    
    with open("password.txt", "r") as f:
        for line in f.readlines():
            user, enc_pass = line.strip().split("|")
            decrypted_pass = fer.decrypt(enc_pass.encode()).decode()
            print(f"Account: {user} | Password: {decrypted_pass}")

# Add a new password
def add():
    account = input("Account name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    
    with open("password.txt", "a") as f:
        f.write(f"{account}|{encrypted_pwd}\n")
    print(f"Password for '{account}' added successfully!")

# Main loop
while True:
    mode = input("Would you like to add a new password or view existing ones (view/add)? Press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option. Try again.")
