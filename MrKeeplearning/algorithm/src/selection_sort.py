# 오름차순으로 정렬
def selection_sort(array):
    for i in range(len(array) - 1):
        # array의 첫 데이터가 가장 작은 값이라고 가정하고 시작한다.
        min = i
        for index in range(i + 1, len(array)):
            if array[min] > array[index]:
                min = index
        array[min], array[i] = array[i], array[min]
    return array
