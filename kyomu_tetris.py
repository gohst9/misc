import pyxel
SIZE = 10
WIDTH = 10
HEIGHT = 20

class PlayerBlock:
    def __init__(self,x,y,color = 1):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color

class App:
    def __init__(self):
        self.board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.s_x = WIDTH // 2
        self.s_y = 0
        self.player_block = PlayerBlock(self.s_x,self.s_y)
        self.gameover = False
        pyxel.init(WIDTH*SIZE,HEIGHT*SIZE,fps=10,display_scale=5)
        pyxel.run(self.update,self.draw)

    def is_fallable(self,x,y):
        return y + 1 < HEIGHT and self.board[y+1][x] == 0
    def is_movable(self,x,y,dx):
        return  0 <= x + dx < WIDTH and self.board[y][x+dx] == 0
    def fall_all_blocks(self):
        for y in range(HEIGHT-2,-1,-1):
            if all(map(lambda x:x==0,self.board[y+1])):
                self.board[y+1] = list(self.board[y])
                self.board[y] = [0] * WIDTH

    def update(self):
        if self.gameover:
            return
        self.player_block.dx = pyxel.btnp(pyxel.KEY_RIGHT) - pyxel.btnp(pyxel.KEY_LEFT)
        if self.is_movable(self.player_block.x,self.player_block.y,self.player_block.dx):
            self.player_block.x += self.player_block.dx
        
        if self.is_fallable(self.player_block.x,self.player_block.y):
            self.player_block.y += 1
        else:
            self.board[self.player_block.y][self.player_block.x] = 1
            self.player_block = PlayerBlock(self.s_x,self.s_y)
            if self.board[self.s_y][self.s_x] == 1:
                self.gameover = True
        
        for y in range(HEIGHT):
            if all(self.board[y]):
                self.board[y] = [0 for _ in range(WIDTH)]
        self.fall_all_blocks()

    def draw(self):
        pyxel.cls(0)
        if self.gameover:
            pyxel.text(0,0,"Game Over",4)
            return
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.board[y][x] == 1:
                    pyxel.rect(x*SIZE,y*SIZE,SIZE,SIZE,2)
        pyxel.rect(self.player_block.x*SIZE,self.player_block.y*SIZE,SIZE,SIZE,3)


App()