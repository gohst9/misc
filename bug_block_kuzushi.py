import pyxel

W = 240
H = 240

class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 2
    def update(self,dx):
        self.dx += dx
        self.x += self.dx
        self.y += self.dy
        print(self.x,self.y)

    def draw(self):
        pyxel.rect(self.x,self.y,1,1,2)

class App:
    def __init__(self):

        pyxel.init(W,H)
        self.width = 40
        self.height = 20
        self.y = H - self.height
        self.x = W // 2
        self.ball = Ball(W//2,H//2)
        pyxel.run(self.update,self.draw)

    def update(self):
        dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)
        self.x += dx
        self.y += dy

        if self.x <= self.ball.x <= self.x + self.width and self.y <= self.ball.y <= self.y+self.height:
            self.ball.dy = -self.ball.dy
        if self.ball.x <= 0 or self.ball.x >= W-1:
            self.ball.dx = -self.ball.dx
        if self.ball.y <= 0 or self.ball.y >= H-1:
            self.ball.dy = -self.ball.dy
        self.ball.update(dx)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x,self.y,self.width,self.height,1)

        self.ball.draw()




def main():
    App()

if __name__ == '__main__':
    main()
