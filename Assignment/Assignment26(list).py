#การค้นหาจำนวนสมาชิก(int,char)

mesage = ["aa","asa","ada","aace","sasssa","aaaaaaaaaaaaaaaa"]
result = []

for i in range(len(mesage)):
    
    count = mesage[i].count("a")
    result.append(count)
    
print(result)