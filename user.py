import random 
import string


class User:
"""
generate new instance of contact

"""
    userslist =[]

    def __init__ (self,firstname, lastname,password)

    """
the init method  defines properties of our object
    """

    self.firstname = firstname
    self.lastname =lastname
    self.password = password

def save_user(self):
    """
this method saves user information to the userslist
    """

    User.userslist.append(self)

def delete_user(self):
    """

    the delete  method removes user from th userlist
    """
    User.userslist.remove(self)

@classmethod 
def display_users(cls):
    """
    the class method checks  for infromation in the class user 
    the display  user method displays info from the userlist

"""

return cls.userslist
@classmethod
def find_by_number(cls, number):
"""
the find by number method takes in a suername to return the nubmer that matches  the inouted number

"""
for user in cls.userslist:
    if user.password == number:
        return True
        return False 
        
        
class Credentials :
    """
    the credential class is used to generate new instance of credentials

    """
    accounts=[]
def __init__(self,accountusername,accountname,accountpassword):
"""
init method is used  to define properties of credentisls 
"""

    self.accountusername =accountusername
    self.accountname = accountname
    self.accountpassword =accountpassword

def save_account(self):

    """
    def save  methos  saves user infromation into the account list
    """

   Credentials.accounts.append(self)

def delete_account(self):
    """

    the delete  method removes account from th account 
    """
   Credentials.accounts.remove(self)

@classmethod 
def display_accounts(cls):
    """
    the class method checks  for infromation in the class credentials 
    the display account method displays info from the accounts

"""

return cls.accounts
@classmethod
def find_by_number(cls, number):
"""
the find by number method takes in a suername to return the nubmer that matches  the inouted number

"""
for account in cls.accounts:
    if account.accountusername== number:
        return True
        return False 


