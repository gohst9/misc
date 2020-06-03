import sympy
import collections
import functools

def is_prime(n):
    #nが素数かどうか判定する
    furui = [-1] * (n+1)
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n%i == 0: #n//2までの間に割り切れる数が見つかればnは素数ではない
            return False

    return True

def factor(n):
    if n == 1:
        return [1]
    divs = sympy.divisors(n) #約数列挙
    divs = divs[1:] #1を消去
    d = collections.deque()
    answers = []
    for div in divs:
        d.append([div])
    while d:
        temp = d.popleft()
        prod = functools.reduce(lambda a,b:a*b,temp)
        if prod == n:
            answers.append(temp)
            continue
        elif prod > n:
            continue
        else:
            for new_div in [div for div in divs if div >= temp[-1]]:
                d.append(temp + [new_div])

    return answers



def main():
    n = int(input())
    factors_lst = factor(n)
    for factors in factors_lst:
        if all(map(is_prime,factors)):
            print(" ".join(map(str,factors)),"all prime!")
        else:
            print(" ".join(map(str,factors)))


if __name__ == '__main__':
    main()
