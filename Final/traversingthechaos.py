#first GUI program
from tkinter import *
from tkinter import ttk

#create window
window = Tk()
window.title('Traversing the Chaos')

#canvas for objects on screen
canvas = Canvas(window, width=720,height=540, bg = 'pink')
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
       

def change_color_1(event):
    canvas.configure(bg='black')
    canvas.itemconfig(playercircle, fill = 'red')
    canvas.itemconfig(circle1, outline = 'red')
    canvas.itemconfig(circle2, outline = 'red')
    canvas.itemconfig(circle3, outline = 'white')
    canvas.itemconfig(circle4, outline = 'red')
    
    
def change_color_2(event):
    canvas.configure(bg='pink')
    canvas.itemconfig(playercircle, fill = 'black')
    canvas.itemconfig(circle1, outline = 'black')
    canvas.itemconfig(circle2, outline = 'black')
    canvas.itemconfig(circle3, outline = 'red')
    canvas.itemconfig(circle4, outline = 'black')    

#bind keyboard input to move_circle
canvas.bind_all('<Key>', move_circle)

#bind left button mouse to changing color
canvas.bind('<Button-1>', change_color_1)
canvas.bind('<Button-3>', change_color_2)


#bg lines

def make_purpleline_move():
    line_list1 = []
    
    def make_purpleline():
        purple = canvas.create_line(345,45,565,45, fill="#5B1A86", width=30)
        line_list1.append(purple)
        
    def move_purpleline():
        for purple in line_list1:
            canvas.move(purple, -10, 10)
            if canvas.coords(purple)[0] < 0 and canvas.coords(purple)[1] > 600:
                canvas.coords(purple, 525,-45,745,-45)
        window.after(40, move_purpleline)
        
    window.after(10,make_purpleline)
    window.after(10,move_purpleline)
        

canvas.create_line(28,246,235,246, fill='black', width=6)
canvas.create_line(45,258,252,258, fill='black', width=6)

def make_blacklines_2():
    line_list1 = []
    line_list2 = []
    
    def make_line_1():
        line_1 = canvas.create_line(630,266,630,466, fill='black', width=4)
        line_list1.append(line_1)

    def move_line_1():
        for line_1 in line_list1:
            canvas.move(line_1, 0, 10)
            if canvas.coords(line_1)[1] > 740:
                canvas.coords(line_1, 630,-200,630,0)
        window.after(40, move_line_1)
        
    def make_line_2():
        line_2 = canvas.create_line(643.5,352,643.5,422, fill='black', width=4)
        line_list2.append(line_2)

    def move_line_2():
        for line_2 in line_list2:
            canvas.move(line_2, 0, 10)
            if canvas.coords(line_2)[1] > 826:
                canvas.coords(line_2, 643.5,-114,643.5,-44)
        window.after(40, move_line_2)
    
    window.after(10, make_line_1)
    window.after(10, make_line_2)
    window.after(10, move_line_1)
    window.after(10, move_line_2)

canvas.create_line(370,487,535,485, fill='blue', width=5)
canvas.create_line(535,485,465,473, fill='blue', width=5)
canvas.create_line(465,473,630,471, fill='blue', width=5)
canvas.create_line(630,471,595,462, fill='blue', width=5)
canvas.create_line(595,462,722,459, fill='blue', width=5)

#bg circles
bgcircleset_1 = canvas.create_oval(32,60,140,130, outline = 'black', width=4)
bgcircleset_2 = canvas.create_oval(25,53,147,137, outline = 'red', width=3)

def make_eye_move():
    eye_list = []
    def make_eye():
        eye = canvas.create_oval(60,67,110,123, fill = 'black')
        eye_list.append(eye)
        
    def move_eye():
        for eye in eye_list:
            canvas.move(eye, 1, 0)
            if canvas.coords(eye)[0] > 59:
                canvas.coords(eye, 56,67,112,123)
        window.after(30, move_eye)
        
    window.after(10, make_eye)
    window.after(10, move_eye)
    
bgcircletrio_1 = canvas.create_oval(575,85,625,128, outline = 'darkorange', width=5.5)
bgcircletrio_2 = canvas.create_oval(538,90,583,134, outline = 'darkorange', width=5)
bgcircletrio_3 = canvas.create_oval(610,45,675,110, outline = 'black', width=5.5)

bgcircle_fill = canvas.create_oval(527,316,559,348, fill = 'black')

#bg arcs
canvas.create_arc(20,423,67,363, extent =-270, outline = '', fill ='darkorange', width =4)
canvas.create_arc(40,472,110,392, extent =-260, outline = '', fill ='darkorange', width =4)

#bg polygons
points = [50, 290, 115, 370, 134, 320, 176, 470, 172, 520]
canvas.create_polygon(points, outline = 'blue', fill = '', width = 3)

#circle cursor
#canvas = 720x540 | 720/2=360 , 540/2=270
#circle = posx,posy,sizew,sizeh
circle1 = canvas.create_oval(110,20,610,520, outline = 'black', width=8)
circle2 = canvas.create_oval(140,50,580,490, outline = 'black', width=6)
circle3 = canvas.create_oval(270,180,450,360, outline = 'red', width=6)
circle4 = canvas.create_oval(320,230,400,310, outline = 'black', width=3)
playercircle = canvas.create_oval(335,245,385,295, fill = 'black')


#fg lines

canvas.create_line(22,229,208,229, fill='darkorange', width=6)
canvas.create_line(55,340,235,340, fill='blue', width=10)
canvas.create_line(235,340,155,315, fill='blue', width=10)
canvas.create_line(155,315,270,311, fill='blue', width=10)

def make_blacksquiggle():

    line_list1 = []
    line_list2 = []
    line_list3 = []
    line_list4 = []
    line_list5 = []

    def make_line_1():
        line_1 = canvas.create_line(650,510,450,508, fill='black', width=7)
        line_list1.append(line_1)

    def move_line_1():
        for line_1 in line_list1:
            canvas.move(line_1, 10, 0)
            if canvas.coords(line_1)[0] > 1040:
                canvas.coords(line_1, -450,510,-650,508)
        window.after(40, move_line_1)
        
    def make_line_2():
        line_2 = canvas.create_line(450,508,480,520, fill='black', width=7)
        line_list2.append(line_2)
        
    def move_line_2():
        for line_2 in line_list2:
            canvas.move(line_2, 10, 0)
            if canvas.coords(line_2)[0] > 1040:
                canvas.coords(line_2, -450,508,-420,520)
        window.after(40, move_line_2)

    def make_line_3():
        line_3 = canvas.create_line(480,520,330,523, fill='black', width=7)
        line_list3.append(line_3)
        
    def move_line_3():
        for line_3 in line_list3:
            canvas.move(line_3, 10, 0)
            if canvas.coords(line_3)[0] > 1010:
                canvas.coords(line_3, -480,520,-630,523)
        window.after(40, move_line_3)
        
    def make_line_4():
        line_4 = canvas.create_line(330,523,360,531, fill='black', width=7)
        line_list4.append(line_4)
        
    def move_line_4():
        for line_4 in line_list4:
            canvas.move(line_4, 10, 0)
            if canvas.coords(line_4)[0] > 1010:
                canvas.coords(line_4, -480,523,-450,531)
        window.after(40, move_line_4)
        
    def make_line_5():
        line_5 = canvas.create_line(360,531,150,533, fill='black', width=7)
        line_list5.append(line_5)
        
    def move_line_5():
        for line_5 in line_list5:
            canvas.move(line_5, 10, 0)
            if canvas.coords(line_5)[0] > 1040:
                canvas.coords(line_5, -450,531,-660,533)
        window.after(40, move_line_5)

    window.after(10, make_line_1)
    window.after(10, make_line_2)
    window.after(10, make_line_3)
    window.after(10, make_line_4)
    window.after(10, make_line_5)
    window.after(10, move_line_1)
    window.after(10, move_line_2)
    window.after(10, move_line_3)
    window.after(10, move_line_4)
    window.after(10, move_line_5)


#fg circles
fgcircle_1 = canvas.create_oval(648,202,684,238, outline = 'black', width=7)

#fg arcs

def make_fgarcs():
    arc_list1 = []
    arc_list2 = []
    
    def make_arc1():
        arc_1 = canvas.create_arc(180,83,247,13, extent =-270, outline = '#FCE412', fill ='', width =4)
        arc_list1.append(arc_1)
        
    def move_arc1():
        for arc_1 in arc_list1:
            canvas.move(arc_1, 10, 0)
            if canvas.coords(arc_1)[0] > 787:
                canvas.coords(arc_1, -147,83,-80,13)
        window.after(40, move_arc1)
        
    def make_arc2():
        arc_2 = canvas.create_arc(220,132,300,47, extent =110, outline = '#FCE412', fill ='', width =4)
        arc_list2.append(arc_2)
        
    def move_arc2():
        for arc_2 in arc_list2:
            canvas.move(arc_2, -10, 0)
            if canvas.coords(arc_2)[0] < -217:
                canvas.coords(arc_2, 800,132,720,47)
        window.after(40, move_arc2)
        
    window.after(10, make_arc1)
    window.after(10, make_arc2)
    window.after(10, move_arc1)
    window.after(10, move_arc2)
    
window.after(10, make_purpleline_move)
window.after(10, make_blacklines_2)
window.after(10, make_eye_move)
window.after(10, make_blacksquiggle)
window.after(10, make_fgarcs)

window.mainloop()