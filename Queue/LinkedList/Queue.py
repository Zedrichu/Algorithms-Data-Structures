import sys 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def peek(self):
        return self.head
    
    def contains(self, value):
        iterator = self.head
        while (iterator != self.tail and iterator.value != value):
            iterator = iterator.next
        return iterator.value == value
    
    def enqueue(self, X):
        if (self.tail==None): 
            self.head = X
            self.tail = X
            return     
        self.tail.next = X
        self.tail = X

    def dequeue(self):
        if (self.isEmpty()): 
            return
        temp = self.head
        self.head = self.head.next
        
        if (self.head == None):
            self.tail = None
        
        return temp
        
Q = Queue()

# <| Test Block |>
# Q.enqueue(Node(2))
# Q.enqueue(Node(3))
# Q.enqueue(Node(1))
# print(Q.peek().value)
# print(Q.contains(3))
# print(Q.contains(4))

# <| Problem Block |>     
N = int(input())

for i in range(N):
    str = input().split()
    if str[0][0]=='E':
        Q.enqueue(Node(int(str[1])))
    elif str[0][0]=="D":
        print(Q.dequeue().value)
