from itertools import product

H = "H" #Honest　正直者
D = "D" #Dishonest 嘘つき
U = "U" #Unkind 不親切（正しいことをいうこともあるし嘘をいうこともある）
A = "A" #Any 上記３つのどれかひとつ

##class Statement:
##    def __init__(self,person,character):
##        #誰whoがどんな性格かを表す証言
##        self.person = person
##        self.character = character
##        self.state = (person,character)
##
##    def judge_statement(self,who_said):
##        #誰が言ったか？によってstatementを加工して返す
##


def honest_or_dishonest(n,statements):
    #args:
    #   n:人数
    #   statements:(i,state)の形式で「i番目の人がstate(嘘つきor正直)」
    hypos = list(product(*[("H","D") for _ in range(n)])) #全通りの組み合わせの仮説を作成
    for hypo in hypos:
        for i,h in enumerate(hypo):
            if h == "U":
                break #発言者が不親切だった場合、嘘でも真でもありうるので情報0。無視。

            who,character = change_statement(h,statements[i])
            if hypo[who] != character:
                break
            else:
                if i >= n-1:
                    return True
                continue

    return False

def main():
    n = 3
    statements = [(1,D),(2,H),(1,H)]
    answer = honest_or_dishonest(n,statements)
    print(answer)




def change_statement(character,statement):
    def reverse(c):
        if c == "H":return "D"
        if c == "D":return "H"
    #発言者の人格が正直ものかどうかに応じてstatementsをして返す
    if  character == H:
        return statement
    elif character == D:
        return [statement[0],reverse(statement[1])]
    else:
        return statement #よく分からんからそのまま返しとこ





if __name__ == '__main__':
    main()
