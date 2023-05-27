# module คือการทำโปรแกรมส่วนย่อยๆแต่ละส่วน 
# นำมาสร้างในไฟล์แยกกัน และนำมาใช้ในโปรแกรมหลักได้

import Calculate   # ต้องระบุ module หลักด้วย
from Area import * # ไม่ต้องระบุ module หลัก

Calculate.add(1,2,3,4,5)
Calculate.multi(1,2,3,4,5)
Calculate.sub(5,2)
Calculate.div(5,2)
print("-------------")
sq(5,2)
cir(7)