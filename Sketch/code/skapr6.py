#first GUI program
from tkinter import *
from tkinter import ttk
from random import *

#create window
window = Tk()
window.title('First GUI')

#canvas for objects on screen
canvas = Canvas(window, width=400,height=400, bg = 'pink')
canvas.pack()

def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(playercircle,10,0) #change x
        canvas.move(circle4,8,0)
        canvas.move(circle3,6,0)
        canvas.move(circle2,4,0)
        canvas.move(circle1,2,0)
    elif key == "Left":
        canvas.move(playercircle,-10,0) #change x
        canvas.move(circle4,-8,0)
        canvas.move(circle3,-6,0)
        canvas.move(circle2,-4,0)
        canvas.move(circle1,-2,0)
    if key == "Up":
        canvas.move(playercircle,0,-10) #change y
        canvas.move(circle4,0,-8)
        canvas.move(circle3,0,-6)
        canvas.move(circle2,0,-4)
        canvas.move(circle1,0,-2)
    elif key == "Down":
        canvas.move(playercircle,0,10) #change y
        canvas.move(circle4,0,8)
        canvas.move(circle3,0,6)
        canvas.move(circle2,0,4)
        canvas.move(circle1,0,2)
       
colors = ['red', 'black'] 

def change_color(event):
    canvas.itemconfig(playercircle, fill = choice(colors))
    
#bind keyboard input to move_circle
canvas.bind_all('<Key>', move_circle)

#bind left button mouse to changing color
canvas.bind_all('<Button-1>', change_color)

#circle cursor
circle1 = canvas.create_oval(75,75,325,325, outline = 'black', width=6)
circle2 = canvas.create_oval(100,100,300,300, outline = 'black', width=5)
circle3 = canvas.create_oval(125,125,275,275, outline = 'black', width=4)
circle4 = canvas.create_oval(150,150,250,250, outline = 'black', width=3)
playercircle = canvas.create_oval(175,175,225,225, fill = 'black')


#bg circles
bgcircle_1 = canvas.create_oval(22,30,110,80, outline = 'black', width=4)
bgcircle_1_2 = canvas.create_oval(48,37,84,73, fill = 'black')

bgcircle_2 = canvas.create_oval(320,55,365,100, outline = 'black', width=4)

#bg lines
canvas.create_line(32,185,120,185, fill="darkorange", width=6)
canvas.create_line(25,206,135,206, fill="black", width=6)
canvas.create_line(45,218,145,218, fill="black", width=6)
canvas.create_line(55,250,135,250, fill="blue", width=8)
canvas.create_line(135,250,100,235, fill="blue", width=8)
canvas.create_line(100,235,158,231, fill="blue", width=8)


window.mainloop()