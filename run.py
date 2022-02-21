
import pyperclip
from user import User
/usr/bin/env python3.6

def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()

def main():
        while True:
            print("welcome to password Vault write SU or LG to start")
            print("SU -or LG")
            option-input()
            if option == "SU":
                print("create Account")
                print("-")     

if __name__ == '__main__':
    main()












