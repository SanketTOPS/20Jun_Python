import re

mystr="This is Python!5465"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B69',mystr)
#x=re.findall('\AThis',mystr)
#x=re.findall('65\Z',mystr)
x=re.findall('This|That',mystr)
print(x)