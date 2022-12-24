# การแก้ไขข้อมูล
 
tup=(1,2,3,5,6,7,8)
lis = list(tup) # tup แก้ไขข้อมูลไม่ได้จึงเปลี่ยนเป็น list แทน 

lis[3]=4

tup = tuple(lis) #เปลี่ยนชนิดของข้อมูลจาก list เป็น tuple ดังเดิม
print(tup)

# loop

for i in range(len(tup)):
    print("data : ",tup[i])

# ตรวจสอบข้อมูล

if 30 in tup :
    print("True")
else:
    print("False")
