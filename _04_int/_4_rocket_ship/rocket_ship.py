from tkinter import *

windowWidth = 800
windowHeight = 800
root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()
    
# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # draws a dark blue background
    canvas.create_rectangle(0, 0, windowWidth, windowHeight, fill="#000050")
    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # this defines the x and y coordinated of all three points
    # of a triangle
    points = [100, 60, 150, 150, 50, 150]
    points1 = [100, 60, 135, 100, 65, 100]
    points2 =  [50,120 ,140,140,40,140]
    points3 = [40, 70, 140, 140, 80, 70]
    canvas.create_polygon(points, fill='gray', width=2) #draws triangle
    
    #1. Add details to your rocket to make it look better. You can look at rocket.png for inspiration.
    canvas.create_polygon(points1, fill='red', width=2)
    canvas.create_polygon(points2, fill = 'red', width = 2)
    canvas.create_polygon(points3, fill='green', width = 3)
    #2. Modify the locations of the shapes above so the rocket will be drawn where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()