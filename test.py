import unittest
import main
from unittest import mock
from main import getPIN, getUsername, getEmail, getID, getName,signUp,modifyAccounts
from main import login, checkAdminStatus, checkIfUser, testIfUsernameIsAlreadyUsed, testIfUsernameExists
from main import deposit, withdraw,checkBalance,displayAccounts,removeAccount
from contextlib import redirect_stdout

class testClass(unittest.TestCase):
    def setUp(self):
        main.currentUserID=1
        main.currentUser="JamesTown"
    @mock.patch("main.input")

    def testIfUsernameGotten(self,mock_input):
        self.assertEqual(getUsername(main.currentUserID),"JamesTown")

    def testIfPINGotten(self):
        self.assertEqual(getPIN(1),12)

    def testIfEmailGotten(self):
        self.assertEqual(getEmail(1),"JJ@gmail")

    def testIfNameGotten(self):
        self.assertEqual(getName(1),"James")

    def testIfIDGotten(self):
        self.assertEqual(getID("JamesTown"),1)

    def testIfAdmin(self):
        self.assertFalse(checkAdminStatus(12))
        self.assertTrue(checkAdminStatus(1))

    #def testIfLoggedIn(self):
     #   self.assertTrue(login())

    def checkUserStatus(self):
        self.assertTrue(checkIfUser("JamesTown",12))
        self.assertFalse(checkIfUser("chickenPie",876))
        self.assertTrue(testIfUsernameExists("jj"))
        self.assertFalse(testIfUsernameExists("Donald Duck"))
        self.assertTrue(testIfUsernameIsAlreadyUsed("jj"))
        self.assertFalse(testIfUsernameIsAlreadyUsed("Cart"))

    def testWithdraw(self):
        currentUserID=1
        currentUser="JamesTown"
        print(withdraw(12))
        print(withdraw("12"))

    def testDeposit(self):
        currentUserID=1
        currentUser="JamesTown"
        print(deposit(12))
        print(deposit("12"))
    def testBalance(self):
        currentUserID=1
        currentUser="JamesTown"
        print(checkBalance())
    def testAccount(self):
        currentUserID=14
        currentUser="Christopher"
        #self.assertEqual(signUp(),"Brand")
        print(modifyAccounts(5,True))
        print(displayAccounts())
        self.assertTrue(removeAccount(14))

if __name__=="__main__":
    unittest.main() 