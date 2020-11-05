import random
import pyxel

class Player:
    def __init__(self,x,y,size = 4,color = 10):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def update(self):
        if pyxel.btn(pyxel.KEY_D):
            self.x = min(self.x+1,pyxel.width)
        if pyxel.btn(pyxel.KEY_A):
            self.x = max(self.x-1,0)
        if pyxel.btn(pyxel.KEY_S):
            self.y = min(self.y+1,pyxel.height)
        if pyxel.btn(pyxel.KEY_W):
            self.y = max(self.y-1,0)


    def draw(self):
        pyxel.rect(self.x,self.y,self.size,self.size,self.color)


class Enemy:
    def __init__(self,x,y,size = 1,color=12):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def fall(self):
        self.y += 1
    def is_out(self):
        return self.y > pyxel.height
    def update(self):
        self.fall()
    def draw(self):
        pyxel.rect(self.x,self.y,self.size,self.size,self.color)
    def is_hit(self,target):
        return target.x <= self.x <= target.x + target.size and target.y <= self.y <= target.y+target.size


class App:
    def __init__(self):
        w = 160
        h = 120
        pyxel.init(w, h)
        self.player = Player(w//2,h//2,)
        self.enemy_lst = []
        self.enemy_cool_time = 10
        self.game_over = False
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):

        if not self.game_over:
            self.score += 1
            #プレイヤーの移動
            self.player.update()

            #エネミー生成
            if len(self.enemy_lst) < 10 and self.enemy_cool_time <= 0:
                self.enemy_lst.append(Enemy(random.randint(0,pyxel.width),0))
                self.enemy_cool_time = 10
            else:
                self.enemy_cool_time -= 1


            #敵の移動と当たり判定
            for enemy in self.enemy_lst:
                enemy.update()
                if enemy.is_hit(self.player):
                    self.game_over = True

            for i,enemy in enumerate(self.enemy_lst):
                if enemy.is_out():
                    del self.enemy_lst[i]

        elif self.game_over:
            if pyxel.btn(pyxel.KEY_Y):
                for i,enemy in enumerate(self.enemy_lst):
                    del self.enemy_lst[i]
                self.player.x = pyxel.width // 2
                self.player.y = pyxel.height // 2
                self.score = 0
                self.game_over = False
            if pyxel.btn(pyxel.KEY_N):
                pyxel.quit()





    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        pyxel.text(0,0,"score:"+str(self.score),9)
        for i,enemy in enumerate(self.enemy_lst):
            enemy.draw()
        if self.game_over:
            #pyxel.text(self.player.x + 4,self.player.y,"ITE!",8)
            pyxel.text(pyxel.width//2-12,pyxel.height//2,"GAME OVER",8)
            pyxel.text(pyxel.width//2-12,pyxel.height//2+6,"CONTINUE? y/n",8)

App()