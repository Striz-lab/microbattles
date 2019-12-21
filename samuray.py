from tkinter import *
from PIL import ImageTk, Image
from random import randint
from time import sleep
import math

root = Tk()
root.geometry('1000x750')
canvas = Canvas(root, width=1000, height=750)
canvas.pack()
game = 1

window_x = 1000
window_y = 750
P_length = int(window_x/4)
fps = 10
P_height = int(0.04*window_y)
R_length = 73
g = 0.3
PlayerV = 50/fps
SamuraiSize = 80
SamuraiPicture = None
Background = Image.open("samurai_pics/background.jpg")
Cloud = Image.open("samurai_pics/Cloud.png")
Platform = Image.open("samurai_pics/platform.png")
Rope = Image.open("samurai_pics/Rope.png")
objects = [Image.open("samurai_pics/fruit1.png"), Image.open("samurai_pics/fruit2.png"), Image.open("samurai_pics/fruit3.png"), Image.open("samurai_pics/bomb.png"), Image.open("samurai_pics/redbomb.png")]
score = [Image.open("score/5.jpg"), Image.open("score/4.jpg"), Image.open("score/3.jpg"), Image.open("score/2.jpg"), Image.open("score/1.jpg"), Image.open("score/0.jpg")]

class Obsticles:
    def __init__(self, x = 0, y = 0, ObstPic = None):
        self.x = int(x)
        self.y = int(y)
        self.pic = ObstPic.resize((P_length, P_height))
        self.id = 0

    def Generate(self):
        self.pic = ImageTk.PhotoImage(self.pic)
        self.id = canvas.create_image(self.x, self.y, image=self.pic)

class Objects:
    def __init__(self, Rope, FruitNum):
        self.len = R_length
        self.x = randint(100,900)
        self.y = -(R_length/2 +10)
        self.tlive = 500
        self.type = FruitNum
        self.t = 0
        self.vy = 0
        self.rope = Rope.resize((10, R_length))
        self.pilrope = 0
        self.status = 1
        self.ropeId = 0
        self.fruit = objects[FruitNum].resize((60,60))
        self.pilfruit = 0
        self.fruitId = 0
    def CreateItem(self):
        self.pilrope = ImageTk.PhotoImage(self.rope)
        self.pilfruit = ImageTk.PhotoImage(self.fruit)
        self.ropeId = canvas.create_image(self.x, self.y - R_length/2, image=self.pilrope)
        self.fruitId = canvas.create_image(self.x, self.y, image=self.pilfruit)

    def set_coords(self):
        if not self.fruitId == None:
            canvas.coords(self.fruitId, self.x, self.y)
        if not self.ropeId == None:
            canvas.coords(self.ropeId, self.x, self.y - R_length/2)

    def Bomb(self):
        if self.type == 3:
            if math.fmod(self.tlive, 100) < 50:
                self.pilfruit = ImageTk.PhotoImage(objects[4].resize((60, 60)))
                self.fruitId = canvas.create_image(self.x, self.y, image=self.pilfruit)
            if math.fmod(self.tlive, 100) >= 50:
                self.pilfruit = ImageTk.PhotoImage(objects[3].resize((60, 60)))
                self.fruitId = canvas.create_image(self.x, self.y, image=self.pilfruit)
            if self.tlive == 0:
                canvas.delete (self.fruitId)

    def Act(self):
        self.CreateItem()
        self.Bomb()
        if self.y < R_length and self.status == 1:
            self.vy += 0.01
            self.y += self.vy
            self.set_coords()

        if self.status != 0 and self.tlive != 0:
            self.tlive -= 1
        if self.status != 0 and self.tlive == 0:
            self.vy = -self.t * g
            self.y += self.vy
            self.set_coords()
            self.t += 1
        if self.status == 0:

            canvas.delete(self.fruitId)
            self.fruitId = None
            self.vy = -self.t * 0.03
            self.y += self.vy
            self.set_coords()
            self.t += 1
        if self.vy < 0 and self.y < -30:
            self.t = 0
            canvas.delete(self.ropeId)
            canvas.delete(self.fruitId)
            self.ropeId = None
            self.fruitId = None

        '''if self.ropeId == None:
            self.__del__()'''

    def __del__(self):
        canvas.delete(self.ropeId)
        canvas.delete(self.fruitId)

platforms = [0] * 4
shift_x1 = randint(int(window_x / 6), int(1 * window_x / 3))
shift_x2 = randint(int(window_x / 5), int(1 * window_x / 3))
shift_y = 125
sign = [0,1,0,1]
for j in range(4):
    platforms[j] = Obsticles(int(window_x / 2) + math.sin(j*(math.pi/2))*shift_x1 + math.cos(j*(math.pi/2))*shift_x2, int(window_y/3) + sign[j]*shift_y, Platform)

class Scene:
    def __init__(self):
        global Cloud, Background
        self.cloud = Cloud.resize((int(window_x/4), int(0.05*window_y)))
        self.background = Background.resize((window_x, window_y))
        self.cloudId = 0
        self.cloudV = 2
        self.platform = Platform.resize((int(window_x/4), int(0.04*window_y)))
        self.platformCoords = [0]*4
        self.platformId = [0]*4
        self.cloudPil = 0
        self.backgroundPil = 0
        self.backgroundId = 0


    def DrawCloud(self):
        global Cloud
        self.cloudPil = ImageTk.PhotoImage(self.cloud)
        self.cloudId = canvas.create_image(int(window_x/2), int(150*window_y/750), image=self.cloudPil)


    def MoveCloud(self):
        canvas.move(self.cloudId, self.cloudV, 0)

    def DrawBackground(self):
        global Background
        self.backgroundPil = ImageTk.PhotoImage(self.background)
        self.backgroundId = canvas.create_image(int(window_x/2), int(window_y/2), image=self.backgroundPil)



class Samurai:
    def __init__(self, x = 0, y = 0, Vx = 0, SamuraiPic = None, scoreX = 0):
        self.x = x
        self.y = y
        self.vx = Vx
        self.vy = 0
        self.trecovery = 200
        self.figure = SamuraiPic.resize((SamuraiSize, SamuraiSize))
        self.pilFigure = ImageTk.PhotoImage(self.figure)
        self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)
        self.JumpCondition = 0
        self.PlatformCondition = [0] * 4
        self.score = 0
        self.scoreX = scoreX
        self.scorePic = score[0].resize((125, 125))
        self.scorePic = ImageTk.PhotoImage(self.scorePic)
        self.scoreId = canvas.create_image(self.scoreX, window_y - 125, image=self.scorePic)

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

        if (self.y + SamuraiSize/2 >= player2.y - SamuraiSize/2 and self.vy > 0 and self.x <= player2.x + SamuraiSize and self.x >= player2.x - SamuraiSize):
            self.vy = - self.vy

        if (self.y - SamuraiSize/2 <= player2.y + SamuraiSize/2 and self.vy < 0 and self.x <= player2.x + SamuraiSize and self.x >= player2.x - SamuraiSize):
            self.vy = -self.vy

    def SceneCollision(self):
        if self.x + SamuraiSize/2 >= window_x - 30 and self.vx > 0:
            self.TurnAround()

        if self.x - SamuraiSize/2 <= 30 and self.vx < 0:
            self.TurnAround()

        if self.y + SamuraiSize/2 >= window_y - 250 and self.vy > 0:
            self.vy = 0
            self.y = window_y - 250 - SamuraiSize/2
            self.JumpCondition = 0

        if self.y - SamuraiSize/2 <= 0 and self.vy < 0:
            self.vy = -self.vy


    def ObstCollision(self):
        global platforms
        for i in range(4):
            #if (self.y + SamuraiSize / 2 >=  platforms[i].y - P_height/ 2 and self.vy > 0 and self.x <= platforms[i].x + P_length / 2 and self.x >= platforms[i].x - P_length / 2) and self.y + SamuraiSize / 2 <=  platforms[i].y + P_height/ 2:
            if (self.y + SamuraiSize / 2 <=  platforms[i].y - P_height/ 2 and self.y + self.vy + SamuraiSize/2 > platforms[i].y - P_height/2 and self.x <= platforms[i].x + P_length / 2 + SamuraiSize/2 - 10 and self.x >= platforms[i].x - P_length / 2 - SamuraiSize/2 + 10):
                self.vy = 0
                self.JumpCondition = 0
                self.y = platforms[i].y - P_height/2 - SamuraiSize/2

    def HitCondition(self, obj):
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (SamuraiSize/2 + 30)**2 and self.trecovery == 200 and obj.fruitId != None:

            if obj.type != 3:
                self.score += 1
            if obj.type == 3:
                if self.score != 0:
                    self.score -= 1
                self.trecovery -= 1
                self.x = 500
                self.y = window_y - 250
            obj.status = 0
            if self.score <= 5:
                canvas.delete(self.scoreId)
                self.scorePic = score[self.score].resize((125, 125))
                self.scorePic = ImageTk.PhotoImage(self.scorePic)
                self.scoreId = canvas.create_image(self.scoreX, window_y - 125, image=self.scorePic)

        if self.trecovery != 200:
            if math.fmod(self.trecovery, 20) >= 10:
                canvas.delete(self.id)
                self.pilFigure = None
            else:
                self.pilFigure = ImageTk.PhotoImage(self.figure)
                self.id = canvas.create_image(self.x, self.y, image=self.pilFigure)

            self.trecovery -= 1
        if self.trecovery == 0:
            self.trecovery = 200


    def Move(self, obj):

        self.Interactions(obj)
        self.SceneCollision()
        self.ObstCollision()
        self.x += self.vx
        self.y += self.vy
        self.vy += g
        self.set_coords()


    def Jump(self, event):
        if self.JumpCondition != 1:
            self.vy = -10
            self.JumpCondition += 0.5

def samurays():

    canvas.create_rectangle(925, 205, 773, 235, fill='yellow', outline='orange')

Main = None
Fruit = None
Player1 = None
Player2 = None

def Game():
    global Main, Fruit, Player1, Player2
    Main = Scene()

    Main.DrawCloud()
    Main.DrawBackground()


    for i in range(4):
        platforms[i].Generate()
        platforms[i].id

    Fruit = [None]*3
    Player1 = Samurai(200, 200, PlayerV, Image.open("samurai_pics/samurai_1.png"), 200)
    Player2 = Samurai(400, 200, -PlayerV, Image.open("samurai_pics/samurai_2.png"), 800)

    Animated(Player1, Player2, Fruit)



def Animated(Player1, Player2, Fruit):
    Player2.Move(Player1)
    Player1.Move(Player2)
    root.bind('<p>', Player2.Jump)
    root.bind('<q>', Player1.Jump)
    for i in range(3):
        if Fruit[i] != None:
            if Fruit[i].ropeId == None:
                Fruit[i] = None

        n = randint(0, 100)
        if Fruit[i] == None and n == 1:
            Fruit[i] = Objects(Rope, randint(0, 3))
        if Fruit[i] != None:
            Fruit[i].Act()
            Player1.HitCondition(Fruit[i])

            Player2.HitCondition(Fruit[i])

    root.after(fps,lambda: Animated(Player1, Player2, Fruit))

Game()

mainloop()
