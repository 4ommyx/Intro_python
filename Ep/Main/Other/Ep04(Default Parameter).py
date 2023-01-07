# default Parameter
# เป็นการกำหนดค่าเริ่มต้น หากเราไม่ได้ใส่ค่าไว้ใน parameter

def arg (name,age,pp="ไม่ระบุ"):
    print("ชื่อ : ",name,"อายุ : ",age,"น้ำหนัก : ",pp)
arg("nattawut",20,"male")

# การใช้ keyword argument
arg(age=20,name="music   ",pp="female")

# การใช้ default parameter 
# การไม่ระบุเพศ ค่า pp จะวิ่งไปที่ default parameter
arg(age=20,name="prayut  ")
