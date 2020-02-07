myStr = '공부는 재밌어요. 공부를 해야해요'
strPosList = []
index = 0

while True :
    try :
        index = myStr.index('파이썬', index)
        strPosList.append(index)
        index = index +1
    except :
        break

print('파이썬 글자 위치 -->', strPosList)