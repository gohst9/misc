import pyxel

class App:
    def __init__(self):
        pyxel.init(20, 40)
        self.fixed_mino = []
        self.x = pyxel.width // 2
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_D):
            self.x += 1
        if pyxel.frame_count%3 == 0:
            if self.y + 1 < pyxel.height and (self.x,self.y+1) not in self.fixed_mino:
                self.y += 1
            else:
                self.fixed_mino.append((self.x,self.y))
                self.x = pyxel.width // 2
                self.y = 0


    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 1, 1, 9)
        for mino in self.fixed_mino:
            x,y = mino
            pyxel.rect(x,y,1,1,9)

App()