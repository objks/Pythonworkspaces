inFp = None
inStr = ""

inFp = open("C:/DEV/Pythonworkspaces/data1.txt","r", encoding="UTF-8")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()
