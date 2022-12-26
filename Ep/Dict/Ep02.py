#การเปลี่ยนแปลงข้อมูล คล้ายๆlist
room = {100:"aom",101:"ohm",102:"pee",103:"aus"}
print(room)
room[100] = "nattawut"
print(room)

#การเพิ่มข้อมูล update() (นำข้อมูลที่เพิ่มมาต่อท้าย)
room.update({"099":"doraemon",100:"aom"})
print(room)

# การใช้loop [.key() แสดงค่า key | .value() แสดงค่า value]

for i in room.keys():
    print(i)

for i in room.values():
    print(i)

#การใช้ loopเพื่อแสดงทั้ง key,value
for i in room.items():
    print(i)

for i,j in room.items():
    print("key : ",i,"value : ",j)

#การลบข้อมูล pop()ลบแบบระบุ key / popitem()ลบสมาชิกตัวท้ายสุดออก
room.pop(102)
print(room)
room.popitem()
print(room)

#clear() ทำให้เป็นdictว่าง
room.clear()
print(room)
