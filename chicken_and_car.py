import pyxel
import random
width = 16
height = 16




def is_out_of_range(x,y):
    return x < 0 or x >= pyxel.width or y < 0 or y >= pyxel.height

class Car:
    def __init__(self,x,y,width,height,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
    def is_in_range(self,x,y):
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height
        return x1 <= x < x2  and y1 <= y < y2
    
    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.height,4)
    

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def update(self):
        self.dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        self.dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)
        self.x += self.dx
        self.y += self.dy
        self.x = min(max(0,self.x),pyxel.width-1)
        self.y = min(max(0,self.y),pyxel.height-1)



    def draw(self):
        pyxel.rect(self.x,self.y,1,1,3)



class App:
    def __init__(self):
        pyxel.init(160,160)
        self.player = Player(80,80)
        self.cars = []
        pyxel.run(self.update,self.draw)
    def update(self):
        self.player.update()
        delete_flags = [False] * len(self.cars)
        for i,car in enumerate(self.cars):
            car.update()
            x1 = car.x
            x2 = car.x + car.width
            y1 = car.y
            y2 = car.y + car.height
            if  (x1 >= pyxel.width or
                y1 >= pyxel.height or
                x2 < 0 or
                y2 < 0):
                delete_flags[i] = True
            if car.is_in_range(self.player.x,self.player.y):
                print("Hit!")
        self.cars = [self.cars[i] for i in range(len(self.cars)) if not delete_flags[i]]

        if len(self.cars) < 2:
            x = random.randint(0,pyxel.width)
            y = random.randint(0,pyxel.height)
            while True:
                dx = random.choice([-1,0,1])
                dy = random.choice([-1,0,1])
                if dx + dy != 0:
                    break
            self.cars.append(Car(x,y,2+abs(dx*3),2+abs(dy*3),dx,dy))

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        for car in self.cars:
            car.draw()


App()