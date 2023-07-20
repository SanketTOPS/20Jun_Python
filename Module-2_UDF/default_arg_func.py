"""def getdata(id,name,sub='Python'):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

#getdata(101,'Sanket')

getdata(102,'Nirav','JAVA')"""


def getdata(id,name,sub='Python',city='Rajkot'):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)
    print("City:",city)


stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")
stcity=input("Enter City:")

getdata(stid,stnm)