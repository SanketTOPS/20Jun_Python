class studinfo:
    stid=12
    stnm='Sanket'

    def myfunc(self):
        print("This is studinfo class.")

# Object of class
st=studinfo()
print("Student ID:",st.stid)
print("Student Name:",st.stnm)
st.myfunc()
