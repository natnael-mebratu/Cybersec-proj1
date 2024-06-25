#hash and hide a string
import hashlib
import getpass # hide the user inputed password
#dict to store key value pairs
password_manager = {}

def create_account():
    username = input("Enter your desired User name\n")
    while True:
              password = getpass.getpass("Enter your desired password\n:")
              if len(password) >= 10:
                   break
              else:
                   print("Password length too short, minimum length is 10")
                
    hashed_password = hashlib.sha256(password.encode()).hexdigest()#hexdigest() converts this byte array into a human-readable string format using hexadecimal characters (0-9 and A-F).
    password_manager[username] = hashed_password
    print("Account created successfully")


def login_account():
    username = input("Enter your User Name\n")
    password = getpass.getpass("Enter your password\n")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Sucess")
    else:
        print("Invalid Username or password")

def main():
    while True:
        choice = input("Enter 1 to create account, 2 to Login, 3 to exit\n")
        if choice == "1":
            create_account()
        elif choice == "2":
            login_account()
        elif choice == "3":
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()