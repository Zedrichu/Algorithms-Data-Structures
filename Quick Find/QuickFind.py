class QuickFind:
    
    def __init__(self, N):
        self.ids = [k for k in range(N)]
        self.size = N
    
    def find(self, i):
        return self.ids[i]

    def union(self, i, j):
        iID = self.find(i)
        jID = self.find(j)
        if (iID != jID):
            for k in range(self.size):
                if (self.ids[k] == iID):
                    self.ids[k] = jID

N = int(input())
M = int(input())
lines = [input().split() for _ in range(M)]
QF = QuickFind(N)
for line in lines:
    if line[0]=='F':
        print(QF.find(int(line[1])))
    elif line[0]=='U':
        QF.union(int(line[1]),int(line[2]))
