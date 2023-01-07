# Recursive function เป็นฟังก์ชั่นที่เป็นการวน 
# loop เรื่อยๆ แทนการใช้ loop 
# ใช้ฟังก์ชั่นวนฟังก์ชั่น

"""
หาจุดวนซ้ำ
หาจุดออกจาก function (return)
ต้องมี parameter ด้วย

1-5 โดยไม่ใช้ loop



"""
def display(n):

    if n == 6 :
        return
    else :
        print(n)
        n+=1
        display(n)

# display(1)

def summ(n):
    if n <= 0 :
        return n
    else:
        return n+summ(n-1)

print(summ(4))
