# Function คือ โปรแกรมย่อยที่อยู่ในโปรแกรมหลัก 
# เป็นการแยกคำสั่งแต่ละคำสั่งให้อยู่ในโซนนั้นๆทำให้คำสั่งในการเขียนโปรแกรม
# มีความเรียบง่ายไม่งงด้วย

# การสร้าง Function 
# def function name ():

def hi (n):
    print("Hello function",n)

def summ(m):
    sumN = 0
    i = 0
    while i <=m:
        sumN = sumN + i
        i+=1
    print(sumN)

def primeN(o):

    i = 2
    while True:
        
        if o % i == 0:
            o = o/i
            print(i)
            i=2
        elif o == 1:
            break
        else:
            i+=1

# hi(2) #เรียกใช้งานfunction
# summ(100)
primeN(555)