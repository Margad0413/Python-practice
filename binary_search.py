#Binary Search (Cycle)
def binary_search(A,key,low,high):
    if(low <=high):
        mid = (low+high)//2
        if key == A[mid]:
            return mid
        elif key <A[mid]:
            return binary_search(A,key,low,mid-1)
        else:
            return binary_search(A,key,mid+1,high)
    return -1

#Binary Search (iterative)
def binary_search_iter(A,key,low,high):
    while(low<=high):
        mid = (low+high)//2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

list = [1,3,8,13,13,16,21,26,27,30,33,36,39,41,44,49]

print("33: ",binary_search(list,33,0,len(list)-1))
print("33: ",binary_search_iter(list,33,0,len(list)-1))
