#ทำงานต่อไปเรื่อยๆ จนกว่าค่าจะถึง100
total,i,summ = 0,0,0

# num1 = int(input("Enter your count : "))
print("--------------")

while (total <= 100):
    summ = int(input("Enter your number : "))
    i+=1
    total = total + summ
    print("sum",i,"=",total)

print("Answer : ",total)