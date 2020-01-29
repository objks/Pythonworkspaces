def multi(v1, v2) :
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

# 전역변수
myList = []
hap, sub = 0,0

# 메인코드 부분
myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 : %d, %d" % (hap, sub))