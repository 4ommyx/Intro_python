# Assignment เรียงลำดับตัวเลข
number = []
while True :

    a = int(input("Enter num : "))
    number.append(a)

    if a <= 0 :
        break

print(number)
number.sort() #เรียงข้อมูลจากน้อยไปมากใน list number
print(number)
number.reverse() #เป็นการกลับตำแหน่งสมาชิกใน list จะใช้ได้เมื่อใช้ sort() ก่อนเท่านั้น
print(number)
