#todo
#衝突判定 done
#壁衝突判定
#エサを食べる
# ↓
#スコア
#エサのランダム配置

import pyxel
import random

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
        #エサの初期配置
        self.food_x = random.randint(0,pyxel.width)
        self.food_y = random.randint(0,pyxel.height)
        self.dx = 0
        self.dy = 0


        pyxel.run(self.update, self.draw)

    def draw_food(self):
        pyxel.rect(self.food_x,self.food_y,1,1,1)

    def update(self):
        self.dx,self.dy = 0,0 #デバッグ用
        #入力受け取り
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx,self.dy = -1,0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dx,self.dy = 1,0
        elif pyxel.btn(pyxel.KEY_UP):
            self.dx,self.dy = 0,-1
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.dx,self.dy = 0,1
        elif pyxel.btnp(pyxel.KEY_SPACE):
            print(self.head.get_positions())


        #自身への衝突判定
        if self.head.is_crash_to_self_body():
            self.is_game_over = True
        else:
            self.is_game_over = False


        #壁衝突判定
        if self.head.x < 0 or self.head.x > pyxel.width or self.head.y < 0 or self.head.y > pyxel.height:
            self.is_game_over = True

        #エサを食べられるかどうかの判定
        if self.head.x + self.dx == self.food_x and self.head.y + self.dy == self.food_y:
            self.head = Body(self.head.x+self.dx,self.head.y+self.dy,self.head)
            self.food_x = random.randint(0,pyxel.width)
            self.food_y = random.randint(0,pyxel.height)


        self.head.move(self.dx,self.dy)

    def draw(self):
        pyxel.cls(0)
        if self.is_game_over:
            pyxel.text(0,0,"game over",10)
        self.head.draw()
        self.draw_food()

App()