'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
        score = 0
        window = Tk()
        R1 = simpledialog.askstring(title="riddle", prompt="What word in the dictionary is spelled incorrectly?")
        R2 = simpledialog.askstring(title="riddle", prompt="What does the winner of a marathon lose?")
        R3 = simpledialog.askstring(title="riddle", prompt="What can you eat from a calendar?")

        if R1 == "incorrectly":
            score = score + 1
        if R2 == "his breath":
            score = score + 1
        if R3 == "dates":
            score = score + 1
        messagebox.showinfo(title=score,message="Your score is " + str(score))