#global
a=34
b=65

def production():
    #local
    a=34
    b=65
    print("Mul:",a*b)

print("Sum:",a+b)
production()