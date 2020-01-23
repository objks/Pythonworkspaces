age = int(input("나이 : "))
point = True
count = int(input("적립 횟수는 ? : "))

if (age < 18) : 
    print("티켓을 판매할 수 없다.")
elif ((age <= 60) or ((point == True) and (count ==5))) :
    print("티켓은 5,000원 입니다.")
else :
    print("티켓은 8,000원 입니다.")

    
