
#정수의 합
print('1부터 n까지의 합')
n = int(input('n을 입력하시오:'))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지의 합은 {sum}입니다.')



#a-b까지 합
print('a to b sum')
def absum(a,b):
    sum = 0
    #정렬
    if a > b:
        a,b = b,a
    for i in range(a,b+1):
        if i < b:
            print(f'{i}+', end = '')
        else:
            print(f'{i}=', end = '')
        sum += i
    print(sum)


#두 값 교환히기
a= 7
b = 8
t = a
a = b
a = t

#+ - 번갈아 출력하기
print('+-를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for _ in range(n//2):
    print('+-', end = '')

if n % 2: #홀수일때를 의미함
    print('+', end = '')

print()



#*를 n개 출력하되 w개마다 줄바꿈하기

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈을 할까요?'))

for i in range(n):
    print('*', end = '')
    if i % w == w - 1:
        print()
if n % w:
    print()

#2버전
n = int(input('몇개 출력?'))
w = int(input('몇개마다 줄 바꿈?'))

for i in range(1, n+1):
  print('*', end = '')
  if i % w == 0:
    print()

#3버전
for _ in range(n // w):
  print('*' * w)
  
rest = n % w
if rest :
  print('*' * rest)

# 정수값 가로,세로 직사각형에서 변의 길이 구하기

area = int(input('직사각형의 넓이를 입력하세요:'))

for i in range(1, area + 1):
  if i * i > area:
    break
  if area % i: continue
  print(f'{i} x {area // i}')

#10-99사이 난수 n개 생성하기 (13나오면 중단)
import random

n = int(input('몇 개를 생성할까요?'))

for _ in range(n):
  a = random.randint(10, 99)
  print(a, end = ' ')
  if a == 13:
    print('프로그램을 종료합니다.')
    break

print('\n난수 생성을 종료합니다.')

#구구단곱셈표
for i in range(1, 10):
  for j in range(1,10):
    print(f'{i * j:3}', end = ' ')
  print()

#오른쪽 아래가 직각인 삼각형 *모양으로 만들기
n = 4
for i in range(n):
  for _ in range(n - i - 1):
    print(' ', end = '')
  for _ in range(i+1):
    print('*', end = '')
  print()