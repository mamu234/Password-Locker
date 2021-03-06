
import string
from random import *
from user import User
from user import Credentials



def create_user(username,userpassword,phonenumber):
    newuser= User(username,userpassword,phonenumber)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()
def find_user(phonenumber):
    return User.find_by_number
def display_users():
    return User.display_users()

def create_account(accountusername,accountname,accountpassword):
    newaccount=Credentials(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return Credentials.find_by_number
def display_accounts():
    return Credentials.display_accounts()


def main():
        while True:
            print("welcome to password Vault write SU or LG to start")
            print("SU -or- LG")
            option=input()
            if option == "SU":
                print("create Account")
                print("-"*10)   
                print("set your username..")
                username=input()
                print("set your password..")
                userpassword=input()
                print("set your number..")
                usernumber=input()
                save_user(create_user(username,userpassword,usernumber))
                print("your account was successfuly created  these are  your accounts detials")
                print("-*10")
                print(f"name:Username:{username} \nPassword:{userpassword} \nNumber:{usernumber}")
                print("\nUse LOgin to your account with the details")
                print("\n \n")
            elif option == "LG":
             print("your Username")
            loginUsername = input()
            print("your password")
            loginPassword=input()
            
            if find_user(loginPassword):
                print("\n")
                print("you can create several account and also view them")
                print("*60")
                print("AC -or- VC")
                choose=input()
                print("\n")
                if choose == "AC":
                 print("add your credential account")
                print("*25")
                accountusername=loginUsername
                print("account name")
                accountname= input()
                print("\n")
                print("generate password automatically or create new password to generate choose and to type out choose c")
                decision=input()
                if  decision == "G":
                    characters=string.ascii_letter + string.digits
                    accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                    print(f"Password: {accountpassword}")
                elif decision == "C":
                    print ("enter your password")
                    accountpassword=input()
                else:
                    print("please put valid choice")
                    save_user(create_account(accountusername,accountname,accountpassword))
                    print("\n")
                    print(f"Username:{accountusername} \nAccount Name{accountname} \nPassword:{accountpassword}")
            elif choose == "VC":
                if find_user(accountusername):
                    print("here is a list of  accounts created")
                    print("-"*25)
                    for user in display_accounts():
                        print(f"Account: {accountusername}/nName: {user.accountname} \nPassword: {user.accountpassword} \n\n")
            else:
                print("Invalid credentials")
    

if __name__ == '__main__':
    main()












