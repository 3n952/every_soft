def solution(price, money, count):
    answer = -1
    price_list = []
    for i in range(count):
        price_list.append(price)
        price = price_list[0] + (price * i)
    
    for j in range(len(price_list)):
        total = price_list.pop()
        total += total

    if money >= total:
        return 0
    else:
        answer = total - money
    
    return answer
   

print(solution(3,20,4))