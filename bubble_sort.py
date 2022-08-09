def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
                
some_list = [10, 2, 7, 19, 22, 101, 31, 57, 84, 6, 11]
bubble_sort(some_list)
print(some_list)
