from tkinter import *
from PIL import ImageTk, Image
from random import randint
from time import sleep
import math

root = Tk()
root.geometry('1000x750')
canvas = Canvas(root, width=1000, height=750)
canvas.pack()

window_x = 1000
window_y = 750
P_length = int(window_x/4)
P_height = int(0.04*window_y)
SamuraiSize = 80
SamuraiPicture = None
Background = Image.open("samurai_pics/background.jpg")
Cloud = Image.open("samurai_pics/Cloud.png")
Platform = Image.open("samurai_pics/platform.png")

class Obsticles:
    def __init__(self, x = 0, y = 0, ObstPic = None):
        self.x = int(x)
        self.y = int(y)
        self.pic = ObstPic.resize((P_length, P_height))
        self.id = 0

    def Generate(self):
        self.pic = ImageTk.PhotoImage(self.pic)
        self.id = canvas.create_image(self.x, self.y, image=self.pic)

platforms = [0] * 4
shift_x1 = randint(int(window_x / 6), int(1 * window_x / 3))
shift_x2 = randint(int(window_x / 5), int(1 * window_x / 3))
shift_y = 125
sign = [0,1,0,1]
for j in range(4):
    platforms[j] = Obsticles(int(window_x / 2) + math.sin(j*(math.pi/2))*shift_x1 + math.cos(j*(math.pi/2))*shift_x2, int(window_y/3) + sign[j]*shift_y, Platform)

class Scene:
    def __init__(self):
        self.cloud = Cloud.resize((int(window_x/4), int(0.05*window_y)))
        self.background = Background.resize((window_x, window_y))
        self.cloudId = 0
        self.cloudV = 2
        self.platform = Platform.resize((int(window_x/4), int(0.04*window_y)))
        self.platformCoords = [0]*4
        self.platformId = [0]*4


    def DrawCloud(self):
        global Cloud
        Cloud = ImageTk.PhotoImage(self.cloud)
        self.cloudId = canvas.create_image(int(window_x/2), int(150*window_y/750), image=Cloud)
        self.x = 500
        self.y = 150

    def MoveCloud(self):
        canvas.move(self.cloudId, self.cloudV, 0)

    def DrawBackground(self):
        global Background
        Background = ImageTk.PhotoImage(self.background)
        canvas.create_image(int(window_x/2), int(window_y/2), image=Background)



class Samurai:
    def __init__(self, x = 0, y = 0, Vx = 0, SamuraiPic = None):
        self.x = x
        self.y = y
        self.vx = Vx
        self.vy = 0
        self.figure = SamuraiPic.resize((SamuraiSize, SamuraiSize))
        self.pilFigure = ImageTk.PhotoImage(self.figure)
        self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)
        self.BorderCondition = 0
        self.JumpCondition = 0
        self.PlatformCondition = [0] * 4
    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

    def TurnAround(self):
        self.vx = -self.vx
        self.figure = self.figure.transpose(Image.FLIP_LEFT_RIGHT)
        self.pilFigure = ImageTk.PhotoImage(self.figure)
        self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)

    def Interactions(self, player2):
        if (self.x + (SamuraiSize/2) >= player2.x - (SamuraiSize/2) and self.vx > 0 and player2.vx < 0 and self.y <= (player2.y + SamuraiSize/2) and self.y >= player2.y - (SamuraiSize/2)) and  self.x < player2.x:
            self.TurnAround()
            player2.TurnAround()

        if (self.x - SamuraiSize/2 <= player2.x + SamuraiSize/2   and self.vx < 0 and player2.vx > 0 and self.y <= player2.y + SamuraiSize/2 and self.y >= player2.y - SamuraiSize/2) and player2.x < self.x:
            self.TurnAround()
            player2.TurnAround()

        if (self.y + SamuraiSize/2 >= player2.y - SamuraiSize/2 and self.vy > 0 and self.x <= player2.x + SamuraiSize/2 and self.x >= player2.x - SamuraiSize/2):
            self.vy = 0
            self.JumpCondition = 0

        if (self.y - SamuraiSize/2 <= player2.y + SamuraiSize/2 and self.vy < 0 and self.x <= player2.x + SamuraiSize/2 and self.x >= player2.x - SamuraiSize/2):
            self.vy = -self.vy

    def SceneCollision(self):
        if self.x + SamuraiSize/2 >= window_x - 30 and self.vx > 0:
            self.vx = -self.vx
            self.figure = self.figure.transpose(Image.FLIP_LEFT_RIGHT)
            self.pilFigure = ImageTk.PhotoImage(self.figure)
            self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)

        if self.x - SamuraiSize/2 <= 30 and self.vx < 0:
            self.vx = -self.vx
            self.figure = self.figure.transpose(Image.FLIP_LEFT_RIGHT)
            self.pilFigure = ImageTk.PhotoImage(self.figure)
            self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)

        if self.y + SamuraiSize/2 >= window_y - 250 and self.vy > 0:
            self.vy = 0
            self.y = window_y - 250 - SamuraiSize/2
            self.BorderCondition = 1
            self.JumpCondition = 0

        if self.y - SamuraiSize/2 <= 0 and self.vy < 0:
            self.vy = -self.vy

        if self.vy != 0:
            self.BorderCondition = 0

    def ObstCollision(self):
        global platforms
        for i in range(4):
            #if (self.y + SamuraiSize / 2 >=  platforms[i].y - P_height/ 2 and self.vy > 0 and self.x <= platforms[i].x + P_length / 2 and self.x >= platforms[i].x - P_length / 2) and self.y + SamuraiSize / 2 <=  platforms[i].y + P_height/ 2:
            if (self.y + SamuraiSize / 2 <=  platforms[i].y - P_height/ 2 and self.y + self.vy + SamuraiSize/2 > platforms[i].y - P_height/2 and self.x <= platforms[i].x + P_length / 2 and self.x >= platforms[i].x - P_length / 2):
                self.vy = 0
                self.JumpCondition = 0
                self.y = platforms[i].y - P_height/2 - SamuraiSize/2

    def Move(self, obj):

        self.Interactions(obj)
        self.SceneCollision()
        self.ObstCollision()
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.3
        self.set_coords()


    def Jump(self, event):
        if self.BorderCondition == 1 or self.JumpCondition != 1:
            self.vy = -10
            self.JumpCondition += 0.5
def samurays():

    canvas.create_rectangle(925, 205, 773, 235, fill='yellow', outline='orange')

Main = Scene()


Main.DrawBackground()
Main.DrawCloud()

for i in range(4):
    platforms[i].Generate()
    platforms[i].id

Player1 = Samurai(200, 200, 2, Image.open("samurai_pics/samurai_1.png"))
Player2 = Samurai(400, 200, -2, Image.open("samurai_pics/samurai_2.png"))
root.bind('<p>', Player2.Jump)
root.bind('<q>', Player1.Jump)


def Game():
    Player1.Move(Player2)
    Player2.Move(Player1)
    root.after(10, Game)

Game()
mainloop()
