import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.target_x = 10
        self.target_y = 10
        self.target_size = 10
        self.score = 0
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (self.target_x <= pyxel.mouse_x <= self.target_x+self.target_size) and(self.target_y <= pyxel.mouse_y <= self.target_y + self.target_size):
            self.score += 1
            self.target_x = random.randint(0,pyxel.width - self.target_size)
            self.target_y = random.randint(0,pyxel.height - self.target_size)


    def draw(self):
        pyxel.cls(0)
        pyxel.text(0,0,str(self.score),2)
        pyxel.rect(self.target_x, self.target_y, self.target_size, self.target_size, 9)

App()