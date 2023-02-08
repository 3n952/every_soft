'''선형 검색 알고리즘'''
#while 문 선형검색

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
  '''시퀀스 a에서 key와 값이 같은 원소를 선형검색'''
  i = 0
  while True:
    if a[i] == len(a):
      return -1
    if a[i] == key:
      return i
    i += 1

if __name__ == '__main__':
  num = int(input('원소 수를 입력하세요:'))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  ky = int(input('검색 할 key 값은?'))
  idx = seq_search(x, ky)

  if idx == -1:
    print('검색값 존재 x')
  else:
    print(f'키 값은 x[{idx}]에 있습니다.')


#for 문으로 구현
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
  for i in range(len(a)):
    if a[i] == key:
      return i
  return -1

if __name__ == '__main__':
  num = int(input('원소 수를 입력하세요:'))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  ky = int(input('검색 할 key 값은?'))
  idx = seq_search(x, ky)

  if idx == -1:
    print('검색값 존재 x')
  else:
    print(f'키 값은 x[{idx}]에 있습니다.')


#선형 검색 알고리즘 (보초법)
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
  a = copy.deepcopy(seq)
  a.append(key)

  i = 0
  while True:
    if a[i] == key:
      break
    i+=1
  return -1 if i == len(seq) else i


'''이진 검색 알고리즘'''

from typing import Any, Sequence
def bin_search(a: Sequence, key: Any) -> int:
  pl = 0
  pr = len(a) - 1

  while True:
    pc =  (pl + pr) // 2
    if a[pc] == key:
      return pc
    elif a[pc] < key:
      pl = pc + 1
    else:
      pl = pc -1
    if pl > pr:
      break
  return -1

'''체인법으로 구현한 해시 프로그램'''

import hashlib

#노드 클래스
class node:
  def __init__(self, key, value, next) -> None:
    self.key = key
    self.value = value
    self.next = next

#체인법 해시클래스 
class chainhash:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.table = [None] * self.capacity
  
  def hash_value(self, key) -> int:
    if isinstance(key, int):
      return key % self.capacity
    return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

  #해시법 검색
  def search(self, key):
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
      if p.key == key:
        return p.value
      p = p.next
    return None

  def add(self, key, value):
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
      if p.key == key:
        return False
      p = p.next
    
    temp = node(key, value, self.table[hash])
    self.table[hash] = temp
    return True
  
  def remove(self, key):
    hash = self.hash_value(key)
    p = self.table[hash]
    pp = None

    while p is not None:
      if p.key == key:
        if pp is None:
          self.table[hash] = p.next
        else:
          pp.next = p.next
        return True
      pp = p
      p = p.next
    return False
  
  #원소출력 함수 dump
  def dump(self):
    for i in range(self.capacity):
      p = self.table[i]
      print(i, end ='')
      while p is not None:
        print(f' ->{p.key} ({p.value})', end ='')
        p = p.next
      print()

'''오픈 주소법으로 구현한 해시 프로그램'''

from enum import Enum
import hashlib

#버킷의 속성
class Status(Enum):
  OCCUPIED = 0
  EMPTY = 1
  DELETED = 2

class Bucket:
  def __init__(self, key, value, stat: Status = Status.EMPTY):
    self.key = key
    self.value = value
    self.stat = stat
  
  def set(self, key, value, stat):
    '''모든 필드에 값을 설정하기'''
    self.key = key
    self.value = value
    self.stat = stat
  
  def set_status(self,stat):
    self.stat = stat
  
class Openhash:
  '''open hash법으로 클래스 구현'''
  def __init__(self, capacity):
    self.capacity = capacity
    self.table = [Bucket()] * self.capacity
  
  def hash_value(self, key):
    if isinstance(key, int):
      return key % self.capacity
    return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
  
  def rehash_value(self, key):
    return (self.hash_value(key)+ 1) % self.capacity
  
  def search_node(self, key):
    hash = self.hash_value(key)
    p = self.table[hash]
    for i in range(self.capacity):
      if p.stat == Status.EMPTY:
        break
      elif p.stat == Status.OCCUPIED and p.key == key:
        return p
      hash = self.rehash_value(hash)
      p = self.table[hash]
    return None
  
  def search(self, key):
    p = self.search_node(key)
    if p is not None:
      return p.value
    else:
      return None
  
  def add(self, key, value):
    '''원소 추가'''
    if self.search(key) is not None:
      return False
    hash = self.hash_value(key)
    p = self.table[hash]
    for i in range(self.capacity):
      if p.stat == Status.EMPTY or p.stat == Status.DELETED:
        self.table[hash] = Bucket(key, value, Status.OCCUPIED)
        return True
      hash = self.rehash_value(hash)
      p = self.table[hash]
    return False
  
  def remove(self, key):
    '''키값이 일치하면 원소를 삭제'''
    p = self.search_node(key)
    if p is None:
      return False
    p.set_status(Status.DELTED)
    return True
  
