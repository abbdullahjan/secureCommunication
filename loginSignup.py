import hashlib


def signup(username, password):
   username = username.lower()
   userIndex = userExists(username)
   if(userIndex != -1):
       return 0 #Invalid Operation | user already exsts
   else:
       createUser = open(r"LabMid\Files\users.txt", "a")
       hashedPassword = hashPass(password)
       createUser.write(f'\n{username} {hashedPassword}')
       createUser.close()
       return 1

def userExists(username):
    checkUser = open(r"LabMid\Files\users.txt", "r")
    Allusers = checkUser.readlines()
    j = 0
    for i in Allusers:
        user = i.split(" ")
        if user[0] == username:
            checkUser.close()
            return j,user[1] 
        j += 1
    checkUser.close()
    return -1

def hashPass(password):
    return hashlib.sha256(password.encode()).hexdigest()       

def signin(username,password):
    userIndex, storedPassword = userExists(username);
    if userIndex == -1:
        return 0
    hashedPassword = hashPass(password)
    if hashedPassword == storedPassword:
        return 1
    else: 
        return 0