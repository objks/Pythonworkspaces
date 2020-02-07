inFp = None
inStr = ""

inFp = open("C:\DEV\Pythonworkspaces\data1.txt", "r", encoding="UTF-8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end="")

inFp.close()
