
name = {"mu","aom","mumond"}

# การลบสมาชิก 
# remove() ลบสมาชิก ถ้าไม่มีสมาชิกแล้วลบจะติด Error
# discard() ลบสมาชิก จะมีหรือไม่มีสมาชิกก็ไม่ติด Error แน่ๆ 
name.remove("aom")
# name.remove("ohm") # Error

name.discard("ohm")  
name.discard("mu")
print("before : ",name)

#การเปลี่ยนแปลงข้อมูลสมาชิก เนื่องจากแก้ไขเหมือน set / list ไม่ได้
# จึงต้องทำการลบและเพิ่มข้อมูลเข้ามาใหม่เท่านั้น
# เปลี่ยนจาก mumond --> mumu
print("before : ",name)
name.discard("mumond")
name.add("mumu")
print("after  : ",name)

# del ลบทั้งตัวแปร ,clear()ทำให้เป็นตัวแปรว่างๆ (เหมือน list)
name.clear()
print(name)