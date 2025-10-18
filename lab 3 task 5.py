def login_system():
    username = "admin"
    password = "12345"
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if user == username and pwd == password:
        print("Login successful! Welcome,", user)
    else:
        print("Invalid username or password. Please try again.")
login_system()
