
# แลกเงินนนนนนน

money = int(input("Enter your money : "))

if money >= 1000:
    print("1000 = ", money//1000)
    money = money % 1000
if money >= 500:
    print("500 = ", money//500)
    money = money % 500
if money >= 100:
    print("100 = ", money//100)
    money = money % 100
if money >= 50:
    print("50 = ", money//50)
    money = money % 50
if money >= 20:
    print("20 = ", money//20)
    money = money % 20
