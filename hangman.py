from tkinter import *
from hangman import images, Image
import os


class Hangman:
    DIR = False

    def __init__(self, word="testword"):
        self.window = Tk()
        self.window.title("Hangman Game")

        self.WORD = word.lower()
        self.FOUND = ""
        self.WRONG = 0
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.update_image()
        self.update_word()

        self.entry = Entry(master=self.window, text="Input:")
        self.entry.grid(row=2, column=0)

        self.submit = Button(master=self.window, text="Submit", command=self.check)
        self.submit.grid(row=3, column=0)

        self.window.mainloop()

    def reveal_cheak(self):
        reveal = ""
        for i in self.WORD:
            if i in self.FOUND:
                reveal += i
            else:
                reveal += " _ "
        return reveal

    def update_image(self):
        if Hangman.DIR:
            dir_img = "{}/img/{}.gif".format(self.dir_path, self.WRONG)
        else:
            dir_img = "img/{}.gif".format(self.WRONG)
        image = ImageTk.PhotoImage(Image.open(dir_img))
        img = Label(master=self.window, image=image)
        img.image = image
        img.grid(row=0, column=0)

    def check(self):
        letter = self.entry.get()[0].lower()
        print(letter)
        if letter not in self.WORD:
            self.WRONG += 1
        self.FOUND += letter
        self.update_word()
        if self.WRONG == 7:
            self.submit.grid(row=0, column=0)
            self.entry.grid(row=0, column=0)
            self.update_word(self.WORD)
        self.update_image()
        self.FOUND += letter
        self.reveal_cheak()

    def update_word(self, word=None):
        if not word:
            word = self.reveal_cheak()
        lb = Label(master=self.window, text=word)
        lb.grid(row=1, column=0)


hm = Hangman("Happy")