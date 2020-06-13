def main():
    fallen_pins = list(map(int,input().split()))
    first_throw = True
    score = []

    for fallen_pin in fallen_pins:
        if first_throw:
            if fallen_pin == 10:
                score.append("Strike!")
                continue
            else:
                temp =fallen_pin
                first_throw = False
        else:
            if temp + fallen_pin == 10:
                score.append("Spare!")
            else:
                score.append(temp + fallen_pin)
                temp = 0
            first_throw = True
    print(score)





if __name__ == '__main__':
    main()
