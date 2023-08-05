import sys
sys.path.append("../Linked Lists")
from SinglyLinkedList import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order using MergeSort. O(n log n)
    """
    
    if (linked_list.size() == 1 or not linked_list.head):
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
     
    return merge(left, right)
 
def split(linked_list):
    """ 
    Divide the unsorted list at midpoint into sublists.
    """
    if linked_list == None or linked_list.head == None:
        left  = linked_list
        right = None
    else:
        size = linked_list.size()
        mid = size // 2
        
        midNode = linked_list.nodeAtIndex(mid - 1)
        
        left = linked_list
        right = LinkedList()
        right.head = midNode.next
        midNode.next = None
    return left, right

def merge(link1, link2):
    """ 
    Merges the two linked lists, sorting in order
    Returns the newly merged linked list.
    """
    
    merged = LinkedList()
    # Fake head to be discarded later
    merged.add(0)
    # Set current to the head of the linked list
    current = merged.head
    # Obtain head nodes for the 2 sublists 
    lhd = link1.head
    rhd = link2.head
    
    # Iterate over left and right until reached tailed node
    while lhd or rhd:
        # If left is a tail, continue with right node
        if lhd is None:
            current.next = rhd
            rhd = rhd.next
        # If right is a tail, continue with left node
        elif rhd is None:
            current.next = lhd
            lhd = lhd.next
        else:
            left_key = lhd.data
            right_key = rhd.data
            # If data is less on the left, continue with left node
            if left_key < right_key:
                current.next = lhd
                lhd = lhd.next
            # If data is less on the right, continue with right node
            else:
                current.next = rhd
                rhd = rhd.next
        # Move forwards in the formed list
        current = current.next
    
    
    # Discard the fake head
    head = merged.head.next
    merged.head = head
    
    return merged