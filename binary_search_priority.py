def binary_search_depth(left,right,depth_lst,depth):
    if abs(right - left) <= 1:
        return
    mid = (right + left) // 2
    #print(*depth_lst)
    depth_lst[mid] = depth
    binary_search_depth(mid,right,depth_lst,depth+1)
    binary_search_depth(left,mid,depth_lst,depth+1)
    return depth_lst


def meguru_bisect(ng,ok,target,lst,depths):
    depth = 1

    def is_ok(n,target):
        return lst[n] >= target

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        depths[mid] = depth
        if lst[mid] == target:
            return mid #目標を見つけたらその時点でリターン
        if is_ok(mid,target):
            ok = mid
        else:
            ng = mid

        depth += 1
    return ok

def main():
    lst = list(map(int,input("探索する数列").split()))
    target = int(input("探索する数値"))

    depths = ["*"] * len(lst)

    answer = meguru_bisect(-1,len(lst),target,lst,depths)
    depths2 = ["*"] * len(lst)
    all_depth = binary_search_depth(-1,len(lst),depths2,1)
    print("答え",answer,"" if 0 <= answer < len(lst) else "(目標未発見)")
    print(*depths," ",max([x for x in depths if x != "*"]),"回探索を実行")
    print(*all_depth,"←すべてのインデックスの優先順位")

if __name__ == '__main__':
    main()
