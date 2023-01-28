#어디서 틀린지 모름
from typing import Any, Sequence

def max(a : Sequence) -> Any:
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

print('배열의 최댓값 구합니다.')
print('end를 입력하면 종료.')

num = 0
x = []

while True:
    s = input(f'x[{num}]값을 입력하시오: ')
    if s == 'end' or 'End':
        break
    x.append(int(s))
    num += 1

print(f'{num}개의 원소를 입력했습니다.')
print(f'최댓값은 {max(x)} 입니다.')


#배열 원소를 역순으로 정렬
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

#리스트의 역순 .reverse()
x.reverse()
#역순으로 정렬한 리스트 생성 reversed()
y = list(reversed(x))

#10진수 받아 (2~36)다른 진수로 변환하여 출력
def card_conv(x:int, r:int) -> str:
  d = ''
  dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  while x > 0:
    d += dchar[x % r]
    x //= r
  return d[::-1]

num = int(input('10진수 값:'))
rum = int(input('몇 진수로 바꾸겠습니까?:'))
print(f'{num}을 {rum}진수로 바꾸면 {card_conv(num, rum)}입니다')

#1부터 n까지 정수의 합 구하기

def sum_1ton(n:int) -> int:
  s = 0
  while n >0:
    s += n
    n -= 1
  return s

n = int(input('n의 값을 구하시오:'))
print(sum_1ton(n))


#1000이하의 소수 개수 구하기

counter = 0

for i in range(2,1001):
  for n in range(2,i):
    counter += 1
    if i % n == 0:
      break
    else:
      print(i)

print(f'1000까지 소수와 이를 확인하기 위해 나눈 횟수:{counter}')

#1000이하의 소수 개수 구하기 (제곱근안에서 구하기:알고리즘개선)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
  i = 1
  while prime[i] * prime[i] <= n:
    counter += 2
    if n % prime[i] == 0:
      break
    i += 1
  else:
    prime[ptr] = n
    ptr += 1
    counter += 1

for i in range(ptr):
  print(prime[i])

print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

#얕은 복사와 깊은 복사
#얕은 복사
x = [[1,2,3], [4,5,6]]
y = x.copy()
x[0][1] = 9

print( x,'\n', y)

#깊은복사
import copy
x = [[1,2,3], [4,5,6]]
y = copy.deepcopy(x)
x[0][1] = 9

print( x,'\n', y)
