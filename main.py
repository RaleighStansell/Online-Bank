import mysql.connector
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
print("connected")
connection.close()
loggedIn=False
global currentUser
global currentUserID


#reformats the table so all id's are sequential.
def restructureMySQL():
    global currentUserID
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT id FROM accounts")
    idList=cursor.fetchall()
    cursor.close()
    connection.close()
    #Loops through every id in the table, and resetes their value sequentially.
    for i,values in enumerate(idList):
        values=int(values[0])
        if values==currentUserID:
            currentUserID=i+1
            print(f"Your ID={currentUserID}")
        connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
        cursor=connection.cursor()
        cursor.execute(f"Update accounts Set id={i+1} Where id={values}")
        connection.commit()
        cursor.close()
        connection.close()
#Takes in the parameter of an ID and returns the username connected to that ID
def getUsername(id):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    result=cursor.fetchone()
    username=result[3]
    cursor.close()
    connection.close()
    return username

#Takes in the parameter of an ID and returns the PIN connected to that ID
def getPIN(id):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    result=cursor.fetchone()
    pin=result[4]
    cursor.close()
    connection.close()
    return pin

#Takes in the parameter of an ID and returns the email connected to that ID
def getEmail(id):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    result=cursor.fetchone()
    email=result[2]
    cursor.close()
    connection.close()
    return email

#Takes in the parameter of an ID and returns the name connected to that ID
def getName(id):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    result=cursor.fetchone()
    name=result[1]
    cursor.close()
    connection.close()
    return name
#Tests whether or not the person connected to the ID is an admin
def checkAdminStatus(id):
    
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    result=cursor.fetchone()
    admin=result[6]
    cursor.close()
    connection.close()
    return admin

#Removes a certain amount of money from the users account based on the parameter.
def withdraw(amount):
    if(type(amount)!=float and type(amount)!=int):
        while(amount.isdigit()==False ):
            # root=Tk()
            # print1=Label(root,text="I'm sorry, that isn't a number")
            # print1.pack()
            # root.mainloop()
            print("I'm sorry, that isn't a number")
            amount=(input("Select Amount You'd like to Withdraw: "))
        amount=round(float(amount),2)
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    addMoney=(f"UPDATE accounts SET balance=balance-{amount} WHERE id={currentUserID}")
    cursor.execute(addMoney)
    connection.commit()
    cursor.close()
    connection.close()
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={currentUserID}")
    result = cursor.fetchone()
    userBalance=result[5]
    cursor.close()
    connection.close()
    if(userBalance<0):
        print(f"Balance: -${abs(userBalance)}\n")
    else:
        print(f"Balance: ${abs(userBalance)}\n")
#ads a certain amount of money to a users account based on the parameter
def deposit(amount):
    if(type(amount)!=float and type(amount)!=int):
        while(amount.isdigit()==False):
            print("I'm sorry, that isn't a number")
            amount=(input("Select Amount You'd like to Deposit: "))
        amount=round(float(amount),2)
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    addMoney=(f"UPDATE accounts SET balance=balance+{amount} WHERE id={currentUserID}")
    cursor.execute(addMoney)
    connection.commit()
    cursor.close()
    connection.close()
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id={currentUserID}")
    result = cursor.fetchone()
    userBalance=result[5]
    cursor.close()
    connection.close()
    if(userBalance<0):
        print(f"Balance: -${abs(userBalance)}\n")
    else:
        print(f"Balance: ${abs(userBalance)}\n")
#checks the balance of the current user, and print it out. (also tells them if they are in debt)
def checkBalance():
    global currentUser
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    balance=(f"SELECT * FROM accounts WHERE username='{currentUser}'")
    cursor.execute(balance)
    result = cursor.fetchone()
    userBalance=result[5]
    cursor.close()
    connection.close()
    if(userBalance<0):
        print(f"Balance: ${abs(userBalance)} in debt\n")
    else:
        print(f"Balance: ${abs(userBalance)}\n")
#Tests if the username in the parameter exists, returns true if used and false if not.
def testIfUsernameExists(username):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username='"+username+"'")
    result = cursor.fetchone()
    #Checjs to make sure the result exists
    if(result is not None):
        chosenUsername = result[3]
    else:
        chosenUsername=""
    cursor.close()
    connection.close()
    # If the result doesn't exist return false, else return true
    if(len(chosenUsername)==0):
        print("I'm sorry, that username is incorrect")
        return False
    else:
        return True
#tests if the username is already used, returns true if the username is used and false if not.
def testIfUsernameIsAlreadyUsed(username):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT username FROM accounts Where username='{username}' Limit 1")
    userExists=False
    result=cursor.fetchone()
    #If the result is empty, return true
    if result is not None:
        userExists=True
    cursor.close()
    connection.close()
    return userExists
#Tests if the someone is a user based on the parameters of their username and PIN.
#If they aren't a user, they are prompted if they would like to continue logging in.
#Should they refuse to continue or their username isn't in the list, the function returns false.
#Otherwise, the functions returns true.
def checkIfUser(username,pin):
    if(testIfUsernameExists(username)==True):
        connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username='"+username+"'")
        result = cursor.fetchone()
        testPin = result[4]
        cursor.close()
        connection.close()
        if(pin==testPin):    
            print("Your signed in")
            return True
        else:
            print("I'm sorry that pin or username is incorrect")
            continueToSignIn=input("Would you like to continue logging in?(y/n) ")
            if(continueToSignIn=="y"):
                login()
            elif(continueToSignIn=="n"):
                return False
    else:
        print("I'm sorry that pin or username is incorrect")
        return False
#Returns the ID of the user based on the username in the parameter.
def getID(username):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM accounts where username='{username}'")
    result=cursor.fetchone()
    #If the id of the username doesn't exist, the ID is returned as 0.
    if(result is not None):
        currentID=result[0]
    else:
        currentID=0
    cursor.close()
    connection.close()
    return currentID
#Displays all the accunts based on the id input, including username, email, name, PIN, and Balance.
def displayAccounts(id):
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    #If the ID is a number, it prints out only the information for that ID
    #Otherwise, the information for all accounts is displayed.
    if(id is not None):
        cursor.execute(f"SELECT * FROM accounts WHERE id={id}")
    else:
        cursor.execute(f"SELECT * FROM accounts")
    root=Tk()
    root.geometry("1000x1000")
    root.title("Accounts")
    root.resizable(0, 0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.columnconfigure(5,weight=1)

    # Email label
    email_label = ttk.Label(root, text="Name:")
    email_label.grid(column=1, row=0)
    # Name label
    name_label = ttk.Label(root, text="Email:")
    name_label.grid(column=2, row=0)
    # Username label
    username_label = ttk.Label(root, text="Username:")
    username_label.grid(column=3, row=0)
    # Password label (you can add an entry widget here)
    password_label = ttk.Label(root, text="Password:")
    password_label.grid(column=4, row=0)
    # Balance label (you can add an entry widget here)
    balance_label = ttk.Label(root, text="Balance:")
    balance_label.grid(column=5, row=0)

    # ID label (you can add an entry widget here)
    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=0)
    for i, items in enumerate(cursor):
        idAdded=ttk.Label(root,text=items[0])
        idAdded.grid(column=0,row=i+1)
        name_label = ttk.Label(root, text=items[1])
        name_label.grid(column=1, row=i+1)
        email_label = ttk.Label(root, text=items[2])
        email_label.grid(column=2, row=i+1)
        username_label = ttk.Label(root, text=items[3])
        username_label.grid(column=3, row=i+1)
        password_label = ttk.Label(root, text=items[4])
        password_label.grid(column=4, row=i+1)
        balance_label = ttk.Label(root, text=f"${items[5]}")
        balance_label.grid(column=5, row=i+1)
    root.mainloop()
    cursor.close()
    connection.close()
#Removes the account connected to the ID in the parameter.
def removeAccount(id):
    global currentUserID
    deleteAccount=False
    checkOneForDelete=input("By clicking continue, you are agreeing to delete the allocated account and sign out\nwould you like to continue?\n(y/n)")
    #Initiates multiple checks to ensure the user truly wants to delete the account.
    if(checkOneForDelete=="y"):
        checkTwoForDelete=input("Are you sure you want to delete your account?(y/n)")
        if(checkTwoForDelete==("y")):
            deleteAccount=True
    #Deletes the account if both cheks equal true
    if(checkOneForDelete=="y" and checkTwoForDelete=="y"):
        connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
        cursor=connection.cursor()
        cursor.execute(f"DELETE FROM accounts WHERE id={id}")
        connection.commit()
        cursor.close()
        connection.close()
        print("Account Deleted")
        restructureMySQL()
        #If the account is the users account, signs the user out and return true.
        if(deleteAccount==True and currentUserID==id):
            currentUser=None
            loggedIn=False
            return True
        else:
            return False
    else:
        print("Okay\n")
#Prompts the user with ways to modify accounts based on the ID entered and whether or not they are an admin.
def modifyAccounts(id,admin):
    global currentUser
    modifier=int(input("What would you like to modify?\n1.Username\n2.PIN\n3.Name\n4.Email\n5.That's All\n"))
    #Loops continuously until the user requests otherwise
    while(modifier!=5):
        #If the user enters in the number one, it allos them to modify the username connected to the ID.
        if(modifier==1):
            newUsername=input("Username: ")
            #Prevents the user from changing their username when someone else already uses it.
            while(testIfUsernameIsAlreadyUsed(newUsername)==True):
                print("\nThat username is already used")
                newUsername=input("Username: ")
            connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
            cursor=connection.cursor()
            cursor.execute(f"Update accounts Set Username='{newUsername}' Where id={id}")
            connection.commit()
            cursor.close()
            connection.close()
            #If they aren't an admin, the users username is changed.
            if(admin==False):
                currentUser=newUsername
        #If the user chooses the second option, allows them to change the pin based on the  ID.
        if(modifier==2):
            newPIN=input("PIN: ")
            connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
            cursor=connection.cursor()
            cursor.execute(f"Update accounts Set PIN={newPIN} Where id={id}")
            connection.commit()
            cursor.close()
            connection.close()
        #If the user chooses the third option, they are prompted on how to change the name based on the ID.
        if(modifier==3):
            newName=input("Name: ")
            connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
            cursor=connection.cursor()
            cursor.execute(f"Update accounts Set Name='{newName}' Where id={id}")
            connection.commit()
            cursor.close()
            connection.close()
        #Should the user choose the fourth option, they can change the email of the account connected to the ID.
        if(modifier==4):
            newEmail=input("Email: ")
            connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
            cursor=connection.cursor()
            cursor.execute(f"Update accounts Set email='{newEmail}' Where id={id}")
            connection.commit()
            cursor.close()
            connection.close()
        #If the user is an admin, display all accounts. Otherwise, display their account.
        if(admin==True):
            displayAccounts(None)
        else:
            displayAccounts(id)
        modifier=int(input("What would you like to modify?\n1.Username\n2.PIN\n3.Name\n4.Email\n5.That's All\n"))
#The login function decides if the user may log in based on what they input for their username and PIN in the funciton.
#Once successfully logged in, the user is then stated as the current user.
def login():
    print("\nPlease enter in your username and your numerical PIN to continue")
    userUsername=input("Username: ")
    userPin=int(input("PIN: "))
    #Loops continuously if the username and PIN don't match an account.
    while(checkIfUser(userUsername,userPin)==False):
        
        print("I'm sorry, you don't seem to have an account")
        requestSignUp=input("Would you like to sign up and join our bank?(y/n)")
        #If the user agrees to sign up since they don't have an account, they are redirected to the sign up function.
        #Otherwise, they are prompted to try again.
        if(requestSignUp=="y"):
            signUp()
        else:
            print("\nPlease enter in your username and your numerical PIN to continue")
            userUsername=input("Username: ")
            userPin=int(input("PIN: "))
    loggedIn=True
    
    currentUser=userUsername   
    return currentUser
#Allows the user to sign up and create an account. Then adds the account to the SQL list.
def signUp():
    print("Welcome to Rob's Bank, please enter in the required information to \njoin us")
    
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    cursor.execute(f"Select * from accounts where id={1}")
    r=cursor.fetchone()
    userUsername=r[3]
    connection.commit()
    cursor.close()
    connection.close()
    #Loops until the username entered isn't already used.
    #Lets the user input a username, email, name, pin, and bank account balance.
    while(testIfUsernameIsAlreadyUsed(userUsername)==True ):
        root=Tk()
        userName=input("Name: ")
        userEmail=input("Email: ")
        userUsername=input("Username: ")
        userPin=int(input("PIN: "))
        userBalance=float(input("Starting Balance: ")) 
    print("connected")
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    cursor=connection.cursor()
    addAccount=(f"INSERT INTO  accounts(Name, email, username, PIN, balance, isAdmin)VALUES('{userName}','{userEmail}','{userUsername}',{userPin}, {abs(userBalance)}, {False})")
    cursor.execute(addAccount)
    connection.commit()
    cursor.close()
    connection.close()
    loggedIn=True
    return userUsername
#The main function where all functions come together.
def main():
    
    connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Psych0S0ng!')
    print("connected")
    connection.close()
    #Sets the global variables for the program.
    loggedIn=False
    global currentUser
    global currentUserID

    print(f"Welcome to Robs Bank.\n")
    loginInput=int(input("Before we get Stated, please sign in.\nPush 1 for Sign in.\nDon't have an Account? Press 2 to Create One now\n"))
    #Loops continuously while logged in is false.
    #Prompts the user whether or not they want to sign in.
    while(loggedIn==False):
        #If the user inputs the number 1, calls the login function and sets loggedIn to equal true.
        if (loginInput==1):
            currentUser=login()
            currentUserID=getID(currentUser)
            restructureMySQL()
            loggedIn=True
        #Else if the user inputs number 2, the sign up function is called and loggedIn is set to true.
        elif (loginInput==2):
            currentUser=signUp()
            currentUserID=getID(currentUser)
            loggedIn=True
        #Else, recalls the user input to choose one of the 2 options
        else:
            print("I'm sorry, that isn't a valid option")
            loginInput=input("Before we get Stated, please sign in.\nPush 1 for Sign in.\nDon't have an Account? Create One now");
    
    #Tests if the user is logged in or not.
    if(currentUser is not None):
        print(f"Welcome to Robs Bank {currentUser}.\n")

        userInput=int(input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Modify Account\n5.Remove Account\n6.That's All\n"))
        #Loops as long as the user doesn't input the number 6.
        while (userInput!=6):
            #If the user enters the number 1, call the check balance function.
            if(userInput==1):
                checkBalance()
            #If the user enters the number 2, prompt them to enter a number to deposit.
            #Then, call the deposit function with the inputted number as the parameter.
            if(userInput==2):
                amountDeposited=(input("Select Amount You'd like to Deposit: "))
                #amountDeposited=round(amountDeposited,2)
                deposit(amountDeposited)
            #If the user enters the number 3, prompt them to enter a number to withdraw.
            #Then, call the withdraw function with the inputted number as the parameter.
            if(userInput==3):
                amountDeposited=(input("Select Amount You'd like to Withdraw: "))
                #amountDeposited=round(amountDeposited,2)
                withdraw(amountDeposited)
            #If the user inputs the number 4, display accounts based on admin status.
            #Then, allow the user to input a number and call the modify accounts function with
            #the number and the users admin status as parameters.
            if(userInput==4):
                #If the user is an admin, display all accounts and allow the user to choose
                #the id of the accounts they want to modify.
                if(checkAdminStatus(currentUserID)==1):
                    displayAccounts(None)
                    accountToChange=int(input("What is the ID of the account you would like to change? "))
                    modifyAccounts(accountToChange,True)
                #Otherwise, modify the users account.
                else:
                    modifyAccounts(currentUserID,False)
            #Lastly if the user inputs the number 5, delete accounts based on the users admin status.
            if(userInput==5):
                #If the user is an admin, display all accounts and allow them to delete a specific account.
                if(checkAdminStatus(currentUserID)==True):
                    displayAccounts(None)
                    accountToDelete=int(input("What is the ID of the account you want to delete? "))
                    deletedMyAccount=removeAccount(accountToDelete)
                    #If the user deletes their account, sign them out.
                    if(deletedMyAccount==True):
                        loggedIn=False
                        currentUserID=None
                        currentUser=None
                        break
                #Otherwise, delete the current users account.
                else:
                    deletedMyAccount=removeAccount(currentUserID)
                    #Signs the user out as an extra precaution.
                    if(deletedMyAccount==True):
                        loggedIn=False
                        currentUserID=None
                        currentUser=None
                        break
            userInput=int(input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Modify Account\n5.Remove Account\n6.That's All\n"))
    print("Have a lovely day.")
if __name__ == "__main__":
    main()    