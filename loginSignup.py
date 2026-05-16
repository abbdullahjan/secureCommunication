import hashlib


def signup(username, password):
   username = username.lower()
   userIndex, _ = userExists(username)  # Unpack tuple properly
   if(userIndex != -1):
       return 0 #Invalid Operation | user already exsts
   else:
       createUser = open(r"Files\users.txt", "a")
       hashedPassword = hashPass(password)
       createUser.write(f'\n{username} {hashedPassword}')
       createUser.close()
       return 1

def userExists(username):
    checkUser = open(r"Files\users.txt", "r")
    Allusers = checkUser.readlines()
    j = 0
    for i in Allusers:
        if i.strip():  # Skip empty lines
            user = i.strip().split(" ")
            if user[0] == username:
                checkUser.close()
                return j, user[1] 
            j += 1
    checkUser.close()
    return -1, None  # Return tuple consistently

def hashPass(password):
    return hashlib.sha256(password.encode()).hexdigest()       

def signin(username,password):
    userIndex, storedPassword = userExists(username)
    if userIndex == -1:
        return 0
    hashedPassword = hashPass(password)
    if hashedPassword == storedPassword.strip():  # Strip newline from stored password
        return 1
    else: 
        return 0