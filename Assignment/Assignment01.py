# โปรแกรมคำนวนค่า BMI (ดัชนีมวลร่างกาย)
# BMI = น้ำหนัก / ส่วนสูง * ส่วนสูง

# input
w = int(input("ป้อนน้ำหนักของคุณ (KG):"))
H = int(input("ป้อนส่วนสูงของคุณ (CM):"))  # แปลง input จาก str เป็น int

# process
h = H/100

bmi = w/(h**2)

# output
print("bmi", bmi)
