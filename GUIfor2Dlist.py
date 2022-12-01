import pyxel
import sys

class App:
    #1と0の二種類の要素を持つ二次元リスト作成用GUI
    def __init__(self,h,w,scale = 10):
        self.h = h
        self.w = w
        self.scale = scale
        self.lst = [[0 for _ in range(w)]for _ in range(h)]
        pyxel.init(self.w*self.scale,self.h*self.scale)
        pyxel.mouse(True)

        pyxel.run(self.update,self.draw)

    def update(self):
        x = pyxel.mouse_x // self.scale
        y = pyxel.mouse_y // self.scale
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            #マウスボタンを押したまま画面外に行くとIndexErrorが発生するのを防ぐため
            pass
        elif  pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            #マウス左ボタンで要素を「1」にする
            self.lst[y][x] = 1
            print(x,y)
        elif pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            #マウスの右ボタンで要素を「0」にする
            self.lst[y][x] = 0
            print(x,y)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            #スペースキーでリストの内容をコマンドラインに出力
            print("[",end="")
            for i in range(len(self.lst)):
                print(self.lst[i],"," if i != len(self.lst)-1 else "")
            print("]",end="",flush=True)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for y in range(self.h):
            for x in range(self.w):
                if self.lst[y][x]:
                    pyxel.rect(x*self.scale,y*self.scale,self.scale,self.scale,1)


def main():
    if len(sys.argv) == 3:
        h = int(sys.argv[1])
        w = int(sys.argv[2])
    else:
        h,w = map(int,input("h,w = ").split())
    App(h,w)

if __name__ == '__main__':
    main()
