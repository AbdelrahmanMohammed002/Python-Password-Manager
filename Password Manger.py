from cryptography.fernet import Fernet

# This function is created and called only one time for the creation of the key. Once it created we comment it.
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb")as key_file:
        key_file.write(key)

write_key()
"""

def load_key():
    return open("key.key", "rb").read()


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            user, pwd = line.rstrip().split(",")
            print(f"User: {user}, Password: {fer.decrypt(pwd.encode()).decode()}")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{name}, {fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view/ add) or (press q to quit): "
    ).lower()

    if mode == "q":
        quit()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
