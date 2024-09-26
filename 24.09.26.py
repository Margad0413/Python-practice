a = [5,3,8,4,2,7]
key = 6
def sequential_search(a,key):
    for i in range(0,len(a)):
        if a[i]==key:
            return i
    return -1

print(sequential_search(a,key))

a = ['B','R','U','T','E','F','O','R','A']
key = ['F','O','R']

def match_string(a,key):
    for j in range(0,len(a)-len(key)+1):
        if key[0] == a[j]:
            for k in range(1,len(key)):
                if a[j+k] != key[k]:
                    break
            return j
    return -1
print(a)
print(" in ")
print(key)
print(match_string(a,key))

import math

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
def closest_pair(a):
    min = float("inf")
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            dis = distance(a[i],a[j])
            if dis < min:
                min = dis
    return min
a = [(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
print("최근접거리:",closest_pair(a))
                
