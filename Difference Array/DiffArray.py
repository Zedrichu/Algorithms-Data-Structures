# Difference Array structure for fast range updates and single queries
# Initialization - create the difference and prefix sum arrays (Fenwick) - O(n) time/space complexity
# Add(i,j,k) - update the range [i;j] by adding k to each value - O(1) time complexity
# Lookup(i) - query a single value in array after preprocessing - O(1) time complexity

class DiffArray:
    def __init__():
        pass
    
    def initialize(A):
        n = len(A)
        D = [0] * (n + 1)
        for i in range(1, n):
            D[i] = A[i] - A[i-1]
        P = [0] * (n + 1)
        for i in range(1, n + 1):
            P[i] = P[i-1] + D[i]
        return D, P

    def add(D, i, j, k):
        D[i] += k
        D[j+1] -= k

    def lookup(P, i):
        return P[i]

# Example usage
A = [1, 2, 3, 4, 5]  # Original array
dfa = DiffArray()
D, P = dfa.initialize(A)
dfa.add(D, 2, 4, 10)  # Add 10 to elements from index 2 to 4
print(dfa.lookup(P, 3))  # Lookup the value at index 3
