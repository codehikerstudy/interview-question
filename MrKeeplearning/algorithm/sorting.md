<p align="middle"><iframe src="https://giphy.com/embed/XVJcwIbSdFNs1Ni7N4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></p>

# 개요

프로그램을 작성할 때 빈번하게 사용되는 정렬은 어떤 데이터가 주어졌을 때 정해진 순서대로 나열하는 것을 말한다. 일반적으로 숫자라면 오름차순 또는 내림차순으로 정렬할 수 있고, 문자 또한 아스키코드에 해당되는 번호에 따라서 정렬이 가능하다.

정렬을 위한 알고리즘의 종류에는 다양한 알고리즘이 존재하고, 각 알고리즘은 서로 다른 성능을 가지고 있다.

이번 글에서는 대표적인 알고리즘에 대해서 알아보고, 최종적으로 어떤 알고리즘이 빠른지 확인해보고자 한다. 각 정렬 알고리즘 이미지 밑에 달아놓은 시각화자료 사이트로 이동해서 어떤 식으로 동작하는지 직접 확인한다면 훨씬 이해하기 편리하다.

# 1. Bubble sort

<br/>

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215260683-867658ab-abc3-45e1-960f-f05bfb751f33.gif" width=500>
<figcaption><b>이미지 출처: emre.me</b><figcaption>
</figure>

<p align = "center"><a href="https://visualgo.net/en/sorting" target="_blank">버블 정렬 시각화 자료(VISUALGO)</a></p>

버블 정렬은 매우 단순한 정렬로 정렬 자체가 어떻게 동작하는지 쉽게 이해하기에 좋은 정렬이다.

기본적으로 버블 정렬은 배열의 두 수를 앞에서부터 비교해가면서 정렬을 진행한다. 두 수 a와 b가 있을 때 오름차순으로 정렬할 때는 `a < b`를 만족하도록, 내림차순으로 정렬할 때는 `a > b`를 만족할 수 있도록 서로 위치를 바꾸면서 배열의 마지막 숫자까지 이동한다.

이렇게 배열의 시작부터 배열의 끝까지 loop를 돌면서 비교를 하기 때문에 많은 실행시간이 소요된다.

따라서 시간 복잡도는 $O(n^2)$ 으로 매우 느린 모습을 보여준다.

```python
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

```

# 2. Selection sort

<br/>

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215265129-4113bdbb-f3fe-4d96-9b5f-27628d0fa0f9.gif" width=500>
<figcaption><b>이미지 출처: emre.me</b><figcaption>
</figure>

<p align = "center"><a href="https://visualgo.net/en/sorting" target="_blank">선택 정렬 시각화 자료(VISUALGO)</a></p>

선택 정렬 또한 버블 정렬처럼 간단한 정렬 알고리즘이다.

입력으로 들어온 배열에서 최소값을 찾아 그 값을 배열의 가장 첫 번째 값과 위치를 바꾼다. 그 뒤 두 번째 값을 기준으로 나머지 배열의 공간에서 가장 작은 값을 찾은 후 마찬가지로 위치를 서로 바꾼다. 이렇게 정렬이 될 때까지 반복을 진행한다.

비교를 하는데 상수 시간만큼 소요된다고 가정할 때, 버블 정렬과 마찬가지로 배열 내의 n개의 요소를 정렬하는데 $O(n^2)$의 시간복잡도를 가진다.

버블 정렬과 달리 선택 정렬은 이미 정렬이 완료된 것을 다시 검사하지 않는다. 따라서 둘 다 시간복잡도가 $O(n^2)$ 일지라도 선택 정렬이 항상 더 나은 성능을 보여준다.

```python
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

```

# 3. Insertion sort

<br/>

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215271384-59cec219-d30a-4748-a359-600fdbf7425e.gif" width=500>
<figcaption><b>이미지 출처: emre.me</b><figcaption>
</figure>

<p align = "center"><a href="https://visualgo.net/en/sorting" target="_blank">삽입 정렬 시각화 자료(VISUALGO)</a></p>

삽입 정렬은 두 번째 인덱스부터 시작된다. 현재 인덱스 앞에 있는 데이터부터 비교해서 현재 인덱스의 값보다 앞에 있는 데이터가 더 크다면 바로 뒤로 이동시키면서 적절한 위치를 찾아 삽입하는 방식이다.

삽입정렬은 동일하게 $O(n^2)$의 시간복잡도를 가지지만 앞서 다룬 버블정렬과 선택정렬 대비 빠르고 단순하다. 또한 안정정렬이고 in-place 알고리즘(제자리 알고리즘)이라는 장점도 존재한다.

완전히 정렬되어 있는 상태라면 최선의 경우 $O(n)$의 시간복잡도를 가질 수 있다.

### 💡제자리 알고리즘(Wikipedia 정의)

* 자료구조를 추가로 사용하지 않고 입력을 변환하는 알고리즘을 말한다.
* 보통 추가적인 변수를 위해 약간의 추가 저장 공간은 허용된다. 일반적으로 알고리즘이 실행되면서 입력 값이 출력 값으로 덮어써지는데 입력 요소를 출력 요소로 교체하거나 요소의 위치를 바꾸는 방식으로 업데이트한다.

### 💡안정 정렬

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215306793-93434fcf-55b8-4ab4-a56b-91ce16b96a6a.png">
<figcaption><b>이미지 출처: 나무위키 - 정렬 알고리즘</b><figcaption>
</figure>

* 안정 정렬은 반복되는 요소를 입력 때와 동일한 순서로 정렬한다.
* 즉, 정렬의 기준이 여러 개가 존재할 때, 기존에 적용했던 정렬 형태를 유지한 상태에서 추가적인 정렬을 하는 것을 의미한다.

```python
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

```

# 4. Heap sort

<br/>

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215307605-b90404eb-5126-435e-b4c0-084a1c2d2467.gif" width=500>
<figcaption><b>이미지 출처: emre.me</b><figcaption>
</figure>

힙 정렬은 선택정렬의 개선된 버전으로 힙 자료구조를 활용한 정렬 방법이다. 내림차순 정렬을 위해서는 최소 힙을 구성하고 오름차순 정렬을 위해서는 최대 힙을 구성한다.

힙 정렬은 다음 순서에 따라서 진행된다.

1. 주어진 데이터를 완전 이진 트리로 구성한다.
2. 완전 이진 트리 내에서 최대 힙을 구성한다. 단말 노드를 자식 노드를 지닌 부모노드부터 구성하면서 말단부터 루트까지 올라가며 순차적으로 생성한다.
3. 루트에 위치한 가장 큰 수를 트리 내의 가장 작은 수와 교환한다.
4. 2번과 3번을 반복한다.

선택정렬에서 다음으로 가장 큰 요소를 탐색하는데 $O(n)$의 시간 복잡도가 걸리는 것과 달리 힙 자료구조는 $O(\log n)$의 시간 복잡도를 가진다(최대 힙으로 재구성).

따라서, 최대 힙으로 재구성된 트리에서 힙 정렬을 수행하는데 걸리는 시간은 힙 구성시간과 n개의 데이터 삭제 및 재구성 시간을 포함하기에 $O(n \log n)$의 시간복잡도를 가진다.

```python
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

```

# 5. Merge sort

<br/>

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215314385-76c2e543-2352-4d6d-b7f5-913a26b6f2e8.gif" width=500>
<figcaption><b>이미지 출처: emre.me</b><figcaption>
</figure>

<p align = "center"><a href="https://visualgo.net/en/sorting" target="_blank">병합 정렬 시각화 자료(VISUALGO)</a></p>

병합정렬은 분할 정복이 적용된 좋은 예시 중 하나이다. 재귀 용법을 활용한 2-way 병합정렬 과정은 다음과 같이 이루어진다.

1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
2. 각 부분 리스트를 재귀적으로 병합 정렬을 이용해 정렬한다.
3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 병합한다.

병합 정렬은 최악, 최선, 평균 모두 $O(n \log n)$의 시간 복잡도를 가진다.

```python
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

```

# 6. Quick sort

<p align = "center"><a href="https://visualgo.net/en/sorting" target="_blank">퀵 정렬 시각화 자료(VISUALGO)</a></p>

## 6.1. Quick sort 개요

퀵 정렬은 피벗을 기준으로 좌우를 나누는 특징을 가지고 있어 파티션 교환 정렬이라는 이름으로 불리기도 한다. 퀵 소트 역시 분할 정복 알고리즘이고 피벗을 기준으로 작으면 왼쪽으로, 크면 오른쪽으로 이동시키면서 분할한다.

n개의 데이터를 정렬하는데 최악의 경우 $O(n^2)$의 시간 복잡도를 가질 수도 있지만 평균적으로 $O(n \log n)$의 시간 복잡도를 가진다. 또한, 정렬해야할 데이터에 적합하게 잘 짜여진 퀵 정렬 알고리즘은 병합 정렬이나 힙 정렬에 비해서 2~3배 더 빠른 모습을 보이기도 한다.

퀵소트는 다음과 같은 순서에 따라서 진행된다.

1. 리스트 가운데의 원소를 하나 선택하고, 이것을 피벗이라고 한다.
2. 피벗을 기준으로 피벗 앞에는 피벗보다 작은 값이, 피벗 뒤에는 피벗보다 큰 값이 올 수 있도록 분할한다.
3. 재귀적 용법으로 위의 두 과정을 리스트의 크기가 0 또는 1이 될 때까지 반복한다.

퀵 정렬은 피벗에 따라서 정렬이 이루어지기 때문에 어떤 피벗을 선택하는지, 그리고 어떤 분할 알고리즘을 사용하는지(**Hoare partition v.s. Lomuto partition**)에 따라서 알고리즘의 효율성이 영향을 받는다.

### Quick sort의 단점

정렬 후, 입력값이 유지되는 안정 정렬이 입력값이 유지되지 않는 불안정 정렬보다 훨씬 유용할 것이다. 한편, merge sort와 bubble sort가 안정정렬인 것과 달리, 퀵정렬은 불안정 정렬이고 입력값에 따라 버블 정렬만큼 느려질 수도 있다. 

Quick sort의 **호어 분할 방식**은 피봇을 맨 왼쪽값으로 했을 때, 최소값이 피봇으로 선택되면 분할이 발생하지 않아 다른 정렬 알고리즘과 다를 바 없어져 시간복잡도로 $O(n^2)$을 가질 수도 있다. 그리고 **로무토 분할 방식**은 배열의 모든 인자가 같은 수이거나 이미 정렬된 배열이 입력값으로 주어진 경우 swap이 계속 발생하기 때문에 $O(n^2)$의 시간복잡도를 가질 수도 있다.

이처럼 Quick sort의 고르지 못한 성능으로 인해 실무에서는 팀소트(Timsort) 또는 병합 정렬이 활발히 쓰인다고 한다.

## 6.2. Hoare partition scheme

퀵 정렬을 고안한 호어의 방식을 따르면 가장 먼저 주어진 리스트의 첫 데이터를 피벗으로 설정한다.

두 개의 인덱스를 두어 하나는 왼쪽에서부터 오른쪽으로 이동하며 피벗보다 큰 데이터를 찾고, 나머지 인덱스는 오른쪽에서 왼쪽으로 이동하며 피벗보다 피벗보다 작은 데이터를 찾는다. 그리고 이 둘을 교환하는 과정을 거친다.

이러한 일련의 과정을 반복하면 피벗을 기준으로 정렬이 된다.

`[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]`과 같이 구성된 리스트가 있을 때 이것을 호어의 방식에 따라 퀵소트를 하면 다음과 같다.

### Step1.

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215331853-709eef7a-810b-45a7-96db-024c3aa1a435.png" >
</figure>

* 항상 리스트의 첫 번째 데이터를 피벗으로 설정한다.
* 피벗인 5보다 큰 데이터를 왼쪽에서부터 선택하기 때문에 7이 선택되고 오른쪽에서는 피벗보다 작은 데이터인 4가 선택된다.
* 이렇게 선택된 데이터의 위치를 서로 바꾼다.

### Step2.

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215332250-04c80efe-c7a0-4051-81a5-e8b384536aa0.png" >
</figure>

* 다시 왼쪽에서부터는 피벗보다 큰 수를, 오른쪽에서부터는 피벗보다 작은 수를 찾는다.
* 조건에 부합하는 숫자를 찾았다면 서로 위치를 바꾼다.

### Step3.

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215332394-1e9e29de-36ce-4f18-bece-276313ed89be.png" >
</figure>

* 이렇게 계속해서 두 개의 인덱스를 이동시키면서 위치를 서로 바꾸는 작업을 하다보면, 어느 시점에서 두 개의 인덱스가 엇갈리는 시점이 생긴다.
* 두 개의 인덱스가 만나게 되면, 둘 중 가장 작은 값을 피벗과 위치를 서로 바꾼다.

### Step4.

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/215335454-c930b562-1d3e-4860-bf76-3c46a1684be8.png" >
</figure>

* 분할이 완료되었다면 위와 같이 왼쪽 리스트와 오른쪽 리스트로 분할할 수 있게 된다.
* 피벗을 기준으로 위치를 바꾼 것이기 때문에 왼쪽 리스트는 피벗보다 항상 작고, 오른쪽 리스트는 피벗보다 항상 큰 수만 있다.
* 이 상태에서 왼쪽 리스트와 오른쪽 리스트를 각각 앞에서 피벗을 정하고 위치를 바꾼 것과 같이 반복 수행을 하면 정렬이 완료된다.
* 퀵 정렬이 완전히 종료되는 조건은 현재 리스트의 데이터 수가 1개인 경우이다.

```python
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

```

## 6.3. Lomuto partition scheme

호어 분할 방식이 주어진 데이터의 첫 데이터(가장 왼쪽)를 피벗으로 설정한 것과 달리, 로무토 분할 방식은 가장 끝의 데이터(가장 오른쪽)를 피벗으로 설정한다.

<figure align = "center">
<img src = "https://user-images.githubusercontent.com/27791880/218331452-7b28b6b4-c2fe-4b6c-aef0-72ab4f8bbd34.png" width=500>
<figcaption><b>이미지 출처: 나무위키 - 정렬 알고리즘</b><figcaption>
</figure>

위의 이미지에서도 확인할 수 있듯이 로무토 분할 방식에서는 피벗 외에 2개의 포인터(`left`, `right`)가 추가로 존재한다. `right`포인터는 계속 피벗쪽으로 이동하고, 만약 `right`포인터가 피벗보다 작거나 같다면 `left`와 `right`을 스왑한다. 그리고 스왑 이후에는 `left`포인터가 한 칸 이동한다.

`right`포인터가 피봇 직전까지 오게 되면 `left`와 피봇을 서로 스왑한다.

사실 말로 설명하는 것보다 영상으로 보는 것이 더 확실하니 아래의 영상을 참고해보자.

<p align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/86WSheyr8cM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

```python
def quick_sort_lomuto(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(items, low, high):
    if low < high:
        split_point = partition(items, low, high)
        quick_sort_helper(items, low, split_point - 1)
        quick_sort_helper(items, split_point + 1, high)

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

```

# 7. 파이썬 내장함수, 그리고 Timsort

앞에서 수 많은 정렬 알고리즘을 다루었지만, 파이썬을 사용한다면 `sorted()`나 `sort()`와 같이 파이썬에서 기본적으로 제공하는 정렬함수를 사용하는 것이 더 빠를 수 있다. 그리고 파이썬의 `sorted()`는 정렬을 위해 **팀소트(Timsort)**를 사용한다.

실제 데이터의 대부분은 이미 정렬되어 있다는 가정을 바탕으로, 실제 데이터에서 고성능을 낼 수 있도록 설계한 팀소트 알고리즘은 삽입 정렬과 병합 정렬을 휴리스틱(heuristic)하게 적절히 조합해서 사용한다. 현실의 데이터에서 높은 성능을 낼 수 있다는 뛰어난 장점으로 인해서 팀소트 알고리즘은 자바, 스위프트 그리고 안드로이드, 크롬 등의 플랫폼까지 다양한 영향을 미쳤다.

```python
# 파이썬 sort()
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr.sort()

print(arr)
# Output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr.sort(reverse=True)

print(arr)
# Output is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

<br/>

```python
# 파이썬 sorted()
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorted_arr = sorted(arr)

print(sorted_arr)
# Output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse_sorted_arr = sorted(arr, reverse=True)
print(reverse_sorted_arr)
# Output is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

# 8. 무엇이 가장 빠른가?

앞에서 살펴 본 알고리즘들의 시간복잡도와 공간복잡도를 정리하면 아래와 같다.

| **알고리즘**           | **시간복잡도(최선)** | **시간복잡도(평균)** | **시간복잡도(최악)** | **공간복잡도**     |
|:------------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| **Bubble sort**    | $O(n)$        | $O(n^2)$      | $O(n^2)$      | $O(1)$        |
| **Selection sort** | $O(n^2)$      | $O(n^2)$      | $O(n^2)$      | $O(1)$        |
| **Insertion sort** | $O(n)$        | $O(n^2)$      | $O(n^2)$      | $O(1)$        |
| **Heap sort**      | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$        |
| **Merge sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$        |
| **Quick sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$      | $O(n \log n)$ |
| **Tim sort**       | $O(n)$        | $O(n \log n)$ | $O(n \log n)$ | $O(n)$        |

어떤 알고리즘이 "항상 빠르다"라고 말하기는 어렵다. 입력값으로 들어온 값이 얼마나 큰지, 입력값에 얼마만큼의 고유한 값이 존재하는지, 메모리 측면에서 어느 정도의 오버헤드까지 용인할 수 있는지, 그리고 최악의 시간복잡도로 $O(n^2)$을 가지더라도 용인할 수 있는지 등 다양한 상황을 고려하여 적절한 알고리즘을 사용해야 한다. 그럼에도 몇 가지 알고리즘들은 고려해 볼 만하다.

**Quick sort**는 입력값에 맞추어 피봇만 잘 설정한다면 최악의 시간복잡도로 $O(n^2)$을 가지게 되는 경우를 쉽게 피할 수 있고, 또 실제로 빠른 정렬 알고리즘이기 때문에 가장 처음으로 떠올리기에 좋은 정렬 알고리즘이다. 그리고 **Heap sort**는 절대로 $O(n^2)$의 시간복잡도가 발생하면 안되고, 최소한의 공간복잡도를 가져야 하는 상황에서 적절한 선택이 될 수 있다. 마지막으로 안정적인 성능이 보장되어야 하는 상황일 때는 실제로 실무에서도 많이 활용한다는 **Merge sort**를 고려해 볼 수 있다.

<br/>

## 더 많은 정렬 알고리즘을 확인하고 싶다면?

* [Wikipedia - Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

## Reference.

* [Sorting Algorithms with Animations](https://emre.me/algorithms/sorting-algorithms)
* [나무위키 - 정렬 알고리즘 안정 정렬 이미지](https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98#s-3)
* [퀵 정렬 - 호어/로무토 분할 알고리즘](https://ldgeao99.tistory.com/376)
* [stackoverflow - Quicksort: Choosing the pivot](https://stackoverflow.com/questions/164163/quicksort-choosing-the-pivot)
* [파이썬 알고리즘 인터뷰, 책만 출판사](https://www.onlybook.co.kr/entry/algorithm-interview)