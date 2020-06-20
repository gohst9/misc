#入力1　原材料となる木材の長さのリスト
#入力2　作る必要のある木材の長さのリスト
#出力　 入力1の木材を使って入力2の木材を全て作ることができるかどうか


import heapq #優先度付きキュー

def main():
    source_woods = list(map(int,input().split())) #原材料の木材
    source_woods = [-n for n in source_woods]
    heapq.heapify(source_woods) #優先度付きキュー（全ての要素を負の数にして逆順に）
    products = list(map(int,input().split())) #作りたい木材
    products.sort()
    while products and source_woods: #作る必要のある木材が存在する間
        print("source woods:",source_woods)
        print("products:",products)
        source_wood = -heapq.heappop(source_woods)
        product = products.pop()
        if product <= source_wood:
            source_wood -= product
        else:
            products.append(product)
            break

        if source_wood > 0: #材料の木がまだ残っているときは優先度付きキューである原材料リストに戻す
            heapq.heappush(source_woods,-source_wood)

    if len(products) > 0:
        print("No")
    else:
        print("Yes")




if __name__ == '__main__':
    main()
