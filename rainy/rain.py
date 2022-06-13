import pyxel
from random import randint
TILE = 16
#blt(x, y, img, u, v, w, h, [colkey])

class Umbrella:
    def __init__(self,x,y,size = TILE):
        self.x = x
        self.y = y
        self.size = size
    def is_collide(self,target):
        sl = self.x
        sr = self.x + self.size
        tl = target.x
        tr = target.y + target.size
        su = self.y
        sd = self.y + self.size
        tu = target.y
        td = target.y + target.size
        return (sl <= tr and tl <= sr) and (su <= td and tu <= sd)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.size, self.size)



class Bullet:
    def __init__(self,x,y,color=1,size = 1):
        self.x = x
        self.y = y
        self.dy = 1
        self.size = 1
        self.alive = True
        self.color = color

    def update(self):
        self.y += self.dy
        if self.is_outside():
            self.alive = False

    def is_outside(self):
        return not (0 <= self.x <= pyxel.width) or not(0 <= self.y <= pyxel.height)

    def draw(self):
        pyxel.rect(self.x,self.y,1,1,self.color)

class App:
    def __init__(self):
        pyxel.init(240,240,display_scale=4)
        pyxel.load("my_resource.pyxres")
        self.x = 0
        self.y = 0
        self.bullets = []
        self.umbrella = Umbrella(pyxel.width //2 ,pyxel.height-TILE,TILE)
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.bullets.append(Bullet(self.x,self.y))
        self.umbrella.update()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.bullets = [b for b in self.bullets if b.alive]
        for b in self.bullets:
            if self.umbrella.is_collide(b):
                b.dy = -1
            b.update()


    def draw(self):
        pyxel.cls(0)
        for b in self.bullets:
            b.draw()
        self.umbrella.draw()

App()
