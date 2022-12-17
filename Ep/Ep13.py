
"""
โครงสร้างควบคุม (Control Structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ

การใช้ if

if expression:
    statement

"""
age = int(input("ป้อนอายุของคุณ : "))

if age >= 15:  # ต้องกดtab ด้วยนา
    print("นาย นางสาว")
else:
    print("เด็กชาย เด็กหญิง")

if age <= 15:  # ต้องกดtab ด้วยนา
    print("วัยเด็ก")
elif age > 15 and age <= 20:
    print("วัยรุ่น")
elif age > 20 and age <= 29:
    print("วัยทำงาน")
else:
    print("วัยผู้ใหญ่")  # elif = else if

print("จบโปรแกรม")
