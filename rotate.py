from tkinter import *
from PIL import ImageTk, Image


for i in range(36):
    global pilImage, image
    pilImage = Image.open("cowboy_photos/пуля1.png")

    im = pilImage.rotate(10 * i)
    im.save('cowboy_photos/rot' + str(10 * i) + '.png')
