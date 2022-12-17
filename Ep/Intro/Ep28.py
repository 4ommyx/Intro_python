# Break / Continue

i = 0
while i<= 10 :
    print("รอบที่ : ",i)

    if i == 5 :
        break # หลุดloopเลย

    i+=1

print("------------")

while i<= 100 :
    i+=1

    if (i % 2 == 0) :
        continue # เด้งไป loop while
    print("รอบที่ : ",i)

print("------------")