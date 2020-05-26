from collections import deque

def main():
    n = int(input())
    for answer in dfs(n):
        print(answer)


def dfs(n):
    #counter = 0
    arrows = "↑→↓←"
    d = deque()
    d.append("")
    answers = []
    while d:
        temp = d.popleft()
        if len(temp) >= n:
            answers.append(temp)
            counter += 1
            continue
        else:
            for arrow in arrows:
                d.append(temp+arrow)

    #print("手筋の数は",counter)

    return answers


if __name__ == '__main__':
    main()
