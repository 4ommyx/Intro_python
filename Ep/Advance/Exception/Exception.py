# Exception คือการทำงานเมื่อเจอรูปแบบของ Error ต่างๆ
# และสามารถแจ้งกับผู้ใช้งานให้แก้ไขข้อมูลที่ป้อนในส่วนของ Input ในโปรแกรมได้

# โปรแกรมหารตัวเลขที่หารได้เฉพาะจำนวนเต็มบวก
# ------------------------------------ 

i = 0
while True:
    # หน้า main ปกติเขียนโค้ดต่างๆในหน้า try
    try:
        i+=1
        num1 = int(input("Enter your num 1 : "))
        num2 = int(input("Enter your num 2 : "))
        if (num1<=0) or (num2 <=0) :
            # เป็นการบ่งบอกชนิด error โดยตัวเราเอง
            raise Exception("number is not positive integer")
        sum = num1/num2
        print(sum)

    # ส่วนที่พบ Error จะทำงานในส่วนนี้
    except Exception as e :
        print(e)

    # ถ้าไม่ใช่ Error 2 อันข้างต้นจะทำงานส่วนนี้
    else: 
        print("Not found Error !!")
        
    # ไม่ว่าจะทำงานได้หรือError จะทำงานในส่วนนี้เสมอ
    finally:
        print("Round : {}".format(i))
        print("---------------------")
        