#Type conversion
x = 10
y = 3.14
z = "20"

print(type(x))
print(type(y))
print(type(z))

# string --> int
sum0 = x+int(z) #int(variable) แปลงชนิดของข้อมูล จาก str --> int  
print(sum0)

# int --> string
sum1 = str(x)+"-"+z

print("-"+ sum1)

# int --> float
print(float(z))

