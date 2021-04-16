#todo
#衝突判定
#エサを食べる
# ↓
#スコア
#エサのランダム配置

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

    def get_positions(self):
        lst = []
        x = self.x
        y = self.y
        lst.append((x,y))
        nxt = self.tail
        while nxt:
            lst.append((nxt.x,nxt.y))
            nxt = nxt.tail
        return lst

    def is_crash_to_self_body(self):
        lst = self.get_positions()
        return (self.x,self.y) in lst[1:]


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.head = Body(pyxel.width//2,pyxel.height//2)
        self.is_game_over = False
        for i in range(10):
            self.head = Body(self.head.x+1,self.head.y,self.head) #新しい頭を作って、既存の頭を新しい頭の尻尾にする

        pyxel.run(self.update, self.draw)

    def update(self):
        dx,dy = 0,0
        #move
        if pyxel.btn(pyxel.KEY_LEFT):
            dx,dy = -1,0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx,dy = 1,0
        elif pyxel.btn(pyxel.KEY_UP):
            dx,dy = 0,-1
        elif pyxel.btn(pyxel.KEY_DOWN):
            dx,dy = 0,1
        elif pyxel.btnp(pyxel.KEY_SPACE):
            print(self.head.get_positions())


        #自身への衝突判定
        if self.head.is_crash_to_self_body():
            self.is_game_over = True
        else:
            self.is_game_over = False
        self.head.move(dx,dy)



    def draw(self):
        pyxel.cls(0)
        if self.is_game_over:
            pyxel.text(0,0,"game over",10)
        self.head.draw()

App()