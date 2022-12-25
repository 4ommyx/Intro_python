
#การคัดลอกข้อมูล
number = [1,2,3,4,5,6,7]
name = ["aon","mu"]
num1 =[]

print(num1)
num1 = number.copy()

print(num1)

#การรวมข้อมูล 2 แบบ

a = number + name
print(a)

number.extend(name)
print(number)

#แสดงจำนวนสมาชิก(ว่าในลิสต์)มีสามชิกตัวนี้อยู่กี่ตัว count()
number1 = [1,2,3,3,2,35,7,6,5,4,3,7,6,5,8,9,0,0,0,9,8,8,7,6,5,3,2,2,21,1,5,2,3,5,6,7]
x = number1.count(3)
z = number1.count(8)
print("3 : ",x)
print("8 : ",z)