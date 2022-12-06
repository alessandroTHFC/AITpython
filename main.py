from tkinter import *
import loginPage as lp


def page():
        window = lp.Tk()
        lp.loginPage(window)
        window.mainloop()


if __name__ == '__main__':
    page()