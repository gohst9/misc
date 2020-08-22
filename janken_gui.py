import PySimpleGUI as sg
import random

hands = {0:"グー",
         1:"チョキ",
         2:"パー"}

def judge(your_hand,enemy_hand):
    if your_hand == "グー":
        if enemy_hand == "チョキ":
            return "win"
        elif enemy_hand == "パー":
            return "lose"
        else:
            return "draw"
    if your_hand == "チョキ":
        if enemy_hand == "パー":
            return "win"
        elif enemy_hand == "グー":
            return "lose"
        else:
            return "draw"
    if your_hand == "パー":
        if enemy_hand == "グー":
            return "win"
        elif enemy_hand == "チョキ":
            return "lose"
        else:
            return "draw"



layout = [
        [sg.Text("ジャンケン")],
        [sg.Button("✊",key="グー"),sg.Button("✌",key="チョキ"),sg.Button("✋",key="パー")],
        [sg.Text("相手の手："),sg.Text("Enemy_hand",key = "enemy")],
        [sg.Text("result",key="result")]
]

window = sg.Window("Janken",layout)

while True:
    event,values = window.read()
    enemy_hand = random.randint(0,2)
    enemy_hand = hands[enemy_hand]
    if event is None:
        print("exit")
        break

    result = ""
    if event == "グー":
        result = judge("グー",enemy_hand)
    elif event == "チョキ":
        result = judge("チョキ",enemy_hand)
    elif event == "パー":
        result = judge("パー",enemy_hand)
    window["enemy"].update(enemy_hand)
    window["result"].update(result)


window.close()

def main():
    pass

if __name__ == '__main__':
    main()
