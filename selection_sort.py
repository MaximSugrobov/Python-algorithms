def search_for_min(lst):
    min_value = lst[0]
    index_of_min = 0
    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            index_of_min = i
    return index_of_min

def selection_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        index_of_min = search_for_min(lst)
        new_lst.append(lst.pop(index_of_min))
    return new_lst
  
selection_sort([5, 1, 2, 3, 10, 98, 1, 24])
