from tkinter import *
from tkinter import messagebox
import hashlib 
userArray = []

class user:
    
    def __init__(self, username, password, highscore):
        self.username = username
        self.password = password
        self.score = int(highscore)
    
    
    #Function checks password. If password exists in user array returns true 
    def checkUsername(username):

         for users in userArray:
            if(users.username == username):
                return(True)
            return(False)

    # Function takes in a string and returns a hash
    def hashPassword(password):
        md5hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        return (md5hash)


    # Function takes a hashed password and checks against the objects in the user array
    def checkPassword(hashedP):
        for users in userArray:
            if(users.password == hashedP):
                return(True)
            return(False)


    # Function adds users to the user array and writes to the csv file
    # Checks if username and password already exists if so will pop up with error message and return so user can re try
    # creates new User object with username, the hashed password and highscore of 0, pushes it to the array.
    def addUser(username, password):

        if(user.checkUsername(username) == True):
            messagebox.showerror("Error", "This username is already in use")
            return

        hashedP = user.hashPassword(password)

        if(user.checkPassword(hashedP) == False):
            messagebox.showerror("Error", "This password is already in use")
            return

        newUser = user(username, hashedP, 0)
        userArray.push(newUser)
        #write to file

    def loginFunction():
        
