inFp, outFp = None, None
inStr = ""

inFp = open("C:\Windows\win.ini", "r")
outFp = open("C:\DEV\Pythonworkspaces\data2.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("-정상적으로 복사됨")