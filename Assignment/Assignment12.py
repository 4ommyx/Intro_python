# Find max min

maxx,minn = 0,10000 # border
i = 0
while True :

    i+=1
    numm = int(input("Enter your num : "))

    if numm <0 or numm>10000 : #เช็คว่าหลุด loop ไหม
        break

    if numm < minn :
        minn = numm

    if numm > maxx :
        maxx = numm

print("max is :" ,max,"min is :",min)


