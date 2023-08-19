import re

mystr="This is Python!4564654"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
x=re.findall('59$',mystr)
print(x)