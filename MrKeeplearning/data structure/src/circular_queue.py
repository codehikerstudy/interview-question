class circular_queue():

    def __init(self, size):
        self.size = size

        self.queue = [None for i in range(size)]    # queue를 size만큼의 크기로 초기화
        self.front = self.rear = -1                 # 원형 큐에서 공백 상태의 조건은 front == rear

    def enqueue(self, data):

        # 큐가 포화상태일 때
        if ((self.rear + 1) % self.size == self.front):
            print("큐는 포화상태입니다.")
        
        # 공백 상태의 큐일 때
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        # 공백이 아닌 상태의 큐에 새로운 데이터를 넣어야 하는 경우
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = datas

    def dequeue(self):

        # 큐가 공백일 때
        if (self.front == -1):
            print("큐는 공백상태입니다.")
        
        # 큐에 단 한 개의 데이터만 담겨 있을 때
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            # dequeue를 한 뒤 공백 큐가 되기 때문에 초기 상태로 만든다.
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):

        # 큐가 공백일 때
        if (self.front == -1):
            print("공백 큐입니다.")
        
        elif (self.rear >= self.front):
            print("원형 큐 상태:", end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            print("원형 큐 상태:", end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        
        if ((self.rear + 1) % self.size == self.front):
            print("포화 상태입니다.")


cq = circular_queue(5)
cq.enqueue(14)
cq.enqueue(22)
cq.enqueue(13)
cq.enqueue(-6)
cq.display()
print("삭제한 값 = ", cq.dequeue())
print("삭제한 값 = ", cq.dequeue())


