import pyxel

dot = 20

shapes =[[[0,0,0,0],
          [0,1,0,0],
          [1,1,1,0],
          [0,0,0,0]],

         [[0,0,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,1,0,0]],

         [[0,0,0,0],
          [0,0,0,0],
          [1,1,1,0],
          [0,1,0,0]],

         [[0,0,0,0],
          [0,1,0,0],
          [1,1,0,0],
          [0,1,0,0]
          ]
        ]
WIDTH = 8
HEIGHT = 12

class Board:
    def __init__(self,width,height):
        self.game_over = False
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.block_start_x = width//2
        self.block_start_y = -2
        self.block = Block(self.block_start_x,self.block_start_y,shapes)
        self.score = 0

    def update(self):
        self.board,point = delete_full_line(self.board)
        self.score += point
        speed_up = pyxel.btn(pyxel.KEY_S)
        dx = pyxel.btnp(pyxel.KEY_D) - pyxel.btnp(pyxel.KEY_A)
        if pyxel.btnp(pyxel.KEY_W) and self.block.is_rotatable(self.board):
            self.block.rotate()
        if self.block.is_slidable(dx,self.board):
            self.block.x += dx
        if self.block.is_fallable(self.board) :
            if speed_up or pyxel.frame_count%10==0:
                self.block.fall()
        else:
            self.block.fix(self.board)
            self.create_new_block()
            for i in range(self.block.height):
                for j in range(self.block.width):
                    if self.block_start_y + i < 0:
                        continue
                    if self.board[self.block.y + i][self.block.x + j] and self.block.shape[i][j]:
                        if not self.game_over:print("Game Over,score:",self.score)
                        self.game_over = True




    def draw(self):
        self.block.draw()
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pyxel.rect(j*dot,i*dot,dot,dot,9)


    def create_new_block(self):
        self.block = Block(self.block_start_x,self.block_start_y,shapes)

class Block:
    def __init__(self,x:int,y:int,shapes:list):
        self.x = x #左端
        self.y = y #上端
        self.shapes = shapes
        self.rotate_n = 0
        self.shape = self.shapes[self.rotate_n]
        self.height = len(self.shape)
        self.width = len(self.shape[0])


    def update(self,fall_flag:bool):
        pass

    def is_rotatable(self,board):
        new_shape = self.shapes[(self.rotate_n + 1)%4]
        for i in range(self.height):
            for j in range(self.width):
                if new_shape[i][j] and board[self.y + i][self.x + j]:
                    return False
                if not (0 <= self.y + i < len(board)) or not (0 <= self.x + j < len(board[0])):
                    return False
        return True



    def rotate(self):
        self.rotate_n = (self.rotate_n + 1) % 4
        self.shape = self.shapes[self.rotate_n]

    def fix(self,lst):
        for i in range(self.height):
            for j in range(self.width):
                assert i < len(self.shape)
                assert j < len(self.shape[0])
                fix_x = self.x + j
                fix_y = self.y + i
                if not self.shape[i][j]:
                    continue
                assert fix_y < len(lst)
                assert fix_x < len(lst[0])
                lst[fix_y][fix_x] = 1


    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.shape[i][j]:
                    continue
                draw_x = self.x * dot + j * dot
                draw_y = self.y * dot + i * dot
                pyxel.rect(draw_x,draw_y,dot,dot,9)

    def fall(self):
        self.y += 1

    def is_slidable(self,dx,lst):
        board_width = len(lst[0])
        for i in range(self.height):
            for j in range(self.width):
                if not self.shape[i][j]:
                    continue
                if not (0 <= self.x + j + dx < board_width):
                    return False
                if lst[self.y + i][self.x + j + dx]:
                    return False
        return True

    def is_fallable(self,lst):
        for i in range(self.height):
            for j in range(self.width):
                #そのマス目が空白の場合、無視して続行
                if not self.shape[i][j]:
                    continue
                nxt_x = self.x + j
                nxt_y = self.y + i + 1
                if nxt_y >= len(lst):
                    return False
                if lst[nxt_y][nxt_x]:
                    return False
        return True


def delete_full_line(board):
    width = len(board[0])
    del_count = 0
    new_board = []
    for line in board:
        #1行全て埋まっているとき消去（新しいボードに行を追加しない）
        if all(line):
            del_count += 1
        else:
            new_board.append(line)
    new_board = [[0 for _ in range(width)] for _ in range(del_count)] + new_board
    board = new_board #ボードを新しいボードに差し替え
    return new_board,del_count



class App:
    def __init__(self):
        pyxel.init(WIDTH*dot, HEIGHT*dot)
        self.board = Board(WIDTH,HEIGHT)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.board.game_over:
            self.board.update()
        else:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        if self.board.game_over:
            pyxel.text(0,0,"GAME OVER,SCORE:"+str(self.board.score),7)
            return

        self.board.draw()
App()
