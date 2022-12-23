# จับคู่คำทักทาย / บุคคล

"""
Hi,hello

ก้อง,แก้ม

= Hiก้อง , Hiแก้ม , Helloก้อง , Helloแก้ม 

"""

a = ["Hi","Hello","Gn"]
p = ["mu","aom","prayut"]
total = []

for i in range(len(a)):

    for j in range(len(p)):

        # print(a[i]," ",p[j]) แบบ normal

        t=a[i]+p[j]
        total.append(t)

print(total) # แบบ list 
    
print("-------------")
