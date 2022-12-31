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