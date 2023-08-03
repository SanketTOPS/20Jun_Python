fl=open('newfile.txt','a')


n=int(input("Enter number of students:"))

def getdata():
    id=input("Enter ID:")
    name=input("Enter Name:")
    fl.write(f"ID:{id}")
    fl.write(f"\nName:{name}\n")

for i in range(n):
    getdata()

    