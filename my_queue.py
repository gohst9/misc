class Queue_item:
    #キュー内の要素にはそれ自体の値と次の値へのリンクがある
    def __init__(self,v,next=None):
        self.value = v
        self.next = next

class Queue:
    def __init__(self,v=0):
        self.first = None
        self.last = None
    def push(self,v):
        #キューの一番後ろに値を付け足す
        if self.first == None:
            self.first = Queue_item(v)
            self.last = self.first
        else:
            #キューの一番最後の要素に新しい要素へのリンクを追加した後、
            #一番最後を新しい要素に変える
            self.last.next = Queue_item(v)
            self.last = self.last.next
    def pop(self):
        if self.first == None:
            return None

        #一番最初の要素を取り出した後、
        #Queue_Item内の次の要素へのリンク（next）をつかって
        #一番最初の要素を次の要素に変える
        temp = self.first.value
        if self.first.next != None:
            self.first = self.first.next
        else:
            self.first = None
            self.last = None
        return temp




def main():
    q = Queue()
    for i in [1,2,3]:
        q.push(i)

    for i in range(3):
        print(q.pop())
        #先入れ先出しで「1,2,3」の順番で出力される

if __name__ == '__main__':
    main()
