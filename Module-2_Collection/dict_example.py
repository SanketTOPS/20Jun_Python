mydict={'id':1,'name':'sanket','sub':'python'}
"""print(mydict)
print(mydict['sub'])
print(mydict.get('name'))
print(mydict.keys())
print(mydict.values())"""

"""if 'name' in mydict:
    print("Yes...")
else:
    print("Nooo")"""

"""if 'sanket' in mydict.values():
    print("Yes...")
else:
    print("Nooo")"""

#print(len(mydict))

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""

"""for i,j in mydict.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

# -------------------------------- #
print(mydict)
#mydict['id']=2
#mydict['city']='rajkot'
#mydict.pop('name')
mydict.clear()
print(mydict)


"""newdict=mydict.copy()
print(newdict)"""