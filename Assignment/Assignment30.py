# หา sum , avg

#aom
def summ(number):
    total = 0
    for i in range(len(number)):

        total += number[i]

    print("sum is : ",total)
    print("avg is : ",total/len(number))

#aom1
def summ1(num):
    total = 0
    for i in num :
        total += i

    return total , total/len(num)


x = [10,2,3,4,5]
# y = [10,2,3,4,5]

summ(x)
sum , avg = summ1(x)
print("sum is :",sum , "| avg is :",avg)