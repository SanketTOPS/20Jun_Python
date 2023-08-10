class student:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Calling via object
"""st=student()
#st.getdata()
st.stid=2
st.stnm='Sanket'
st.getdata()"""

# Calling via Instance
student().getdata()
student().stid=2
student().stnm='Ashok'
student().getdata()
