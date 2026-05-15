import loginSignup as ls
import RSA_Keygen

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
                PublicKeyFile = open(r"LabMid\Files\publicKeyTable.txt", "a")
                PublicKeyFile.write(f"\n{signedInUser} {public_key}")
                PrivateKeyFile = open(f"LabMid\\Files\\PrivateKeys\\{username}.txt", "w")
                PrivateKeyFile.write(private_key)
                PublicKeyFile.close()
                PrivateKeyFile.close()
                break          
            print("Account already exists...!")
        else:
            print("Invalid Input")


start()        