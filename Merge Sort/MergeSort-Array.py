def merge_sort(list):
    """
    Sorts a list in ascending order, returning a new sorted list. O(n log n) time.
    
    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in the previous step.
    Combine: Merge the sorted sublists created in the previous step.
    """
    
    if (len(list)<=1):
        return list
    
    left_half, right_half = split(list)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
    
    
def split(list):
    """ 
    Divide the unsorted list at midpoint into sublists. O(log n) time.
    """
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(list1, list2):
    """ 
    Merges the two lists, in a sorted order. O(n) time
    """
    
    l = []
    i = j = 0
    
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            l.append(list1[i])
            i += 1
        else:
            l.append(list2[j])
            j += 1
    
    while i<len(list1):
        l.append(list1[i])
        i += 1
        
    while j<len(list2):
        l.append(list2[j])
        j += 1
    
    return l