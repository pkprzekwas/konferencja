def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[int(len(lst)/2)]
    left = [x for x in lst if x < pivot]
    mid = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
