
from tkinter import *
from PIL import ImageTk, Image
from random import randrange as rnd, choice
#import viking
import v_init
import Cowboy
#import samuray

import webbrowser

root = Tk()
root.geometry('1000x750')
canvas = Canvas(root, width=1000, height=750)
canvas.pack()

#viking.root = root
#viking.canvas = canvas
v_init.canvas = canvas
v_init.root = root

Cowboy.root = root
Cowboy.canvas = canvas

#samuray.root = root
#samuray.canvas = canvas

global updateTime
updateTime = 0
i = 0


'''
генерация вызова вещи
'''
something = rnd(1, 100)


def random():
    if something<=30:
        first_game()
    if (something >= 31) and (something <= 60):
        second_game()
    if (something >= 61) and (something <= 90):
        third_game()
    if (something >= 91):
        ads()
'''
функции, вызывающие программы с играми и рекламу
'''
def forgotten():
    
    start_button.pack_forget()
    start_button.pack()
    button2.pack_forget()
    button2.pack()
    button3.pack_forget()
    button3.pack()
    button4.pack_forget()
    button4.pack()
    button5.pack_forget()
    button5.pack()
    
def first_game():
    canvas.delete(ALL)
    forgotten()
    #start_button.destroy()
    v_init.main()
    if (v_init.viking1.lives == 0) or (v_init.viking2.lives == 0):
        canvas.delete(ALL)
        forgotten()
        main()
    #viking.main()
    #button1.pack
    button1.place(x=110, y=8)
    i = 0


def second_game():
    Cowboy.kill()
    forgotten()
    #start_button.destroy()
    i = 0
    canvas.delete(ALL)

    Cowboy.main()
    button1.place(x=110, y=8)
    

def third_game():
    canvas.delete(ALL)
    forgotten()
    #start_button.destroy()
    i = 0
    samuray.Game()
    button1.place(x=110, y=8)

def ads():
    canvas.delete(ALL)
    forgotten()
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
    i = 0
    menu()

'''
импорт фото
'''

root.geometry('1200x750')


pilImage = Image.open("main_photos/main_menu.png")
im = ImageTk.PhotoImage(pilImage)

pilImage = Image.open("main_photos/vikings.jpeg")
vik = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/kovboys.jpeg")
kov = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/samurays.jpeg")
sam = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/ass.jpeg")
ass = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/thinga.jpg")
thingas = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/lala.jpeg")
lala = ImageTk.PhotoImage(pilImage)

pilImage = Image.open("main_photos/button2.jpeg")
buton2 = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/button3.jpeg")
buton3 = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("main_photos/button4.jpeg")
buton4 = ImageTk.PhotoImage(pilImage)


    
'''
создание графического фона
'''


def menu():
    updateTime = 0
    v_init.kostyl()
    
    Cowboy.calboy1 = Cowboy.calboy2 = Cowboy.table_r = Cowboy.table_b = None
    #Cowboy.kill()
    canvas.delete(ALL)
    
    
    inn = canvas.create_image(200, 300, image = thingas)
    imagesprite = canvas.create_image(502,300,image=im)
    start_button.place(x=470, y=382)
    button2.place(x=326,y=170)
    button3.place(x=471,y=170)
    button4.place(x=614,y=170)
    button5.place(x=757,y=170)
    button1.pack_forget()
    button1.pack()
    
    
    #l2 = canvas.create_image(600,650,image=thingas)

    
ima9 = ImageTk.PhotoImage(file="main_photos/start.jpeg")
start_button = Button(root, image=ima9, command=random)

ima10 = ImageTk.PhotoImage(file="main_photos/button1.jpg")
button1 = Button(root, image=ima10, command=menu)


button2 = Button(root, image=vik, command=first_game)
button3 = Button(root, image=kov, command=second_game)
button4 = Button(root, image=sam, command=third_game)
button5 = Button(root, image=ass, command=ads)

if __name__ == "__main__":
    menu()
    

mainloop()
root.mainloop()
