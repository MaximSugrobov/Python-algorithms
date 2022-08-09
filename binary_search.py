def binary_search(lst, item):
    low = 0
    high = len(lst)
    while low < high:
        mid = (low+high)//2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            low = mid+1
        else:
            high = mid-1
    return print(None)
    
    
binary_search([1, 3, 5, 7, 9, 11, 21, 33, 58], 3)
