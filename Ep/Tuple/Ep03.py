
numm = (1,2,3,4,5,6,7,8,12)

# นับจำนวนสมาชิก len
print(len(numm))

# การสร้างและเพิ่มข้อมูล 
# การสร้าง
num1 = (1) # จะมองว่าเป็น int
num2 = (1,) # มองเป็น Tuple(ให้ใส่คอมม่าต่อหลังด้วย)
print(type(num1))
print(type(num2))

#การเพิ่ม (บวกคล้ายๆ list)
name = ("aom","mu")  # ttuple
#new = ("mumond")    # str (ต้องแปลงจาก str เป็น tuple ก่อน)
new = ("mumond",)    # tuple 

name = name + new
print(name)