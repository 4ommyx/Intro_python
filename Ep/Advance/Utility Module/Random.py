import random

lis = ["a", "b", "c", 1, 2, 3]
for i in range(5):
    print(random.uniform(1,10))   # สุ่มแบบทศนิยม
    print(random.randrange(1,10)) # สุ่มแบบจำนวนเต็ม (start, stop, step)
    print("-----------")

    print(random.choice(lis))     # สุ่มจาก lis ที่เราสร้างไว้
    print(random.choice("012"))  
    random.shuffle(lis)           # สุ่มการสลับตำแหน่งใน lis ที่เราสร้างไว้
    print(lis)
    print("-----------")