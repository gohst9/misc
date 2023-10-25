#jump
import pyxel
import random

class Enemy:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 1
    def update(self):
        self.x += self.dx
        self.y += self.dy
    def touch(self,tgt):
        tgt_left,tgt_right = tgt.x,tgt.x + tgt.size
        tgt_up,tgt_bottom = tgt.y,tgt.y + tgt.size
        this_left,this_right = self.x,self.x + self.size
        this_up,this_bottom = self.y,self.y+self.size
        flag1 = tgt_left <= this_right and tgt_right >= this_left 
        flag2 = tgt_up <= this_bottom and tgt_bottom >= this_up
        return flag1 and flag2

    def draw(self):
        pyxel.rect(self.x,self.y,1,1,4)

class Player:
    def __init__(self,x,y,size=2):
        self.x = x
        self.y = y
        self.hp = 10
        self.dx = 0
        self.dy = 0
        self.size = size
        self.jump = False
        self.damaged = False
    
    def update(self):
        if self.damaged:
            self.hp -= 1
        self.damaged = False
        if not self.jump and pyxel.btnp(pyxel.KEY_SPACE):
            self.jump = True
            self.dy = -9
        
        self.dx = pyxel.btn(pyxel.KEY_D)-pyxel.btn(pyxel.KEY_A)
        
        if self.jump:
            self.y += self.dy
            self.dy += 0.5
            if self.y >= pyxel.height - self.size:
                self.jump = False
                self.dy = 0
        self.x += self.dx
    
    def draw(self):
        pyxel.rect(self.x,self.y,self.size,self.size,2)
        if self.damaged:
            pyxel.text(self.x,self.y-6,"ITE!",4)


class App:
    def __init__(self):
        self.damaged = False
        self.enemy_lst = []
        self.game_over = False
        H = 100
        W = 100
        size = 2
        pyxel.init(W,H)
        self.player = Player(pyxel.width//2 - size,pyxel.height - size,size)
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if self.player.hp <= 0:
            self.game_over = True
        if self.game_over:
            return
        self.player.update()
        self.player.damaged = False
        if len(self.enemy_lst) <= 15 and pyxel.frame_count%10==0:
            direction = random.randint(0,3)
            if direction == 0:
                x = pyxel.width-1
                y = random.randint(0,pyxel.height-1)
                dx = -1
                dy = 0
            elif direction == 1:
                x = random.randint(0,pyxel.width-1)
                y = 0
                dx = 0
                dy = 1
            elif direction == 2:
                x = 0
                y = random.randint(0,pyxel.height-1)
                dx = 1
                dy = 0

            elif direction == 3:
                x = pyxel.width-1
                y = pyxel.height - 1
                dx = -1
                dy = 0

            self.enemy_lst.append(Enemy(x,y,dx,dy))
        
        for i,enemy in enumerate(self.enemy_lst):
            if enemy.x < 0 or enemy.x >= pyxel.width or enemy.y < 0 or enemy.y >= pyxel.height:
                del self.enemy_lst[i]
                continue
            enemy.update()
            if enemy.touch(self.player):
                self.player.damaged = True



    
    def draw(self):
        if self.game_over:
            pyxel.text(pyxel.width//2-20,pyxel.height//2,"GAME OVER",7)
            return
        pyxel.cls(0)

        self.player.draw()
        pyxel.text(0,0,str(self.player.hp),1)
        for enemy in self.enemy_lst:
            enemy.draw()

App()

