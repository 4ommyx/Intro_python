
# แปลงอุณหภูมิ
temp = input("Enter your degree : ") #45c

degree = temp[:-1] # start index - before right 1 character
unit = temp[-1].upper() #นับจากฝั่งขวา1ตำแหน่ง
# print(degree,unit)


if unit == "C":
    ans = (int(degree)* 9/5) + 32
    print(ans)

elif unit == "F":
    ans = (int(degree)-32)*5/9
    print(ans)