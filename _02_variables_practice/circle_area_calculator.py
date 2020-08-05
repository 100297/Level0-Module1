import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    ans = simpledialog.askinteger(title = "question", prompt = "what shall the radius be?")
    
    # Make a new turtle
    Zach = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    Zach.circle(ans)
    # Call the turtle .penup() method
    Zach.penup()
    # Move your turtle to a new x,y position using .goto()
    Zach.goto(30,30)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = math.pi*ans*ans/4
    # Write the area of your circle using the turtle .write() method
    # myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    Zach.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    # Hide your turtle
    Zach.hideturtle()
    # Call turtle.done()
    #Zach.done()

    window.mainloop()