<p align="center"><img src="https://user-images.githubusercontent.com/27791880/219936950-9f95d65b-94b9-4fec-a2e4-37142383b732.svg" width=400></p>

# 1. 개요

> **트리(Tree)**는 추상 자료형으로 루트 값과 부모-자식 관계의 서브트리로 구성되어 있는 자기 참조(Self-Referential) 자료구조이다. 그리고 이진트리와 이진 탐색 트리는 트리 중에서도 가장 널리 사용되는 트리 자료구조이지, 트리 자체를 대변하는 것은 아니다.

이진 탐색 트리는 **정렬된** 트리로 다음의 조건을 만족해야 한다.

* 노드의 왼쪽 서브 트리에는 현재 노드의 값보다 작은 값을 가진 노드가 온다.
* 노드의 오른쪽 서브 트리에는 현재 노드의 값보다 큰 값을 가진 노드가 온다.
* 왼쪽과 오른쪽 서브 트리 모두 이진 탐색 트리여야 한다.

# 2. 이진 탐색 트리의 특징

이진 탐색 트리는 시간복잡도 측면에서 강점을 가지고 있다.

| **연산**         | **시간복잡도(평균)** | **시간복잡도(최악)** |
|:--------------:|:-------------:|:-------------:|
| **삽입**         | $O(\log n)$   | $O(n)$        |
| **탐색(lookup)** | $O(\log n)$   | $O(n)$        |
| **삭제**         | $O(\log n)$   | $O(n)$        |

어떤 자료구조에서든지 수행하는 대표적인 삽입, 삭제, 탐색에 대한 시간복잡도는 평균적으로 $O(\log n)$을 가진다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/219946851-544e39aa-4309-4a48-89ef-f2d6b2374643.gif" width=400></p>

위의 사진에서도 확인할 수 있듯이, 정렬된 배열에서 숫자 27을 찾기까지 총 10번의 탐색을 거쳐야 하지만 이진 탐색 트리는 단 3번만에 탐색이 완료되는 것을 확인할 수 있다. 하지만, 이렇게 빠른 동작 시간을 보여주는 것은 균형잡힌 트리일 경우에만 해당된다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/219949806-3e8c2832-df99-4951-aa28-207c6738d347.png" width=400></p>

만약 극단적으로 균형이 깨진 트리인 경우 Linked list와 다를 바 없는 형태를 가지게 되며 이 때 시간복잡도는 최악의 경우인 $O(n)$이 된다.

이처럼 균형이 깨질 경우 시간복잡도에 큰 영향을 받는 이진 탐색 트리의 장점을 유지하기 위해 사용하는 것이 **자가 균형 이진 탐색 트리(Self-Balancing Binary Search)** 이다. 자가 균형 이진 탐색 트리에서는 위의 균형이 깨진 이진 탐색 트리와는 달리 삽입과 삭제 과정에서 자동으로 높이를 낮게 유지하는 노드 기반의 이진 탐색 트리이다.

자가 균형 이진 탐색 트리를 적용한 대표적인 사례로는 **AVL트리**와 **Red-black tree**가 존재하며 Java의 해시맵에서는 개별체이닝에 linked list와 red-black tree를 병행해서 저장한다.

# 3. 이진 탐색 트리 구현

이진 탐색 트리를 링크드리스트의 개념을 활용하여 실제로 구현해본다.

## 3.1. 삽입과 검색

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class bst:
    """
    bst에 처음 들어오는 노드는 root 노드가 됨
    """
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head   # 트리를 순회하는 노드
        while True:
            # value는 BST에 삽입하려는 값.
            # value가 현재 위치의 노드보다 작다면 왼쪽으로 가야 한다.
            if value < self.current_node.value:
                # 만약 왼쪽 브랜치에 이미 값이 있다면
                if self.current_node.left != None:
                    # 비교할 대상을 왼쪽 브랜치에 있는 값으로 바꿔준다.
                    self.current_node = self.current_node.left
                else:
                    # 만약 왼쪽 브랜치 자체가 없다면
                    # 새로운 노드를 생성해서 연결시켜준다.
                    self.current_node.left = Node(value)
                    break
            # value가 현재 위치의 노드보다 크거나 같다면 오른쪽으로 간다.
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        # 루트 노드부터 시작해서 내가 찾는 값이
        # 어디에 있는지 판단하기 위해 사용되는 노드
        self.current_node = self.head
        # self.current_node가 None이 될 때
        # (트리의 모든 노드를순회 완료)
        # while구문은 종료된다.
        while self.current_node:
            if self.current_node.value == value:
                return True
            # 찾는 값이 아닐 때
            # value가 현재 위치의 노드보다 작다면 왼쪽으로 이동.
            # 만약 왼쪽 브랜치 자체가 없다면 None이기 때문에
            # while구문을 종료한다.
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

```

```python
head = Node(1)
BST = bst(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))    # Output: True
print(BST.search(-1))   # Output: False
```

## 3.2. 삭제

삭제 기능을 구현하기 위해서는 고민해야 할 부분이 많다. 여러 가지 경우의 수가 존재하기 때문에 해당 경우의 수를 하나씩 구분해보았다.

## 3.2.1. 리프 노드 삭제

<p align="center"><img src = "https://user-images.githubusercontent.com/27791880/219986727-1eb51e11-1b85-4e86-b99c-b5a404a2b366.png" width=500></p>

리프 노드를 삭제하는 경우 부모 노드가 더 이상 삭제하는 노드를 가리키지 않도록 만들어야 한다.

## 3.2.2. 자식 노드가 하나인 노드 삭제

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/219987821-c099886d-1624-4c72-af62-1a6f0b144c46.png" width=700></p>

위의 이미지처럼 삭제하려는 노드가 가진 child가 하나일 때 child노드를 기준으로 parent의 parent노드가 child 노드를 가리킬 수 있도록 수정해야 한다.

## 3.2.3. 자식 노드가 두 개인 노드 삭제

자식 노드가 두 개인 노드를 삭제할 때는 2가지 경우를 생각해 볼 수 있다.

1. 삭제할 노드의 right child 중 가장 작은 값을 삭제할 노드의 parent가 가리키도록 한다.
2. 삭제할 노드의 left child 중 가장 큰 값을 삭제할 노드의 parent가 가리키도록 한다.

결국에는 두가지 경우 모두 이진 탐색 트리의 특징(왼쪽 노드는 현재 노드보다 작은 값, 오른쪽 노드는 현재 노드보다 큰 값)을 지키려 한다는 점에서 사실상 동일한 경우의 수이기 때문에 전자에 초점을 맞춰서 정리하려 한다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/220025952-c0db35ce-15d7-492a-bf35-2846438f2db3.png" width=300></p>

위의 이미지와 같은 트리가 있다고 할 때, 5를 담고 있는 노드를 삭제한다고 생각해보자. 이 때 삭제할 노드의 right child 중에서 가장 작은 값을 삭제할 노드의 parent인 10이 가리키도록 하려고 한다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/220027934-1522d01d-bdcc-4c06-b1f0-497be7167a56.png" width=300></p>

Right child 중에서 가장 작은 값은 가장 왼쪽에 있는 노드인 3이 해당된다.

해당 노드를 삭제할 노드의 parent인 10의 왼쪽 브랜치가 가리키도록 한다. 또한 나머지 기존 5를 담은 노드의 left child와 right child와도 관계를 맺어 서로 가리킬 수 있도록 만들어준다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/220030248-3fecd501-df31-4791-b4d4-a92ac90f4679.png" width=300></p>

위의 이미지에서는 해당되지 않지만, 만약 노드 3이 child node를 가지고 있었을 경우, 노드 3의 parent였던 노드 4가 노드 3의 child node를 가리키도록 만들면 된다.

## 3.2.4. 삭제 메서드 구현

삭제 기능을 구현할 때 가장 먼저 생각해야 하는 것은 삭제할 value가 tree내에 존재하는지 확인하는 것이다. 삭제할 value가 tree 내에 없을 경우 False를 반환해야 한다.

```python
def delete(self, value):
    # searched는 트리를 순회하면서 value에
    # 해당하는 노드를 찾았는지 여부를 나타낸다.
    searched = False
    # current_node는 삭제할 노드를 지칭.
    self.current_node = self.head
    # parent는 삭제할 노드의 parent 노드를 지칭.
    self.parent = self.head

    while self.current_node:
        # 삭제할 value를 찾음.
        if self.current_node.value == value:
            searched = True
            break
        # value가 현재 노드의 값보다 작을 때
        elif value < self.current_node.value:
            self.parent = self.current_node
            self.current_node = self.current_node.left
        # value가 현재 노드의 값보다 클 때
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right
    
    # 삭제하려는 노드가 트리에 존재하지 않음
    if searched == False:
        return False

```

이제 3.2.1 부터 3.2.3까지 기술한 각 케이스들을 코드로 구현해본다.

### Case 1: 삭제할 노드가 leaf 노드인 경우

```python
def delete(self, value):

    ...

    """
    삭제할 노드가 leaf 노드일 경우

    self.current_node : 삭제할 노드
    self.parent : 삭제할 노드의 부모 노드
    """
    if self.current_node.left == None and self.current_node.right == None:
        # 삭제할 노드의 값이 parent 보다 작은 경우 왼쪽에 위치한다.
        # 따라서 parent의 left child와의 연결을 끊어준다.
        if value < self.parent.value:
            self.parent.left = None
        else:
            self.parent.right = None

        # 현재 삭제하려는 노드는 객체이기 때문에
        # del을 사용하면 메모리 상에서도 지워진다.
        del self.current_node

```

### Case 2: 삭제할 노드의 child node가 한 개인 경우

삭제할 노드의 child node가 한 개인 경우, 고려해야 할 경우의 수가 2가지 더 늘어난다.

![bst_deletion_1child_left](https://user-images.githubusercontent.com/27791880/220084493-ac34a1d4-e061-486a-bd85-ebd2cda9709d.png) |![bst_deletion_1child_right](https://user-images.githubusercontent.com/27791880/220084551-039546bf-0c88-4f91-a115-568644019a8e.png)
--- | --- |

1. 삭제할 노드의 child node가 left node인 경우
2. 삭제할 노드의 child node가 right node인 경우

linked list의 형태로 구현하기 때문에 연결되는 노드의 정보가 중요하다. 따라서, child node가 왼쪽에 있는지 오른쪽에 있는지 구분하여 삭제하는 노드의 parent와 관계를 맺어주어야 한다.

```python
def delete(self, value):

    ...

    """
    삭제할 노드의 child node가 한 개 인 경우

    self.current_node : 삭제할 노드
    self.parent : 삭제할 노드의 부모 노드
    """
    # 삭제할 노드의 child node가 left node 하나인 경우
    if self.current_node.left != None and self.current_node.right == None:
        # 현재 삭제하려는 값이 parent의 value보다 작을 때
        # (current_node와 value는 같은 값)
        if value < self.parent.value:
            # value를 삭제하게 되면 value의 parent의 left node는 연결이 끊어진다.
            # 또한 value의 left child node도 연결이 끊어진다.
            # 따라서, 이 둘을 이어준다.
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    
    # 삭제할 노드의 child node가 right node 하나인 경우
    elif self.current_node.left == None and self.current_node.right != None:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right

```

### Case 3-1: 삭제할 노드가 child node를 2개 가진 경우

다음은 삭제할 노드가 child node를 두 개 가지고 있는 경우이다. 그 중에서도 **삭제할 노드가 parent node의 왼쪽에 있는 경우에 해당한다.**

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/220104372-8316479c-98e7-4a2f-b8bf-a63413118ebf.png" width=700></p>

이러한 케이스에서 삭제 후 취할 수 있는 전략은 2가지가 존재한다.

1. 삭제한 노드의 오른쪽 child 중에서 가장 작은 값을 삭제한 노드의 parent 노드가 가리킨다.
2. 삭제한 노드의 왼쪽 child 중에서 가장 큰 값을 삭제한 노드의 parent 노드가 가리킨다.

둘 중 어떤 전략을 취하든 상관 없지만 첫 번째 전략을 사용해본다.

이 때 경우의 수는 또 2가지로 나누어진다.

1-1. 삭제한 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 child 노드가 없을 때
1-2. 삭제한 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 오른쪽에 child 노드가 있을 때

```python
def delete(self, value):

    ...

    """
    삭제할 노드의 child node가 2개 인 경우
    (삭제할 노드가 parent의 왼쪽에 있는 경우)

    self.current_node : 삭제할 노드
    self.parent : 삭제할 노드의 부모 노드
    """
    # case3: 삭제할 노드의 child node가 2개인 경우
    if self.current_node.left != None and self.current_node.right != None:
        # case3-1: 삭제할 노드가 parent의 왼쪽에 있는 경우
        if value < self.parent.value:
            # 가장 작은 값을 current_node로 올리기 위해서는
            # 가장 작은 값을 담을 change_node와
            # 해당 값의 parent인 change_node_parent가 필요
            self.change_node = self.current_node.right          # 초기화
            self.change_node_parent = self.current_node.right   # 초기화

            # 이진 탐색 트리에서 가장 작은 값은 왼쪽 노드에만 있다.
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left

            # 삭제한 노드의 오른쪽 자식 중 가장 작은
            # 값을 가진 노드의 오른쪽에 child 노드가 있을 때
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            # 삭제한 노드의 오른쪽 자식 중 가장 작은
            # 값을 가진 노드의 오른쪽에 child 노드가 없다면
            # 기존의 연결고리를 끊어주어야 한다.
            else:
                self.change_node_parent.left = None
            
            self.parent.left = self.change_node
            self.change_node.right = self.current_node.right
            self.change_node.left = self.current_node.left

```

### Case 3-2: 삭제할 노드가 child node를 2개 가진 경우

이번에도 역시 삭제할 노드가 child node를 2개 가진 경우이지만, **삭제할 노드가 parent node의 오른쪽에 있는 경우에 해당한다.**

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/220120078-06babb2f-d084-4e77-92c6-df6884e2f495.png" width=700></p>

Case 3-1에서 살펴보았던 삭제 후 취할 수 있는 전략 2가지도 동일하고, 이번에도 동일하게 삭제한 노드의 오른쪽 child 중에서 가장 작은 값을 삭제한 노드의 parent 노드가 가리킬 수 있도록 구현한다.

이 때의 경우의 수 역시 동일하게 2가지로 나누어진다.

1. 삭제한 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 child 노드가 없을 때
2. 삭제한 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 오른쪽에 child 노드가 있을 때

```python
def delete(self, value):

    ...

    """
    삭제할 노드의 child node가 2개 인 경우
    (삭제할 노드가 parent의 왼쪽에 있는 경우)

    self.current_node : 삭제할 노드
    self.parent : 삭제할 노드의 부모 노드
    """
    # case3: 삭제할 노드의 child node가 2개인 경우
    if self.current_node.left != None and self.current_node.right != None:
        # case3-1: 삭제할 노드가 parent의 왼쪽에 있는 경우
        if value < self.parent.value:
            
            ...
            
            self.parent.left = self.change_node
            self.change_node.right = self.current_node.right
            self.change_node.left = self.current_node.left
        
        # case3-2: 삭제할 노드가 parent의 오른쪽에 있는 경우
        else:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right

            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right

```

# Reference

* [Wikipedia - Binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)
* [파이썬 알고리즘 인터뷰](https://www.onlybook.co.kr/entry/algorithm-interview)
* [ORIE 6125: Computational Methods in Operations Research](https://people.orie.cornell.edu/snp32/orie_6125/data-structures/binary-tree.html)
* [math.oxford.emory.edu](https://math.oxford.emory.edu/site/cs171/23trees/)
