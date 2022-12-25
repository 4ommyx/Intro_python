# การลบข้อมูลของ tuple 
# (ต้องแปลงจาก tuple เป็น list แล้วค่อยลบข้อมูล)

tup = (1,2,3,4,5,"mumond",55,5)
lis = list(tup)
lis.remove("mumond")
lis.pop()

print("list : ",lis)
tup = tuple(lis)
print("tuple : ",tup)

# ค้นหาและนับจำนวนสมาชิก count()
tup = (1,2,3,4,5,"mumond",55,5)
a = tup.count(5)
print(a)

# ค้นหาสมาชิกด้วย index() บอกว่าสมาชิกที่จะค้นหาอยู่ที่ index อะไร

b = tup.index("mumond")
print(b)

# การ sort() เรียงลำดับข้อมูล

tupp = (212,1,2,343,32,56,443,4,3,2,87)
# tupp.sort() ไม่มีฟังก์ชั่น sort ต้องแปลงเป็น list แทน
lis = list(tupp)
lis.sort()
tupp = tuple(lis)
print(tupp)

