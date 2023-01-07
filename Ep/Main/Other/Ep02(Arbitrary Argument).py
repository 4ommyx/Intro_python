# args คือ argument ที่ส่งค่าได้แบบ infinity 
# ระบุ * ไว้หน้าตัวแปรเสมอ 
# ข้อมูลที่ได้เก็บในรูป tuple


def summ (*num):
    total = 0
    print(num)
    for i in range(len(num)):
        total = total + num[i]
    print(total)


summ(10,5)
summ(10,5,20)
summ(10,5,20,15)
summ(10,5,20,15,50)

# kwargs --> parameter มีหลายชื่อ 
# เก็บข้อมูลในรูปของ dict จึงมี parameter ได้เยอะ 
# **kwrgs

def data(**dataa):
    print(dataa)
    print(dataa["age"])

data(age=18,ww=60,hh=170)
data(age=23,ww=46)
data(age=14)

