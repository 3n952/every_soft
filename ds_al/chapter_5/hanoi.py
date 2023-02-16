#no -> 옮겨야할 원반의 개수 x ->시작 기둥 y -> 목표 기둥(1~3사이 범위의 기둥)

def move(no, x, y):
    if no > 1:
        move(no-1, x, 6-x-y)
    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옯깁니다.')
    if no > 1:
        move(no-1, 6-x-y, y)

print('tower of hanoi')
n = int(input('원반의 개수:'))
move(n,1,3)
