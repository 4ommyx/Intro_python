# keyword argument 
# เป็นการระบุ kerword ของ argument

def arg (name,age,ww):
    print("ชื่อ : ",name,"อายุ : ",age,"น้ำหนัก : ",ww)
arg("nattawut",20,65)
arg(20,"nattawut",65) #ข้อมูล Error

# การใช้ keyword argument
arg(age=20,name="nattawut",ww=65)
