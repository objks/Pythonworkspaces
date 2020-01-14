

while(True) :
    result = int(input("변환할 진수를 선택 : "))
    num = input("값 입력 : ")
    if result == 16 :
        numReturn = int(num, 16)
        break
    if result == 10 :
        numReturn = int(num, 10)
        break
    if result == 8 :
        numReturn = int(num , 8)
        break
    if result == 2 :
        numReturn = int(num , 2)
        break
    else :
         print("16,10,8,2 진수만 입력하세요")

print("16진수 ==> ",hex(numReturn))
print("10진수 ==> ",numReturn)
print("8진수 ==> ",oct(numReturn))
print("2진수 ==> ",bin(numReturn))
