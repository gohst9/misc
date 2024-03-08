import pyxel
h,w = 3,5
n = 5
a = [1,2,3,4,5]


class App:
    def __init__(self):
        self.h = h
        self.w = w
        self.pointer = 0
        self.dx = 1
        self.dy = 0
        self.is_curve = False
        pyxel.init(self.w,self.h,capture_scale=10)
        self.colors = [[0 for _ in range(self.w)] for _ in range(self.h)]
        self.color=1
        self.y = 0
        self.x = 0
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if not pyxel.btn(pyxel.KEY_SPACE):
            return
        if self.y >= self.h:
            return
        self.colors[self.y][self.x] = self.color
        a[self.pointer] -= 1
        if a[self.pointer] == 0:
            self.pointer += 1
            self.color += 1
        nxt_x = self.x + self.dx
        if nxt_x < 0 or nxt_x >= self.w:
            self.y += 1
            self.dx = -self.dx
            return
        self.x = nxt_x



    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                pyxel.pset(j,i,self.colors[i][j])


App()


