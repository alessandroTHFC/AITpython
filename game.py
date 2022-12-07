from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import user


# TODO: add other pictures with more elifs
# TODO: increase score based on throw or keep, put label with updated score
# TODO: make fishing button disseaper until you have selected to keep or throw? 

class Game:


    currScore = 0

    # * Initialise game window
    def __init__(self, gameWindow, userObject):

        self.gameWindow = gameWindow
        self.gameWindow.geometry("740x500")
        self.gameWindow.title("Gone Fishin'")
        self.gameWindow.resizable(False, False)
        self.gameWindow.configure(bg='#55c5d9')
        print(userObject.username + " is Logged In")


        self.fishFrame = Frame(self.gameWindow, bg='black', width='700', height='450')
        self.fishFrame.place(x=20, y=20)
        self.txt = "Gone Fishin'"
        self.heading = Label(self.fishFrame, text=self.txt, font=('yu gothic ui', 30, 'bold'), bg='black', fg='#54c4d8', width=20)
        self.heading.place(x=110, y=2)

        txt = "User: " + userObject.username
        self.userLabel = Label(self.fishFrame, text=txt, bg='black', fg="#55c5d9", width=15, font=('yu gothic ui', 10))
        self.userLabel.place(x=20, y=30)

        hs = "Highscore: " + str(userObject.highscore)
        self.hsLabel = Label(self.fishFrame, text=hs, bg='black', fg="#55c5d9", width=15, font=('yu gothic ui', 10))
        self.hsLabel.place(x=580, y=30)

        self.fishBtn = Button(self.fishFrame, text="Play With Ya Rod", bg="#55c5d9", fg="black", cursor="hand2", command=lambda: Game.fishGame(self, userObject))
        self.fishBtn.place(x=20, y= 120)



    def keepFish(result, userObject, self): 
        if result == "King George Whiting":
            Game.currScore += 50
        elif result == "Lost Bait":
            Game.currScore -= 10
        elif result == "Small Mulloway":
            Game.currScore -=10
        elif result == "Snapper":
            Game.currScore += 30
        elif result == "Large Mullet":
            Game.currScore += 20
        elif result == "Seaweed Monster":
            Game.currScore += 5
        elif result == "Hep C":
            Game.currScore -= 100
            print("Why would you keep Hep C!?")
        elif result == "Crabs":
            Game.currScore -= 50
            print("Get ready to scratch")
        self.catchBtn.destroy()
        self.throwBtn.destroy()
        self.fishBtn = Button(self.fishFrame, text="Play With Ya Rod", bg="#55c5d9", fg="black", cursor="hand2", command=lambda: Game.fishGame(self, userObject))
        self.fishBtn.place(x=20, y=120)
        user.User.updateHighscore(userObject, Game.currScore)

    def throwFish(result, userObject, self): 
        if result == "King George Whiting":
            Game.currScore += 70
        elif result == "Lost Bait":
            Game.currScore -= 0
        elif result == "Small Mulloway":
            Game.currScore += 10
        elif result == "Snapper":
            Game.currScore += 40
        elif result == "Large Mullet":
            Game.currScore += 20
        elif result == "Seaweed Monster":
            Game.currScore += -5
        elif result == "Hep C":
            Game.currScore += 100
        elif result == "Crabs":
            Game.currScore += 50
        self.catchBtn.destroy()
        self.throwBtn.destroy()
        self.fishBtn = Button(self.fishFrame, text="Play With Ya Rod", bg="#55c5d9", fg="black", cursor="hand2", command=lambda: Game.fishGame(self, userObject))
        self.fishBtn.place(x=20, y= 120)
        user.User.updateHighscore(userObject, Game.currScore)



    # *Fish Game functionality, 
    def fishGame(self, userObject):
        self.fishBtn.destroy()

        hs = "Highscore: " + str(userObject.highscore)
        self.hsLabel = Label(self.fishFrame, text=hs, bg='black', fg="#55c5d9", width=15, font=('yu gothic ui', 10))
        self.hsLabel.place(x=580, y=30)


        fishArray = ['Seaweed Monster', 'King George Whiting',
                        'Lost Bait', 'Small Mulloway','Snapper', 'Large Mullet', 'Hep C', "Crabs"]
        print(Game.currScore)
        self.caughtLabel = Label(self.fishFrame, text="You Caught: ", bg='black', fg="#55c5d9", width=20, font=('yu gothic ui', 15))
        self.caughtLabel.place(x=230, y=120)
        result = random.choice(fishArray)
        self.fishLabel = Label(self.fishFrame, text=result, bg='black', fg="#55c5d9", width=20, font=('yu gothic ui', 25))
        self.fishLabel.place(x=155, y=160)

        self.catchBtn = Button(self.fishFrame, text="Keep",  bg="#55c5d9", fg="black", cursor="hand2", font=('yu gothic ui', 15), width=20, command= lambda: Game.keepFish(result, userObject, self))
        self.catchBtn.place(x=60, y=370)
        self.throwBtn = Button(self.fishFrame, text="Throw",  bg="#55c5d9", fg="black", cursor="hand2", font=('yu gothic ui', 15), width=20, command= lambda: Game.throwFish(result, userObject, self))
        self.throwBtn.place(x=400, y=370)
        
        score = "Current Score is " + str(Game.currScore)
        self.scoreLabel = Label(self.fishFrame, text=score, bg='#55c5d9', fg="black", width=20, font=('yu gothic ui', 25))
        self.scoreLabel.place(x=160, y=250)



