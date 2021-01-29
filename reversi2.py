def reverse(lst,x,y,player):
    dxs = [-1,0,1]
    dys = [-1,0,1]
    reverse_lst = [(y,x)]
    for dy in dys:
        for dx in dxs:
            temp = []
            stack = []
            stack.append((y,x))
            while stack:
                now_y,now_x = stack.pop()
                now_x+=dy
                now_y+=dx
                if now_y < 0 or now_y >= len(lst) or now_x < 0 or now_x >= len(lst[0]) or lst[now_y][now_x] == ".":
                    temp = []
                    continue
                elif lst[now_y][now_x] == player:
                    reverse_lst = reverse_lst + temp
                    temp = []
                    continue
                stack.append((now_y,now_x))
                temp.append((now_y,now_x))

    return reverse_lst

def display_board(lst):
    print(" ","0 1 2 3 4 5 6 7")
    for i,line in enumerate(lst):
        print(i,*line)






def main():
    lst = ["........",
           "........",
           "........",
           "...xo...",
           "...ox...",
           "........",
           "........",
           "........"]
##    lst = ["oooooooo",
##           "xxxxxxxx",
##           "oooooooo",
##           "xxxxxxxx",
##           "oooooooo",
##           "xxxxxxxx",
##           "oooooooo",
##           "xxxxxxx."]
    board = [list(line) for line in lst]

    player1 = "x"
    player2 = "o"
    turn = 1
    gameover = False
    while not gameover:
        r_lst = []
        now_player = player1 if turn else player2
        display_board(board)
        print("now player:",now_player)
        while True:
            x,y = map(int,input("どこにコマを置く？").split())
            r_lst = reverse(board,x,y,now_player)
            if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board) or len(r_lst) == 1 or board[y][x] != ".":
                print("そこにはおけません！")
                continue
            else:
                break
        for y,x in r_lst:
            board[y][x] = now_player
        gameover = True
        for line in board:
            for square in line:
                if square == ".":
                    gameover = False
                    break
        turn = not turn
    player1_counter = 0
    player2_counter = 0
    for line in board:
        for square in line:
            if square == player1:
                player1_counter += 1
            else:
                player2_counter += 1

    print("player_1:",player1_counter,"player_2:",player2_counter)
    winner = "player_1" if player1_counter >= player2_counter else "player_2"
    if player1_counter == player2_counter:
        winner = "draw"

    print("winner:",winner)




if __name__ == '__main__':
    main()
