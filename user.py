

class User :
   """
   Class that generates news isntance of user

   """

   userlist = []
   def __init__(self,user_name,password,phonenumber):
       self.user_name = user_name
       self.password = password
       self.phonenumber = phonenumber

   def  save_user(self):

        """
        save-user method is used to  create new user objects to the user_list 

        """     
        User.userlist.append(self)
   
   def delete_user(self):# delete method deletes saved user from the userlist
         
       User.userlist.remove(self)

   @classmethod
   def display_users(cls):
       return cls.userlist


   @classmethod
   def find_by_number(cls,phonenumber):

       for user in cls.userlist:
           if user.phonenumber== phonenumber:
               return True

#    @classmethod
#    def clear_all(cls):
#        if(len(cls.userlist) == 0):
#                 return "Empty"
       else:
            for user in cls.userlist:
                cls.userlist.remove(user)

class Credentials:
    """
    this class generates new isntnaces of Credentials
    """

    accounts =[]
    def __init__(self,accountusername,accountname,accountpassword):
        """
        init methos helps define propertie of the object
        """

        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
    def save_account(self):
        """
        save account method saves user info in the accounts
        """

        Credentials.account.append(self)

    def delete_account(self):
        """
        delete_account  method removes thesaves credentials from accounts
        """

        Credentials.accounts.remove(self)
    @classmethod
    def display_accounts(cls):
        """
        display_accounts returns a list of the accounts
        """
        for account in cls.accounts:
            return cls.accounts
        
    @classmethod
    def find_by_number(cls,number):
        """
        find by number method takes in a nubmer and return a contact if it matches the number
        """
        for account in cls.accounts:
            if account.accountusername == number:
                return account



