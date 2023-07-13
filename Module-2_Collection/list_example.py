tech=['python','php','java','ruby','react','angular']
"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[1:4])
print(tech[2:])
print(tech[:4])
print(len(tech))
tech[2]='android'
print(tech)"""

# ------------------------------------ #

#print(tech)
#print(tech.index('react'))

#0 = python
#1 = php
"""for i in tech:
    #print(i)
    #print(tech.index(i),"=",i)
    print(f"{tech.index(i)}={i}")"""

"""if 'php' in tech:
    print('Yes...')
else:
    print('Nooo')"""

# ------------------------------------------- #

print(tech)
tech.append('c++')
tech.insert(2,'html')
#tech.pop()
#tech.pop(1)
#tech.remove('java')
#del tech[0]
#tech.clear()
#del tech
#tech.reverse()
#tech.sort()
print(tech)

#newtech=tech.copy()
#print(newtech)

newtech=["C","C++","CSS","JS"]
print(newtech)
#print(tech+newtech)
tech.extend(newtech)
print(tech)
