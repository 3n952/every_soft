#FIFO구조의 큐queue

'''ring buffer구조의 큐 구현'''

class FixedQueue:
    #고정길이 queue을 구현

    class Empty(Exception):
        #큐가 비어있을 때 dequeue 예외처리
        pass
    class Full(Exception):
        #가득찬 큐에 enqueue 할때 예외처리
        pass

def __init__(self, capacity):
    self.no = 0 #현재의 데이터 개수
    self.front = 0 #프론트 인덱스
    self.rear = 0 #리어 인덱스
    self.capacity = capacity
    self.que = [None] * capacity

def __len__(self):
    return self.no 
def is_empty(self):
    return self.no <= 0
def is_full(self):
    return self.no >= self.capacity

def enque(self, x):
    #데이터 삽입
    if self.is_full():
        raise FixedQueue.Full
    
    self.que[self.rear] = x
    self.rear += 1
    self.no += 1
    if self.rear == self.capacity:
        self.rear = 0

def deque(self):
    #데이터 삭제
    if self.is_empty():
        raise FixedQueue.Empty
    x = self.que[self.front]
    self.front += 1
    self.no -= 1
    if self.front == self.capacity:
        self.front = 0
    return x

def peek(self):
    #데이터 들여다보기
    if self.is_empty():
        raise FixedQueue.Empty
    return self.que[self.front]

def find(self, value):
    #queue에서 데이터 찾기
    for i in range(self.no):
        idx = (i + self.front) % self.capacity
        if self.que[idx] == value:
            return idx
    return -1

def count(self, value):
    #queue에 있는 value 개수 반환
    c= 0
    for i in range(self.no):
        idx = (i + self.front) % self.capacity
        if self.que[idx] == value:
            c += 1
    return c

def __contains__(self, value):
    #queue에 value가 있는지 반환
    return self.count(value)

def clear(self):
    self.no = self.front = self.rear = 0
        

