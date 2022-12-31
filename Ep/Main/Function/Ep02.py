#การรับค่าเข้า function โดยระบบ parameter

def name(a):
    print("name : ",a)

a = "music"
name("aom")
name(a)

def name1(a,b):
    print("name : ",a ,"  age : ",b)

name1("aom",20)

# Argument  --> ค่าที่ส่งเข้าไปใน function (aom,20)
# Parameter --> ค่าตัวแปรที่รับข้อมูลจาก Argument มาทำงาน (a,b) 
