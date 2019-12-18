
from tkinter import *
from PIL import ImageTk, Image
from random import randint
from time import sleep

global life1, life2, viking1, Time, Scoreboard
life1 = 1
life2 = 1
Time = 20
viking1 = None
viking2 = None

class Score():
    def __init__(self, x=0, y=0, st=None):
        self.x=0
        self.y=0
        self.st = st
        self.pilIm = Image.open(self.st)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)
        
    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

class Platform():
    def __init__(self, x=0, y=0, v=0, str=None):
        self.x = x
        self.y = y
        self.v = v
        self.r = 22
        self.t = 60
        self.m = self.x
        self.fire_flag = False
        self.bullet = None
        self.str = str
        self.num_of_bullets = 1
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)
    
    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

    def move(self):
        if self.x > self.m + 20 or self.x < self.m - 170:
            self.v = -self.v
        self.x -= self.v
        
        self.set_coords()
        root.after(self.t, self.move)
        self.t = 60
        
        

class Beam:
    def __init__(self, x=0, y=0, vy=0, vx=0, str=None):
        self.lives = 5
        self.x = x
        self.y = y
        self.vy = vy
        self.vx =vx
        self.r = 16
        self.t = 60
        self.fire_flag = False
        self.bullet = None
        self.str = str
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)

    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

    def move(self):
        if self.y > 340 or self.y < 170:
            self.vy = -self.vy
        self.y -= self.vy
        self.set_coords()
        root.after(self.t, self.move)
        self.t = 60


class Viking():
    def __init__(self, x=0, y=0, vx=0, vy=0,  str=None, ax=0):
    
       self.lives = 5
       self.life = 1
       self.x = x
       self.y = y
       self.vx = vx
       self.vy = vy
       self.m = self.x
       self.r = 22
       self.t = 60
       self.fire_flag = False
       self.bullet = None
       self.str = str
       self.ax = ax
       self.num_of_axes = 1
       self.pilIm = Image.open(self.str)
       self.Im = ImageTk.PhotoImage(self.pilIm)
       self.id = canvas.create_image(self.x, self.y, image=self.Im)
       
       
    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)



    def move(self):
        self.t = 60
        if (life1 == 0) and (life2 == 0):
            self.num_of_axes = 1
        if self.x > self.m + 20 or self.x < self.m - 170:
            self.vx = -self.vx
        self.x -= self.vx
        self.set_coords()
        root.after(self.t, self.move)
       
        
    
    
    def jump(self):
        self.t = Time
        if self.vy > -19 :
            self.vy -= 1
            self.y -= self.vy
            root.after(self.t, self.jump)
        else:
            self.vy = 20
    '''
    def fire_start(self):
        a = canvas.create_line(self.x, self.y-30, self.x+axe2.vy, self.y-30, width=9, fill='yellow')
        canvas.move(a, self.vx, self.vy)
        if self.ax == 2:
            if axe2.vx >=20:
                axe2.vx -=1
                axe2.vy -=1
            if axe2.vx <=0:
                axe2.vx += 1
                axe2.vy += 1
            root.after(20, self.fire_start)
           
        if self.ax == 1:
            a = canvas.create_line(self.x, self.y-30,self.x+axe1.vx,self.y-30,width=9,fill='yellow')
            canvas.move(a, self.vx, self.vy)
            
            if axe1.vx >=20:
                axe1.vx -=1
                axe1.vy -=1
            if axe1.vx <=0:
                axe1.vx += 1
                axe1.vy += 1
            root.after(20, self.fire_start)
    '''
    def fire(self):
        self.time = Time
        if self.ax == 2:
            canvas.delete(self.id)
            self.str = 'viking_photos/red_boy.png'
            self.pilIm = Image.open(self.str)
            self.Im = ImageTk.PhotoImage(self.pilIm)
            self.id = canvas.create_image(self.x, self.y, image=self.Im)
            axe2 = Axe(viking2.x, viking2.y, -18, -15, "viking_photos/ax.png")
            root.after(self.time, axe2.create)
           
        if self.ax == 1:
            canvas.delete(self.id)
       
            self.str = 'viking_photos/blue_boy.png'
            self.pilIm = Image.open(self.str)
            self.Im = ImageTk.PhotoImage(self.pilIm)
            self.id = canvas.create_image(self.x, self.y, image=self.Im)
            axe1 = Axe(viking1.x, viking1.y, 18, -15, "viking_photos/ax.png")
            root.after(self.time, axe1.create)
       
    def reset(self):
        if (life1 == 0) and (life2 == 0):
            if self.ax == 4:
                canvas.delete(self.id)
            
                self.str = 'viking_photos/red_boy.png'
                self.pilIm = Image.open(self.str)
                self.Im = ImageTk.PhotoImage(self.pilIm)
                self.id = canvas.create_image(self.x, self.y, image=self.Im)
                axe2 = Axe(viking2.x, viking2.y, -18, -15, "viking_photos/ax.png")
                root.after(self.time, axe2.create)
               
            if self.ax == 3:
                canvas.delete(self.id)
               
                self.str = 'viking_photos/blue_boy.png'
                self.pilIm = Image.open(self.str)
                self.Im = ImageTk.PhotoImage(self.pilIm)
                self.id = canvas.create_image(self.x, self.y, image=self.Im)
                axe1 = Axe(viking1.x, viking1.y, 18, -15, "viking_photos/ax.png")
                root.after(self.time, axe1.create)
        root.after(self.time, reset)
       
    def act(self, event):
        '''
        if self.num_of_axes == 2:
            self.fire_start()
            self.num_of_axes = 1
        '''
        if self.num_of_axes == 1:
            self.fire()
            self.num_of_axes = 0
        else:
            if self.vy == 20:
                self.jump()
        


class Axe:
    def __init__(self, x=0, y=0, vx=0, vy=0,str=None):
        
        self.x = x
        self.m = self.x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = 1
        self.r = 30
        self.ti = 0
        self.tim = 0
        self.str = str
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        
        self.flag = False
        self.id = None
        
    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)
    
    def create(self):

        self.move()
        

    def move(self):
        global scoreboard
        self.t = 20
        if self.ti >= 17:
            self.ti = 0
        else:
            self.ti+=1
        self.tim+=1
       
        if ((self.x-beam1.x)**2 + (self.y-beam1.y)**2 <= (self.r+beam1.r)**2):      #соударение с балкой
            if self.x-beam1.x < 0:
                self.vx = - self.vx
            if self.y-beam1.y > 0:
                self.vy = - self.vy
        
        if ((self.x-beam2.x)**2 + (self.y-beam2.y)**2 <= (self.r+beam2.r)**2):
            if self.x-beam2.x < 0:
                self.vx = - self.vx
            if self.y-beam2.y > 0:
                self.vy = - self.vy
            
        if (self.x <=75) or (self.x>=935):       #соударение со стенами
            self.vx = - self.vx
        
        
        if ((self.x-viking1.x)**2 + (self.y-viking1.y)**2 <= (self.r+viking1.r)**2):     #соударение с викингом
            if self.tim > 4:
                self.x = -500
                self.y = 0
                viking2.lives -= 1
                scoreboard = Scoreboard()
                #print(viking2.lives)
                if self.x == -500:
                     self.life = 0
                
                                
                
        if ((self.x-viking2.x)**2 + (self.y-viking2.y)**2 <= (self.r+viking2.r)**2):
            if self.tim > 4:
                scoreboard = Scoreboard()
                self.x = -500
                self.y = 0
                viking1.lives -= 1
                scoreboard = Scoreboard()
                
                if self.x == -500:
                    self.life = 0
                    
               
                
        
            
        canvas.delete(self.id)
        self.str = 'viking_photos/ax' + str(self.ti) +'.png'
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.5
        #print(self.tim)
        if self.y <= 500:
        
            root.after(self.t, self.move)
        else:
            self.x = -500
            if self.x == -500:
                 self.life = 0
                 #print(self.life)
            
        
def risu():
        global platform1, platform2, pilImage1, image1, pilImage2, image2, viking1, viking2, image3, image4, pilImage3, pilImage4, image5, image6, pilImage5, pilImage6, beam1, beam2, image7, image8, pilImage7, pilImage8, axe1, axe2, viking2, viking1
        
        platform1 = Platform(300, 385, -6, "viking_photos/platform.png")
        pilImage1 = platform1.pilIm
        image1 = platform1.Im
        platform2 = Platform(850, 385, 6, "viking_photos/platform.png")
        pilImage2 = platform2.pilIm
        image2 = platform2.Im
        
        
        viking1 = Viking(300, 326, -6, 20,  "viking_photos/blue_boy.png", 1)
        pilImage3 = viking1.pilIm
        image3 = viking1.Im
        
        viking2 = Viking(850, 326, 6, 20, "viking_photos/red_boy.png", 2)
        pilImage4 = viking2.pilIm
        image4 = viking2.Im
        
        beam1 = Beam(455, 278, 8, 15, "viking_photos/beam.png")
        pilImage5 = beam1.pilIm
        image5 = beam1.Im
        beam2 = Beam(555, 278, -8, 0, "viking_photos/beam.png")
        image6 = beam2.pilIm
        image6 = beam2.Im
        
        axe1 = Axe(270, 325, 8, -15, "viking_photos/axe.png")
        pilImage7 = axe1.pilIm
        image7 = axe1.Im
        axe2 = Axe(875, 325, -8, -15, "viking_photos/axe.png")
        pilImage8 = axe2.pilIm
        image8 = axe2.Im
        
        leftScore = Score(800, 300, "score/" + str(viking1.lives) + ".jpg")
        pilImage7 = axe1.pilIm
        image7 = axe1.Im

        
def collide():
    
    if (viking1.num_of_axes == 0) and (viking2.num_of_axes == 0):

        viking1.num_of_axes = 1
        viking2.num_of_axes = 1
        
    root.after(Time, collide)

def anim():
    
    platform1.move()
    platform2.move()
    viking1.move()
    viking2.move()
    
    collide()
    beam1.move()
    beam2.move()
    
#def score():
#
#    global pilImage2, rig, right, pilImage1, lef, left
#    pilImage1 = Image.open('score/'+str(viking1.lives)+'.jpg')
#    lef = ImageTk.PhotoImage(pilImage1)
#    left = canvas.create_image(400,650,image=lef)
#
#    pilImage2 = Image.open('score/'+str(viking2.lives)+'.jpg')
#    rig = ImageTk.PhotoImage(pilImage2)
#    right = canvas.create_image(600,650,image=rig)
#    root.after(Time, score)
            
def kostyl():
    global pilImage21, rig1, right1, pilImage11, lef1, left1
    pilImage11 = Image.open('score/6.jpg')
    lef1 = ImageTk.PhotoImage(pilImage11)
    left1 = canvas.create_image(400,650,image=lef1)
        
    pilImage21 = Image.open('score/6.jpg')
    rig1 = ImageTk.PhotoImage(pilImage21)
    right1 = canvas.create_image(600,650,image=rig1)
    #root.after(Time, score)
    
def update_picture(obj, str):
    canvas.delete(obj.id)
    obj.pilIm = Image.open(str)
    obj.Im = ImageTk.PhotoImage(obj.pilIm)
    obj.id = canvas.create_image(obj.x, obj.y, image=obj.Im)


def scene():
    global pilImage, image
    pilImage = Image.open("viking_photos/main.jpeg")
    image = ImageTk.PhotoImage(pilImage)
    canvas.create_image(500, 375, image=image)


def main():
    global scoreboard
    scene()
    risu()
    scoreboard = Scoreboard()
    #new_game()
    
    root.bind('<p>', viking2.act)
    
    root.bind('<q>', viking1.act)
    
    #print(axe2.life)
        


    anim()
    
class Scoreboard:
    def __init__(self):
        global viking1, viking2
        if viking1 is not None and viking2 is not None:
            if viking1.lives < 0:
                viking1.lives = 0
            if viking2.lives < 0:
                viking2.lives = 0
            self.blue_score = viking2.lives
            self.red_score = viking1.lives
            self.blue_pilIm = Image.open("score/"+str(self.blue_score) + ".jpg")
            self.blue_Im = ImageTk.PhotoImage(self.blue_pilIm)
            self.blue_id = canvas.create_image(400, 650, image=self.blue_Im)
            self.red_pilIm = Image.open("score/"+str(self.red_score) + ".jpg")
            self.red_Im = ImageTk.PhotoImage(self.red_pilIm)
            self.red_id = canvas.create_image(600, 650, image=self.red_Im)
        if (viking1.lives == 0):
            viking1.num_of_axes = -1
            viking2.num_of_axes = -1
            global pilImage3, bwin, blue_win
            pilImage3 = Image.open('viking_photos/blue_wins.jpg')
            bwin = ImageTk.PhotoImage(pilImage3)
            blue_win = canvas.create_image(500,80,image=bwin)
            #super_update()
            
            
        if (viking2.lives == 0):
            viking1.num_of_axes = -1
            viking2.num_of_axes = -1
            global pilImage4, rwin, red_win
            pilImage4 = Image.open('viking_photos/red_wins.jpg')
            rwin = ImageTk.PhotoImage(pilImage4)
            red_win = canvas.create_image(500,80,image=rwin)

