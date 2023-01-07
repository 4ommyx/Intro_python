#การใช้ return

def randomnum(x):

    if len(x)<=2: #หลุด loop
        return
    else:
        if x == "112":
            print("ถูกรางวัล")
            return 1000
        else:
            print("ไม่ถูกรางวัล")
            return 0

x = randomnum("11")
print(x)
