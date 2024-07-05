def insert(L, x):
    sorted_list = L[:]  # Create a copy of the original list to avoid disturbing it
    index = 0
    # Find the index where x should be inserted to maintain sorted order
    while index < len(sorted_list) and sorted_list[index] < x:
        index += 1
    # Insert x at the found index
    sorted_list.insert(index, x)
    return sorted_list
l = [1,2,3,4,5]
x = 4
result = insert(l,x)
print(result)