class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
    
    def isLeaf(self):
        if self.left != None and self.right != None:
            return True
        return False
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, node):
        y = None
        x = self.root
        while (x != None):
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif (node.key < y.key):
            y.left = node
        else:
            y.right = node

    def predecessor(self, node):
        if node.left != None:
            return self.maximum(node.left)
        y = node.parent
        x = node
        while (y != None and x == y.right):
            x = y
            y = y.parent
        return y

    def successor(self, node):
        if node.right != None:
            return self.minimum(node.right)
        y = node.parent
        x = node
        while (y != None and x == y.left):
            x = y
            y = y.parent
        return y
    
    def maximum(self, node):
        x = node
        while x.right != None:
            x = x.right
        return x

    def minimum(self, node):
        x = node
        while x.left != None:
            x = x.left
        return x

    def size(self, root):
        if (root == None):
            return 0
        return self.size(root.left)+self.size(root.right)+1

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right =v
        if v != None:
            v.p = u.p

    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def search(self, root, key):
        if root == None or key == self.root.key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inOrder(self, root):
        if root == None:
            return ""
        s = str(root.key)+" "
        return self.inOrder(root.left)+s+self.inOrder(root.right)

    def preOrder(self, root):
        if root == None:
            return ""
        s = str(root.key)+" "
        return s+self.preOrder(root.left)+self.preOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return ""
        s = str(root.key)+" "
        return self.postOrder(root.left)+self.postOrder(root.right)+s



elements = list(map(int, input().split()))
tree = BinaryTree()
for value in elements:
    tree.insert(Node(value))

print("In-order traversal"+tree.inOrder(tree.root))
print("Pre-order traversal"+tree.preOrder(tree.root))
print("Post-order traversal"+tree.postOrder(tree.root))