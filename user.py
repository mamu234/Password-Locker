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
    