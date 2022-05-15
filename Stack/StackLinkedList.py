import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def push(self,X):
        if self.isEmpty():
            self.head = X
        else:
            X.next = self.head
            self.head = X
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            X = self.head
            self.head = self.head.next
            print(X.value)
            return X

S = Stack()    
N = int(input())

for i in range(N):
    str = input().split()
    if str[0][0]=='P':
        if (str[0][1] =='U' ):
            S.push(Node(int(str[1])))
        else:
            S.pop()
