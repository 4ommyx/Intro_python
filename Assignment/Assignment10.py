
total,i,summ = 0,0,0

num1 = int(input("Enter your count : "))
print("--------------")

while (i<num1):
    summ = int(input("Enter your number : "))
    total = total + summ
    print("sum",i+1,"=",total)
    i+=1

print("Answer : ",total)
print("Avg : ",total/num1)