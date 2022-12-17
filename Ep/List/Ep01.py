# non-primative (list)
# ตัวแปร 1 ตัว เก็บได้หลายค่า(datatype เดียวกันหรือต่างกันก็ได้)

empty = [] #list ว่าง
number = [1,2]
name = ["a","aom","music"]

## output

print(type(name))
print(name)
print(number)

##การเข้าถึงข้อมูล 5 ตัว

# normal index [0,1,2,3,4] 
# negative index [-5,-4,-3,-2,-1]

print(number[0]+number[1])
print(name[-1])
print(name[0:2])
print(name[-3:-1])

