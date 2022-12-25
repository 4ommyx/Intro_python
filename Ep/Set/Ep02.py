
#เพิ่มข้อมูลสมาชิก add()
name = {"mu","aom","mumond"}
print(name)
name.add("music")
print(name)

# เพิ่มสมาชิกหลายๆตัว update()
lis = ["a","b","c","a"]
name.update(lis)
print(name)

#แสดงผลของสมาชิกแต่ละตัว
for i in name:
    print(i)

#เช็คว่าสมาชิกตัวนี้อยู่ใน set ไหม

if "mu" in name :
    print("True")
else:
    print("false")
