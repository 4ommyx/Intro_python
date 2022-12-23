# เรียงชื่อ
name = []

while True :
    a = input("Enter your name : ")
    if a == "stop":
        break
    name.append(a)
     
print(name)
name.sort()
print(name)
