# 힙 정렬 어렵다
# 정리하자면, 이진 트리, 힙피파이 하게 만들고, 최댓값이 나오면 그걸 정렬하는 것!
# 최댓값을 히피파이하게 찾는 것이다.

a = [14, 5, 10, 8, 9, 13, 15, 4, 13, 10]

def heapify(list, node, size):
    maxi = node
    left_index = 2*node + 1
    right_index = 2*node + 2
    if left_index < size and list[left_index] > list[maxi]:
        maxi = left_index
    if right_index < size and list[right_index] > list[maxi]:
        maxi = right_index
    if maxi != node:
        list[maxi], list[node] = list[node], list[maxi]
        heapify(list, maxi, size)

def heap_sort(dommy):
    n = len(dommy)
    # 모두 히피파이 완료
    for i in range(n//2-1, -1, -1):
        heapify(dommy, i, n)
    
    for j in range(n-1, 0, -1):
        dommy[j], dommy[0] = dommy[0], dommy[j]
        heapify(dommy, 0, j)
    return dommy

b = heap_sort(a)
print(b)