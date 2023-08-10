class student:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
# Object of class
st=student()
st.getdata()