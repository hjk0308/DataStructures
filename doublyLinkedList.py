class Node:  # Node 클래스 
    def __init__(self, key = None):
        self.key = key  # 노드들 간 구분하는 key
        self.prev = self  # 노드의 전 노드를 연결하는 link
        self.next = self  # 노드의 후 노드를 연결하는 link

    def __str__(self):
        return str(self.key)



class DoublyLinkedList:  # 양방향 연결 리스트 클래스
    def __init__(self):
        self.head = Node();
        self.size = 0
    
    def __iter__(self):
        v = self.head

        while v != None:
            yield v
            v = v.next
        
    def __str__(self):
        return " -> ".join(str(v) for v in range self)
    
    def __len__(self):
            return self.size

    # 양방형 연결 리스트의 이동 및 삽입 연산들
    def splice(self, a, b, x):  # 노드 a에서 노드 b까지를 떼어서 노드 x 뒤에 붙이는 연산
        if a == None or b == None or x == None:
            return

        ap = a.prev
        bn = b.next

        ap.next = bn
        bn.prev = ap

        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
    
    def moveAfter(self, a, x):  # 노드 a를 노드 x 뒤로 이동시키는 연산
        self.splice(a, a, x)
    
    def moveBefore(self, a, x):  # 노드 a를 노드 x 앞으로 이동시키는 연산
        self.splice(a, a, x.prev)
    
    def insertAfter(self, x, key):  # 노드 x 뒤에 key를 가진 새 노드를 생성해 삽입하는 연산
        self.moveAfter(Node(key), x)
        self.size += 1

    def insertBefore(self, x, key):  # 노드 x 앞에 key를 가진 새 노드를 생성해 삽입하는 연산
        self.moveBefore(Node(key), x)    
        self.size += 1

    def pushFront(self, key):  # key를 가진 새 노드를 생성해 head 다음에 삽입하는 연산
        self.insertAfter(self.head, key)
        self.size += 1

    def pushBack(self, key):  # key를 가진 새 노드를 생성해 head 전에 삽입하는 연산
        self.insertBefore(self.head, key) 
        self.size += 1

    # 양방형 연결 리스트의 삭제 연산들  
    def remove(self, x):  # 양방형 연결 리스트에서 노드 x를 삭제하는 연산 
        if x == None or x == self.head:
            return
        
        x.prev.next = x.next
        x.next.prev = x.prev

        del x

        self.size -= 1

    def popFront(self):  # 양방형 연결 리스트에서 head 다음 노드를 삭제하는 연산 
        if self.isEmpty():
            return None
        
        key = self.head.next.key
        self.remove(self.head.next)
        self.size -= 1

        return key
    
    def popBack(self):  # 양방형 연결 리스트에서 head 전 노드를 삭제하는 연산 
        if self.isEmpty():
            return None
        
        key = self.head.prev.key
        self.remove(self.head.prev)
        self.size -= 1

        return key
    
    # 양방형 연결 리스트의 탐색 및 기본 연산들
    def search(self, key):  # 양방형 연결 리스트에서 입력받은 key와 동일한 key를 가진 노드를 찾아 리턴하는 연산
        if self.isEmpty():
            return None
        
        n = self.head.next
        while n != self.head:
            if n.key == key:
                return n
            
            n = n.next
        
        return None

    def isEmpty(self):  # 양방형 연결 리스트가 비었는지를 리턴하는 연산 
        if self.size == 0:
            return True
        else:
            return False

    def first(self):  # 양방형 연결 리스트의 처음 노드를 리턴하는 연산
        if self.isEmpty():
            return None
        else:
            return self.head.next
    
    def last(self):  # 양방형 연결 리스트의 마지막 노드를 리턴하는 연산
        if self.isEmpty():
            return None
        else:
            return self.head.prev
