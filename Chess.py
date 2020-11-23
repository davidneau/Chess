from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Chess():
    def __init__(self):
        self.fen = Tk()
        self.COTE = 400
        self.case = int(self.COTE/8)
        self.can=Canvas(self.fen,bg="light gray", height=self.COTE+self.case, width=self.COTE)
        self.can.pack()
        self.point_ref = (0,self.case)
        self.click = False
        self.old_x = 0
        self.old_y = 0
        self.current_piece = ""
        self.deplacement = {"Tour"}
        self.photo_list =  []
        self.corresp_piece = {"bt":"BTour", "bc":"BChev", "bf":"BFou", "bq":"BReine", "bk":"BRoi", "bp":"BPion",
                              "nt":"NTour", "nc":"NChev", "nf":"NFou", "nq":"NReine", "nk":"NRoi", "np":"NPion"}
        self.grill = np.array([["bt","bc","bf","bq","bk","bf","bc","bt"],
                               ["bp","bp","bp","bp","bp","bp","bp","bp"],
                               ["","","","","","","",""],
                               ["","","","","","","",""],
                               ["","","","","","","",""],
                               ["","","","","","","",""],
                               ["np","np","np","np","np","np","np","np"],
                               ["nt","nc","nf","nk","nq","nf","nc","nt"]])
        self.init_board()
        def callback(event):
            x, y = self.whereOn(event.x, event.y)
            print("clicked at", x, y)
            if self.click == True:
                if (self.old_x + self.old_y)%2 ==0:
                    self.can.create_rectangle(self.old_x*self.case,(self.old_y+1)*self.case,(self.old_x+1)*self.case,(self.old_y+2)*self.case, fill="white")
                else:
                    self.can.create_rectangle(self.old_x*self.case,(self.old_y+1)*self.case,(self.old_x+1)*self.case,(self.old_y+2)*self.case, fill="#333333")
                self.put_img((x*self.case) + self.case /2,((y+1)*(self.case)) + self.case/2,"icon/" + self.corresp_piece[self.current_piece] + ".png")
                self.click = False
                self.grill[self.old_y, self.old_x] = ""
                self.grill[y, x] = self.current_piece
                self.current_piece = ""
            else:
                self.current_piece = self.grill[y,x]
                self.old_x = x
                self.old_y = y
                self.click = True
        self.can.bind("<Button-1>", callback)
        print(self.grill)
        self.fen.mainloop()

    def init_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    self.can.create_rectangle(self.point_ref[0]+i*self.case,self.point_ref[1]+j*self.case,self.point_ref[0]+(i+1)*self.case,self.point_ref[1]+(j+1)*self.case, fill ="white")
                else:
                    self.can.create_rectangle(self.point_ref[0]+i*self.case,self.point_ref[1]+j*self.case,self.point_ref[0]+(i+1)*self.case,self.point_ref[1]+(j+1)*self.case, fill ="#333333")
        i = self.case
        self.put_img(25,75,"icon/BTour.png")
        self.put_img(i+25,75,"icon/BChev.png")
        self.put_img(2*i+25,75,"icon/BFou.png")
        self.put_img(3*i+25,75,"icon/BReine.png")
        self.put_img(4*i+25,75,"icon/BRoi.png")
        self.put_img(5*i+25,75,"icon/BFou.png")
        self.put_img(6*i+25,75,"icon/BChev.png")
        self.put_img(7*i+25,75,"icon/BTour.png")
        self.put_img(25,i+75,"icon/BPion.png")
        self.put_img(i+25,i+75,"icon/BPion.png")
        self.put_img(2*i+25,i+75,"icon/BPion.png")
        self.put_img(3*i+25,i+75,"icon/BPion.png")
        self.put_img(4*i+25,i+75,"icon/BPion.png")
        self.put_img(5*i+25,i+75,"icon/BPion.png")
        self.put_img(6*i+25,i+75,"icon/BPion.png")
        self.put_img(7*i+25,i+75,"icon/BPion.png")
        self.put_img(25,7*i+75,"icon/NTour.png")
        self.put_img(i+25,7*i+75,"icon/NChev.png")
        self.put_img(2*i+25,7*i+75,"icon/NFou.png")
        self.put_img(3*i+25,7*i+75,"icon/NReine.png")
        self.put_img(4*i+25,7*i+75,"icon/NRoi.png")
        self.put_img(5*i+25,7*i+75,"icon/NFou.png")
        self.put_img(6*i+25,7*i+75,"icon/NChev.png")
        self.put_img(7*i+25,7*i+75,"icon/NTour.png")
        self.put_img(25,6*i+75,"icon/NPion.png")
        self.put_img(i+25,6*i+75,"icon/NPion.png")
        self.put_img(2*i+25,6*i+75,"icon/NPion.png")
        self.put_img(3*i+25,6*i+75,"icon/NPion.png")
        self.put_img(4*i+25,6*i+75,"icon/NPion.png")
        self.put_img(5*i+25,6*i+75,"icon/NPion.png")
        self.put_img(6*i+25,6*i+75,"icon/NPion.png")
        self.put_img(7*i+25,6*i+75,"icon/NPion.png")

    def put_img(self,x,y,strimage):
        img = PhotoImage(file=strimage)
        self.can.create_image(x,y,image=img)
        self.photo_list.append(img)
        self.can.grid()

    def whereOn(self,x,y):
        return(x//self.case, (y//self.case) -1)



Ch = Chess()
