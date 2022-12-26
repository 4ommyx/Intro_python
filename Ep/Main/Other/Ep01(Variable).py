# Global / Local variable

def local():
    x = 50
    print("local ",x)

local()
x = 100
print("global",x)

# local  ตัวแปรที่ใช้ในขอบเขตที่สร้างไว้ เช่น ที่ function นั้นๆ
# global ตัวแปรที่ประกาศไว้ใช้ได้ทั้งโปรแกรมเลย
