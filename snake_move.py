import pyxel

class Body:
    def __init__(self,x,y,tail = None):
        self.x = x
        self.y = y
        self.tail = tail
    def move(self,dx,dy):
        pre_x = self.x
        pre_y = self.y
        self.x += dx
        self.y += dy
        if self.tail and (dx != 0 or dy != 0):
            self.tail.move(pre_x - self.tail.x,pre_y - self.tail.y)
    def draw(self):
        pyxel.rect(self.x,self.y,1,1,1)
        if self.tail:
            self.tail.draw()


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.head = Body(pyxel.width//2,pyxel.height//2)
        for i in range(50):
            self.head = Body(self.head.x+1,self.head.y,self.head) #新しい頭を作って、既存の頭を新しい頭の尻尾にする

        pyxel.run(self.update, self.draw)

    def update(self):
        dx,dy = 0,0
        if pyxel.btn(pyxel.KEY_LEFT):
            dx,dy = -1,0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx,dy = 1,0
        elif pyxel.btn(pyxel.KEY_UP):
            dx,dy = 0,-1
        elif pyxel.btn(pyxel.KEY_DOWN):
            dx,dy = 0,1
        self.head.move(dx,dy)



    def draw(self):
        pyxel.cls(0)
        self.head.draw()

App()