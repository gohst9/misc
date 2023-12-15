import pyxel
import math
import random

def calc_direction(x1,y1,x2,y2):
    width = x2 - x1
    height = y2 - y1
    length = math.sqrt(width**2 + height**2)
    return (width / length,height / length)

def calc_length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def is_inside_display(x,y):
    return (0 <= x <= pyxel.width-1) and (0 <= y <= pyxel.height) 

class AttackAI:
    def __init__(self,enemy,player):
        self.enemy = enemy
        self.player = player
    
    def move(self):
        dx,dy = calc_direction(self.enemy.x,self.enemy.y,self.player.x,self.player.y)
        return dx,dy
    
    def attack(self):
        length = calc_length(self.enemy.x,self.enemy.y,self.player.x,self.player.y)
        if length >= 100:
            return None
        else:
            return calc_direction(self.enemy.x,self.enemy.y,self.player.x,self.player.y)
        
        


class Enemy:
    def __init__(self,x,y,player,width = 10,height = 10,AI=AttackAI):
        self.width = width
        self.height = height
        self.reload = 0
        self.reload_time = 30
        self.aim_time = 5
        self.aiming = 0
        self.x = x
        self.y = y
        self.player = player
        self.AI = AI(self,player)
    def update(self):
        if self.aiming:
            self.aiming -= 1
        else:
            dx,dy = self.AI.move()
            self.x += dx
            self.y += dy
        attack_act = self.AI.attack()
        if attack_act:
            if self.reload != 0:
                self.reload -= 1
            else:
                dx,dy = attack_act
                self.player.enemy_bullets.append(Bullet(9,(self.x * 2 + self.width)/2,(self.y*2 + self.height)/2,dx,dy))
                self.reload = self.reload_time
                self.aiming  = self.aim_time

    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.height,8)

class Bullet:
    def __init__(self,color,x,y,dx,dy):
        self.dx = dx
        self.dy = dy
        self.color = color
        self.x = x
        self.y = y
    def update(self):
        self.x += self.dx
        self.y += self.dy
    
    def draw(self):
        pyxel.rect(self.x,self.y,1,1,self.color)
    
    def is_in_range(self):
        return  (0 <= self.x <= pyxel.width-1) and (0 <= self.y <= pyxel.height-1)
    


class App:
    def __init__(self):
        pyxel.init(600,400)
        pyxel.mouse(True)
        self.score = 0
        self.max_health = 10
        self.game_over = False
        self.health = self.max_health
        self.start_x = pyxel.width / 2
        self.start_y = pyxel.height / 2
        self.x = self.start_x
        self.y = self.start_y
        self.width = 10
        self.height = 10
        self.bullets = []
        self.enemies = []
        self.enemy_bullets = []
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.score = 0
                self.enemies = []
                self.bullets = []
                self.enemy_bullets = []
                self.x = self.start_x
                self.y = self.start_y
                self.health = self.max_health
                pyxel.mouse(True)
                self.game_over = False
            return
        dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)
        self.x += dx
        self.y += dy
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.create_bullet()


        remain_bullets = [True] * len(self.bullets)
        for bullet in self.bullets:
            bullet.update()
        
        #敵の生成
        if pyxel.frame_count % 100 == 0 and len(self.enemies) <= 10:
            x = random.randint(0,pyxel.width-1)
            y = random.randint(0,pyxel.height-1)
            #プレイヤーに近すぎるときは再度、敵の出現位置を変更
            while (self.x -10 <= x <= self.x + 10) and (self.y - 10 <= y <= self.x + 10):
                x = random.randint(0,pyxel.width-1) 
                y = random.randint(0,pyxel.height-1)
            self.enemies.append(Enemy(x,y,self))

        #プレイヤーの弾が敵に当たったか
        survive_enemy = [True] * len(self.enemies)
        for i,bullet in enumerate(self.bullets):
            for j,enemy in enumerate(self.enemies):
                if enemy.x <= bullet.x <= (enemy.x + enemy.width) and enemy.y <= bullet.y <= (enemy.y + enemy.height):
                    survive_enemy[j] = False
                    remain_bullets[i] = False
                    self.score += 100
                    break
        
        #画面外に行ったプレイヤーの弾を消す
        for i in range(len(remain_bullets)):
            bullet = self.bullets[i]
            if not is_inside_display(bullet.x,bullet.y):
                remain_bullets[i] = False
        self.bullets = [self.bullets[i] for i in range(len(self.bullets)) if remain_bullets[i]]
            


        #弾が命中した敵を消す
        self.enemies = [self.enemies[i] for i in range(len(self.enemies)) if survive_enemy[i]]
        for enemy in self.enemies:
            enemy.update()
        

        remain_bullets = [True] * len(self.enemy_bullets)
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update()

        for i,enemy_bullet in enumerate(self.enemy_bullets):
            if self.x <= enemy_bullet.x <= self.x + self.width and self.y <= enemy_bullet.y <= self.y + self.width:
                self.health -= 1
                remain_bullets[i] = False

        #画面外にいった敵の弾を消す

        for i in range(len(remain_bullets)):
            bullet = self.enemy_bullets[i]
            if not is_inside_display(bullet.x,bullet.y):
                remain_bullets[i] = False
        self.enemy_bullets = [self.enemy_bullets[i] for i in range(len(self.enemy_bullets)) if remain_bullets[i]]

        if self.health <= 0:
            self.game_over = True
    def create_bullet(self):
        x1 = (self.x + self.x + self.width) / 2
        y1 = (self.y + self.y + self.height) / 2
        x2 = pyxel.mouse_x
        y2 = pyxel.mouse_y
        dx,dy = calc_direction(x1,y1,x2,y2)
        self.bullets.append(Bullet(3,x1,y1,dx,dy))


    def draw(self):
        if self.game_over:
            pyxel.mouse(False)
            pyxel.text(0,0,"health:"+"O"*self.health,10)
            pyxel.text(0,5,"score:"+str(self.score),10)
            pyxel.text(pyxel.width //2 -30,pyxel.height//2,"GAME OVER:press space to continue",4)

            return
        pyxel.cls(0)
        pyxel.text(0,0,"health:"+"O"*self.health,10)
        pyxel.text(0,5,"score:"+str(self.score),10)
        pyxel.rect(self.x,self.y,self.width,self.height,1)
        for bullet in self.bullets:
            bullet.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw()

App()