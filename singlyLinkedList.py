class Node:  # Node 클래스 
    def __init__(self, key = None, value = None):
        self.key = key  # 노드들 간 구분하는 key
        self.value = value  # value는 추가 데이터
        self.next = None  # 노드를 연결하는 link

    def __str__(self):
        return str(self.key)
    



class SinglyLinkedList:  # 한방향 연결 리스트 클래스
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        v = self.head

        while v != None:
            yield v
            v = v.next
        
    def __str__(self):
        return " -> ".join(str(v) for v in range self)
    
    # 한방향 연결 리스트의 삽입 연산들
    def pushFront(self, key, value = None):  # 한방향 연결 리스트에서 맨 앞에 노드를 삽입하는 연산
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pushBack(self, key, value = None):  # 한방향 연결 리스트에서 맨 뒤에 노드를 삽입하는 연산
        new_node = Node(key, value)

        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            
            tail.next = new_node
        
        self.size += 1

    # 한방향 연결 리스트의 삭제 연산들
    def popFront(self):  # 한방향 연결 리스트에서 맨 앞에 노드를 삭제하는 연산
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            del x
            self.size -= 1

            return key

    def popBack(self):  # 한방향 연결 리스트에서 맨 뒤에 노드를 삭제하는 연산
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            
            if prev == None:
                self.head = None
            else:
                prev.next = tail.next
            
            key = tail.key
            del tail
            self.size -= 1

            return key

    def remove(self, v = None):  # 한방향 연결 리스트에서 입력받은 노드를 삭제하는 연산
        if self.size == 0 or v == None:
            return None
        elif self.head == v:
            return self.popFront()
        else:
            prev, tail = None, self.head
            while tail != None:
                if tail == v:
                    prev.next = tail.next
                    key = tail.key
                    del tail
                    self.size -= 1

                    return key

                prev = tail
                tail = tail.next
            
            return None

    # 한방향 연결 리스트의 탐색 연산
    def search(self, key):  # 한방향 연결 리스트에서 입력받은 key와 일치하는 노드를 찾아 리턴하는 연산
        v = self.head

        while v != None:
            if v.key == key:
                return v
            
            v = v.next
        
        return None

    