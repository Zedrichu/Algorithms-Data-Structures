class QuickUnion:
    def __init__(self, N):
        self.p = [k for k in range(N)]
    
    def find(self, i):
        while (i != self.p[i]):
            i = self.p[i]
        return i

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if (ri != rj):
            self.p[ri] = rj

N = int(input())
M = int(input())
lines = [input().split() for _ in range(M)]
QU = QuickUnion(N)
for line in lines:
    if line[0]=='F':
        print(QU.find(int(line[1])))
    elif line[0]=='U':
        QU.union(int(line[1]),int(line[2]))
