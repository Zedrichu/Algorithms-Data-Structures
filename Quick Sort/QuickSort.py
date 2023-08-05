def quicksort(values):
    """ 
    Recursive Quick Sort. O(n log n) time.
    """
    if len(values) <= 1:
        return values
    
    less = []
    greater = []
    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less.append(value)
        else:
            greater.append(value)
    print("%15s %1s %-15s" % (less, pivot, greater))
    return quicksort(less) + [pivot] + quicksort(greater)
    
# TEST:
arr = [4, 7, 2, 3, 6, 0, 4, 9]
print(quicksort(arr))