
import unittest
from random import randint

class WrongWordError(Exception):
    pass
class WrongWordLength(Exception):
    pass

#お題の単語リスト
word_lst = ["tight",
            "swift",
            "humor",
            "laser",
            "watch",
            "total",
            "robby",
            "solar",
            "polar",
            "plant",
            "fight"]



#「同じ位置で同じ文字」を"!"で表した後、
#「違う位置で同じ文字」を"?"で表す
def same_char(right,query):
    if len(right) != len(query):
        raise WrongWordLength
    if "!" in query or "?" in query:
        raise WrongWordError
    rtn_string = []
    for i in range(len(query)):
        if right[i] == query[i]:
            rtn_string.append("!")
        else:
            rtn_string.append("_")
    return "".join(rtn_string)

def create_mid_string(right,query):
    #「同じ位置で同じ文字」(!)だけを確定させた中間文字列を作る
    if len(right) != len(query):
        return WrongWordLength
    rtn_string = ["_"] * len(right)
    for i in range(len(right)):
        if query[i] == "!":
            rtn_string[i] = "!"
        else:
            rtn_string[i] = right[i]

    return "".join(rtn_string)

def same_char_but_diff_pos(right,query):
    #先にsame_charを実行して、「同じ位置」の文字は「!」に変わってる前提
    if len(right) != len(query):
        raise WrongWordLength
    if "!" in query or "?" in query:
        return WrongWordError
    rtn_string = ["_"] * len(right)
    temp_right = list(right)
    for i in range(len(query)):
        if right[i] == "!":
            rtn_string[i] = "!"
            continue
        for j in range(len(temp_right)):
            if temp_right[j] == -1:
                continue
            if query[i] == temp_right[j]:
                rtn_string[i] = "?"
                temp_right[j] = -1
                break
    return "".join(rtn_string)

def word_check(right,query):
    temp = same_char(right,query)
    mid_string = create_mid_string(right,temp)
    rtn = same_char_but_diff_pos(mid_string,query)
    return rtn

def game_main():
    result = []
    mx_game_counter = 6
    temp_game_counter = 0
    right_word = word_lst[randint(0,len(word_lst)-1)]
    print("word length:",len(right_word))
    while temp_game_counter < mx_game_counter:
        try:
            query = input()
            if len(query) != len(right_word):
                print("wrong word length")
                continue
            temp = word_check(right_word,query)
            temp_game_counter += 1
            result.append(temp)
            if set(temp) == set("!") :
                print("congratulations!")
                break
            print(temp)


        except WrongWordError:
            print("don't use '?' or '!'")
            continue
        except WrongWordLength:
            print("wrong word length")

    print("GAME OVER the secret word is",right_word)
    print(str(temp_game_counter) + "/" + str(mx_game_counter) )
    for line in result:
        print(line)







class MyTest(unittest.TestCase):

    def test_same_char(self):
        self.assertEqual(same_char("apple","ajjel"),"!____")

    def test_same_char_but_diff_pos(self):
        self.assertEqual(same_char_but_diff_pos("!pple","ajjel"),"!__??")

    def test_create_mid_string(self):
        self.assertEqual(create_mid_string("apple","!____"),"!pple",create_mid_string("!____","apple"))

    def test_3_same_char_func(self):
        right = "apple"
        query = "ajjel"
        temp = same_char(right,query)
        self.assertEqual(temp,"!____")
        mid_string = create_mid_string(right,temp)
        self.assertEqual(mid_string,"!pple")
        self.assertEqual(same_char_but_diff_pos(mid_string,query),"!__??")

    def test_3_same_char_func2(self):
        right = "apple"
        query = "alldl"
        temp = same_char(right,query)
        self.assertEqual(temp,"!____")
        mid_string = create_mid_string(right,temp)
        self.assertEqual(mid_string,"!pple")
        self.assertEqual(same_char_but_diff_pos(mid_string,query),"!?___")

if __name__ == "__main__":
    #unittest.main()
    game_main()