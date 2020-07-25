#hanged_man

import sys


def proved_word(target,proved):
    temp = []
    for i,c in enumerate(target):
        if proved[i] == True:
            temp.append(c)
        else:
            temp.append("_")

    return "".join(temp)



def main():
    target_word = input()
    left_chance = 5
    success = False
    game_continue = True
    proved = [False] * len(target_word)
    while game_continue:
        usr_input = input()
        if len(usr_input)!=1:
            print("input length must be a character.")
            continue
        for i,c in enumerate(target_word):
            if c == usr_input:
                proved[i] = True
        print(proved_word(target_word,proved))
        if proved_word(target_word,proved) == target_word:
            success = True
            game_continue = False
        left_chance -= 1
        if left_chance <= 0:
            game_continue = False
    if success == True:
        print("Congratulations!")
        print("The answer is:",target_word)
    else:
        print("Game Over")
        print("The answer is:",target_word)
    input("type something to quit.:")
    sys.exit()






if __name__ == '__main__':
    main()
