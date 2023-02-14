# 왼쪽 자식 노드
def get_lchild(i):
    return 2 * i + 1

# 오른쪽 자식 노드
def get_rchild(i):
    return 2 * i + 2

def max_heap(arr, n, i):
    left = get_lchild(i)
    right = get_rchild(i)
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 최대 힙 생성
    for i in range(n, -1, -1):
        max_heap(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, i, 0)
    
    return arr
