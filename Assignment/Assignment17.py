# เกมทายลูกเต๋า
# 1 2 3 4 5 6 

import random
numRan = random.randrange(1,6+1)
i = 0


while True :
       
    number = int(input("Enter your answer : "))

    if number == 0 or i ==5 :
        break

    if numRan == number :
        print("correct")
        numRan = random.randrange(1,6+1)
        i+=1

    elif numRan > number:
        print("less")

    elif numRan < number :
        print("more")
    
    print("number :",number,"random :",numRan,"you win : ",i)
    print("-----------------------")
