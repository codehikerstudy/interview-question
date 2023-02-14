# Quick sort - Hoare partition scheme
# 피벗은 가장 첫 번째 값으로 설정한다.

def quick_sort(array, start, end):
    
    # 원소가 1개인 경우 이미 정렬된 상태이다.
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # 피벗보다 큰 데이터가 나오기 전까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 피벗보다 작은 데이터가 나오기 전까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # 엇갈리는 상황이라면 작은 데이터와 피벗을 교환한다.
        # 그렇지 않다면, 작은 데이터와 큰 데이터를 교환한다.
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 리스트와 오른쪽 리스트에서 각각 정렬을 수행한다.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
