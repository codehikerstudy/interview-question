# 오름차순으로 정렬
def bubble_sort(array):

    # 최소한 한 번은 loop를 돌 수 있도록 만들어 검사를 진행한다.
    swap = True

    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # 오름차순 정렬을 위한 조건을 만족한 경우
                # 다시 loop를 돌아야 하기 때문에 True로 변경해준다.
                swap = True

    return array
