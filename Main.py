import loginSignup as ls
import RSA_Keygen
import messageManagement as mm

def start():
    signedInUser = ""
    print("\n______________________________\n")
    print("         Login/SignUp")
    print("______________________________\n")

    print("Press 1 to Login")        
    print("Press 2 to SignUp")

    choice = int(input("Your Choice: "))
    while(True):
        if choice == 1:
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            if ls.signin(username, password):
                signedInUser = username
                print(f"Succesfully signedIn! username = {signedInUser} ")
                break
            print("Invalid Credentials! Try again...!")
            # login component
        elif choice == 2:
            # Signup component
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            if ls.signup(username, password) :
                signedInUser = username
                print(f"Succesfully signedIn! username = {signedInUser} ")
                public_key, private_key = RSA_Keygen.generate_key()
                PublicKeyFile = open(r"Files\publicKeyTable.txt", "a")
                PublicKeyFile.write(f"\n{signedInUser} {public_key}")
                PrivateKeyFile = open(f"Files\\PrivateKeys\\{username}.txt", "w")
                PrivateKeyFile.write(private_key)
                PublicKeyFile.close()
                PrivateKeyFile.close()
                break          
            print("Account already exists...! Try again!")
        else:
            print("Invalid Input! Try again")

    while(True):
        print("\n______________________________\n")
        print("         Main Menu")
        print("______________________________\n")

        print("press 1 to send a Message ")
        print("press 2 to View Inbox ")
        print("press 3 to Exit ")
        choice = int(input("Your Choice: "))
        if choice == 1:
            mm.sendMessage(signedInUser)
        elif choice == 2:
            mm.receiveMessage(signedInUser)
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid Input! Try Again")        

start()        