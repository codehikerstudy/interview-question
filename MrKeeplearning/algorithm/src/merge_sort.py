import random

def merge_sort(array):
    # array의 개수가 한 개라면 해당값을 return
    if len(array) <= 1:
        return array

    # 그렇지 않다면 반으로 분할
    medium = int(len(array) / 2)

    # 각 부분 리스트를 재귀적 용법으로 병합 정렬
    left = merge_sort(array[:medium])
    right = merge_sort(array[medium:])

    # 새로운 공간에 정렬된 리스트를 병합한다.
    return merge(left, right)

def merge(left, right):
    result = []
    left_point, right_point = 0, 0

    for i in range(len(left) + len(right)):
        if left_point < len(left) and right_point < len(right):

            # 만약 왼쪽 부분 리스트의 값이 더 작다면, 정렬된 리스트에 담아준다.
            if left[left_point] <= right[right_point]:
                result.append(left[left_point])
                left_point += 1

            # 오른쪽 부분 리스트의 값이 더 작다면, 정렬된 리스트에 담아준다.
            else:
                result.append(right[right_point])
                right_point += 1
        
        # 만약 왼쪽 부분 리스트의 끝까지 정렬을 마쳤다면, 오른쪽 부분 리스트의 요소를 추가한다.
        elif left_point == len(left):
            result.append(right[right_point])
            right_point += 1
        
        # 만약 오른쪽 부분 리스트의 끝까지 정렬을 마쳤다면, 왼쪽 부분 리스트의 요소를 추가한다.
        elif right_point == len(right):
            result.append(left[left_point])
            left_point += 1
    
    return result

data_list = random.sample(range(100), 10)
print(merge_sort(data_list))
