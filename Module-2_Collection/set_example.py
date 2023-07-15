myset={'a','b','c','d','e','f','a','b'}
#print(myset)
#print(myset[0])

#print(len(myset))

"""if 'b' in myset:
    print("Yes...")
else:
    print("Nooo")"""

"""for i in myset:
    print(i)"""

# ----------------------------------------- #
print(myset)
#myset.add('g')
#myset.update(['h','i','j'])
#myset.remove('d')
#myset.pop()
#myset.clear()
#print(myset)

"""newset=myset.copy()
print(newset)"""

newset={'p','q','r','s','a','b','d'}
print(newset)

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)