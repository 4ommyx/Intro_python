name = 'nattawut  th' # index start at 0
sen = 'มาดิไอเวน'

# print(name[0])
# print(name[1])
# print(name[-1])    # นับจากข้างหลัง
# print(name[1:10])  # start at 1 เอาถึง index 10-1 
print(len(name))     # string lenght

name = name.strip()  # strip = ลบช่องว่าง space bar
name1 = name.lstrip()
name2 = name.rstrip()
print(len(name))
print(len(name1))
print(len(name2))

print(name.upper()) # upper พิมพ์ใหญ่
print(name.lower()) # lower พิมพ์ใหญ่
print(name.capitalize()) #ขึ้นต้นพิมพ์ใหญ่

print(name.replace("n","-")) # การแทนที่

x = 'มา' in sen # เช็คว่าคำนั้นๆมีใน string ไหม

if x == True :
    print(sen.replace('มา','ma'))

 