import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 100
        self.ground = 100
        self.d_y = 0
        self.grounded = True
        self.obstacle_x = 50
        self.obstacle_y = 100
        pyxel.run(self.update, self.draw)


    def update(self):
        self.x = (self.x + 1) % pyxel.width
        if pyxel.btnp(pyxel.KEY_SPACE) and self.grounded:
            self.d_y = -10
            self.grounded = False
        self.y += self.d_y
        self.d_y += 1
        if self.y >= self.ground:
            self.d_y = 0
            self.y = self.ground
            self.grounded = True


    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.obstacle_x,self.obstacle_y,8,8,8)
        pyxel.rect(self.x, self.y, 8, 8, 9)
        if self.x == self.obstacle_x and self.y == self.obstacle_y:
            pyxel.text(self.x,self.y-10,"ITE!",7)

App()