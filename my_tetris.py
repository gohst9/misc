import pyxel

shape1 = [[0,0,0,0],
          [0,1,0,0],
          [1,1,1,0],
          [0,0,0,0]]

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.block_start_x = width//2
        self.block_start_y = 10
        self.block = Block(self.block_start_x,self.block_start_y,shape1)

    def update(self):
        if self.block.is_fallable(self.board):
            self.block.fall()
        else:
            self.block.fix(self.board)
            self.create_new_block()

    def draw(self):
        self.block.draw()
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pyxel.rect(j,i,1,1,9)

    def create_new_block(self):
        self.block = Block(self.block_start_x,self.block_start_y,shape1)

class Block:
    def __init__(self,x:int,y:int,shape:list):
        self.x = x #左端
        self.y = y #上端
        self.height = len(shape)
        self.width = len(shape[0])
        self.shape = shape

    def update(self,fall_flag:bool):
        dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        self.x += dx * self.is_slidable(dx,lst)
        if pyxel.frame_count % 10 == 0:
            if fall_flag:
                self.fall()

    def fix(self,lst):
        for i in range(self.height):
            for j in range(self.width):
                assert i < len(self.shape)
                assert j < len(self.shape[0])             #fix、もしくはis_fallableが間違っていて、ブロックがすでに配置されたブロックの上にめり込む
                fix_x = self.x + j
                fix_y = self.y + i
                if not self.shape[i][j]:
                    continue
                assert fix_y < len(lst)
                assert fix_x < len(lst[0])
                lst[fix_y][fix_x] = True


    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.shape[i][j]:
                    continue
                draw_x = self.x + j
                draw_y = self.y + i
                pyxel.rect(draw_x,draw_y,1,1,9)

    def fall(self):
        self.y += 1

    def is_slidable(self,dx,lst):
        return 0 <= self.x + dx < len(lst[0])

    def is_fallable(self,lst):
        for i in range(self.height):
            for j in range(self.width):
                #そのマス目が空白の場合、無視して続行
                if not self.shape[j][i]:
                    continue
                nxt_x = self.x + j
                nxt_y = self.y + i + 1
                if nxt_y >= len(lst):
                    return False
                if lst[nxt_y][nxt_x]:
                    return False
        return True






class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.board = Board(160,120)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.board.update()

    def draw(self):
        pyxel.cls(0)
        self.board.draw()
App()
