
class PriorityQueue:
    def __init__(self):
        self.heap = [None]
        self.n = 0

    def less(self, x, y):
        return 1<=x<=self.n and 1<=y<=self.n and self.heap[x]<self.heap[y]

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp

    def bubbleUp(self,node):
        parent = node//2
        if (self.less(parent,node)):
            self.swap(node,parent)
            self.bubbleUp(parent)

    def bubbleDown(self,node):
        left = node*2
        child = left + self.less(node*2,node*2+1)
        if (self.less(node,child)):
            self.swap(node,child)
            self.bubbleDown(child)

    def max(self):
        return self.heap[1]

    def insert(self, x):
        self.heap.append(x)
        self.n += 1
        self.bubbleUp(self.n)

    def extractMax(self):
        r = self.heap[1]
        self.heap[1] = self.heap[self.n]
        self.heap.pop()
        self.n -= 1
        self.bubbleDown(1)
        return r
    
    def increaseKey(self, x, key):
        self.heap[x] = key
        self.bubbleUp[x]

    def print(self):
        for i in range(self.n):
            print(self.heap[i+1],end=' ')
        print()

N = int(input())
lines = [input().split() for _ in range(N)]

pq = PriorityQueue()
for line in lines:
    if line[0]=='I':
        pq.insert(int(line[1]))
    elif line[0]=='E':
        print(pq.extractMax())
    elif line[0]=='P':
        pq.print()
