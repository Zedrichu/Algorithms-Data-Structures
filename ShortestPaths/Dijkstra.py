class PriorityQueue:
    def __init__(self, N):
        self.heap = [None]
        self.size = 0
        self.pos = [0 for _ in range(N)] # Position of each vertex in the ordered heap
        self.inHeap = [False for _ in range(N)] # Tracker for what vertices are outside MST at each point

    def isEmpty(self):
        return self.size == 0 

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp
        
        temp = self.pos[self.heap[x][1]]
        self.pos[self.heap[x][1]] = self.pos[self.heap[y][1]]
        self.pos[self.heap[y][1]] = temp
        

    # Function to determine which node has the greater cut edge weight
    def greater(self, x, y):
        return 1<=x<=self.size and 1<=y<=self.size and \
                    self.heap[x][0] > self.heap[y][0]

    # Functions to maintain the heap invariant
    def bubbleUp(self, node):
        parent = node // 2
        if (self.greater(parent,node)):
            self.swap(node,parent)
            self.bubbleUp(parent)
    def bubbleDown(self,node):
        left = node*2
        child = left + self.greater(node*2,node*2+1)
        if (self.greater(node,child)):
            self.swap(node,child)
            self.bubbleDown(child)

    # Insert a new entry pair in the priority queue
    def insert(self, pair):
        self.heap.append(pair)
        self.size += 1
        self.pos[pair[1]] = self.size
        self.inHeap[pair[1]] = True
        self.bubbleUp(self.size)

    # Extract the minimum entry from priority queue
    def extractMin(self):
        (key, ver) = self.heap[1]
        self.inHeap[ver] = False
        self.pos[ver] = 0
        self.pos[self.heap[self.size][1]] = 1
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.bubbleDown(1)
        return (key, ver)

    # Decrease the key of a specific node in the priority queue
    def decreaseKey(self, x, key):
        index = self.pos[x]
        if key < self.heap[index][0]:
            # print("{}#{}".format(key,index))
            self.heap[index] = (key, x)  
            self.bubbleUp(index)

N, M = map(int, input().split())
# Function to build the adjacency list of the graph
def AdjList():
    adj = [[] for _ in range(N)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        (adj[i]).append((w, j))
        (adj[j]).append((w, i))
    return adj
G = AdjList()   

# Dijkstra's algorithm for computing shortest paths
def Dijkstra(G, s):
    # Keep a minimum priority queue of pairs->(distance estimate, vertex)
    PQ = PriorityQueue(N)
    distance = [float('inf') for _ in range(N)]
    # Initialize all vertices in priority queue with infinity
    for i in range(N):
        PQ.insert((float('inf'), i))
    # The starting node gets decreased to 0 distance
    PQ.decreaseKey(s,0)
    # As long as there are nodes to be reached
    while (not PQ.isEmpty()):
        # Extract the smallest distance estimate
        p, u = PQ.extractMin()
        distance[u] = p
        # Relax all edges leaving u
        for wht, v in G[u]:
            if (distance[v] > distance[u]+wht):
                PQ.decreaseKey(v, distance[u]+wht)
    return distance

print(Dijkstra(G, 0))