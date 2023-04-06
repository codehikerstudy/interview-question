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
    
    def __len__(self):
        """
        스택의 현재 사이즈(데이터의 개수)를 반환한다.
        """
        return self.pointer
    
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
    
    def __contains__(self, value):
        """
        스택에 value가 있는지 확인한다.
        """
        return self.count(value)
    
    def dump(self):
        """
        스택 안의 모든 데이터를 bottom부터 top까지 출력한다.
        """
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack[:self.pointer])
