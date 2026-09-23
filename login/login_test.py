print("Im inside login page")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "Admin@123":
        print("login successful")