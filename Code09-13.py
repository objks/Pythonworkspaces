import random

#함수
def getNumber() :
    return random.randrange(1, 46)

# 전역변수
lotto = []
num = 0

# 메인 코드
print("*** 로또 추첨 시작 ***")

while True :
    num = getNumber()
    if lotto.count(num) == 0 :
        lotto.append(num)
    
    if len(lotto) >= 6 :
        break

print("추첨된 로또 번호 : ", end= '')
lotto.sort()
for i in range(0, 6) :
    print("%d " % lotto[i], end = '')