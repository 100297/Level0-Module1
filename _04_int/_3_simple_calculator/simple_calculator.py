# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    N1 = simpledialog.askstring(title="Num1",prompt="Name a Number")
    N2 = simpledialog.askstring(title="Num1", prompt="Name a Number")


    N3 = int(N1) + int(N2)
    messagebox.showinfo(title="sum", message="the sum of your numbers is " + str(N3))