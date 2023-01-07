# ฟังก์ชั่น เรียก ฟังก์ชั่น

def city():
    print("Samutprakan")

def country():
    print("Thailand")
    city()
country()

def number (x,y,z):

    return maxnum (maxnum(x,y),z)

print("------------------")

def maxnum (x,y):
    if x > y :
        return x
    else:
        return y 

max = number (10,-2,33)
print(max)
