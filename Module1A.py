import Module1

Module1.func1()
Module1.func2()
Module1.func3()

myList = [1,2,3,4,5]
def add10(num) :
    return num + 10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList)

def genFunc() :
    yield 1
    yield 2
    yield 3
print(list(genFunc()))