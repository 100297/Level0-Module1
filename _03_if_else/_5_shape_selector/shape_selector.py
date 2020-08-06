import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Zach = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="question",prompt="how many sides do you want your shape to have")
    Angle = 360/int(shape)
    # Draw the shape requested by the user using if-elif-else statements
    for i in range(int(shape)):
        Zach.forward(50)
        Zach.right(Angle)
    # Call the turtle .done() method
    
    window.mainloop()