# การนำข้อมูลใน tuple ใส่ไว้ในตัวแปรต่างๆ
tup = (1,2,3,4,5,6)
a,b,c,d,e,f = tup # แต่ละตัวแปรเก็บข้อมูลใน tup ตามตำแหน่ง comma

print(a)
print(tup[0])

print(b)
print(tup[1])

print(c)
print(tup[2])

print(d)
print(tup[3])

# switch tuple
a = (1,2,3,4)
b = (12,23,34,45)

print(a)
print(b)

a,b = b,a 
print("---------------")

print(a)
print(b)

