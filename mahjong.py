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
        hand = hand + s + ("p" if len(s) > 0 else "")
        s = ""

        for i,n in enumerate(self.souzu):
            s = s + str(i) * int(n)
        hand = hand + s + ("s" if len(s) > 0 else "")
        s = ""

        for i,n in enumerate(self.manzu):
            s = s + str(i) * int(n)
        hand = hand + s + ("m" if len(s) > 0 else "")
        s = ""

        return hand

    def is_tempai(self):
        manzu = self.manzu
        pinzu = self.pinzu
        souzu = self.souzu
        suits = [manzu,pinzu,souzu]
        shunts = 0
        kots = 0
        toits = 0

        #順子の数をカウント
        for s in suits:
            for i in range(1,8):
                while s[i]>=1 and s[i+1]>=1 and s[i+2]>=1:
                    s[i]-=1
                    s[i+1]-=1
                    s[i+2]-=1
                    shunts += 1

        #刻子の数をカウント
        for s in suits:
            for i in range(1,10):
                while s[i] >= 3:
                    s[i] -= 3
                    kots += 1

        #対子の数をカウント
        for s in suits:
            for i in range(1,10):
                while s[i] >= 2:
                    s[i] -= 2
                    toits += 1

        print("順子の数:",shunts)
        print("刻子の数",kots)
        print("対子の数",toits)
        tempai = (shunts + kots) == 4 and toits == 1
        print("テンパイ","しています" if tempai else "していません")







    def show(self):
        print(self.hand_to_s())





def main():
    pass

if __name__ == '__main__':
    s = input("123m456p789s形式で麻雀の手牌を入力してください")
    hand = Hand(s)
    hand.show()
    hand.is_tempai()
