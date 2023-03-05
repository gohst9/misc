import  PySimpleGUI as sg
#黒色と白色を切り替えることができる二次元ボードを作成する

def main():
    colors = [("white","black"),("black","white")]
    h,w = map(int,input().split()) #ボードの縦と横の長さを指定する
    board = [[0 for _ in range(w)] for _ in range(h)]
    layout = [[sg.Button(key=str(y)+":"+str(x),button_text="  ",button_color=("white","black")) for x in range(w)] for y in range(h)]
    window = sg.Window("test",layout)
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            y,x = map(int,event.split(":"))
            nxt_color = board[y][x] ^ 1
            board[y][x] = nxt_color
            window[event].update(button_color=colors[nxt_color])
    window.close()

if __name__ == '__main__':
    main()
