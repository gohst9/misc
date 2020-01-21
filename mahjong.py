#Mahjong


class Hand:
    def __init__(self,s:str):
        self.pinzu = [0] * 10
        self.souzu = [0] * 10
        self.manzu = [0] * 10
        self.s_to_hand(s)

    def s_to_hand(self,s:str):
        #sは123m456p789sのように数字＋mpsで書かれている文字列
        temp = []
        nums = "123456789"
        suit = {"p":self.pinzu,"s":self.souzu,"m":self.manzu}
        for c in s:
            if c in nums:
                temp.append(int(c))
            if c in suit.keys():
                for i in temp:
                    suit[c][i] += 1
                temp = []

    def hand_to_s(self):
        s = ""
        hand = ""
        for i,n in enumerate(self.pinzu):
            s = s + str(i) * int(n)
        hand = hand + s + "p" if len(s) > 0 else ""
        s = ""

        for i,n in enumerate(self.souzu):
            s = s + str(i) * int(n)
        hand = hand + s + "s" if len(s) > 0 else ""
        s = ""

        for i,n in enumerate(self.manzu):
            s = s + str(i) * int(n)
        hand = hand + s + "m" if len(s) > 0 else ""
        s = ""

        return hand

    def show(self):
        print(self.hand_to_s())





def main():
    pass

if __name__ == '__main__':
    hand = Hand("231546m798s11p")
    hand.show()
