a=34 #1

print("A:",a)

def getvalue():
    global a #2
    a=78
    print("A:",a)

getvalue()
