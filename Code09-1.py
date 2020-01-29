coffee = 0

# 함수 선언
def coffee_machine(button) :
    print("뜨거운 물")
    print("종이컵")

    if coffee == 1 :
        print("보통커피")
    elif coffee == 2 :
        print("블랙커피")
    elif coffee == 3 :
        print("설탕커피")
    else :
        print("다시 주문하세요")

    print("물붓기")
    print("스푼")

coffee = int(input("어떤 커피??"))
coffee_machine(coffee)
print("손님 여기있어요")