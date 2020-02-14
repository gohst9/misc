#そろばん
#そろばん文字列→数値
#数値→そろばん文字列
#
#そろばん文字列の形式　そろばんを左に回したもの
# *-|*-***
# -*|***-*   =　   381
# *-|***-*

def n_to_soroban(n):
    #数値nをソロバン文字列に変換
    s = str(n)
    answer = []
    for c in s:
        answer.append(soroban_row(int(c)))
    return answer[-1::-1]


def soroban_row(n):
    #一桁ごとの数値（0～9）をソロバン文字列に変換して返す
    five = n // 5 == 1
    four = n % 5
    s = ("-*" if five else "*-") + "|" + ("*"*four + "-" + ("*" * (4 - four)))
    return s

def soroban_to_n(lst):
    r_lst = lst[-1::-1]
    answer = ""

    for s in r_lst:
        answer += str(to_n(s))
    return int(answer)


def to_n(row):
    #ソロバン文字列を数値に変換して返す
    answer = 0
    five,four = row.split("|")
    answer += 5 if five == "-*" else 0
    answer += four.split("-")[0].count("*")
    return answer



def main():
    choice = input("数値をそろばんに変更する：0、そろばんを数値に変更する:1")
    if choice == "0":
        n = int(input("数値？:"))
        for soroban in n_to_soroban(n):
            print(soroban)
    elif choice == "1":
        lst = []
        while True:
            inp = input("そろばん？")
            if inp == "":
                break
            else:
                lst.append(inp)
        print(soroban_to_n(lst))







if __name__ == '__main__':
    main()
