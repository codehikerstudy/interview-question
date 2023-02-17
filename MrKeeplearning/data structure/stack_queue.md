<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214284129-c552621d-93ee-4860-9334-dc3e3eb1ce3c.jpeg" width=400>
<figcaption><b>이미지 출처: twitter - Greg Kyte, CPA</b></figcaption>
</figure>

# 1. 개요

스택과 큐는 데이터 **접근 방식을 설명**하는 대표적인 자료구조이다. 즉, 자료구조가 코드로 정의된 것이 아니라 행동 양식이 정의되어 어떤 자료구조가 스택 또는 큐로 구분되기 위한 **규칙**에 해당한다. 이러한 것들을 다른 말로 **추상적 자료구조**(ADT, Abstract, Data Type)라고 부른다.

데이터를 입력하고 출력하는 그 순서에 따라서 스택과 큐가 구분되고, 이러한 특징을 적재적소에 활용하여 많은 실제 시스템 또는 서비스 등에 적용하고 있다.

이번 글에서는 스택과 큐에 대한 개념과 실제 구현까지 다루어보려고 한다.

# 2. 스택(Stack)

<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214289299-031b3bf5-b368-472b-a4c4-833991c56956.svg" width=400>
<figcaption><b>이미지 출처: Wikipedia - Stack</b></figcaption>
</figure>

스택을 설명하는 한 단어를 선택하라고 한다면 바로 **LIFO(Last In First Out)** 라고 할 수 있다.

스택은 같은 구조와 크기의 자료를 top이라고 정한 곳에서만 접근할 수 있는데, 스택에 자료가 삽입되면 이 자료는 스택의 마지막 자료이며 top은 이 마지막 자료를 가리킨다. 마찬가지로, 스택에서 자료를 삭제할 때는 top에서만 가능하기 때문에 top이 가리키는 스택의 마지막 자료만 삭제할 수 있다.

<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214294904-b6f584c2-31b2-4673-be5d-f6614e5b6e5d.svg" width=400>
<figcaption><b>이미지 출처: Wikipedia - Stack</b></figcaption>
</figure>

결과적으로 스택은 접근하는 순서에 따라서 데이터가 스택에 쌓이게 되고, 가장 마지막에 삽입된 데이터가 가장 먼저 삭제되는 후입선출(LIFO)의 구조를 갖는다.

스택에서 top으로 데이터를 삽입하는 연산을 **push**, top에서 데이터를 삭제하는 연산을 **pop**이라고 한다.
그리고 push와 pop의 시간복잡도는 모두 $O(1)$의 시간복잡도를 가진다.

개발자들이 가장 많이 사용하는 사이트의 이름으로도 존재하듯이 완전히 가득 찬 스택에 데이터를 추가로 삽입하려고 할 때는 **스택 오버플로우(stack overflow)** 가 발생한다.

## 2.1. 스택의 적용

스택의 개념은 실생활 속에서도 적용된다. 함수를 호출할 때 인수의 전달에도 스택이 활용되고 후위 표기법이라고 알고 있는 역폴란드 표기법에도 스택이 활용되며 DFS에도 스택이 적용된다. 또한 현재 이 글을 보고 있는 웹브라우저에서 뒤로가기 기능을 수행하는 것 자체도 웹 히스토리를 담은 스택의 최상단 링크를 리턴하는 방식이라고 볼 수 있다.

### 역폴란드 표기법(RPN, reverse Polish notation)

후위 표기법이라고도 불리는 역폴란드 표기법은 연산자를 연산 대상의 뒤에 쓰는 연산 표기법이다. 예를 들어 `1 + 2`가 일반적인 중위 표기법이라면, RPN으로 작성했을 때 `1 2 + `가 된다.

RPN으로 수식을 작성한다면 앞에서부터 읽어나가면서 스택에 저장하면 되기 때문에 컴퓨터 친화적인 표기법이다. 예를 들어 `(3 + 5) * 4`를 RPN으로 표기한다면 `3 5 + 4 *`이 되는데 이것의 연산 과정은 다음과 같다.

1. 숫자 `3`이 스택에 담긴다.
2. 숫자 `5`가 스택에 담긴다.
3. `+`가 입력되면 스택에서 두 수를 꺼내고 더한 뒤 그 결과(`8`)를 스택에 담는다.
4. 숫자 `4`가 스택에 담긴다.
5. `8`과 `4`를 스택에서 꺼내어 곱한 뒤 그 결과(`32`)를 스택에 담는다.

# 3. 스택 구현

> 스택 구현에 활용한 코드는 "[Do it! 자료구조와 함께 배우는 알고리즘 입문 : 파이썬 편](https://github.com/easysIT/doit_dsalgo_with_python)"의 코드를 활용했습니다.


스택은 앞에서도 다루었듯이 ADT이다. 따라서 스택의 행동 양식이 중요한데, 파이썬에서는 이미 `pop()`이라는 메서드를 제공하고 있다. 또한 push와 동일한 기능으로 `append()`를 사용할 수 있다.

```python
stack = []
stack.append(1)
stack.append(2)

stack           # Output: [1, 2]

stack.pop()     # Output: 2
```

파이썬 내부에 정의된 메서드를 활용해서 쉽게 스택을 구현할 수도 있지만, 이번 글에서는 스택의 작동 방식을 이해하기 위함이기 때문에 하나씩 구현해보려 한다. 현재 구현하는 스택은 가변 길이 배열을 활용한 것이 아닌 고정된 길이의 배열이다.

```python
class Stack:
    class Empty(Exception):
        """
        빈 상태의 Stack에 pop 또는 peek를 수행하려 할 때 보내는 예외 처리
        """
        pass

    class Full(Exception):
        """
        가득 찬 상태의 Stack에 push를 수행하려 할 때 보내는 예외 처리
        """
        pass

    def __init__(self, capacity):
        self.stack = [None] * self.capacity # 스택 본체. 최대 용량에 맞춰 초기화한다.
        self.capacity = capacity            # 스택의 최대 용량
        self.pointer = 0                    # 스택 포인터
       
    def is_empty(self):
        """
        스택이 비어있는지 확인한다.
        만약 포인터가 0이라면 해당 스택은 빈 스택이다.
        """
        return self.pointer <= 0

    def is_full(self):
        """
        스택이 가득 찬 상태인지 확인한다.
        만약 포인터가 스택 용량과 동일하다면 해당 스택은 가득 찬 상태이다.
        """
        return self.pointer >= self.capacity
```

위에서 **스택 포인터**는 스택의 모든 작업의 기반이 되는 변수인데, 해당 변수는 현재 스택에 저장된 데이터의 수를 담고 있다.

```python
def push(self, value):
    if self.is_full():
        raise Stack.Full
    self.stack[self.pointer] = value    # pointer가 스택의 사이즈를 담고 있기 때문에 다음 위치에 value를 넣게 된다.
    self.pointer += 1
    
def pop(self):
    if self.is_empty():
        raise Stack.Empty
    self.pointer -= 1
    return self.stack[self.pointer]
    
def peek(self):
    """
    스택의 최상단 데이터를 반환한다.
    해당 데이터를 삭제하진 않는다.
    """
    if self.is_empty():
        raise Stack.Empty
    return self.stack[self.pointer - 1]
    
def clear(self):
    """
    스택의 모든 데이터를 삭제한다.
    """
    self.pointer = 0

```

`clear` 메소드는 스택의 모든 데이터를 삭제하는 기능을 한다. 스택이 스택 포인터를 중심으로 동작하기 때문에 데이터를 배열 내에서 삭제할 필요 없이 단순히 스택 포인터를 0으로 초기화하는 것으로 삭제 역할을 할 수 있다.

```python
def find(self, value):
    """
    특정 value를 검색한다.
    검색에 성공하면 해당 인덱스를 반환하고,
    검색에 실패하면 -1을 반환한다.
    """
    for i in range(self.pointer -1, -1, -1):
        if self.stack[i] == value:
            return i    # 검색 성공
    return -1           # 검색 실패
    
def count(self, value):
    """
    스택에 포함된 특정 value의 개수를 반환한다.
    """
    count = 0
    for i in range(self.pointer):
        if self.stack[i] == value:
            count += 1
    return count
    
def dump(self):
    """
    스택 안의 모든 데이터를 bottom부터 top까지 출력한다.
    """
    if self.is_empty():
        print("Stack is empty")
    else:
        print(self.stack[:self.pointer])
```

위에서 `find` 메소드는 특정 value를 검색하고 해당 value의 인덱스를 반환하는 메소드이다. 현재 위치에서부터(스택 포인터는 전체 사이즈를 의미하기 때문에 -1을 해야 현재 위치를 가리키게 된다) Bottom까지 루프를 돌면서 원하는 value를 검색한다.

`count` 메소드는 스택의 전체 사이즈만큼 for문을 돌면서 탐색하려는 value와 동일한 값이 있을 때 count의 값을 갱신하여 특정 value의 개수를 반환하는 역할을 한다.

# 4. 큐(Queue)

<figure align = "center"><img src="https://user-images.githubusercontent.com/27791880/219057638-88a448ea-1551-41a9-8cdb-85ef904d4ec7.svg" width=400><figcaption><b>이미지 출처: Wikipedia - Queue</b></figcaption></figure>

앞서 스택을 설명하는 한 단어를 선택한다고 하면 LIFO라고 답했던 것과 반대로, 큐를 대표할 수 있는 한 단어는 FIFO(First In First Out)라고 할 수 있다. 따라서, 먼저 넣은 데이터가 먼저 출력되는 선입선출의 형식을 따른다.

큐의 동작은 크게 `enqueue`와 `dequeue` 2가지로 구분할 수 있다. Enqueue의 경우 큐의 가장 뒤(`Rear`)에 데이터를 추가하는 작업을 뜻하고, $O(1)$의 시간복잡도를 가진다. 그리고 Dequeue는 큐의 가장 앞(`Front`)에 있는 데이터를 삭제하는 작업으로 시간복잡도는 동일하게 $O(1)$이다.

# 5. 큐 구현

스택과 마찬가지로 큐도 파이썬에서 기본적으로 제공해주는 `pop()`과 `append()`를 활용해서 쉽게 구현할 수 있다.

```python
queue = []

queue.append(1)
queue.append(2)

queue           # Output: [1, 2]
queue.pop(0)    # Output: 1
```

큐의 구현 방식은 **Array-Based queue**와 **List-Based queue** 2가지로 구분할 수 있다.

## 5.1. Array-Based queue

1차원 배열을 사용한 순차 자료구조 방식의 큐는 포화상태가 아닐 때만 삽입 연산을 수행할 수 있도록 정의되어 있다. 따라서, 포화상태인지 검사하기 위해 큐의 rear가 배열의 마지막 인덱스인지 확인하는 작업이 필요하다.

하지만 아래 그림과 같은 상태라면 문제가 발생한다.

<figure align = "center"><img src="https://user-images.githubusercontent.com/27791880/219652917-4b84f045-ac14-4657-a0ae-2baed5eefbcf.png" width=400></figure>

Dequeue를 진행한 상태이고, front의 데이터가 빠진 상태이므로 인덱스 0번, 1번, 2번에 자리가 있다. 그럼에도 rear가 배열의 마지막 위치에 있기 때문에 포화상태로 인식하고 삽입 연산을 수행하지 않는다.

이러한 경우 큐의 빈자리를 활용하기 위해서 모든 원소를 앞으로 이동시켜야 하는데 이 작업을 위해서는 $O(n)$의 시간복잡도가 소요된다. 따라서 enqueue와 dequeue의 시간복잡도가 $O(1)$인 큐의 효율성을 떨어뜨린다.

### 원형 큐

<figure align = "center"><img src="https://user-images.githubusercontent.com/27791880/219665990-b107d9bc-efbf-42e8-8903-a1a8debff1b5.png" width=400></figure>

이러한 문제를 해결하기 위해서 **원형 큐(Circular Queue)**를 사용하며, Array-Based queue는 원형 큐로 구현하는 것이 일반적이다. 원형 큐 또한 1차원 배열을 사용하지만 논리적으로 배열의 처음과 끝이 연결되어 있는 상태로 생각한다.

초기 공백 상태에서 둘 front와 rear는 둘 다 인덱스 0를 가리키며 `front == rear`인 상태를 유지한다. Enqueue 시 rear는 한 칸 씩 이동하면서 데이터를 삽입하고, Dequeue를 수행할 때 front는 rear가 이동한 방향으로 이동하면서 데이터를 삭제한다.

배열의 처음과 끝이 논리적으로 연결되어 있는 상태라고 가정하기 때문에 배열의 사이즈가 n일 때 인덱스 `n-1`에 도달한 뒤 새로운 데이터를 넣기 위해서는 인덱스 0로 돌아가야 한다.

이러한 방식으로 동작하기 위해서 `modulo` 연산자를 사용해 새로운 데이터가 삽입되어야 하는 인덱스를 알려준다.

예를 들어 전체 배열의 크기가 4이고 현재 인덱스가 배열의 끝인 3일 때 다음으로 삽입되어야 하는 위치는 인덱스 0이다. 현재 인덱스를 배열의 크기로 모듈로 연산을 진행하면 `3 % 4 == 0` 원형 큐의 동작 방식을 구현할 수 있다.

# References

* [Greg Kyte, CPA - twitter](https://twitter.com/gregkyte/status/1012088894886572032)
* [Wikipedia - 스택](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* [Wikipedia - 큐](https://ko.wikipedia.org/wiki/%ED%81%90_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
* [Wikipedia - 역폴란드 표기법](https://ko.wikipedia.org/wiki/%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C_%ED%91%9C%EA%B8%B0%EB%B2%95)
* [노마드 코더 - 개발자라면 무조건 알아야 하는 자료구조! 5분컷.](https://youtu.be/Nk_dGScimz8)
* [Do it! 자료구조와 함께 배우는 알고리즘 입문 : 파이썬 편](https://github.com/easysIT/doit_dsalgo_with_python)
* [Introductuion and Array Implementation of Circular Queue](https://www.geeksforgeeks.org/introduction-and-array-implementation-of-circular-queue/)
