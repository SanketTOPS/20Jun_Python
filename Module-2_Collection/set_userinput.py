"""nameset=[]

n=int(input("Enter number of value:"))
for i in range(n):
    x=input("Enter your name:")
    nameset.append(x)

print(set(nameset))"""


nameset=set()

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter a name:")
    nameset.add(x)

print(nameset)
