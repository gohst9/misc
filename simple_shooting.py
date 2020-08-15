import pyxel

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 4

    def shoot(self):
        pass
    def move(self,dx,dy):
        self.x = min(pyxel.width,max(self.x + dx,0))
        self.y = min(pyxel.height,max(self.y + dy,0))
    def draw(self):
        pyxel.rect(self.x,self.y,self.size,self.size,4)

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        self.y -= 1
        if self.y < 0:
            del self

    def is_not_inside(self):
        pass


    def draw(self):
        pyxel.rect(self.x,self.y,1,1,10)

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 4
    def damage(self):
        pyxel.text(self.x+self.size+1,self.y,"ITE!",7)

    def is_hit(self,bullet):
        left = self.x
        right = self.x + self.size
        up = self.y
        down = self.y + self.size
        if left <= bullet.x<= right and up <= bullet.y <= down:
            return True
        else:
            return False
    def draw(self):
        pyxel.rect(self.x,self.y,self.size,self.size,12)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player(pyxel.width//2,pyxel.height-4)
        self.bullets = []
        self.enemy = Enemy(pyxel.width // 2,10)
        self.enemy_hit = False
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        #入力
        self.enemy_hit = False
        if pyxel.btn(pyxel.KEY_A):
            self.player.move(-1,0)
        elif pyxel.btn(pyxel.KEY_D):
            self.player.move(1,0)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append(Bullet(self.player.x,self.player.y))
        for i,bullet in enumerate(self.bullets):
            bullet.move()
            if bullet.y < 0:
                del self.bullets[i]
            if self.enemy.is_hit(bullet):
                self.enemy_hit = True
                self.score += 1




    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.enemy.draw()
        if self.enemy_hit:
            self.enemy.damage()
        pyxel.text(0,0,"SCORE:"+str(self.score),7)

App()
