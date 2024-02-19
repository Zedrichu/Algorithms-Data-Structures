def merge_sort(values):
    """
    Recursive Merge Sort. O(n log n) time.
    """
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left_side = merge_sort(values[:mid])
    right_side = merge_sort(values[mid:]) 
    
    print("%15s %-15s" % (left_side, right_side))
    
    sortd = []
    lindex = 0
    rindex = 0
    
    while lindex < len(left_side) and rindex < len(right_side):
        if left_side[lindex] < right_side[rindex]:
            sortd.append(left_side[lindex])
            lindex += 1
        else:
            sortd.append(right_side[rindex])
            rindex += 1
    
    # Handle remaining values
    sortd += left_side[lindex:]
    sortd += right_side[rindex:]
    
    return sortd

# TEST:
arr = [4, 7, 2, 3, 6, 0, 4, 9]
print(arr)
srt = merge_sort(arr)
print(srt)