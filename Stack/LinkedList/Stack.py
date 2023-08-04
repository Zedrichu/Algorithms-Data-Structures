import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None
    
    def peek(self):
        return self.top
    
    def contains(self, value):
        iterator = self.top
        while (iterator.next and iterator.value != value):
            iterator = iterator.next
        return iterator.value == value
        
    def push(self,X):
        if self.isEmpty():
            self.top = X
        else:
            X.next = self.top
            self.top = X
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            X = self.top
            self.top = self.top.next
            print(X.value)
            return X

S = Stack()    

# <| Test Block |>
# S.push(Node(2))
# S.push(Node(3))
# print(S.contains(1))
# print(S.peek().value)

# <| Problem Block |>
N = int(input())

for i in range(N):
    str = input().split()
    if str[0][0]=='P':
        if (str[0][1] =='U' ):
            S.push(Node(int(str[1])))
        else:
            S.pop()