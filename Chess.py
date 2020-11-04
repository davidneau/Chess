from tkinter import *
from PIL import Image, ImageTk
import numpy as np

fen=Tk()
COTE = 400

case = int(COTE/8)
can=Canvas(fen,bg="light gray", height=COTE+case, width=COTE)
can.pack()
point_ref = (0,case)
click = False
old_x = 0
old_y = 0

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            can.create_rectangle(point_ref[0]+i*case,point_ref[1]+j*case,point_ref[0]+(i+1)*case,point_ref[1]+(j+1)*case, fill ="white")
        else:
            can.create_rectangle(point_ref[0]+i*case,point_ref[1]+j*case,point_ref[0]+(i+1)*case,point_ref[1]+(j+1)*case, fill ="black")


image = Image.open("BQueen.jpg")
photo = ImageTk.PhotoImage(image.resize((50,50)))

can.create_image(25,75,image=photo)

def whereOn(x,y):
    return(x//case, (y//case) -1)

def callback(event):
    global click
    global old_x, old_y
    x, y = whereOn(event.x, event.y)
    print("clicked at", x, y)
    if click == True:
        print("carré blanc a :",old_x*case,old_y*(case+1),old_x*(case+1),old_y*(case+2))
        can.create_rectangle(old_x*case,(old_y+1)*case,(old_x+1)*case,(old_y+2)*case, fill="white")
        can.create_image((x*case) + case /2,((y+1)*(case)) + case/2,image=photo)
        click = False
    else:
        old_x = x
        old_y = y
        click = True

can.bind("<Button-1>", callback)
fen.mainloop()
