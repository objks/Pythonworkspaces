def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2

    return result

#전역 변수 선언
res = 0
var1, var2, oper = 0, 0, ""

# 메인코드
oper = input("계산 입력(+,-,*,/) :")
var1 = int(input("첫번째 수 :"))
var2 = int(input("두번째 수 :"))

res = calc(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" % (var2, oper, var2, res))