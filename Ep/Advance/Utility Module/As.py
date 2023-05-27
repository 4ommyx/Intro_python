import random

ATM_PASSWORD="000000"
count = 0
result = ""

while result!=ATM_PASSWORD:
    count+=1
    result=""
    for i in range(len(ATM_PASSWORD)):
        digit = random.choice("0123456789")
        result = ""+result+digit
    print("Round {} is : {}".format(count, result))
print("Password is : {} --> count {} ".format(result, count))