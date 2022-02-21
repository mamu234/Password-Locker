import random
from user import User

def main():

     while True:
         print("welcome to pssword locker!!")
         print('\n')
         print("choose a short code to creae new user  using 'nu' to login in the account 'lg' or 'ex' to exit")
         short_code = input().lower()
         print('\n')

         if short_code == 'nu'
             print('create username')
             created_user_name = input()

             print('create password')
             created_password = input()

             while confrim_password != created_user_password:
                 print("invalid password  did nto match")
                 print("enter your password")
                 created_user_password = input()
                 print("confirm your password")
                 confrim_password = input()

             else:
                 print(f"congratualtions{created_user_name}! account successfully created")
                 print('\n')
                 print("process to login")
                 print("Username")
                 entred_username = input()
                 print("your password")
                 entered_password = input()

             while entred_username!= created_user_name or entered_password !=created_user_password:
                 print("invalid username or password")
                 print("username")
                 entred_username = input()
                 print("your password")
                 entered_password = input()

            else:
                  print(f"congratulations{created_user_name} ! account created successfuly")
                  print('\n')
                  print("proced to login")
                  print("Username")
                  entered_username = input()
                  print("your password")
                  entered_password = input()

              else:
                  print(f"welcome: {entered_username} to your account")
                  print('\n')


              elif short_code == 'lg':
                  print("welcome")
                  print("enter user name")
                  default_user_name = input()

                  print("enter password")
                  default_user_password = input()
                  print('\n')
                  while default_user_name != 'testuser' or default_user_password != '09876'
                  print("wrong userName or password.Username"  'testuer' and password '09876')
                  print("enter user name")
                  default_user_name = input()


                  print("enter password")
                  default_user_password = input()
                  print('\n')

              else:
                  print("login sucess")
                  print('\n')
                  print('\n')


               elif short_code == 'ex':
                   break
               else:
                   print("enter vslid code to continue")

        
 if __name__ == '__main__':
     main()












