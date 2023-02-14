# Quick sort - Hoare partition scheme
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 정렬된 것으로 간주함
    # quick sort 종료 조건이자, 예외처리
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    left_list = [x for x in tail if x <= pivot]
    right_list = [x for x in tail if x > pivot]

    # 분할을 완료한 뒤 왼쪽과 오른쪽 리스트에서 각각 정렬 후 전체 리스트를 반환
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

array = [2,0,2,1,1,0]
#array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))
