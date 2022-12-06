from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import signUp as sU
from user import User


class loginPage: 
    

    # Main Window Area(black area)
    def __init__(self, window):

        username = StringVar()
        password = StringVar()

        # main window set up
        self.window = window
        self.window.geometry("740x500")
        self.window.title("Gone Fishin'")
        self.window.resizable(False, False)

        # background image
        self.background = Image.open('background.jpg')
        bg = ImageTk.PhotoImage(self.background)
        self.background = Label(self.window, image=bg)
        self.background.image = bg
        self.background.pack(fill='both', expand='yes')

        # Internal Login Frame (black area)
        self.lgn_frame = Frame(self.window, bg='black', width='700', height='350')
        self.lgn_frame.place(x=20, y=65)
        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 20, 'bold'), bg='black', fg='#54c4d8')
        self.heading.place(x=464, y=2)


        # login area widgets
        # ====================
        # log in avatar
        self.logInImg = Image.open('logIn.png')
        resized_logIn= self.logInImg.resize((100,100))
        img = ImageTk.PhotoImage(resized_logIn)
        self.logInImg_label = Label(self.lgn_frame, image=img, bg='black')
        self.logInImg_label.image = img
        self.logInImg_label.place(x=480, y=45)
        # Sign in Label
        self.sign_in_label = Label(self.lgn_frame, text='Sign In', bg='Black', fg='#54c4d8', font=('yu gothic ui', 15))
        self.sign_in_label.place(x=500, y=150)
        # Username Label
        self.usernameLabel = Label(self.lgn_frame, text='Username', bg='black', fg='#54c4d8', font=('yu gothic ui', 12))
        self.usernameLabel.place(x=360, y=185)
        # Username EntryField
        self.usernameEntry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#F1A742', fg='black', font=('yu gothic ui', 11), textvariable=username)
        self.usernameEntry.place(x=450, y=189)
        # Password Label
        self.passwordLabel = Label(self.lgn_frame, text='Password', bg='black', fg='#54c4d8', font=('yu gothic ui', 12))
        self.passwordLabel.place(x=360, y=225)
        # Password EntryField
        self.passwordEntry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#F1A742', fg='black', font=('yu gothic ui', 11), show='*', textvariable=password)
        self.passwordEntry.place(x=450, y=227)
        # Log In Button
        self.loginButton = Button(self.lgn_frame, text='Sign In', bg='#F1A742', fg='black', width=10, cursor='hand2', command=lambda: User.userLogin(username.get(), password.get()))
        self.loginButton.place(x=492, y=275)
        # Sign Up Buton
        self.signUpButton = Button(self.lgn_frame, text='Not a Member? Sign Up', font=('yu gothic ui', 9, 'underline'), fg='#54c4d8', bg='black', bd=0 ,cursor='hand2', command=sU.openRegisterWindow)
        self.signUpButton.place(x=466, y=318)


        # fish image area
        # =================
        self.side_image = Image.open('fishing.png')
        resized_image= self.side_image.resize((270,300))
        photo = ImageTk.PhotoImage(resized_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='black')
        self.side_image_label.image = photo
        self.side_image_label.place(x=1, y=10)
        fishTxt = "Gotta Catch 'Em All"
        self.fishHeading = Label(self.lgn_frame, text=fishTxt, font=('Kozuka Mincho Pro L', 20, 'bold'), bg='black', fg='#54c4d8')
        self.fishHeading.place(x=15, y=305)


