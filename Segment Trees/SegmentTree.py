class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (4 * self.n)  # Allocate memory
        self.build(array, 0, 0, self.n - 1)

    def build(self, array, node, start, end):
        if start == end:  # Leaf node
            self.tree[node] = array[start]
        else:
            mid = (start + end) // 2
            # Recursively build the left and right children
            self.build(array, 2 * node + 1, start, mid)
            self.build(array, 2 * node + 2, mid + 1, end)
            # Internal node's value is the sum of its children
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_sum(self, node, start, end, L, R):
        if L <= start and end <= R:  # Total overlap
            return self.tree[node]
        if end < L or R < start:  # No overlap
            return 0
        # Partial overlap
        mid = (start + end) // 2
        sum_left = self.query_sum(2 * node + 1, start, mid, L, R)
        sum_right = self.query_sum(2 * node + 2, mid + 1, end, L, R)
        return sum_left + sum_right

    def sum_range(self, L, R):
        return self.query_sum(0, 0, self.n - 1, L, R)

# Example Usage
array = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(array)
print(seg_tree.sum_range(1, 3))  # Query the sum of elements from index 1 to 3


# Steps to Process Sum Queries with Segment Trees:

# Build the Segment Tree:
#   Construct a segment tree from the given array. Each node in the segment tree represents a range of the array (with leaf nodes representing a single element) and stores the sum of that range.
#   The root of the tree represents the sum of the entire array.

# Query the Sum of a Range:
#   To query the sum of a range [L, R], you traverse the tree starting from the root, narrowing down to the segments that fall within the query range.
#   If a segment is completely within the range [L, R], its sum is included in the total sum.
#   If a segment is outside the range [L, R], it is ignored.
#   If a segment partially overlaps with the range [L, R], the search continues to that segment's children.

# Complexity Analysis
#   Space Complexity: 
#       O(n), as the segment tree requires space proportional to the size of the input array.
#   Time Complexity:
#       Building the segment tree: O(n), since each node of the tree is filled exactly once.
#       Querying the sum of a range: O(logn), due to the binary nature of the tree traversal.