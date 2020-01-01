#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     01/01/2020
# Copyright:   (c) user 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# x oはコマ、-は空マス

class Reversi:
    def __init__(self,setup = "--xoxo--"):
        self.lst = ["-"] + list(setup) + ["-"]

    def main_loop(self):
        turn = 0
        while True:
            player = "o" if turn % 2 == 0 else "x"
            self.show()
            i = int(input(player+"さん入力してください"))
            self.put(i,player)
            turn += 1


    def show(self):
        print("".join(self.lst[1:-1]))

    def put(self,i,piece):
        #インデックスiにコマpieceを置く
        self.lst[i] = piece
        reverse_lst = []
        start = i
        pointer = i + 1

        #右側チェック
        while not self.lst[pointer] in [piece,"-"]:
            reverse_lst.append(pointer)
            pointer += 1
        if self.lst[pointer] == piece:
            for j in reverse_lst:
                self.lst[j] = piece
        else:
            pass
        reverse_lst = []

        #左側チェック
        pointer = i - 1
        while not self.lst[pointer] in [piece,"-"]:
            reverse_lst.append(pointer)
            pointer -= 1
        if self.lst[pointer] == piece:
            for j in reverse_lst:
                self.lst[j] = piece
        else:
            pass
        reverse_lst = []









if __name__ == '__main__':
    board = Reversi()
    board.main_loop()
