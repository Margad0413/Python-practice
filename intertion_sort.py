def insertion_sort(A):
    n  = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
        printStep(A,i)
def printStep(arr, val) :   
    print("  Step %2d = " % val, end='')	
    print(arr)
  
A = [5,3,8,4,9,1,6,2,7]
print(A)
insertion_sort(A)
