inFp = None
inStr = ""

inFp = open("C:\DEV\Pythonworkspaces\data1.txt", "r", encoding="UTF-8")

inList = inFp.readlines()
print(inList)


inFp.close()
