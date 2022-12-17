
h = int(input("Enter your (CM) : "))/100
w = int(input("Enter your (M) : "))

bmi = w/h**2

if bmi<18.5:
    print("ต่ำกว่าเกณฑ์")

elif bmi>=18.5 and bmi<=22.9:
    print("สมส่วน")

elif bmi>22.9 and bmi<=24.9:
    print("น้ำหนักเกิน")

elif bmi>24.9 and bmi<=29.9:
    print("ต่ำกว่าเกณฑ์")

else :
    print("ต่ำกว่าเกณฑ์")

print("bmi = ",bmi)


