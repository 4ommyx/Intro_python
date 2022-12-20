
#การทำงานโดยใช้ loop
number = [1,2,3,4,5,6,7,8]
i = 0
summ = 0


while i <= len(number)-1:
    print(number[i])
    summ = number[i]+summ
    i+=1

print(summ)

#ตรวจสอบข้อมูล
name = ["aom","music","aomond"]

if "aom" in  name: # for mix if
    print("True")
else:
    print("False")
