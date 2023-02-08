#LIFO 방식의 stack 구현

class FixedStack:
    #고정길이 스택을 구현

    class Empty(Exception):
        #스택이 비어있을 때 팝 예외처리
        pass
    class Full(Exception):
        #가득찬 스택에 푸시할때 예외처리
        pass

    def __init__(self, capacity = 256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0
    
    def is_full(self):
        return self.pty >= self.capacity

    def push(self, value):
        #마지막 인덱스에 저장
        if self.is_full():
            raise FixedStack.Full #예외처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        #마지막 인덱스에 저장된 값을 꺼냄
        if self.is_empty():
            raise FixedStack.Empty #예외처리발생
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self):
        #마지막 인덱스에 저장된 값을 호출만 함
        if self.is_empty():
            raise FixedStack.Empty #예외처리발생
        return self.stk[(self.ptr-1)]
    
    def clear(self):
        #스택의 모든 데이터를 삭제
        self.ptr = 0
    
    def find(self, value):
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                return i #검색성공
        return -1 #검색 실패
    
    def count(self, value):
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value: #하나 검색 성공
                c += 1
        return c
    
    def __contains__(self, value):
        return self.count(value) > 0
    


