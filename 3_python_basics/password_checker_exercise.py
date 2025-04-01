username = input("Enter username: ")
password = input("Enter password: ")

password_len = len(password)
hidden_password = "*" * len(password)

print(f"{username}\'s password is {hidden_password} and it is {password_len} long.")
