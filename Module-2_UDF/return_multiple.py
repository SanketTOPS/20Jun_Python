def getdata(id,name):
    return id,name

#x=getdata(1,'Sanket')
"""print(x[0])
print(x[1])"""

"""print(f"ID:{x[0]}")
print(f"Name:{x[1]}")"""


def data():
    x=getdata(1,'Sanket')
    stid=x[0]
    stnm=x[1]
    print(f"ID:{stid}")
    print(f"Name:{stnm}")

data()