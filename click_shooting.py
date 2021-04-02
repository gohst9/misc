import pyxel
from random import randint

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isDestroyed = False
        self.w = 4
        self.h = 4
        self.color = 2

    def is_clicked(self):
        return self.x <= pyxel.mouse_x <= self.x+self.w and self.y <= pyxel.mouse_y <= self.y + self.h and pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)
    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h,self.color)
    def destroy(self):
        self.isDestroyed = True




class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)
        self.enemy_lst = []
        self.score = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.frame_count % 30 == 0:
            if len(self.enemy_lst) >= 10:
                pass
            else:
                self.enemy_lst.append(Enemy(randint(0,pyxel.width-4),randint(0,pyxel.height-4)))
        for e in self.enemy_lst:
            if e.is_clicked():
                e.destroy()
                self.score += 50
        self.enemy_lst = [e for e in self.enemy_lst if not e.isDestroyed] #敵リストから破壊フラグの立っているものだけを取り除く

    def draw(self):
        pyxel.cls(0)
        for e in self.enemy_lst:
            e.draw()
        pyxel.text(0,0,"SCORE:"+str(self.score),7)

App()