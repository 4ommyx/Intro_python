# ฟังก์ชั่นแบบคืนค่า มีการใช้ ฟังก์ชั่น return 
# ซึ่งทำการ return ค่าของฟังก์ชั่นนั้นๆ ตามที่เรากำหนด 
# return ยังทำหน้าที่คล้าย break ได้ด้วย

"""
1.ไม่มีการรับและส่งค่า
def name():

2.มีการรับค่าเข้าไปทำงาน
def name(a,b):

3.รับค่าเข้าไปทำงานและส่งออกมา
def add(a,b):
    return a+b

4.ไม่มีการรับค่าแต่มีการส่งออกไป
def zero():
    return 0

"""
def add (a,b):
    return a+b

def shownum(): #ไม่มีการรับแต่มีการส่งออกไป
    return 112

a = add (10,20)
print(a)
b = shownum ()
print(b)