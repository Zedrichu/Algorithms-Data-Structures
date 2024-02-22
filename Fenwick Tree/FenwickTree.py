# Partial Sum Data Structure - Fenwick Tree
# Space complexity: in-place
# Construction: O(N * log N) - add each of N elements to tree once
# Query complexity: both `update` and `sum` operations in O(log N) time

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx

    def sum(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

# Range Update and Point Query in O(log n) Time Complexity

# Pre-processing: 
#   compute Difference Array D for original array A - O(N)
#   build Fenwick tree corresponding to Difference Array - O(N*log N)

# Update Range (add(i,j,k)): increase difference value at i and decrease 
#   difference value at j+1 by k - simulate updating range with same values
#   Inner difference values remain the same - only margins change - O(log N)

# Point Query (lookup(i)): compute partial sum [1 -> i] 
#   for maintained original value at index i - O(log N)

def add(fenwickTree, i, j, k):
    fenwickTree.update(i, k)
    fenwickTree.update(j + 1, -k)

def lookup(fenwickTree, i):
    return fenwickTree.sum(i)

n = 5  # Length of the array
fenwickTree = FenwickTree(n)

for item in [1, 2, 3, 4, 5]:
    fenwickTree.update(item, item)
    
print(fenwickTree.tree)
print(lookup(fenwickTree, 5))

# Suppose we want to ADD(1, 3, 10) to the array [1, 2, 3, 4, 5]
add(fenwickTree, 1, 3, 10)
print(fenwickTree.tree)

# Now, let's do a Lookup(3) to get the updated value at index 3
print(lookup(fenwickTree, 3))  # Output will reflect the updates
