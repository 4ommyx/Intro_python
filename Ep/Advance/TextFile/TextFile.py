# File จะเป็นการจัดเก็บข้อมูลในรูปแบบของข้อความ โดยแยกส่วนของ Data ไว้อีกไฟล์หนึ่งให้มีความชัดเจน
# Syntax open("Filename", "mode", encoding=) mode จะเป็น r = อ่านอย่างเดียว w = เขียนแบบทับข้อมูลเดิม a = เขียนแบบทับข้อมูลเดิม
# หากมีการ open จะมีการ close เสมออ

import os
try:
    # การอ่าน read() ---> [read() = อ่านแบบทั้งไฟล์, readlines() = อ่านทีละบรรทัศเก็บไว้ใน list ]
    fr = open("Ep/Advance/TextFile/textfile.txt", "r", encoding="utf-8")
    
    # การเขียน (write())
    fw = open("Ep/Advance/TextFile/textfile.txt", "a", encoding="utf-8")
    fw.writelines("A\n")
    print(fr.readlines())
    fr.close()
    fw.close()

    # การลบไฟล์ remove()
    os.remove("Filename.txt")

except:
    pass
