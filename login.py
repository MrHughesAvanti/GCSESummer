usernames = ["user1","user2","user3","user4"]
passwords = ["pass1","pass2","pass3","pass4"]

def signup():
    newuser = input("enter a new username")
    while checkuname(newuser):
        newuser = ("Sorry thats taken,enter a new username")
    newpwd = input("enter a new password")
    usernames.append(newuser)
    passwords.append(newpwd)
    return    
            

def checkuname(usr):
    for i in range(len(usernames)):
        if usr == usernames[i]:  
            return True
    return False

def checklogin(uname, pwd):
    for i in range(len(usernames)):
        if uname == usernames[i]:  
            if pwd == passwords[i]:
                return True
    return False

def menu():

    print("Welcome! Choose and option below:")
    print("1. Login")
    print("2. Sign Up")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        login()
    elif choice == 2:
        signup()
    else:
        print("Please enter 1 or 2")

def login():

    user = input("enter username")
    userpwd = input("enter a password")


    if checklogin(user, userpwd):
        print("Access Granted")
    else:
        print("Access Denied")

while True:
    menu()
