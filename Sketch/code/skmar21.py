#first GUI program
from tkinter import *

#create window
window = Tk()
window.title('First GUI')

#canvas for objects on screen
canvas = Canvas(window, width=400,height=400)
canvas.pack()

#function within button
def hello_function():
    print('Hello, World')
    display_area.config(text = "Hello, World", \
fg="yellow", bg = "black")


def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(circle,10,0) #change x
    elif key == "Left":
        canvas.move(circle,-10,0) #change x
    if key == "Up":
        canvas.move(circle,0,-10) #change y
    elif key == "Down":
        canvas.move(circle,0,10) #change y

def move_myguy(event):
    canvas.coords(myguy,event.x,event.y)
     
#bind keyboard input to move_myguy
canvas.bind_all('<Key>', move_circle)
    
#bind left button mouse to moving the circle
canvas.bind_all('<Button-1>', move_myguy)


#button widget
button1 = Button(window, text="Click Me", command  = hello_function)
button1.pack() #places button on window

#display area using label widget
display_area = Label(window, text="")
display_area.pack() #places text area on window

#circle
circle = canvas.create_oval(75,75,325,325, fill = 'purple')

#message
screen_message = canvas.create_text(200,200, text= 'Welcome', \
fill='black', font = ('Helvetica', 30))

#create img obj
img = PhotoImage(file='twinpeaks.gif')

#create canvas image
myguy = canvas.create_image(100,325,image = img)

window.mainloop()

from PIL import Image