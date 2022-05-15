import sys 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self,X):
        X.next = self.head
        if (self.head==None): 
            self.tail = X
        self.head = X

    def dequeue(self):
        if (self.head==None and self.head == self.tail):
            val = self.head.value
            self.tail = None
            self.head = None
        else:
            q = self.head
            while (q.next != self.tail):
                q = q.next
            val = self.tail.value
            q.next = None
            self.tail = q
        return val    
        
Q = Queue()    
N = int(input())

for i in range(N):
    str = input().split()
    if str[0][0]=='E':
        Q.enqueue(Node(int(str[1])))
    elif str[0][0]=="D":
        print(Q.dequeue())
