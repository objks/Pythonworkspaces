import os

inFp = None
fName, inList, inStr ="", [], ""

fName = input("C:\DEV\Pythonworkspaces\data1.txt : ")

if os.path.exists(fName) :
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end= "")

    inFp.close()

else :
    print("%s 파일 없음. " % fName)