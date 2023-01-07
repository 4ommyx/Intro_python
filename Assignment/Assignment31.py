# find upper lower of character

def checkC(m):
    result = {"UPPER":0,"LOWER":0}
    for i in range(len(m)):
        if m[i].isupper():
            result["UPPER"]+=1
        elif m[i].islower():
            result["LOWER"]+=1
        else:
            pass

    return result

mes = input("Enter your massege : ")
x = checkC(mes)
