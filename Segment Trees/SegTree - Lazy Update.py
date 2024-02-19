# Segment tree for range updates and single point queries
# Construction - build the Segment Tree - O(n) time/space complexity
# Update Range (add(i,j,k)): tree traversal and updates from index i to j with +k - O(log n) time complexity
# Query (lookup(i)): traverses the tree down to a specific leaf, applying any pending updates along the way - O(log n) time complexity
class SegmentTree:
    def __init__(self, A):
        self.n = len(A)
        self.tree = [0] * (4 * self.n)  # Segment tree array
        self.lazy = [0] * (4 * self.n)  # Lazy propagation array
        self.build(A, 0, 0, self.n - 1)

    def build(self, A, node, start, end):
        if start == end:
            self.tree[node] = A[start]
        else:
            mid = (start + end) // 2
            # Recursively build the left and right children
            self.build(A, 2*node+1, start, mid)
            self.build(A, 2*node+2, mid+1, end)
            # Internal node will have the sum of both of its children
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update_range(self, node, start, end, l, r, val):
        # Update current node if it has any pending updates
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            # Propagate the update to the children nodes if not a leaf node
            if start != end:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0

        # No overlap condition
        if start > end or start > r or end < l:
            return

        # Total overlap condition
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:  # Not a leaf node
                self.lazy[2*node+1] += val
                self.lazy[2*node+2] += val
            return

        # Partial overlap condition
        mid = (start + end) // 2
        self.update_range(2*node+1, start, mid, l, r, val)
        self.update_range(2*node+2, mid+1, end, l, r, val)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, start, end, idx):
        # Ensure all pending updates are applied to this node
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:  # Propagate updates to children
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0

        # If the current node represents the element at idx
        if start == end == idx:
            return self.tree[node]

        mid = (start + end) // 2
        if idx <= mid:
            return self.query(2*node+1, start, mid, idx)
        else:
            return self.query(2*node+2, mid+1, end, idx)

# Example usage
A = [1, 2, 3, 4, 5]
seg_tree = SegmentTree(A)
seg_tree.update_range(0, 0, len(A)-1, 1, 3, 10)  # ADD(1, 3, 10)
print(seg_tree.query(0, 0, len(A)-1, 2))  # Lookup(2)

