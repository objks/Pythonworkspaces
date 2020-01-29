ch = ""
a,b, = 0,0

while True :
    a = int(input("첫번째 수 : "))
    b = int(input("두번째 수 : "))
    ch = input("연산자 : ")

    if(ch == "+") :
        print("%d + %d = %d" % (a,b, a+b))
    elif (ch == "-") :
        print("%d - %d = %d" % (a,b, a-b))
    elif (ch == "*") :
        print("%d * %d = %d" % (a,b, a*b))
    elif (ch == "/") :
        print("%d / %d = %d" % (a,b, a/b))
    elif (ch == "%") :
        print("%d %% %d = %d" % (a,b, a%b))
    elif (ch == "//") :
        print("%d // %d = %d" % (a,b, a // b))
    elif (ch == "**") :
        print("%d ** %d = %d" % (a,b, a**b))
    else :
        print ("연산자 다시")