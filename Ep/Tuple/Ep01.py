# Tuple เปลี่ยนแปลงข้อมูลไม่ได้ password/personal-id

tup = (1,2,"mu")
lis = [1,2]

lis[0] = 0
#tup[0] = 0 ไม่สามารถเปลี่ยนแปลงข้อมูลได้

print(tup)
print(lis)
print("--------")

#การเข้าถึงข้อมูล
print(tup[0:3])
print(tup[1:])
print()
