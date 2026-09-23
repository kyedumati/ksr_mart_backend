import logging
logger = logging.getLogger(__name__)
logger.debug("Welcome to login, Im inside login")
actual_password = "Admin@123"
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == actual_password:
        print("login successful")