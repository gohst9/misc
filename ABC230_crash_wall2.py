import pyxel

#GUIで入力を受け取る用
import sys,io

try:
    import PySimpleGUI as sg
    layout = [[sg.Text("Input")],
              [sg.Multiline(size = (30,5),key="textbox")],
              [sg.Button("send",key="send")]]
    window = sg.Window("input",layout)
    while True:
        event,values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "send":
            f = io.StringIO(values["textbox"])
            sys.stdin = f
            break
    window.close()
except ImportError:
    pass

input = lambda:sys.stdin.readline().rstrip()

class Wall:
    def __init__(self,y,l,r):
        self.y = y
        self.l = l
        self.r = r
        self.crash = False

    def is_crash(self):
        return self.crash

    def set_crash(self):
        self.crash = True

    def draw(self,x_diff,y_diff):
        pyxel.rect(self.l - x_diff,self.y - y_diff,self.r-self.l+1,1,7)

class Shot:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y -= 1

    def draw(self,x_diff,y_diff):
        pyxel.rect(self.x-x_diff,self.y-y_diff,1,1,8)

    def is_hit(self,x1,y1,x2,y2):
        return (x1 <= self.x <= x2) and (y1 <= self.y <= y2)

    def is_out_of_range(self):
        return self.y < 0



class App:
    def __init__(self):
        self.n,self.d = map(int,input().split())
        width = 120
        height = 160
        pyxel.init(width,height)
        self.x_diff = 0
        self.x = width -2
        self.y = self.n + height -10
        self.y_diff = self.n
        self.shots = []
        self.shot_count = 0
        self.walls = []
        for i in range(self.n):
            i+=1
            l,r = map(int,input().split())
            self.walls.append(Wall(i,l,r))
        pyxel.run(self.update,self.draw)


    def update(self):
        #キー入力
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if self.x - self.x_diff < pyxel.width - (pyxel.width//3 * 1):
                self.x += 1
            else:
                self.x += 1
                self.x_diff += 1
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            if self.x - self.x_diff >= pyxel.width//3:
                self.x -= 1
            else:
                self.x -= 1
                self.x_diff -= 1

        #ゲーム終了
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.y -= 1
            self.y_diff -= 1
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.y += 1
            self.y_diff += 1

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shot_count += 1
            for i in range(self.d):
                self.shots.append(Shot(self.x+i,self.y))

        for shot in self.shots:
            shot.update()
            for wall in self.walls:
                if shot.is_hit(wall.l,wall.y,wall.r+1,wall.y):
                    wall.set_crash()


        #画面外に行った弾の消去処理
        self.shots = [shot for shot in self.shots if not shot.is_out_of_range()]
        self.walls = [wall for wall in self.walls if not wall.is_crash()]


    def draw(self):
        pyxel.cls(0)
        pyxel.text(0,0,"shot count:"+str(self.shot_count),11)
        pyxel.text(0,pyxel.height-7,"walls left:"+str(len(self.walls)),11)
        for shot in self.shots:
            shot.draw(self.x_diff,self.y_diff)

        for wall in self.walls:
            wall.draw(self.x_diff,self.y_diff)

        pyxel.rect(self.x-self.x_diff,self.y-self.y_diff,1,1,3)


n = 100
App()
