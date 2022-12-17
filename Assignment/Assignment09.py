# แม่สูตรคูณ

st = int(input("start : "))
sp = int(input("stop : "))

for i in range(st,sp+1,1):

    for j in range(1,13,1):
        print(i,"*",j,"=",i*j)
    
    print("------------")
