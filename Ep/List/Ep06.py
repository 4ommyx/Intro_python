number = [1,2,3,4,5,6,7,8]
print("before :",number)

#remove() ลบสมาชิกออกแบบระบุตัวสมาชิกเองเลย
number.remove(5)
print("after remove :",number)

#pop() ลบสมาชิกตัวสุดท้าย (คล้ายๆ append() แต่เป็นการลบ)
number.pop()
print("after pop :",number)

#del = delete เป็นการลบแบบระบบ index / ลบทั้งlist
del number[0]
print("after del :",number)
# del number ลบทั้งตัวแปรออกเลย

#clear() ลบสมาชิกทุกตัว ให้เป็นลิสต์ว่าง
number.clear()
print("after clear :",number)
