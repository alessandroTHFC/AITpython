from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random


class Game:

    def __init__(self, gameWindow, userObject):

        self.gameWindow = gameWindow
        self.gameWindow.geometry("740x500")
        self.gameWindow.title("Gone Fishin'")
        self.gameWindow.resizable(False, False)
        self.gameWindow.configure(bg='#42BAF1')
        print(userObject.username + " is Logged In")

        self.fishFrame = Frame(self.gameWindow, bg='black', width='700', height='450')
        self.fishFrame.place(x=20, y=20)
        self.txt = "Gone Fishin'"
        self.heading = Label(self.fishFrame, text=self.txt, font=('yu gothic ui', 20, 'bold'), bg='black', fg='#54c4d8')
        self.heading.place(x=250, y=2)

        self.fishBtn = Button(self.fishFrame, text="Play With Ya Rod", bg="#42BAF1", fg="black", cursor="hand2", command=lambda: Game.fishGame(self, userObject))
        self.fishBtn.place(x=20, y= 120)

        # Game.fishGame(self, userObject)
        
    def addThrowKeep(self):
        self.catchBtn = Button(self.fishFrame, text="Keep",  bg="#42BAF1", fg="black", cursor="hand2")
        self.catchBtn.place(x=150, y=380)

    def fishGame(self, userObject):
        fishArray = ['Seaweed Monster', 'King George Whiting',
                        'Lost Bait', 'Small Mulloway','Snapper', 'Large Mullet']
        print(userObject.highscore)
        result = random.choice(fishArray)
        self.fishLabel = Label(self.fishFrame, text=result, bg='black', fg="#42BAF1", width=20)
        self.fishLabel.place(x=40, y=200)
        
        if(result == 'Seaweed Monster'):
            imgBox = Image.open('seaweed.jpg')
            resized_image = imgBox.resize((350, 300))
            img = ImageTk.PhotoImage(resized_image)
            imgBoxLabel = Label(self.fishFrame, image=img, bg='black')
            imgBoxLabel.image = img
            imgBoxLabel.place(x=250, y = 50)
            Game.addThrowKeep(self)
        # elif(result == 'King George Whiting'):

