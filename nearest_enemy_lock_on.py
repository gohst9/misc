import pyxel
import heapq
import random


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player(pyxel.width//2,pyxel.height//2)
        self.enemy_que = []
        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)

        self.player.update(dx,dy)

        new_enemy_que = []
        first = True
        while self.enemy_que:
            _,now_enemy = heapq.heappop(self.enemy_que)
            if first:
                now_enemy.update(True)
                first = False
            else:
                now_enemy.update()

            heapq.heappush(new_enemy_que,(now_enemy.distance_from(self.player),now_enemy))


        if pyxel.frame_count % 100 == 0:
            new_enemy_x = random.randint(0,pyxel.width)
            new_enemy_y = random.randint(0,pyxel.height)
            new_enemy = Enemy(new_enemy_x,new_enemy_y)
            heapq.heappush(new_enemy_que,(new_enemy.distance_from(self.player),new_enemy))

        self.enemy_que = new_enemy_que

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        for _,enemy in self.enemy_que:
            enemy.draw()


class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self,dx=0,dy=0):
        self.x = min(pyxel.width,max(self.x+dx,0))
        self.y = min(pyxel.height,max(self.y+dy,0))

    def draw(self):
        pyxel.rect(self.x,self.y,1,1,6)

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = 14

    def update(self,is_nearest=False):
        self.color = 14
        if is_nearest:
            self.color = 12

        dx = random.randint(-1,1)
        dy = random.randint(-1,1)
        self.x += dx
        self.y += dy

    def draw(self):
        pyxel.rect(self.x,self.y,1,1,self.color)

    def distance_from(self,player):
        return (player.x - self.x) ** 2  + (player.y - self.y) ** 2

    def __lt__(self,other):
        return id(self) < id(other)

    def __gt__(self,other):
        return id(self) > id(other)

App()