loggedIn=False;


print("Welcome to Robs Bank.\n");
loginInput=input("Before we get Stated, please sign in.\nPush 1 for Sign in.\nDon't have an Account? Create One now");

while(loggedIn==False):
    if (loginInput==1):
       print("Put login function here");
       loggedIn=True;
    elif (loginInput==2):
        print("Put Sign Up function here");
        loggedIn=True;
    else:
        print("I'm sorry, that isn't a valid option")
        loginInput=input("Before we get Stated, please sign in.\nPush 1 for Sign in.\nDon't have an Account? Create One now");
print("Welcome to the Bank\n");
userInput=input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.That's All")
while (userInput!=4):
    if(userInput==1):
        print("Your Balance is good");
        userInput=input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.That's All")
    if(userInput==2):
        print("Put Withdraw function here");
        userInput=input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.That's All")
    if(userInput==3):
        print("put balance function here");
        userInput=input("What would you like to do?\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.That's All")