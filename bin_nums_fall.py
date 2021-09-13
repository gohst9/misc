import pyxel
import random
NUM_SIZE = 8
GREEN = 11
BLACK = 0
INTERVAL = 30
CODE_LENGTH = 8


class Code:
    #上から下に流れるコード（100110101みたいなの）
    def __init__(self,x,y,code=[]):
        self.code = code
        self.x = x
        self.y = y

    def draw(self):
        for i in range(len(self.code)):
            #1文字ずつ、NUM_SIZE分離して下に描画していく
            pyxel.text(self.x,(self.y+i*NUM_SIZE),str(self.code[i]),GREEN)

    def update(self):
        #落下させる
        self.y += 1
    def is_outside(self):
        #画面外に行っているかどうかの判定。コードを消すべきかどうかを決める。
        return self.y >= pyxel.height




class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.codes = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            #Qを押すと終了
            pyxel.quit()
        #INTERVALフレームごとに新しいコードを追加
        if pyxel.frame_count % INTERVAL == 0:
            string = [random.randint(0,1) for _ in range(CODE_LENGTH)]
            new_code = Code(random.randint(0,pyxel.width),-NUM_SIZE*CODE_LENGTH,string)
            self.codes.append(new_code)
        #画面外に行ったコードを破棄
        self.codes = [self.codes[i] for i in range(len(self.codes)) if not self.codes[i].is_outside()]
        for code in self.codes:
            code.update()


    def draw(self):
        pyxel.cls(0)
        for code in self.codes:
            code.draw()


App()