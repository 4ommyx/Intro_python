# for loop
# for in range(start,stop,stap) การกำหนดรอบ

summ = 0

for i in range (5): #start 0,1,2,3,4
    print("รอบที่",i,"Hello world")

print("------------------ ")

for i in range (0,5) :
    summ+=i
    print("รอบที่",i,"=",summ)
print("Total val = ",summ)

for i in range(0,11,2):
    print("ครั้งที่",i/2,"Hello world")