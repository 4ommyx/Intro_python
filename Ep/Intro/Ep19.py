fname = "Nattawut "
lname = "Chayauam "
age = "20 "
salary = 500.56

fullname = fname + lname + age # การต่อ string
print(fullname)
print("First name :"+fname+"Last name :"+lname+"AGE :"+age)

# การจัดวางรูปแบบการแสดงผล format + {}
# เป็นการต่อ string โดยการโยนตัวแปร
text1 = "Frist name :{0} Last name :{1} Age :{2} Salary :{3}"
print(text1.format(lname,fname,age,salary)) 

text = "Frist name :{0} Last name :{1} Age :{2}"
print(text.format(lname,fname,age)) 

#นับจำนวนคำในประโยค (count)
fruit= "ทุเรียน แตงโม เมล่อน กล้วย ทุเรียน"
print(fruit.count("ทุเรียน"))

#เช็คคำขึ้นต้น (startswith)

aa ="Mr.Nattawut"
if aa.startswith("Mr"):
    print("Man")
else:
    print("Woman")

#เช็คคำลงท้าย (endswith)

aa ="Mr.Nattawut"
if aa.endswith("t"):
    print("wow")
else:
    print("fuck")
