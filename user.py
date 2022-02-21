class User :
   """
   this class generates news isntance of user

   """

   userlist = []

   def __init__(self,firstname,lastname,username,password):
       self.firstname = firstname
       self.lastname = lastname
       self.username = username
       self.password = password

   def  save_user(self):

         """
         save-user method is used to  create new user objects to the user_list 

         """     
         User.user_list.append(self)
