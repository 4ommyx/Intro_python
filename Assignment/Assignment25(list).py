# จับคู่สินค้าและราคา 
fruit = ["coca   ","carry  ","sanwich"]
price = [30,60,25]

for i,j in zip(fruit,price) :
    print(i," : ",j)

print("--------------")

# normal
for i in range(len(price)):
    print(fruit[i]," : ",price[i])
print("--------------")

# reverse
for i in range(len(price)):
    print(fruit[i]," : ",price[-i-1])
print("--------------")
