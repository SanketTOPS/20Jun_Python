"""data={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    k=input("Enter a key:")
    v=input("Enter a value:")

    data[k]=v

print(data)"""


data={}

keys=['id','name','sub']

for i in range(len(keys)):
    v=input(f"Enter a value for {keys[i]}:")
    data[keys[i]]=v

print(data)