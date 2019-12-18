from tkinter import *
from PIL import ImageTk, Image
from random import randint
from time import sleep
import v_init
import abb



        
def collide():
    

    if (v_init.axe2.x-v_init.axe1.x)**2 + (v_init.axe2.y-v_init.axe1.y)**2 <= (v_init.axe2.r+v_init.axe1.r)**2:        #соударение с другим топором
        v_init.axe1.vx, v_init.axe2.vx = v_init.axe2.vx, v_init.axe1.vx
        v_init.axe1.vx = 0
        v_init.axe1.vy = 0
    #print(v_init.axe1.x)
    if (v_init.viking1.num_of_axes == 0) and (v_init.viking2.num_of_axes == 0):
    
        global pilImae, imae
        pilImae = Image.open("viking_photos/battle.jpg")
        imae = ImageTk.PhotoImage(pilImage)
        batt = canvas.create_image(500, 375, image=imae)
        #sleep(1)
        canvas.delete(batt)
        v_init.viking1.num_of_axes = 1
        v_init.viking2.num_of_axes = 1
    root.after(20, collide)
    
def anim():
    
    v_init.platform1.move()
    v_init.platform2.move()
    v_init.viking1.move()
    v_init.viking2.move()
    score()
    collide()
    v_init.beam1.move()
    v_init.beam2.move()
    
def score():
    global pilImage2, rig, right, pilImage1, lef, left
    pilImage1 = Image.open('score/'+str(v_init.viking1.lives)+'.jpg')
    lef = ImageTk.PhotoImage(pilImage1)
    left = canvas.create_image(400,650,image=lef)
    
    pilImage2 = Image.open('score/'+str(v_init.viking2.lives)+'.jpg')
    rig = ImageTk.PhotoImage(pilImage2)
    right = canvas.create_image(600,650,image=rig)
        
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
    scene()
    v_init.risu()
    
    
    root.bind('<p>', v_init.viking2.act)
    
    root.bind('<q>', v_init.viking1.act)
    
    print(v_init.axe2.life)
        
    anim()
    
#main()


