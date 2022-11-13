import random

def ran_num():
    global ran_num
    ran_num = []
    while len(ran_num) < 6:
       x = random.randint(1,45)
       if x not in ran_num:
            ran_num.append(x)
    ran_num.sort()
    return ran_num

def user():
    global user
    user= list(map(int,input("6개의 숫자를 중복없이 입력하십시오:").split(',')))
    if len(user) != 6:
        print("다시 입력하십시오:")
    else:
        user.sort()
    return user

def lotto_result():
    global lotto_num
    lotto_num = []
    while len(lotto_num) < 6:
        y = random.randint(1,45)
        if y not in lotto_num:
            lotto_num.append(y)
    return lotto_num  

def result():
    same = 0
    if A == 1:
        my_num = ran_num
    else:
        my_num = user
    for x in my_num:
        if x in lotto_num:
            same += 1
            
    if same == 4:
        return("축하합니다 3등입니다!!")
    elif same == 5:
        return("축하합니다 2등입니다!!")
    elif same == 6:
        return("축하합니다 1등입니다!!")
    else:
        return("아쉽지만 당첨되지 못하셨네요.")
        
        
A = int(input("랜덤으로 뽑으려면 1번을 눌러주세요. default는 직접 입력하는것입니다:"))
if A == 1:
    print("당신의 번호는:",ran_num(),",""당첨 번호는",lotto_result(),result())
else:
    print("당신의 번호는:",user(),",""당첨 번호는",lotto_result(),result())
