from tkinter import *
from PIL import ImageTk, Image
from random import randint
from time import sleep




global pilImage, image
pilImage = Image.open("viking_photos/axe.png")

for i in range(18):
    im = pilImage.rotate(20*i)
    im.save('viking_photos/ax'+str(i)+'.png')
        


