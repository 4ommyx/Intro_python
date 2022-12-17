#หาผลบวกตัวเลข

i = 1
summ = 0

n = input("ระบุจำนวนรอบ : ")
N = int(n)


while i<= N:
    summ = summ + i 
    print("summ ครั้งที่",i,"=",summ)
    i+=1

print("Total sum = ",summ)
print("Avg = ",summ/(i-1))