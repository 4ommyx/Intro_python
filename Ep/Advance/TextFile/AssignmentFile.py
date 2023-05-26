

try:
    # fw = open("Ep/Advance/TextFile/score.txt", "a", encoding="utf-8")
    # for i in range(5):
    #     n = i+1
    #     st = input("Enter your stuID {} : ".format(n))
    #     sc = int(input("Enter your score   : "))
    #     fw.writelines("{} {}\n".format(st,sc))
    # fw.close()

    fr = open("Ep/Advance/TextFile/score.txt", "r", encoding="utf-8")
    fw = open("Ep/Advance/TextFile/grade.txt", "w", encoding="utf-8")

    for line in fr.readlines():
        data = line.split(" ")
        score = int(data[1])
        GD = None
        if score >= 80 :
            GD = "A"
        elif score < 80 and score >= 70:
            GD = "B"
        elif score < 70 and score >= 60:
            GD = "C"
        elif score < 60 and score >= 50:
            GD = "D"
        else:
            GD = "F"
        print("STDID : {} SCORE : {} GRADE : {} ".format(data[0], score, GD))
        fw.writelines("{} {} {}\n".format(data[0], score, GD))
    fw.close()
    fr.close()

except:
    pass