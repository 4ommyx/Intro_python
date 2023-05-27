import datetime

result = datetime.datetime.now() # ดึงวันเวลามาใช้งาน
print(result)
print(result.year)
print(result.month)
print(result.day)

print("-----------------")

newtime = datetime.datetime(2020,1,31)
print(newtime)
print(newtime.year)
print(newtime.month)
print(newtime.day)

print("-----------------")

# ปรับรูปแบบการแสดงผล strftime
print("normal : ",result)
print("d/m/y  : ",result.strftime("%x"))
print("time   : ",result.strftime("%X"))
print("total  : ",result.strftime("%c"))
