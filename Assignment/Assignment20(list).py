# Assignment หากลุ่มเลขคู่/คี่
number = []
odd = []
even = []

while True :
    a = int(input("Enter num : "))

    if a <= 0 :
        break
        
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)
    
    number.append(a)
    
print(number)
print(odd)
print(even)


