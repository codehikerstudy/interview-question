import random

# 오름차순으로 정렬
def insertion_sort(array):
    # 가장 처음 만나는 요소는 정렬이 되어 있다고 가정한다.
    for i in range(1, len(array)):
        elem = array[i]

        # 직전 요소의 인덱스
        j = i - 1

        # 현재 정렬하는 요소의 적절한 위치를 찾을 때까지
        # 정렬되지 않은 요소들을 현재 요소의 오른쪽으로 이동한다.
        while j >= 0 and array[j] > elem:
            array[j + 1] = array[j]
            j -= 1
        
        # 적절한 위치를 찾았다면 해당 위치에 정렬하려는 요소를 넣는다.
        array[j + 1] = elem
    
    return array

data_list = random.sample(range(100), 50)
print(data_list)

print(insertion_sort(data_list))