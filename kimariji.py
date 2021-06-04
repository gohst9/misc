from collections import defaultdict

def main():
    n,l = map(int,input().split()) #n = 言葉の数、l =１つの言葉の長さ
    words = []
    for _ in range(n):
        words.append(input())

    d = defaultdict(list)
    for word in words:
        d[word[0]].append(word)
    answer = dict()
    for i in range(2,l+1):
        new_d = defaultdict(list)
        for key in d.keys():
            words = d[key]
            if len(words) == 1:
                answer[key] = words[0]
            else:
                for word in words:
                    new_d[word[:i]].append(word)
        d = new_d
    print(answer)





if __name__ == '__main__':
    main()
