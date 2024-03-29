#todo
#衝突判定 done
#壁衝突判定
#エサを食べる
# ↓
#スコア
#エサのランダム配置

import pyxel
import random

BODY_COLOR = 10

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
        pyxel.rect(self.x,self.y,1,1,BODY_COLOR)
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
        pyxel.init(120, 80)
        self.head = Body(pyxel.width//2,pyxel.height//2)
        self.is_game_over = False
        #エサの初期配置
        self.food_x = random.randint(0,pyxel.width-1)
        self.food_y = random.randint(0,pyxel.height-1)
        self.dx = 0
        self.dy = 0
        self.length = 1
        pyxel.run(self.update, self.draw)

    def draw_food(self):
        pyxel.rect(self.food_x,self.food_y,1,1,8)

    def update(self):
        #ゲームスピード調整
        if pyxel.frame_count % 2 != 0:
            #スペースキー押してる間は高速化（低速化を無視）
            if pyxel.btn(pyxel.KEY_SPACE):
                pass
            else:
                return

        #self.dx,self.dy = 0,0 #デバッグ用

        if self.is_game_over:
            if pyxel.btn(pyxel.KEY_R):
                self.head = Body(pyxel.width//2,pyxel.height//2)
                self.is_game_over = False
                self.food_x = random.randint(0,pyxel.width-1)
                self.food_y = random.randint(0,pyxel.height-1)
                self.dx = 0
                self.dy = 0
                self.length = 1
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()
            return


        #self.dx,self.dy = 0,0 #デバッグ用
        #入力受け取り
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx,self.dy = -1,0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dx,self.dy = 1,0
        elif pyxel.btn(pyxel.KEY_UP):
            self.dx,self.dy = 0,-1
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.dx,self.dy = 0,1



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
            self.food_x = random.randint(0,pyxel.width-1)
            self.food_y = random.randint(0,pyxel.height-1)
            self.length += 1


        self.head.move(self.dx,self.dy)

    def draw(self):
        pyxel.cls(0)
        if self.is_game_over:
            pyxel.text(0,0,"game over press R to retry",10)
            pyxel.text(pyxel.width//2 -16,pyxel.height//2,"YOUR SCORE:"+str(self.length),pyxel.frame_count//10%15+1)
            return
        pyxel.text(0,0,"LENGTH:"+str(self.length),7)
        self.head.draw()
        self.draw_food()




App()