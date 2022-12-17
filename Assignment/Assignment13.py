#ตัว้ลขขั้ยบันได

"""
input = 6
1
12
123
1234
12345
123456

"""
count = int(input("Enter your count : "))

for y in range(1,count+1):

    for x in range(1,y+1):

        print(x,end=" ")
    print(" ")

count = int(input("Enter your count : "))
numm = count + 1

for y in range(1,numm):

    for x in range(1,y+1):

        print(x,end=" ")
    print(" ")

