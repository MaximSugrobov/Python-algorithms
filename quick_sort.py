def quick_sort(lst):
    if len(lst) < 2
        return lst
    else:
        pivot = lst[0]
        less_then_pivot = [i for i in lst[1:] if i <= pivot]
        greater_then_pivot = [i for i in lst[1:] if i > pivot]
        return quick_sort(less_then_pivot) + [pivot] + quick_sort(greater_then_pivot)
      
quick_sort([31, 2, 14, 5, 6, 81, 101, 45, 72, 3, 4, 1, 10, 1])
