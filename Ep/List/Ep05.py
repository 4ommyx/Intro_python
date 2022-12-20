number = [1,2,3,4,5,6,7,8]

#การเพิ่มข้อมูล append,insert

print("before :",number)

#append() นำสมาชิกใหม่มาต่อท้าย
number.append(100)
number.append(200)

print("after :",number)

#insert (index,newdata) นำข้อมูลมาแทรกนะ index นั้นๆ
number.insert(1,200)
number.insert(0,100)

print("after :",number)
