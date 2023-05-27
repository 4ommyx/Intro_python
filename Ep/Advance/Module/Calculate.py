# *args เก็บในรูป tuple โดยสามารถใส่พารามิเตอร์ได้ไม่จำกัดเลย

def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    print(sum)

def multi(*args):
    sum = 1
    for i in range(len(args)):
        sum *= args[i]
    print(sum)

def sub(n1,n2):
    result = n1-n2
    print(result)

def div(n1,n2):
    result = n1/n2
    print(result)
