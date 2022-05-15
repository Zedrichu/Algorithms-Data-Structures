"""
    Implementation of Hashing with Linear Probing:
        .- the hash table S maintained in array A of size m
        .- element x stored in A[ h(x.key) ] or cluster
            to the right of A[ h(x.key) ]

    Search => linear search key k from A[h(k)] to the right in cluster
    Insert => insert element x on A[ h(x.key) ] if empty or 
                in cluster to the right, otherwise
    Delete => remove element with key from A[h(k)] or later and re-insert 
                all elements in cluster to the right of it
"""

# Pair up the key and value to be stored in the hash table
class Pair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return "{}::{}".format(self.key, self.value)

# Hashing with Linear Probing
class LinearHash:
    
    def __init__(self, size) -> None:
        self.A = [None] * size
        self.size = size
        
    def hash(self, key):
        return key % self.size

    def Search(self, key):
        h = self.hash(key)
        c = 0
        while (not (self.A[h] == None) \
                    and c != self.size):
            if (self.A[h].key == key):
                return self.A[h]
            c += 1
            h = (h+1) % self.size
        return None

    def Insert(self, item):
        h = self.hash(item.key)
        c = 0
        while (c != self.size and not(self.A[h] == None)):
            h = (h+1) % self.size
            c += 1
        if (c != self.size):
            self.A[h] = item
        else:
            raise OverflowError
        
    def Delete(self, key):
        h = self.hash(key)
        c = 0
        
        while (not (self.A[h] is None) and (self.size != c)):
            if (self.A[h].key == key):
                self.A[h] = None
            # Re-insert all keys in the cluster to the right of the item having key
            else:
                temp = self.A[h]
                self.A[h] = None
                self.Insert(temp)
                
            h = (h+1) % self.size
            c+=1    
        
        # -> Attempt to delete key not present in the hash table!
        
    def __str__(self) -> str:
        out = ""
        for item in self.A:
            out += str(item)+" "
        return out


# Application:
#Total number of keys inserted
N = int(input())

#Creating object hashTable
hasher = LinearHash(N)

# Allow insertion and deletions of values from the hash table
for i in range(N):
    line = input().split()
    if line[0] == 'I':
        pair = Pair(int(line[1]), "")
        hasher.Insert(pair)
    elif line[0] == 'D':
        hasher.Delete(int(line[1]))
    print(hasher)

