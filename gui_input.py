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


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(a+b+c)

