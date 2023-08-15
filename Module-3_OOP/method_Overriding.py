class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
class otherstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)
    

st=student()
ot=otherstudent()

st.getdata(101,'Nirav')
ot.getdata(102,'Ashok')