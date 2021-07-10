# 쪼개고 합치기

# 합치는 함수가 더 중요하다.
a = [14, 5, 10, 8, 9, 13, 15, 4, 13, 10]

def merge_sort(dommy):
    n = len(dommy)
    if n <= 1: return dommy
    mid = n//2
    left = merge_sort(dommy[:mid])
    right = merge_sort(dommy[mid:])

    merge = []
    while left and right:
        if left[0] < right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    while left:
        merge.append(left.pop(0))
    while right:
        merge.append(right.pop(0))
    
    return merge

b = merge_sort(a)
print(b)
