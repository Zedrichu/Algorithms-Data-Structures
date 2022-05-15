import sys
sys.setrecursionlimit(5000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def preOrder(node):
    if node is None:
        return ""
    s = str(node.key) + " "
    return s + preOrder(node.left) + preOrder(node.right)

N = int(input())
# Create the binary tree with root in index 0
binTree = [0] * N
binTree[0] = Node(int(input()))

for i in range(1,N):
    line = input().split()
    binTree[i] = Node(int(line[2]))
    if (line[1]=='L'):
        binTree[int(line[0])].left = binTree[i]
    else:
        binTree[int(line[0])].right = binTree[i]

print(preOrder(binTree[0]))