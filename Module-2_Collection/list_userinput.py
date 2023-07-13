tech=[]


n=int(input("Enter number of elements:")) #n=5

for i in range(n):
    x=input("Enter your name:")
    tech.append(x)


tech.sort()
print(tech)

