"""
    Implementation of Hashing with Chaining:
        .- the hash table S maintained in array A of linked lists
        .- element x stored in linked list at A[ h(x.key) ] 

    Search => linear search key k from A[h(k)]
    Insert => insert element x in front of list at A[ h(x.key) ]
    Delete => remove element with key from list at A[h(k)] 
"""

# Pair the key and value
class Pair:
    def __init__(self, key, value) -> None:
        self.key = key 
        self.value = value
    
    def __str__(self) -> str:
        return "{}::{}".format(self.key, self.value)

# Chained Hashing
class ChainHash:
    def __init__(self,size):
        self.A = [[]] * size 
        self.size = size
        
    def __str__(self) -> str:
        out = "["
        for ll in self.A:
            if (ll != []):
                out += "["
                for item in ll:
                    out += str(item)+", "
                out += "] "
            else:
                out += str(ll)+", "
        out += "]"
        return out

    def hash(self, key):
        return key % self.size

    def Delete(self, key):
        h = self.hash(key)
        if (self.A[h] != []):
            # linear search for the key
            for pair in self.A[h]:
                if (pair.key == key):
                    self.A[h].remove(pair)
    
    def Insert(self, x):
        h = self.hash(x.key)
        if (self.A[h] == []):
            self.A[h] = [x]
        else:
            # place element in front of list
            self.A[h].append(x)
    
    def Search(self, key):
        h = self.hash(key)
        if (self.A[h] != []):
            # linear search for the key
            for item in self.A[h]:
                if (item.key == key):
                    return item



N = int(input())
hasher = ChainHash(N)

for _ in range(N):
    line = input().split()
    if (line[0] == "I"):
        pair = Pair(int(line[1]), "")
        hasher.Insert(pair)
    elif (line[0] == "D"):
        hasher.Delete(int(line[1]))
    print(hasher)
