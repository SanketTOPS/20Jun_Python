fl=open('newfile.txt','w')

id=input("Enter ID:")
name=input("Enter Name:")

"""fl.write(id)
fl.write(name)"""

fl.write(f"ID:{id}")
fl.write(f"\nName:{name}")