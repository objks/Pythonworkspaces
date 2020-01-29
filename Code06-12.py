hap = 0
a, b = 0,0

while True :
    a = int(input("더할 첫번째 수 : "))
    if a == 0 :
        break
    b = int(input("더할 두번째 수 :"))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))

print("반복문 탈출")