
def user_union(a,b):
    result = set()
    for i in a:
        result.add(i)
    for i in b:
        result.add(i)
    return result

def user_intersection(a,b):
    result = set()
    for i in a:
        for j in b:
            if i == j:
                result.add(i)
    return result
def user_diff(a,b):
    result = set(a)
    for i in a:
        for j in b:
            if i == j:
                result.remove(i)
    return result
a = {1,2,3,4,5,6}
b = {0,3,4,5,6,7,8}

print(a.union(b))
print(user_union(a,b))
print(a.intersection(b))
print(user_intersection(a,b))
print(a-b)
print(user_diff(a,b))


