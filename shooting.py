import pyxel
import random
class Object:
    def __init__(self,x,y,w=1,h=1,c=1,dx=0,dy=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.dx = dx
        self.dy = dy
    
    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h,self.c)
    
    def is_hit(self,tgt):
        return  self.x < tgt.x + tgt.w and self.x + self.w > tgt.x and self.y < tgt.y+tgt.h and self.y + self.h > tgt.y
    


class Player(Object):
    def update(self):
        self.dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        self.dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)
        self.x = min(pyxel.width,max(0,self.x + self.dx))
        self.y = min(pyxel.height,max(0,self.y + self.dy)) 

class Bullet(Object):
    pass

class Enemy(Object):
    def update(self):
        self.x = min(pyxel.width,max(0,self.x + self.dx))
        self.y += min(pyxel.height,max(0,self.y + self.dy))
        self.dx = random.randint(-1,1)
        self.dy = random.randint(-1,1)


class App:
    def __init__(self,w=100,h=100):
        pyxel.init(100,100,display_scale=5)
        x = w // 2
        y = w // 2
        self.score = 0
        self.player = Player(x,y)
        self.bullets = []
        self.enemy = Enemy(random.randint(0,w-2),random.randint(0,h-2),2,2,4)
        self.enemy_alive = True
        self.player_alive = True
        pyxel.run(self.update,self.draw)
    def update(self):
        if not self.player_alive:
            return
        pyxel.cls(0)
        self.player.update()
        new_bullets = []
        for bullet in self.bullets:
            if bullet.x < 0 or bullet.x > pyxel.width or bullet.y < 0 or bullet.y > pyxel.height:
                continue
            bullet.update()
            if bullet.is_hit(self.enemy):
                self.score += 1
                self.enemy_alive = False
            new_bullets.append(bullet)
        self.bullets = new_bullets
        if self.enemy_alive:
            if self.enemy.is_hit(self.player):
                self.player_alive = False
            self.enemy.update()
        else:
            self.enemy = Enemy(random.randint(0,pyxel.width-2),
                               random.randint(0,pyxel.height-2),
                               2,2,4)
            self.enemy_alive = True
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            dx = pyxel.mouse_x - self.player.x
            dy = pyxel.mouse_y - self.player.y
            dz = pow(dx**2 + dy**2,0.5)
            if not dz == 0:
                dx = dx / dz
                dy = dy / dz
                print(dx,dy)
                self.bullets.append(Object(self.player.x,self.player.y,1,1,3,dx,dy))


    def draw(self):
        if not self.player_alive:
            pyxel.text(pyxel.width//2,pyxel.height//2,"Game Over",15)
            return
        self.player.draw()
        for bullet in self.bullets:
            bullet.draw()
        pyxel.rect(pyxel.mouse_x,pyxel.mouse_y,1,1,2)
        self.enemy.draw()
        pyxel.text(0,0,str(self.score),15)


App()