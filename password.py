#creating password 
password = input("Enter your password: ")

if len(password) < 8 or not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
    if not any(char.isalpha() for char in password):
        print("It must contain at least one letter.")
    if not any(char.isdigit() for char in password):
        print("It must contain at least one number.")
    if len(password) < 8:
        print("It must contain at least 8 characters.")
else:
    print("Strong password!")
