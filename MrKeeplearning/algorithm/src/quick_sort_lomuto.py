def partition(array, low, high):
    pivot = array[high]

    left = low
    right = low
    while right < high:
        if array[right] <= pivot:
            array[left], array[right] = array[right], array[left]
            left += 1
        
        right += 1
    
    # right 포인터가 피봇 직전까지 오게 되면 left와 피봇을 서로 스왑한다.
    array[left], array[high] = array[high], array[left]

    return left

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(items, low, high):
    if low < high:
        split_point = partition(items, low, high)
        quick_sort_helper(items, low, split_point - 1)
        quick_sort_helper(items, split_point + 1, high)
