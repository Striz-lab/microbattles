from tkinter import *
import math
from PIL import ImageTk, Image
from time import sleep
from random import randint
'''
root = Tk()
root.geometry('667x500')
canvas = Canvas(root, width=700, height=700)
canvas.pack()
'''
pilImage = None
pilImage1 = None
image = None
image1 = None
pilImage2 = None
image2 = None
player = None
calboy2 = None
calboy1 = None
image3 = None
pilImage3 = None
cactus_pil = []
cactus_im = []
cactus_list = []
num_of_cactuses = randint(3, 7)
barrel = None
flint = None
extra_bullet = None
scoreboard = None
flag = True
job = None
table_b = None



class Bullet:
    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0, str=None):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.str = str
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)

    def __del__(self):
        self.x = self.y = self.vx = self.vy = 0
        self.str = self.pilIm = self.Im = self.id = None

    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

    def hit(self, player):
        global scoreboard
        if (self.x - player.x) ** 2 <= player.r ** 2 and (self.y - player.y) ** 2 <= player.r ** 2:
            player.lives -= 1
            canvas.delete(self.id)
            self.x = self.vx = self.vy = self.y = 0
            scoreboard = Scoreboard()

    def flint_hit(self):
        global flint
        if flint is not None:
            if self is not None:
                if (self.x - flint.x) ** 2 <= flint.r ** 2 and (
                        self.y - flint.y) ** 2 <= flint.r ** 2:
                    flint = None
                    vx = self.vx
                    vy = self.vy
                    self.vx = math.cos(math.pi / 6) * vx - math.sin(
                        math.pi / 6) * vy
                    self.vy = math.sin(math.pi / 6) * vx + math.cos(
                        math.pi / 6) * vy
                    vx1 = math.cos(-math.pi / 6) * vx - math.sin(
                        -math.pi / 6) * vy
                    vy1 = math.sin(-math.pi / 6) * vx + math.cos(
                        -math.pi / 6) * vy
                    a = math.atan2(self.vy, self.vx)
                    update_picture(self, "cowboy_photos/rot" + str(
                        (int(math.atan2(self.vy, -self.vx) / math.pi * 180) // 10 * 10) % 360) + ".png")
                    str1 = "cowboy_photos/rot" + str((int(a / math.pi * 180) // 10 * 10) % 360) + ".png"
                    bullet = Bullet(self.x, self.y, vx1, vy1, str1)
                    bullet.move()

    def cactus_collision(self):
        global cactus_list
        if self is not None and cactus_list != []:
            for i in range(num_of_cactuses):
                if (self.x - cactus_list[i].x) ** 2 <= cactus_list[i].r ** 2 and (
                        self.y - cactus_list[i].y) ** 2 <= cactus_list[i].r ** 2:
                    z = (cactus_list[i].x - self.x) * self.vy / self.vx + self.y
                    if (self.y - z) != 0:
                        c = math.atan((self.x - self.x) / (self.y - z))
                    else:
                        c = math.pi / 2
                    if (self.y - cactus_list[i].y) != 0:
                        b = math.atan((self.x - cactus_list[i].x) / (self.y - cactus_list[i].y))
                    else:
                        b = math.pi / 2
                    ang = b + c + math.pi
                    vx = self.vx
                    vy = self.vy
                    self.vx = -math.cos(2 * ang) * vx + math.sin(2 * ang) * vy
                    self.vy = math.sin(2 * ang) * vx + math.cos(2 * ang) * vy
                    a = math.atan2(self.vy, self.vx)
                    canvas.delete(self.id)
                    self.pilIm = Image.open('cowboy_photos/rot' + str(int((180 - a * 180 / math.pi + (a * 180 / math.pi) % 10) %
                                                            360)) + '.png')
                    self.Im = ImageTk.PhotoImage(self.pilIm)
                    self.id = canvas.create_image(self.x, self.y, image=self.Im)
                    cactus_list[i] = Object("cowboy_photos/кактус.png")

    def barrel_hit(self):
        global barrel
        if barrel is not None:
            if self is not None:
                if (self.x - barrel.x) ** 2 <= barrel.r ** 2 and (
                        self.y - barrel.y) ** 2 <= barrel.r ** 2:
                    if math.fabs(self.vx) >= 2:
                        self.vx -= 4 * sign(self.vx)
                    if math.fabs(self.vy) >= 2:
                        self.vy -= 4 * sign(self.vy)

                    barrel = None

    def game_check(self):
        global calboy1, calboy2
        self.hit(calboy1)
        self.hit(calboy2)
        self.cactus_collision()
        self.flint_hit()
        self.barrel_hit()

    def move(self):
        if flag:
            self.x += self.vx
            self.y += self.vy
            if self.y > 470 or self.y < 50:
                canvas.delete(self.id)
                self.vy = -self.vy
                a = math.atan2(self.vy, -self.vx)

                self.pilIm = Image.open('cowboy_photos/rot' + str((int(a / math.pi * 180) // 10 * 10) % 360)
                                        + '.png')
                self.Im = ImageTk.PhotoImage(self.pilIm)
                self.id = canvas.create_image(self.x, self.y, image=self.Im)
            self.game_check()
            self.set_coords()
            if self.x >= 990 or self.x <= 10:
                self.x = self.y = self.vx = self.vy = 0
                self.pilIm = self.Im = None
                canvas.delete(self.id)
            else:
                root.after(20, self.move)
        else:
            self.x = self.y = self.vx = self.vy = 0
            self.pilIm = self.Im = self.id = None
            canvas.delete(self.id)


class Cowboy:
    def __init__(self, x=0, y=0, v=0, str=None):
        self.lives = 5
        self.x = x
        self.y = y
        self.v = v
        self.r = 32
        self.t = 30
        self.fire_flag = False
        self.bullet = None
        self.str = str
        self.num_of_bullets = 1
        self.pilIm = Image.open(self.str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)

    def fire(self, event):
        bullet = None
        if self.num_of_bullets == 1:
            if self.x < 250:
                bullet = Bullet(self.x + 23, self.y, 32, 0, "cowboy_photos/пуля2.png")
                self.str = 'cowboy_photos/калбой1.png'
            if self.x > 250:
                bullet = Bullet(self.x - 23, self.y, -32, 0, "cowboy_photos/пуля1.png")
                self.str = 'cowboy_photos/калбой2.png'

            self.t = 200
            update_picture(self, self.str)
            self.v = -self.v
            self.num_of_bullets = 0
            bullet.move()
        else:
            self.t = 150
            self.v = -self.v

    def set_coords(self):
        canvas.coords(self.id, self.x, self.y)

    def move(self):
        self.t = 20
        if not flag:
            self.v = 0
        if self.y > 470 or self.y < 50:
            self.v = -self.v
        if self.y >= 470:
            self.y = 466
        elif self.y <= 50:
            self.y = 52
        else:
            self.y -= self.v
        self.set_coords()
        root.after(self.t, self.move)
        


class Object:
    def __init__(self, str):
        self.x = randint(200, 820)
        self.y = randint(60, 460)
        self.r = 30
        self.pilIm = Image.open(str)
        self.Im = ImageTk.PhotoImage(self.pilIm)
        self.id = canvas.create_image(self.x, self.y, image=self.Im)


def cactuses_generation():
    global cactus_list, cactus_im, cactus_pil
    for j in range(num_of_cactuses):
        obj = Object("cowboy_photos/кактус.png")
        for i in range(len(cactus_list)):
            for k in range(len(cactus_list) - i):
                if (obj.x - cactus_list[k].x) ** 2 + (obj.y - cactus_list[k].y) ** 2 <= 2.5 * cactus_list[k].r ** 2:
                    obj = Object("cowboy_photos/кактус.png")
        cactus_list.append(obj)


def barrel_generation():
    global barrel
    barrel = Object("cowboy_photos/бочка.png")


def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0


def game():
    global calboy1, calboy2, flag
    global image3, pilImage3
    if calboy1.num_of_bullets == 0 and calboy2.num_of_bullets == 0:
        calboy1.num_of_bullets = calboy2.num_of_bullets = 1
        update_picture(calboy2, "cowboy_photos/кулбой2.png")
        update_picture(calboy1, "cowboy_photos/кулбой1.png")
    if calboy2.lives == 0:
        flag = False
        calboy2.num_of_bullets = calboy1.num_of_bullets = -1
        update_picture(calboy2, "cowboy_photos/dead2.png")
        pilImage3 = Image.open("cowboy_photos/blue1.jpg")
        image3 = ImageTk.PhotoImage(pilImage3)
        table_b = canvas.create_image(500, 200, image=image3)
        kill()
        #calboy1.lives = calboy2.lives = 5

    elif calboy1.lives == 0:
        flag = False
        calboy2.num_of_bullets = calboy1.num_of_bullets = -1
        pilImage3 = Image.open("cowboy_photos/red1.jpg")
        image3 = ImageTk.PhotoImage(pilImage3)
        table_r = canvas.create_image(500, 200, image=image3)
        update_picture(calboy1, "cowboy_photos/dead1.png")
        kill()
        #calboy1.lives = calboy2.lives = 5
    root.after(2, game)


def kill():
    global num_of_cactuses, barrel, flint
    barrel = None
    flint = None
    cactus_list.clear()
    image3 = None


def anim():
    calboy1.move()
    calboy2.move()
    game()


def update_picture(obj, str):
    canvas.delete(obj.id)
    obj.pilIm = Image.open(str)
    obj.Im = ImageTk.PhotoImage(obj.pilIm)
    obj.id = canvas.create_image(obj.x, obj.y, image=obj.Im)


def rotate(img, ang):
    out = img.rotate(ang)
    out.save("cowboy_photos/пуля1поворот.png")


def flint_generation():
    global flint
    flint = Object("cowboy_photos/кремень.png")


def scene():
    global pilImage, image
    pilImage = Image.open("cowboy_photos/поле.png")
    image = ImageTk.PhotoImage(pilImage)
    canvas.create_image(500, 375, image=image)


class Scoreboard:
    def __init__(self):
        global calboy1, calboy2
        if calboy1.lives < 0:
            calboy1.lives = 0
        if calboy2.lives < 0:
            calboy2.lives = 0
        self.blue_score = 5 - calboy2.lives
        self.red_score = 5 - calboy1.lives
        self.blue_pilIm = Image.open("cowboy_photos/"+str(self.blue_score) + ".jpg")
        self.blue_Im = ImageTk.PhotoImage(self.blue_pilIm)
        self.blue_id = canvas.create_image(400, 650, image=self.blue_Im)
        self.red_pilIm = Image.open("cowboy_photos/"+str(self.red_score) + ".jpg")
        self.red_Im = ImageTk.PhotoImage(self.red_pilIm)
        self.red_id = canvas.create_image(600, 650, image=self.red_Im)


def generation():
    global num_of_cactuses, flint, barrel
    #if flag == False:

    if cactus_list == [] and flint is None and barrel is None:
        flint_generation()
        barrel_generation()
        cactuses_generation()
#        for i in range(num_of_cactuses):
#            if cactus_list[i].id is None:
#                update_picture(cactus_list[i], "cowboy_photos/кактус.png")
#                print("i am debiliod")
#        if flint is not None and flint.id is None:
#            update_picture(flint, "cowboy_photos/кремень.png")
#        if barrel is not None and barrel.id is None:
#            update_picture(barrel, "cowboy_photos/бочка.png")
    if flint is None:
        if randint(0, 50) > 25:
            flint_generation()
    if barrel is None:
        if randint(0, 50) > 25:
            barrel_generation()
    root.after(1000, lambda: generation())


def main():
    global calboy1, calboy2, pilImage1, image1, pilImage2, image2, scoreboard, flag, num_of_cactuses
    flag = True
    scene()
    calboy1 = Cowboy(100, 260, 9, "cowboy_photos/кулбой1.png")
    pilImage1 = calboy1.pilIm
    image1 = calboy1.Im
    calboy2 = Cowboy(900, 260, -9, "cowboy_photos/кулбой2.png")
    pilImage2 = calboy2.pilIm
    image2 = calboy2.Im
    scoreboard = Scoreboard()
    generation()
    root.bind('<p>', calboy2.fire)
    root.bind('<q>', calboy1.fire)

    anim()


#main()
#root.mainloop()

