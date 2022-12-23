# Assignment เรียงลำดับตัวเลข
number = []

while True :
    a = int(input("Enter num : "))

    if a <= 0 :
        break

    number.append(a)

    
print(number)
minn = min(number) # min(list) หาค่าต่ำสุดใน list
maxx = max(number)
summ = sum(number)
print("max is :",maxx)
print("min is :",minn)
print("sum is :",summ)

number.sort()
print(number)
print("max is :",number[-1])
print("min is :",number[0])
print("sum is :",summ)

