# โปรแกรมธนาคารโดยใช้ Exception

i = 0
sta = 1
db = {"aom":10000, "music":10000, "mewon":10000}

while sta == 1:
    try:
        def main():
            print("Welcome to bank ... {}".format("aom"))
            print("option in bank")
            print("1.Deposite")
            print("2.Withdraw")
            print("3.Transfer")
            print("4.Close progarm")
            a = int(input("Plese selece option : "))

            if a == 1:
                m1 = int(input("Enter your amount : "))
                if m1 <= 0 :
                    raise Exception ("Error ...")
                deposite(m1)
            elif a == 2:
                m2 = int(input("Enter your amount : "))
                if (m2 <= 0) or (m2 > db["aom"]):
                    raise Exception ("Error ...")
                withdraw(m2)
            elif a == 3:
                m3 = int(input("Enter your amount : "))
                n3 = input("Enter for account to transfer : ")
                if (m3 <= 0) or (m3 > db["aom"]):
                    raise Exception ("Error ...")
                transfer(n3, m3)
            elif a == 4:
                sta = 0

        def deposite(money):
            db["aom"]+=money
        def withdraw(money):
            db["aom"]-=money
        def transfer(name, money):
            db["aom"]-=money
            db[name]+=money
            
        main()
    except Exception as e:
        print(e)
    finally:
        print("Thankyou +_+ ")
        print(db)
        print("------------------------------------------")
