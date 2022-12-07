from tkinter import *
from tkinter import messagebox
import hashlib
import csv
import os
import game

import loginPage 
from signUp import closeWindow

userArray = []


class User:
    loginSuccess = 0

    def __init__(self, username, password, highscore):
        self.username = username
        self.password = password
        self.highscore = int(highscore)


# ====================================== #
    # Function checks password. If password exists in user array returns true
    def checkUsername(username):

        for users in userArray:
            if users.username == username:
                return True
        return False


# ====================================== #
    # Function takes in a string and returns a hash
    def hashPassword(password):
        passwordenc = str(password)         #*this might be unnnecessary now that ive used the .get method on the submit button?
        md5hash = hashlib.md5(passwordenc.encode('utf-8')).hexdigest()
        return md5hash


# ====================================== #
    # Function takes a hashed password and checks against the objects in the user array
    def checkPassword(hashedP):
        for users in userArray:
            if users.password == hashedP:
                return True
        return False


# ====================================== #
    # Function adds users to the user array and writes to the csv file
    # Checks if username and password already exists if so will pop up with error message and return so user can re try
    # creates new User object with username, the hashed password and highscore of 0, pushes it to the array.
    def addUser(username, password):

        if User.checkUsername(username) == True:
            messagebox.showerror("Error", "This username is already in use")
            return

        hashedP = User.hashPassword(password)

        if User.checkPassword(hashedP) == True:
            return

        newUser = User(username, hashedP, 0)
        userArray.append(newUser)
    
        # * if user sign up is success write their data to database file in append mode ('a)
        with open('userData.csv', 'a', encoding='UTF8', newline='') as userData:
            writer = csv.writer(userData)
            writer.writerow([username, hashedP, 0])

        messagebox.showinfo("Success", "Sign Up Successful")
        closeWindow(True)
        

# ====================================== #
    def getUser(username):
        for users in userArray:
            if users.username == username:
                return users

# ====================================== #
    def userLogin(username, password):

        if username == '':
            messagebox.showerror("Error", "Don't Leave It Blank Bitch")
            return
        # * if username exists in userArray
        if User.checkUsername(username) == True:
            # * runs hash function on string password and returns hash for comparison
            hashedP = User.hashPassword(password)
            if User.checkPassword(hashedP) == True:
                User.loginSuccess += 1
                # * if password hash exists in user array run getUser function which returns matching user object and return the user obj
                currUser = User.getUser(username)
                if User.loginSuccess == 1:
                    gameWindow = game.Toplevel()
                    game.Game(gameWindow, currUser)
                    gameWindow.mainloop()
                return 

            else:
                return messagebox.showerror("Error", "Password is incorrect")

        else:
            return messagebox.showerror("Error", "Username is incorrect")
            
# ====================================== #
    def importUserData():
        # * checks operating system path for userData.csv 
        # * if it exists, it will import the data, if it doesnt, create new csv file
        if os.path.exists('userData.csv'):

            # * if the file exists, it will open it as userData in read mode ('r')
            with open('userData.csv', 'r') as userData:
                reader = csv.reader(userData, delimiter=',')
                line_count = 0
                # * for each row in the reader object returned by csv.reader, 
                # * initialise a new user object with row0(username), row1(password), row3(highscore)
                # * new user obj is appened to the array
                for row in reader:
                    if line_count == 0:
                         line_count += 1
                    else:    
                
                        newUserObj = User(row[0], row[1], row[2])
                        userArray.append(newUserObj)
        else:
            # * header sets template for CSV file as first Row so we know what each value in subsaquent rows stand for
            header = ['username', 'password', 'highscore']

            # * create new CSV file, opens it in write mode ('w'), sets character encoding and newline prevents blank row in between added rows
            with open('userData.csv', 'w', encoding='UTF', newline='') as userData:
                writer = csv.writer(userData)
                writer.writerow(header)


    def updateHighscore(userObject, currScore):
        if currScore > userObject.highscore:
            userObject.highscore = currScore
        header = ['username', 'password', 'highscore']
        with open('userData.csv', 'w', encoding='UTF', newline='') as userData:
                writer = csv.writer(userData)
                writer.writerow(header)
        with open('userData.csv', 'a', encoding='UTF8', newline='') as usr:
            writer = csv.writer(usr)
            for usr in userArray:
                writer.writerow([usr.username, usr.password, usr.highscore])

User.importUserData()