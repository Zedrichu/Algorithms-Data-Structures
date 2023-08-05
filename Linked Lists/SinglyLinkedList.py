class Node:
    """
    Object storing a single node of the linked list 
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return "< Node ~~ %s>" % self.data
    
class LinkedList:
    """ 
    Object storing the singly-linked list    
    """
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next
            
        return '-> '.join(nodes)
             
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        
        while(current != None):
            count += 1
            current = current.next
        
        return count
    
    def nodeAtIndex(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while (position < index):
                current = current.next
                position += 1
            return current 
    
    def add(self, data):
        """
        Adds new node of data to the head of the list (prepending). O(1) time
        """        
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def search(self, key):
        """ 
        Searches for a node with certain value in the linked list. O(n) time
        Returns the found node or None, otherwise.
        """ 
        current = self.head
        while (current):
            if (current.data == key): 
                return current
            current = current.next
            
        return None    
        
    def insert(self, data, index):
        """ 
        Inserts a new node with data value at specified index in the linked list. O(n) time
        Finding the right position takes O(n) time - actual insertion takes O(1) time
        """
        if (index == 0): 
            self.add(data)

        if (index > 0):
            new = Node(data)
            
            position = index - 1 # Stop one index before 
            current = self.head
            
            while (position > 0):
                current = current.next
                position -= 1
            
            nodeBefore = current
            nodeAfter = current.next
            
            nodeBefore.next = new
            new.next = nodeAfter
    
    def remove(self, key): 
        """ 
        Removes the node with key value from the linked list. O(n) time
        Returns the removed node or None if not found.
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key:
                found = True
                if current is self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
            previous = current
            current = current.next
        return previous
            
        