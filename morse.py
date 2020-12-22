import PySimpleGUI as sg
import winsound
import time

dot = (1000,100)
dash = (1000,300)

def main():
    layout = [[sg.InputText("",key = "morse")],
              [sg.Button("トン",key="sound_1"),sg.Button("ツー",key = "sound_2")],
              [sg.Button("run",key = "run"),sg.Button("exit",key="exit")]]
    window = sg.Window("Morse",layout)
    while True:
        event,values = window.read()
        print(event,values)
        if event in  ["exit",None] :
            break
        elif event == "sound_1":
            window["morse"].update(values["morse"] + ".")
            winsound.Beep(*dot)
        elif event == "sound_2":
            window["morse"].update(values["morse"] + "-")
            winsound.Beep(*dash)
        elif event == "run":
            code = values["morse"]
            for c in code:
                if c == ".":
                    winsound.Beep(*dot)
                elif c == "-":
                    winsound.Beep(*dash)
                else:
                    time.sleep(0.5)



    window.close()

if __name__ == '__main__':
    main()
