from tkinter import *
from PIL import ImageTk, Image
import loginPage as lp
import user as user


def openRegisterWindow():
    username = StringVar()
    password = StringVar()

    registerWindow = Toplevel()
    registerWindow.title("Sign Up")
    registerWindow.geometry("400x400")
    registerWindow.configure(bg='black')
    registerWindow.resizable(False, False)

    heading = Label(registerWindow, text='Sign Up', bg='black', fg='#54c4d8', font=('yu gothic ui', 25, 'bold'))
    heading.place(x=145, y=10)
    
    # sign up icon
    signUpImg = Image.open('signUpIcon.png')
    resized= signUpImg.resize((80,80))
    img = ImageTk.PhotoImage(resized)
    imgLabel = Label(registerWindow, image=img, bg='black')
    imgLabel.image = img
    imgLabel.place(x=165, y=68)

    # user entry area
    usrLabel = Label(registerWindow, text='Username', bg='black', fg='#54c4d8', font=('yu gothic ui', 14))
    usrLabel.place(x=10, y=160)
    usrEntry = Entry(registerWindow, highlightthickness=0, relief=FLAT, bg='#F1A742', fg='black', font=('yu gothic ui', 11), width=25,textvariable=username)
    usrEntry.place(x=110, y=165)

    # user password area
    pswLabel = Label(registerWindow, text='Password', bg='black', fg='#54c4d8', font=('yu gothic ui', 14))
    pswLabel.place(x=10, y=225)
    pswEntry = Entry(registerWindow, highlightthickness=0, relief=FLAT, bg='#F1A742', fg='black', font=('yu gothic ui', 11), width=25, show='*',textvariable=username)
    pswEntry.place(x=110, y=229)

    # sign up button
    signupButton = Button(registerWindow, text='Sign Up', bg='#F1A742', fg='black', width=10, cursor='hand2, 'command=user.addUser())
    signupButton.place(x=170, y=285)
    # TODO: See if there is a way to close window on successful return of addUser function? OR successful message pops up and on click of button close register window?