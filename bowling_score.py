

def main():
    MAX_PIN = 10
    pin_nums = list(map(int,input().split())) #何投目に何本倒したか
    total = 0 #合計点

    #入力された倒したピンの本数をラウンドごとにわけていく
    rounds = []
    this_round_pins = [] #今のラウンドで倒したピンの情報
    for i in range(len(pin_nums)):
        this_round_pins.append(pin_nums[i])
        if sum(this_round_pins) == MAX_PIN or len(this_round_pins) == 2:
            #全部のピンを倒す、もしくは2投行うラウンド終了,roundsにそのラウンドの投球内容を記録
            rounds.append(tuple(this_round_pins))
            this_round_pins = []

    #print(*rounds)
    total = sum(map(sum,rounds))



    #スペアの処理
    pointer = 0 #スペアやストライクをとったときの点数計算用ポインター。pin_nums上で「次のラウンドの1投目」を指す。
    for pins in rounds:
        pointer += len(pins)
        if len(pins) == 2 and sum(pins) == MAX_PIN:
            #スペアをとった場合、（もしあれば）次の１投の点数も加算する
            if pointer < len(pin_nums):
                total += pin_nums[pointer]


    #ストライクの処理
    pointer = 0
    for pins in rounds:
        pointer += len(pins)
        if len(pins) == 1 and sum(pins) == MAX_PIN:
            if pointer < len(pin_nums):
                total += pin_nums[pointer]
            if pointer+1 < len(pin_nums):
                total += pin_nums[pointer+1]


    print(total)












if __name__ == '__main__':
    main()
