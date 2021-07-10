a = [14, 5, 10, 8, 9, 13, 15, 4, 13, 10]

def quick_sort(list):
    if len(list) <= 1: return list
    pivot = list[len(list)//2]
    left = []
    right = []
    equal = []
    for num in list:
        if num > pivot:
            right.append(num)
        elif num < pivot:
            left.append(num)
        else:
            equal.append(num)
        
    return quick_sort(left) + equal + quick_sort(right)

b = quick_sort(a)
print(b)