def selection_sort(data):
    for i in range(0,len(data)):
        min_index = i
        for j in range(i+1,len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

data = [5,3,8,4,9,1,6,2,7]
print("Original:",data)
selection_sort(data)
print("Selection:",data)
