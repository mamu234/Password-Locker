import unittest 
from user import user


class Testuser(unittest.TestCase):
    """
    test class defines test cases for user class
    unittest.TestCse class  creates test class
    """

def setUp(self):
    """
    setup method runs prior to each test case
    """

    self.new_user = user("Carolyne", "Maunda","mamu234")# created contnct object

def test_init(self):
    """
    test init  is used to test  if the object has been initialized
    """

    self.assertEqual(self.new_user.user_name, "Carolyne")
     
     self.assertEqual(self.new_user.password, "mamu234")


def test_save_user(self):
        """
        test_save_user test used to test if the user object  has been saved in the user list 
        """
        self.new_user.save_user() # use for saving new contact
        self.assertEqual(len(user.user_list),1)
def test_delete_user(self):
        """
        test delete  is used to test if the cotnact can be dlelted from the contact list
        """
        self.new_contact.save_contact()
        test_user = user("Test", "user","0712345678","test@user.com") # for new contact
        test_user.save_user()

        self.new_user.delete_user() # for deleleting cotnact object
        self.assertEqual(len(user.user_list),1)


if __name__"" '__main__':
    unittest.main()