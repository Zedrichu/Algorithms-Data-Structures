def selection_sort(values):
    sortd = []
    
    print("%-25s %-25s" % (values, sortd))
    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sortd.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sortd))  
    return sortd

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

# TEST:
arr = [4, 7, 2, 3, 6, 0, 4, 9]
selection_sort(arr)