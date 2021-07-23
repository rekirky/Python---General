name = "ziga"
password = 123

user_input = input("Please enter your name:\n")
if user_input == name:
    print("Success!")
    user_input_password = int(input("Please enter your password: \n"))
    if user_input_password == password:
        print(f"Welcome back {name}")
    else:
        print(f"password invalid")
        exit()
else:
    print("Name invalid")
    exit()